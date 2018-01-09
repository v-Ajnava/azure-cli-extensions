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
    
    @ResourceGroupPreparer(name_prefix='cli_test_eh_alias')
    def test_eh_alias(self, resource_group):

        self.kwargs.update({
            'loc_south': 'SouthCentralUS',
            'loc_north': 'NorthCentralUS',
            'rg': resource_group,
            'namespacenameprimary': self.create_random_name(prefix='eh-nscli', length=20),
            'namespacenamesecondary': self.create_random_name(prefix='eh-nscli', length=20),
            'tags': {'tag1: value1', 'tag2: value2'},
            'sku': 'Standard',
            'tier': 'Standard',
            'authoname': self.create_random_name(prefix='cliAutho', length=20),
            'defaultauthorizationrule': 'RootManageSharedAccessKey',
            'accessrights': 'Send',
            'primary': 'PrimaryKey',
            'secondary': 'SecondaryKey',
            'aliasname': self.create_random_name(prefix='cliAlias', length=20),
            'alternatename': self.create_random_name(prefix='cliAlter', length=20),
            'id': '',
            'test': ''
        })

        self.cmd('eh namespace check-name-availability --name {namespacenameprimary}',
                 checks=[self.check('nameAvailable', True)])

        # Create Namespace - Primary
        self.cmd('eh namespace create --resource-group {rg} --name {namespacenameprimary} --location {loc_south} --tags {tags} --sku-name {sku} --sku-tier {tier}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Get Created Namespace - Primary
        self.cmd('eh namespace show --resource-group {rg} --name {namespacenameprimary}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Create Namespace - Secondary
        self.cmd('eh namespace create --resource-group {rg} --name {namespacenamesecondary} --location {loc_north} --tags {tags} --sku-name {sku} --sku-tier {tier}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Get Created Namespace - Secondary
        getnamespace2result = self.cmd('eh namespace show --resource-group {rg} --name {namespacenamesecondary}',
                                       checks=[self.check('sku.name', self.kwargs['sku'])]).output

        # Create Authoriazation Rule
        self.cmd('eh namespace authorizationrule create --resource-group {rg} --namespace-name {namespacenameprimary} --name {authoname} --access-rights {accessrights}', checks=[self.check('name', self.kwargs['authoname'])])

        partnernamespaceid = json.loads(getnamespace2result)['id']
        self.kwargs.update({'id': partnernamespaceid})
        # Get Create Authorization Rule
        self.cmd('eh namespace authorizationrule show --resource-group {rg} --namespace-name {namespacenameprimary} --name {authoname}', checks=[self.check('name', self.kwargs['authoname'])])

        # CheckNameAvailability - Alias

        self.cmd('eh alias check-name-availability --resource-group {rg} --namespace-name {namespacenameprimary} --name {aliasname}', checks=[self.check('nameAvailable', True)])

        # Create alias
        self.cmd('eh alias create  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname} --partner-namespace {id}')

        # get alias - Primary
        self.cmd('eh alias show  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}')

        # get alias - Secondary
        self.cmd('eh alias show  --resource-group {rg} --namespace-name {namespacenamesecondary} --alias {aliasname}')

        getaliasprimarynamespace = self.cmd('eh alias show  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}').output

        # check for the Alias Provisioning succeeded
        while json.loads(getaliasprimarynamespace)['provisioningState'] != ProvisioningStateDR.succeeded.value:
            time.sleep(30)
            getaliasprimarynamespace = self.cmd('eh alias show  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}').output

        # Break Pairing
        self.cmd('eh alias break-pairing  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}')

        getaliasafterbreak = self.cmd('eh alias show  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}').output

        # check for the Alias Provisioning succeeded
        while json.loads(getaliasafterbreak)['provisioningState'] != ProvisioningStateDR.succeeded.value:
            time.sleep(30)
            getaliasafterbreak = self.cmd('eh alias show  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}').output

        # Create alias
        self.cmd('eh alias create  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname} --partner-namespace {id}')

        getaliasaftercreate = self.cmd('eh alias show  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}').output

        # check for the Alias Provisioning succeeded
        while json.loads(getaliasaftercreate)['provisioningState'] != ProvisioningStateDR.succeeded.value:
            time.sleep(30)
            getaliasaftercreate = self.cmd('eh alias show  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}').output

        # FailOver
        self.cmd('eh alias fail-over  --resource-group {rg} --namespace-name {namespacenamesecondary} --alias {aliasname}')

        getaliasafterfail = self.cmd('eh alias show  --resource-group {rg} --namespace-name {namespacenamesecondary} --alias {aliasname}').output

        # check for the Alias Provisioning succeeded
        while json.loads(getaliasafterfail)['provisioningState'] != ProvisioningStateDR.succeeded.value:
            time.sleep(30)
            getaliasafterfail = self.cmd('eh alias show  --resource-group {rg} --namespace-name {namespacenamesecondary} --alias {aliasname}').output

        # Delete Alias
        self.cmd('eh alias delete  --resource-group {rg} --namespace-name {namespacenamesecondary} --alias {aliasname}')

        time.sleep(30)

        # Delete Namespace - primary
        self.cmd('eh namespace delete --resource-group {rg} --name {namespacenameprimary}')

        # Delete Namespace - secondary
        self.cmd('eh namespace delete --resource-group {rg} --name {namespacenamesecondary}')
