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


# Queue Region
def cli_eheventhub_create(client, resource_group_name, namespace_name, name, messageretentionindays=None, partitioncount=None, status=None,
                          enabled=None, encoding=None, intervalinseconds=None, sizelimitinbytes=None, destination_name=None, storageaccountresourceid=None, blobcontainer=None, archivenameformat=None):
    eventhubparameter = Eventhub(
        name=name,
        message_retention_in_days=messageretentionindays,
        partition_count=partitioncount,
        status=status,
        capture_description=CaptureDescription(
            enabled=enabled,
            encoding=encoding,
            interval_in_seconds=intervalinseconds,
            size_limit_in_bytes=sizelimitinbytes,
            destination=Destination(
                name=destination_name,
                storage_account_resource_id=storageaccountresourceid,
                blob_container=blobcontainer,
                archive_name_format=archivenameformat)
        )
    )
    return client.create_or_update(resource_group_name, namespace_name, name, eventhubparameter)


def cli_eheventhubautho_create(client, resource_group_name, namespace_name, eventhub_name, name, accessrights=None):
    return client.create_or_update_authorization_rule(resource_group_name, namespace_name, eventhub_name, name,
                                                      accessrights_converter(accessrights))
