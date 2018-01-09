# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-statements

from azure.cli.core.commands import CliCommandType
from azext_eventhub._client_factory import (namespaces_mgmt_client_factory, event_hub_mgmt_client_factory,
                                            consumer_groups_mgmt_client_factory,
                                            disaster_recovery_mgmt_client_factory)


def load_command_table(self, _):

    eh_namespace_util = CliCommandType(
        operations_tmpl='azext_eventhub.eventhub.operations.namespaces_operations#NamespacesOperations.{}',
        client_factory=namespaces_mgmt_client_factory,
        client_arg_name='self'
    )

    eh_event_hub_util = CliCommandType(
        operations_tmpl='azext_eventhub.eventhub.operations.event_hubs_operations#EventHubsOperations.{}',
        client_factory=event_hub_mgmt_client_factory,
        client_arg_name='self'
    )

    eh_consumer_groups_util = CliCommandType(
        operations_tmpl='azext_eventhub.eventhub.operations.consumer_groups_operations#ConsumerGroupsOperations.{}',
        client_factory=consumer_groups_mgmt_client_factory,
        client_arg_name='self'
    )

    eh_geodr_util = CliCommandType(
        operations_tmpl='azext_eventhub.eventhub.operations.disaster_recovery_configs_operations#DisasterRecoveryConfigsOperations.{}',
        client_factory=disaster_recovery_mgmt_client_factory,
        client_arg_name='self'
    )

# Namespace Region
    with self.command_group('eh namespace', eh_namespace_util, client_factory=namespaces_mgmt_client_factory) as g:
        g.custom_command('create', 'cli_namespace_create')
        g.command('show', 'get')
        g.custom_command('list', 'cli_namespace_list')
        g.command('delete', 'delete')
        g.command('check-name-availability', 'check_name_availability')

    with self.command_group('eh namespace authorizationrule', eh_namespace_util, client_factory=namespaces_mgmt_client_factory) as g:
        g.custom_command('create', 'cli_namespaceautho_create',)
        g.command('show', 'get_authorization_rule')
        g.command('list', 'list_authorization_rules')
        g.command('list-keys', 'list_keys')
        g.command('regenerate-keys', 'regenerate_keys')
        g.command('delete', 'delete_authorization_rule')

# EventHub Region
    with self.command_group('eh eventhub', eh_event_hub_util, client_factory=event_hub_mgmt_client_factory) as g:
        g.custom_command('create', 'cli_eheventhub_create')
        g.command('show', 'get')
        g.command('list', 'list_by_namespace')
        g.command('delete', 'delete')

    with self.command_group('eh eventhub authorizationrule', eh_event_hub_util, client_factory=event_hub_mgmt_client_factory) as g:
        g.custom_command('create', 'cli_eheventhubautho_create',)
        g.command('show', 'get_authorization_rule')
        g.command('list', 'list_authorization_rules')
        g.command('list-keys', 'list_keys')
        g.command('regenerate-keys', 'regenerate_keys')
        g.command('delete', 'delete_authorization_rule')

# ConsumerGroup Region
    with self.command_group('eh consumergroup', eh_consumer_groups_util, client_factory=consumer_groups_mgmt_client_factory) as g:
        g.command('create', 'create_or_update')
        g.command('show', 'get')
        g.command('list', 'list_by_event_hub')
        g.command('delete', 'delete')

# DisasterRecoveryConfigs Region
    with self.command_group('eh alias', eh_geodr_util, client_factory=disaster_recovery_mgmt_client_factory) as g:
        g.command('create', 'create_or_update')
        g.command('show', 'get')
        g.command('list', 'list')
        g.command('break-pairing', 'break_pairing')
        g.command('fail-over', 'fail_over')
        g.command('check-name-availability', 'check_name_availability')
        g.command('list-authorization_rules', 'list_authorization_rules')
        g.command('show-authorization-rule', 'get_authorization_rule')
        g.command('list-keys', 'list_keys')
        g.command('delete', 'delete')
