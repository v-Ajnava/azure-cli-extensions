# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# AZURE CLI EventHub - NAMESAPCE TEST DEFINITIONS

import json
import time

from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)

from azext_eventhub.eventhub.models import ProvisioningStateDR


# pylint: disable=line-too-long
# pylint: disable=too-many-lines


class EHNamespaceCURDScenarioTest(ScenarioTest):
    @ResourceGroupPreparer(name_prefix='cli_test_eh_eventnhub')
    def test_eh_eventhub(self, resource_group):
        self.kwargs.update({
            'loc': 'westus2',
            'rg': resource_group,
            'namespacename': self.create_random_name(prefix='eh-nscli', length=20),
            'tags': {'tag1: value1', 'tag2: value2'},
            'sku': 'Standard',
            'tier': 'Standard',
            'authoname': self.create_random_name(prefix='cliAutho', length=20),
            'defaultauthorizationrule': 'RootManageSharedAccessKey',
            'accessrights': 'Listen',
            'primary': 'PrimaryKey',
            'secondary': 'SecondaryKey',
            'eventhubname': self.create_random_name(prefix='eh-eventhubcli', length=25),
            'eventhubauthoname': self.create_random_name(prefix='cliEventAutho', length=25),
            'isautoinflateenabled': 'True',
            'maximumthroughputunits': 4,
            'messageretentionindays': 4,
            'partitioncount': 4
        })

        # Create Namespace
        self.cmd('eh namespace create --resource-group {rg} --name {namespacename} --location {loc} --tags {tags} --sku-name {sku} --sku-tier {tier} --is-auto-inflate-enabled {isautoinflateenabled} --maximum-throughput-units {maximumthroughputunits}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Get Created Namespace
        self.cmd('eh namespace show --resource-group {rg} --name {namespacename}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Create Eventhub
        self.cmd('eh eventhub create --resource-group {rg} --namespace-name {namespacename} --name {eventhubname}', checks=[self.check('name', self.kwargs['eventhubname'])])

        # Get Eventhub
        self.cmd('eh eventhub show --resource-group {rg} --namespace-name {namespacename} --name {eventhubname}',
                 checks=[self.check('name', self.kwargs['eventhubname'])])

        # Eventhub List
        listeventhub = self.cmd('eh eventhub list --resource-group {rg} --namespace-name {namespacename}').output
        self.assertGreater(len(listeventhub), 0)

        # Create Authoriazation Rule
        self.cmd('eh eventhub authorizationrule create --resource-group {rg} --namespace-name {namespacename} --event-hub-name {eventhubname} --name {authoname} --access-rights {accessrights}',
                 checks=[self.check('name', self.kwargs['authoname'])])

        # Get Create Authorization Rule
        self.cmd('eh eventhub authorizationrule show --resource-group {rg} --namespace-name {namespacename} --event-hub-name {eventhubname} --name {authoname}',
                 checks=[self.check('name', self.kwargs['authoname'])])

        # Get Authorization Rule Listkeys
        self.cmd('eh eventhub authorizationrule list-keys --resource-group {rg} --namespace-name {namespacename} --event-hub-name {eventhubname} --name {authoname}')

        # Regeneratekeys - Primary
        regenrateprimarykeyresult = self.cmd('eh eventhub authorizationrule regenerate-keys --resource-group {rg} --namespace-name {namespacename} --event-hub-name {eventhubname} --name {authoname} --key-name {primary}')
        self.assertIsNotNone(regenrateprimarykeyresult)

        # Regeneratekeys - Secondary
        regenratesecondarykeyresult = self.cmd('eh eventhub authorizationrule regenerate-keys --resource-group {rg} --namespace-name {namespacename} --event-hub-name {eventhubname} --name {authoname} --key-name {secondary}')
        self.assertIsNotNone(regenratesecondarykeyresult)

        # Delete Eventhub AuthorizationRule
        self.cmd('eh eventhub authorizationrule delete --resource-group {rg} --namespace-name {namespacename} --event-hub-name {eventhubname} --name {authoname}')

        # Delete Eventhub
        self.cmd('eh eventhub delete --resource-group {rg} --namespace-name {namespacename} --name {eventhubname}')

        # Delete Namespace
        self.cmd('eh eventhub delete --resource-group {rg} --name {namespacename}')
