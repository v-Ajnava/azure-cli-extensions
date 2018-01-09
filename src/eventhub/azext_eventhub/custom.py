# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

from knack.util import CLIError

from azext_eventhub._utils import accessrights_converter

from azext_eventhub.eventhub.models import (EHNamespace, Sku, Eventhub, CaptureDescription, Destination)



# Namespace Region
def cli_namespace_create(client, resource_group_name, namespace_name, location, tags=None, sku='Standard', skutier=None, capacity=None, is_auto_inflate_enabled=None, maximum_throughput_units=None):
    return client.create_or_update(resource_group_name, namespace_name, EHNamespace(location, tags,
                                                                                    Sku(sku,
                                                                                        skutier,
                                                                                        capacity), is_auto_inflate_enabled, maximum_throughput_units))


def cli_namespace_list(client, resource_group_name=None, namespace_name=None):
    cmd_result = None
    if resource_group_name and namespace_name:
        cmd_result = client.get(resource_group_name, namespace_name)

    if resource_group_name and not namespace_name:
        cmd_result = client.list_by_resource_group(resource_group_name, namespace_name)

    if not resource_group_name and not namespace_name:
        cmd_result = client.list(resource_group_name, namespace_name)

    if not cmd_result:
        raise CLIError('--resource-group name required when namespace name is provided')

    return cmd_result


# Namespace Authorization rule:
def cli_namespaceautho_create(client, resource_group_name, namespace_name, name, accessrights=None):
    return client.create_or_update_authorization_rule(resource_group_name, namespace_name, name,
                                                      accessrights_converter(accessrights))


# Eventhub Region
def cli_eheventhub_create(client, resource_group_name, namespace_name, name, message_retention_in_days=None, partition_count=None, status=None,
                          capture_description_enabled=None, capture_description_encoding=None, capture_description_interval_in_seconds=None, capture_description_size_limit_in_bytes=None, destination_name=None, destination_storage_account_resource_id=None, destination_blob_container=None, destination_archive_name_format=None):
    eventhubparameter1 = Eventhub()
    if message_retention_in_days:
        eventhubparameter1.message_retention_in_days = message_retention_in_days

    if partition_count:
        eventhubparameter1.partition_count = partition_count

    if status:
        eventhubparameter1.status = status

    if capture_description_enabled and capture_description_enabled is True:
        eventhubparameter1.capture_description = CaptureDescription(
            enabled=capture_description_enabled,
            encoding=capture_description_encoding,
            interval_in_seconds=capture_description_interval_in_seconds,
            size_limit_in_bytes=capture_description_size_limit_in_bytes,
            destination=Destination(
                name=destination_name,
                storage_account_resource_id=destination_storage_account_resource_id,
                blob_container=destination_blob_container,
                archive_name_format=destination_archive_name_format)
        )
    print("Name of EventHub: {}".format(name))
    return client.create_or_update(resource_group_name, namespace_name, name, eventhubparameter1)


def cli_eheventhubautho_create(client, resource_group_name, namespace_name, event_hub_name, name, accessrights=None):
    return client.create_or_update_authorization_rule(resource_group_name, namespace_name, event_hub_name, name,
                                                      accessrights_converter(accessrights))


def cli_ehconsumergroup_create(client, resource_group_name, namespace_name, event_hub_name, name, user_metadata):
    return client.create_or_update(resource_group_name, namespace_name, event_hub_name, name,user_metadata)
