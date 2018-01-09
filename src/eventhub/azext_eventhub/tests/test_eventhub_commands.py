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
    @ResourceGroupPreparer(name_prefix='cli_test_eh_namespace')
    def test_eh_namespace(self, resource_group):
        self.kwargs.update({
            'loc': 'westus2',
            'rg': resource_group,
            'namespacename': self.create_random_name(prefix='eh-nscli', length=20),
            'tags': {'tag1: value1'},
            'sku': 'Standard',
            'tier': 'Standard',
            'authoname': self.create_random_name(prefix='cliAutho', length=20),
            'defaultauthorizationrule': 'RootManageSharedAccessKey',
            'accessrights': 'Send',
            'primary': 'PrimaryKey',
            'secondary': 'SecondaryKey',
            'isautoinflateenabled': 'True',
            'maximumthroughputunits': 4
        })

        # Check for the NameSpace name Availability

        self.cmd('eh namespace check-name-availability --name {namespacename}',
                 checks=[self.check('nameAvailable', True)])

        # Create Namespace
        self.cmd('eh namespace create --resource-group {rg} --name {namespacename} --location {loc} --tags {tags} --sku-name {sku} --sku-tier {tier} --is-auto-inflate-enabled {isautoinflateenabled} --maximum-throughput-units {maximumthroughputunits}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Get Created Namespace
        self.cmd('eh namespace show --resource-group {rg} --name {namespacename}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Get Created Namespace list by subscription
        listnamespaceresult = self.cmd('eh namespace list').output
        self.assertGreater(len(listnamespaceresult), 0)

        # Get Created Namespace list by ResourceGroup
        listnamespacebyresourcegroupresult = self.cmd('eh namespace list --resource-group {rg}').output
        self.assertGreater(len(listnamespacebyresourcegroupresult), 0)

        # Create Authoriazation Rule
        self.cmd('eh namespace authorizationrule create --resource-group {rg} --namespace-name {namespacename} --name {authoname} --access-rights {accessrights}',
                 checks=[self.check('name', self.kwargs['authoname'])])

        # Get Authorization Rule
        self.cmd('eh namespace authorizationrule show --resource-group {rg} --namespace-name {namespacename} --name {authoname}', checks=[self.check('name', self.kwargs['authoname'])])

        # Get Default Authorization Rule
        self.cmd('eh namespace authorizationrule show --resource-group {rg} --namespace-name {namespacename} --name {defaultauthorizationrule}',
                 checks=[self.check('name', self.kwargs['defaultauthorizationrule'])])

        # Get Authorization Rule Listkeys
        self.cmd('eh namespace authorizationrule list-keys --resource-group {rg} --namespace-name {namespacename} --name {authoname}')

        # Regeneratekeys - Primary
        self.cmd(
            'eh namespace authorizationrule regenerate-keys --resource-group {rg} --namespace-name {namespacename} --name {authoname} --key-name {primary}')

        # Regeneratekeys - Secondary
        self.cmd('eh namespace authorizationrule regenerate-keys --resource-group {rg} --namespace-name {namespacename} --name {authoname} --key-name {secondary}')

        # Delete AuthorizationRule
        self.cmd('eh namespace authorizationrule delete --resource-group {rg} --namespace-name {namespacename} --name {authoname}')

        # Delete Namespace list by ResourceGroup
        self.cmd('eh namespace delete --resource-group {rg} --name {namespacename}')

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
        self.cmd('eh consumergroup create --resource-group {rg} --namespace-name {namespacename} --event-hub-name {eventhubname} --name {consumergroupname}',
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
