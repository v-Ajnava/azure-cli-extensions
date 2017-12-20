# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# AZURE CLI SERVICEBUS - NAMESAPCE TEST DEFINITIONS

import json
import time
from azext_servicebus.servicebus.models import ProvisioningStateDR

from azure.cli.testsdk import (
    ScenarioTest, ResourceGroupPreparer)

# pylint: disable=line-too-long
# pylint: disable=too-many-lines


class SBNamespaceCURDScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_sb_namespace')
    def test_sb_namespace(self, resource_group):

        self.kwargs.update({
            'loc': 'westus2',
            'rg': resource_group,
            'namespacename': self.create_random_name(prefix='sb-nscli', length=20),
            'tags': {'tag1: value1'},
            'sku': 'Standard',
            'tier': 'Standard',
            'authoname': self.create_random_name(prefix='cliAutho', length=20),
            'defaultauthorizationrule': 'RootManageSharedAccessKey',
            'accessrights': 'Send',
            'primary': 'PrimaryKey',
            'secondary': 'SecondaryKey'
        })

        # Check for the NameSpace name Availability

        self.cmd('sb namespace check-name-availability --name {namespacename}',
                 checks=[self.check('nameAvailable', True)])

        # Create Namespace
        self.cmd('sb namespace create --resource-group {rg} --name {namespacename} '
                 '--location {loc} --tags {tags} --sku-name {sku} --sku-tier {tier}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Get Created Namespace
        self.cmd('sb namespace show --resource-group {rg} --name {namespacename}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Get Created Namespace list by subscription
        listnamespaceresult = self.cmd('sb namespace list').output
        self.assertGreater(len(listnamespaceresult), 0)

        # Get Created Namespace list by ResourceGroup
        listnamespacebyresourcegroupresult = self.cmd('sb namespace list --resource-group {rg}').output
        self.assertGreater(len(listnamespacebyresourcegroupresult), 0)

        # Create Authoriazation Rule
        self.cmd('sb namespace authorizationrule create --resource-group {rg}'
                 ' --namespace-name {namespacename} --name {authoname} --access-rights {accessrights}',
                 checks=[self.check('name', self.kwargs['authoname'])])

        # Get Authorization Rule
        self.cmd('sb namespace authorizationrule show --resource-group {rg} --namespace-name {namespacename}'
                 ' --name {authoname}', checks=[self.check('name', self.kwargs['authoname'])])

        # Get Default Authorization Rule
        self.cmd('sb namespace authorizationrule show --resource-group {rg} --namespace-name {namespacename}'
                 ' --name {defaultauthorizationrule}',
                 checks=[self.check('name', self.kwargs['defaultauthorizationrule'])])

        # Get Authorization Rule Listkeys
        self.cmd('sb namespace authorizationrule list-keys --resource-group {rg} --namespace-name {namespacename}'
                 ' --name {authoname}')

        # Regeneratekeys - Primary
        self.cmd('sb namespace authorizationrule regenerate-keys --resource-group {rg} --namespace-name {namespacename} --name {authoname} --key {primary}')

        # Regeneratekeys - Secondary
        self.cmd('sb namespace authorizationrule regenerate-keys --resource-group {rg}'
                 ' --namespace-name {namespacename} --name {authoname} --key {secondary}')

        # Delete AuthorizationRule
        self.cmd('sb namespace authorizationrule delete --resource-group {rg} --namespace-name {namespacename}'
                 ' --name {authoname}')

        # Delete Namespace list by ResourceGroup
        self.cmd('sb namespace delete --resource-group {rg} --name {namespacename}')

    @ResourceGroupPreparer(name_prefix='cli_test_sb_queue')
    def test_sb_queue(self, resource_group):
        self.kwargs.update({
            'loc': 'westus2',
            'rg': resource_group,
            'namespacename': self.create_random_name(prefix='sb-nscli', length=20),
            'tags': {'tag1: value1', 'tag2: value2'},
            'sku': 'Standard',
            'tier': 'Standard',
            'authoname': self.create_random_name(prefix='cliAutho', length=20),
            'defaultauthorizationrule': 'RootManageSharedAccessKey',
            'accessrights': 'Listen',
            'primary': 'PrimaryKey',
            'secondary': 'SecondaryKey',
            'queuename': self.create_random_name(prefix='sb-queuecli', length=25),
            'queueauthoname': self.create_random_name(prefix='cliQueueAutho', length=25),
            'lockduration': 'PT10M'

        })

        # Create Namespace
        self.cmd('sb namespace create --resource-group {rg} --name {namespacename} --location {loc} --tags {tags}'
                 ' --sku-name {sku} --sku-tier {tier}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Get Created Namespace
        self.cmd('sb namespace show --resource-group {rg} --name {namespacename}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Create Queue
        self.cmd('sb queue create --resource-group {rg} --namespace-name {namespacename} --name {queuename}'
                 ' --auto-delete-on-idle {lockduration} ', checks=[self.check('name', self.kwargs['queuename'])])

        # Get Queue
        self.cmd('sb queue show --resource-group {rg} --namespace-name {namespacename} --name {queuename}',
                 checks=[self.check('name', self.kwargs['queuename'])])

        # Queue List
        self.cmd('sb queue list --resource-group {rg} --namespace-name {namespacename}')

        # Create Authoriazation Rule
        self.cmd('sb queue authorizationrule create --resource-group {rg} --namespace-name {namespacename}'
                 ' --queue-name {queuename} --name {authoname} --access-rights {accessrights}',
                 checks=[self.check('name', self.kwargs['authoname'])])

        # Get Create Authorization Rule
        self.cmd('sb queue authorizationrule show --resource-group {rg} --namespace-name {namespacename}'
                 ' --queue-name {queuename} --name {authoname}',
                 checks=[self.check('name', self.kwargs['authoname'])])

        # Get Authorization Rule Listkeys
        self.cmd('sb queue authorizationrule list-keys --resource-group {rg} --namespace-name {namespacename}'
                 ' --queue-name {queuename} --name {authoname}')

        # Regeneratekeys - Primary
        regenrateprimarykeyresult = self.cmd(
            'sb queue authorizationrule regenerate-keys --resource-group {rg} --namespace-name {namespacename} --queue-name {queuename} --name {authoname} --key {primary}')
        self.assertIsNotNone(regenrateprimarykeyresult)

        # Regeneratekeys - Secondary
        regenratesecondarykeyresult = self.cmd(
            'sb queue authorizationrule regenerate-keys --resource-group {rg} --namespace-name {namespacename}'
            ' --queue-name {queuename} --name {authoname} --key {secondary}')
        self.assertIsNotNone(regenratesecondarykeyresult)

        # Delete Queue AuthorizationRule
        self.cmd('sb queue authorizationrule delete --resource-group {rg} --namespace-name {namespacename}'
                 ' --queue-name {queuename} --name {authoname}')

        # Delete Queue
        self.cmd('sb queue delete --resource-group {rg} --namespace-name {namespacename} --name {queuename}')

        # Delete Namespace
        self.cmd('sb namespace delete --resource-group {rg} --name {namespacename}')

    @ResourceGroupPreparer(name_prefix='cli_test_sb_topic')
    def test_sb_topic(self, resource_group):
        self.kwargs.update({
            'loc': 'westus2',
            'rg': resource_group,
            'namespacename': self.create_random_name(prefix='sb-nscli', length=20),
            'tags': {'tag1: value1', 'tag2: value2'},
            'sku': 'Standard',
            'tier': 'Standard',
            'authoname': self.create_random_name(prefix='cliAutho', length=20),
            'defaultauthorizationrule': 'RootManageSharedAccessKey',
            'accessrights': 'Send',
            'primary': 'PrimaryKey',
            'secondary': 'SecondaryKey',
            'topicname': self.create_random_name(prefix='sb-topiccli', length=25),
            'topicauthoname': self.create_random_name(prefix='cliTopicAutho', length=25)
        })

        # Create Namespace
        self.cmd(
            'sb namespace create --resource-group {rg} --name {namespacename} '
            '--location {loc} --tags {tags} --sku-name {sku} --sku-tier {tier}',
            checks=[self.check('sku.name', self.kwargs['sku'])])

        # Get Created Namespace
        self.cmd('sb namespace show --resource-group {rg} --name {namespacename}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Create Topic
        self.cmd(
            'sb topic create --resource-group {rg} --namespace-name {namespacename} --name {topicname} ',
            checks=[self.check('name', self.kwargs['topicname'])])

        # Get Topic
        self.cmd(
            'sb topic show --resource-group {rg} --namespace-name {namespacename} --name {topicname} ',
            checks=[self.check('name', self.kwargs['topicname'])])

        # Topic List
        self.cmd('sb topic list --resource-group {rg} --namespace-name {namespacename}')

        # Create Authoriazation Rule
        self.cmd('sb topic authorizationrule create --resource-group {rg} --namespace-name {namespacename}'
                 ' --topic-name {topicname} --name {authoname} --access-rights {accessrights}',
                 checks=[self.check('name', self.kwargs['authoname'])])

        # Get Create Authorization Rule
        self.cmd('sb topic authorizationrule show --resource-group {rg} --namespace-name {namespacename} --topic-name {topicname} --name {authoname}',
                 checks=[self.check('name', self.kwargs['authoname'])])

        # Get Authorization Rule Listkeys
        self.cmd(
            'sb topic authorizationrule list-keys --resource-group {rg} --namespace-name {namespacename}'
            ' --topic-name {topicname} --name {authoname}')

        # Regeneratekeys - Primary
        self.cmd(
            'sb topic authorizationrule regenerate-keys --resource-group {rg} --namespace-name {namespacename}'
            ' --topic-name {topicname} --name {authoname} --key {primary}')

        # Regeneratekeys - Secondary
        self.cmd(
            'sb topic authorizationrule regenerate-keys --resource-group {rg} --namespace-name {namespacename}'
            ' --topic-name {topicname} --name {authoname} --key {secondary}')

        # Delete Topic AuthorizationRule
        self.cmd(
            'sb topic authorizationrule delete --resource-group {rg} --namespace-name {namespacename}'
            ' --topic-name {topicname} --name {authoname}')

        # Delete Topic
        self.cmd('sb topic delete --resource-group {rg} --namespace-name {namespacename} --name {topicname}')

        # Delete Namespace
        self.cmd('sb namespace delete --resource-group {rg} --name {namespacename}')

    @ResourceGroupPreparer(name_prefix='cli_test_sb_subscription')
    def test_sb_subscription(self, resource_group):
        self.kwargs.update({
            'loc': 'westus2',
            'rg': resource_group,
            'namespacename': self.create_random_name(prefix='sb-nscli', length=20),
            'tags': {'tag1: value1', 'tag2: value2'},
            'sku': 'Standard',
            'tier': 'Standard',
            'authoname': self.create_random_name(prefix='cliAutho', length=20),
            'defaultauthorizationrule': 'RootManageSharedAccessKey',
            'accessrights': 'Send, Listen',
            'primary': 'PrimaryKey',
            'secondary': 'SecondaryKey',
            'topicname': self.create_random_name(prefix='sb-topiccli', length=25),
            'topicauthoname': self.create_random_name(prefix='cliTopicAutho', length=25),
            'subscriptionname': self.create_random_name(prefix='sb-subscli', length=25)
        })

        # Create Namespace
        self.cmd('sb namespace create --resource-group {rg} --name {namespacename} '
                 '--location {loc} --tags {tags} --sku-name {sku} --sku-tier {tier}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Get Created Namespace
        self.cmd('sb namespace show --resource-group {rg} --name {namespacename}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Create Topic
        self.cmd('sb topic create --resource-group {rg} --namespace-name {namespacename} --name {topicname} ',
                 checks=[self.check('name', self.kwargs['topicname'])])

        # Get Topic
        self.cmd('sb topic show --resource-group {rg} --namespace-name {namespacename} --name {topicname} ',
                 checks=[self.check('name', self.kwargs['topicname'])])

        # Create Subscription
        self.cmd('sb subscription create --resource-group {rg} --namespace-name {namespacename}'
                 ' --topic-name {topicname} --name {subscriptionname}',
                 checks=[self.check('name', self.kwargs['subscriptionname'])])

        # Get Create Subscription
        self.cmd('sb subscription show --resource-group {rg} --namespace-name {namespacename}'
                 ' --topic-name {topicname} --name {subscriptionname}',
                 checks=[self.check('name', self.kwargs['subscriptionname'])])

        # Get list of Subscription+
        self.cmd('sb subscription list --resource-group {rg} --namespace-name {namespacename} --topic-name {topicname}')

        # Delete Subscription
        self.cmd(
            'sb subscription delete --resource-group {rg} --namespace-name {namespacename} --topic-name {topicname} --name {subscriptionname}')

        # Delete Topic
        self.cmd('sb topic delete --resource-group {rg} --namespace-name {namespacename} --name {topicname}')

        # Delete Namespace
        self.cmd('sb namespace delete --resource-group {rg} --name {namespacename}')

    @ResourceGroupPreparer(name_prefix='cli_test_sb_rules')
    def test_sb_rules(self, resource_group):
        self.kwargs.update({
            'loc': 'westus2',
            'rg': resource_group,
            'namespacename': self.create_random_name(prefix='sb-nscli', length=20),
            'tags': {'tag1: value1', 'tag2: value2'},
            'sku': 'Standard',
            'tier': 'Standard',
            'authoname': self.create_random_name(prefix='cliAutho', length=20),
            'defaultauthorizationrule': 'RootManageSharedAccessKey',
            'accessrights': 'Listen',
            'primary': 'PrimaryKey',
            'secondary': 'SecondaryKey',
            'topicname': self.create_random_name(prefix='sb-topiccli', length=25),
            'topicauthoname': self.create_random_name(prefix='cliTopicAutho', length=25),
            'subscriptionname': self.create_random_name(prefix='sb-subscli', length=25),
            'rulename': self.create_random_name(prefix='sb-rulecli', length=25),
            'sqlexpression': 'test=test'
        })

        # Create Namespace
        self.cmd('sb namespace create --resource-group {rg} --name {namespacename} '
                 '--location {loc} --tags {tags} --sku-name {sku} --sku-tier {tier}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Get Created Namespace
        self.cmd('sb namespace show --resource-group {rg} --name {namespacename}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Create Topic
        self.cmd('sb topic create --resource-group {rg} --namespace-name {namespacename} --name {topicname} ',
                 checks=[self.check('name', self.kwargs['topicname'])])

        # Get Topic
        self.cmd('sb topic show --resource-group {rg} --namespace-name {namespacename} --name {topicname} ',
                 checks=[self.check('name', self.kwargs['topicname'])])

        # Create Subscription
        self.cmd('sb subscription create --resource-group {rg} --namespace-name {namespacename}'
                 ' --topic-name {topicname} --name {subscriptionname}',
                 checks=[self.check('name', self.kwargs['subscriptionname'])])

        # Get Create Subscription
        self.cmd('sb subscription show --resource-group {rg} --namespace-name {namespacename} --topic-name {topicname}'
                 ' --name {subscriptionname}', checks=[self.check('name', self.kwargs['subscriptionname'])])

        # Create Rules
        self.cmd('sb rule create --resource-group {rg} --namespace-name {namespacename} --topic-name {topicname}'
                 ' --subscription-name {subscriptionname} --name {rulename} --filter-sql-expression {sqlexpression}',
                 checks=[self.check('name', self.kwargs['rulename'])])

        # Get Created Rules
        self.cmd('sb rule show --resource-group {rg} --namespace-name {namespacename} --topic-name {topicname}'
                 ' --subscription-name {subscriptionname} --name {rulename}',
                 checks=[self.check('name', self.kwargs['rulename'])])

        # Get Rules List By Subscription
        self.cmd('sb rule list --resource-group {rg} --namespace-name {namespacename} --topic-name {topicname}'
                 ' --subscription-name {subscriptionname}')

        # Delete create rule
        self.cmd('sb rule delete --resource-group {rg} --namespace-name {namespacename} --topic-name {topicname} --subscription-name {subscriptionname} --name {rulename}')

        # Delete create Subscription
        self.cmd('sb subscription delete --resource-group {rg} --namespace-name {namespacename} --topic-name {topicname} --name {subscriptionname}')

        # Delete Topic
        self.cmd('sb topic delete --resource-group {rg} --namespace-name {namespacename} --name {topicname}')

        # Delete Namespace
        self.cmd('sb namespace delete --resource-group {rg} --name {namespacename}')

    @ResourceGroupPreparer(name_prefix='cli_test_sb_alias')
    def test_sb_alias(self, resource_group):

        self.kwargs.update({
            'loc_south': 'SouthCentralUS',
            'loc_north': 'NorthCentralUS',
            'rg': resource_group,
            'namespacenameprimary': self.create_random_name(prefix='sb-nscli', length=20),
            'namespacenamesecondary': self.create_random_name(prefix='sb-nscli', length=20),
            'tags': {'tag1: value1', 'tag2: value2'},
            'sku': 'Premium',
            'tier': 'Premium',
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

        self.cmd('sb namespace check-name-availability --name {namespacenameprimary}',
                 checks=[self.check('nameAvailable', True)])

        # Create Namespace - Primary
        self.cmd('sb namespace create --resource-group {rg} --name {namespacenameprimary} --location {loc_south} --tags {tags} --sku-name {sku} --sku-tier {tier}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Get Created Namespace - Primary
        self.cmd('sb namespace show --resource-group {rg} --name {namespacenameprimary}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Create Namespace - Secondary
        self.cmd('sb namespace create --resource-group {rg} --name {namespacenamesecondary}'
                 ' --location {loc_north} --tags {tags} --sku-name {sku} --sku-tier {tier}',
                 checks=[self.check('sku.name', self.kwargs['sku'])])

        # Get Created Namespace - Secondary
        getnamespace2result = self.cmd('sb namespace show --resource-group {rg} --name {namespacenamesecondary}',
                                       checks=[self.check('sku.name', self.kwargs['sku'])]).output

        # Create Authoriazation Rule
        self.cmd('sb namespace authorizationrule create --resource-group {rg} --namespace-name {namespacenameprimary} --name {authoname} --access-rights {accessrights}', checks=[self.check('name', self.kwargs['authoname'])])

        partnernamespaceid = json.loads(getnamespace2result)['id']
        self.kwargs.update({'id': partnernamespaceid})
        # Get Create Authorization Rule
        self.cmd('sb namespace authorizationrule show --resource-group {rg} --namespace-name {namespacenameprimary}'
                 ' --name {authoname}', checks=[self.check('name', self.kwargs['authoname'])])

        # CheckNameAvailability - Alias

        self.cmd('sb alias check-name-availability --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}', checks=[self.check('nameAvailable', True)])

        # Create alias
        self.cmd('sb alias create  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname} --partner-namespace {id}')

        # get alias - Primary
        self.cmd('sb alias show  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}')

        # get alias - Secondary
        self.cmd('sb alias show  --resource-group {rg} --namespace-name {namespacenamesecondary} --alias {aliasname}')

        getaliasprimarynamespace = self.cmd(
            'sb alias show  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}').output

        # check for the Alias Provisioning succeeded
        while json.loads(getaliasprimarynamespace)['provisioningState'] != ProvisioningStateDR.succeeded.value:
            time.sleep(30)
            getaliasprimarynamespace = self.cmd(
                'sb alias show  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}').output

        # Break Pairing
        self.cmd('sb alias break-pairing  --resource-group {rg} --namespace-name {namespacenameprimary}'
                 ' --alias {aliasname}')

        getaliasafterbreak = self.cmd(
            'sb alias show  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}').output

        # check for the Alias Provisioning succeeded
        while json.loads(getaliasafterbreak)['provisioningState'] != ProvisioningStateDR.succeeded.value:
            time.sleep(30)
            getaliasafterbreak = self.cmd(
                'sb alias show  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}').output

        # Create alias
        self.cmd('sb alias create  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}'
                 ' --partner-namespace {id}')

        getaliasaftercreate = self.cmd(
            'sb alias show  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}').output

        # check for the Alias Provisioning succeeded
        while json.loads(getaliasaftercreate)['provisioningState'] != ProvisioningStateDR.succeeded.value:
            time.sleep(30)
            getaliasaftercreate = self.cmd(
                'sb alias show  --resource-group {rg} --namespace-name {namespacenameprimary} --alias {aliasname}').output

        # FailOver
        self.cmd('sb alias fail-over  --resource-group {rg} --namespace-name {namespacenamesecondary}'
                 ' --alias {aliasname}')

        getaliasafterfail = self.cmd(
            'sb alias show  --resource-group {rg} --namespace-name {namespacenamesecondary} --alias {aliasname}').output

        # check for the Alias Provisioning succeeded
        while json.loads(getaliasafterfail)['provisioningState'] != ProvisioningStateDR.succeeded.value:
            time.sleep(30)
            getaliasafterfail = self.cmd(
                'sb alias show  --resource-group {rg} --namespace-name {namespacenamesecondary} --alias {aliasname}').output

        # Delete Alias
        self.cmd('sb alias delete  --resource-group {rg} --namespace-name {namespacenamesecondary} --alias {aliasname}')

        # Delete Namespace - primary
        self.cmd('sb namespace delete --resource-group {rg} --name {namespacenameprimary}')

        # Delete Namespace - secondary
        self.cmd('sb namespace delete --resource-group {rg} --name {namespacenamesecondary}')
