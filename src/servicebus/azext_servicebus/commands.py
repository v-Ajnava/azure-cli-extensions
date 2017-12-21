# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-statements

from azure.cli.core.commands import CliCommandType
from azext_servicebus._client_factory import (namespaces_mgmt_client_factory,
                                              queues_mgmt_client_factory,
                                              topics_mgmt_client_factory,
                                              subscriptions_mgmt_client_factory,
                                              rules_mgmt_client_factory,
                                              disaster_recovery_mgmt_client_factory,)


def load_command_table(self, _):

    sb_namespace_util = CliCommandType(
        operations_tmpl='azext_servicebus.servicebus.operations.namespaces_operations#NamespacesOperations.{}',
        client_factory=namespaces_mgmt_client_factory,
        client_arg_name='self'
    )

    sb_queue_util = CliCommandType(
        operations_tmpl='azext_servicebus.servicebus.operations.queues_operations#QueuesOperations.{}',
        client_factory=queues_mgmt_client_factory,
        client_arg_name='self'
    )

    sb_topic_util = CliCommandType(
        operations_tmpl='azext_servicebus.servicebus.operations.topics_operations#TopicsOperations.{}',
        client_factory=topics_mgmt_client_factory,
        client_arg_name='self'
    )

    sb_subscriptions_util = CliCommandType(
        operations_tmpl='azext_servicebus.servicebus.operations.subscriptions_operations#SubscriptionsOperations.{}',
        client_factory=subscriptions_mgmt_client_factory,
        client_arg_name='self'
    )

    sb_rule_util = CliCommandType(
        operations_tmpl='azext_servicebus.servicebus.operations.rules_operations#RulesOperations.{}',
        client_factory=rules_mgmt_client_factory,
        client_arg_name='self'
    )

    sb_geodr_util = CliCommandType(
        operations_tmpl='azext_servicebus.servicebus.operations.disaster_recovery_configs_operations#DisasterRecoveryConfigsOperations.{}',
        client_factory=disaster_recovery_mgmt_client_factory,
        client_arg_name='self'
    )

# Namespace Region
    with self.command_group('sb namespace', sb_namespace_util, client_factory=namespaces_mgmt_client_factory) as g:
        g.custom_command('create', 'cli_namespace_create')
        g.command('show', 'get')
        g.custom_command('list', 'cli_namespace_list')
        g.command('delete', 'delete')
        g.command('check-name-availability', 'check_name_availability_method')

    with self.command_group('sb namespace authorizationrule', sb_namespace_util, client_factory=namespaces_mgmt_client_factory) as g:
        g.custom_command('create', 'cli_namespaceautho_create',)
        g.command('show', 'get_authorization_rule')
        g.command('list', 'list_authorization_rules')
        g.command('list-keys', 'list_keys')
        g.command('regenerate-keys', 'regenerate_keys')
        g.command('delete', 'delete_authorization_rule')

# Queue Region
    with self.command_group('sb queue', sb_queue_util, client_factory=queues_mgmt_client_factory) as g:
        g.custom_command('create', 'cli_sbqueue_create')
        g.command('show', 'get')
        g.command('list', 'list_by_namespace')
        g.command('delete', 'delete')

    with self.command_group('sb queue authorizationrule', sb_queue_util, client_factory=queues_mgmt_client_factory) as g:
        g.custom_command('create', 'cli_sbqueueautho_create',)
        g.command('show', 'get_authorization_rule')
        g.command('list', 'list_authorization_rules')
        g.command('list-keys', 'list_keys')
        g.command('regenerate-keys', 'regenerate_keys')
        g.command('delete', 'delete_authorization_rule')

# Topic Region
    with self.command_group('sb topic', sb_topic_util, client_factory=topics_mgmt_client_factory) as g:
        g.custom_command('create', 'cli_sbtopic_create')
        g.command('show', 'get')
        g.command('list', 'list_by_namespace')
        g.command('delete', 'delete')

    with self.command_group('sb topic authorizationrule', sb_topic_util, client_factory=topics_mgmt_client_factory) as g:
        g.custom_command('create', 'cli_sbtopicautho_create')
        g.command('show', 'get_authorization_rule')
        g.command('list', 'list_authorization_rules')
        g.command('list-keys', 'list_keys')
        g.command('regenerate-keys', 'regenerate_keys')
        g.command('delete', 'delete_authorization_rule')

# Subscription Region
    with self.command_group('sb subscription', sb_subscriptions_util, client_factory=subscriptions_mgmt_client_factory) as g:
        g.custom_command('create', 'cli_sbsubscription_create')
        g.command('show', 'get')
        g.command('list', 'list_by_topic')
        g.command('delete', 'delete')

# Rules Region
    with self.command_group('sb rule', sb_rule_util, client_factory=rules_mgmt_client_factory) as g:
        g.custom_command('create', 'cli_rules_create')
        g.command('show', 'get')
        g.command('list', 'list_by_subscriptions')
        g.command('delete', 'delete')

# DisasterRecoveryConfigs Region
    with self.command_group('sb alias', sb_geodr_util, client_factory=disaster_recovery_mgmt_client_factory) as g:
        g.command('create', 'create_or_update')
        g.command('show', 'get')
        g.command('list', 'list')
        g.command('break-pairing', 'break_pairing')
        g.command('fail-over', 'fail_over')
        g.command('check-name-availability', 'check_name_availability_method')
        g.command('list-authorization_rules', 'list_authorization_rules')
        g.command('show-authorization-rule', 'get_authorization_rule')
        g.command('list-keys', 'list_keys')
        g.command('delete', 'delete')
