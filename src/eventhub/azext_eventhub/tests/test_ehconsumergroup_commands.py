# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# AZURE CLI EventHub - NAMESAPCE TEST DEFINITIONS

import json
import time

from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)


# pylint: disable=line-too-long
# pylint: disable=too-many-lines


class EHNamespaceCURDScenarioTest(ScenarioTest):
    
    @ResourceGroupPreparer(name_prefix='cli_test_eh_consumergroup')
    def test_eh_consumergroup(self, resource_group):
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
            'eventhubname': self.create_random_name(prefix='eh-cli', length=25),
            'eventhubauthoname': self.create_random_name(prefix='cliEventAutho', length=25),
            'isautoinflateenabled': 'True',
            'maximumthroughputunits': 4,
            'messageretentionindays': 4,
            'partitioncount': 4,
            'consumergroupname': self.create_random_name(prefix='eh-comcli', length=25),
            'usermetadata1': 'UserId for the given user',
            'usermetadata2': 'UserId for the given user is updated'
        })

        # Create Namespace
        self.cmd('eh namespace create --resource-group {rg} --name {namespacename} --location {loc} --tags {tags} --sku-name {sku} --sku-tier {tier} --is-auto-inflate-enabled {isautoinflateenabled} --maximum-throughput-units {maximumthroughputunits}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Get Created Namespace
        self.cmd('eh namespace show --resource-group {rg} --name {namespacename}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Create Eventhub
        self.cmd('eh eventhub create --resource-group {rg} --namespace-name {namespacename} --name {eventhubname} --message-retention-in-days {messageretentionindays}', checks=[self.check('name', self.kwargs['eventhubname'])])

        # Get Eventhub
        self.cmd('eh eventhub show --resource-group {rg} --namespace-name {namespacename} --name {eventhubname}',
                 checks=[self.check('name', self.kwargs['eventhubname'])])

        # Create ConsumerGroup
        self.cmd('eh consumergroup create --resource-group {rg} --namespace-name {namespacename} --event-hub-name {eventhubname} --name {consumergroupname} --user-metadata {usermetadata}',
                 checks=[self.check('name', self.kwargs['consumergroupname'])])

        # Get Consumer Group
        self.cmd('eh consumergroup get --resource-group {rg} --namespace-name {namespacename} --event-hub-name {eventhubname} --name {consumergroupname}',
                 checks=[self.check('name', self.kwargs['consumergroupname'])])

        # Create/Update ConsumerGroup
        self.cmd('eh consumergroup create --resource-group {rg} --namespace-name {namespacename} --event-hub-name {eventhubname} --name {consumergroupname} --user-metadata {usermetadata2}',
                 checks=[self.check('user_metadata', self.kwargs['usermetadata2'])])

        # Get ConsumerGroup List
        listconsumergroup = self.cmd('eh consumergroup list --resource-group {rg} --namespace-name {namespacename} --event-hub-name {eventhubname}').output
        self.assertGreater(len(listconsumergroup), 0)

        # Delete ConsumerGroup
        self.cmd('eh consumergroup delete --resource-group {rg} --namespace-name {namespacename} --event-hub-name {eventhubname} --name {consumergroupname}')

        # Delete Eventhub
        self.cmd('eh eventhub delete --resource-group {rg} --namespace-name {namespacename} --name {eventhubname}')

        # Delete Namespace
        self.cmd('eh eventhub delete --resource-group {rg} --name {namespacename}')
