# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

helps['eh'] = """
    type: group
    short-summary: Manage Azure EventHub namespace, eventhub, consumergroup and alias (Disaster Recovery Configuration)

    """

helps['eh namespace'] = """
    type: group
    short-summary: Manage Azure EventHub namespace and authorization-rule

    """

helps['eh eventhub'] = """
    type: group
    short-summary: Manage Azure EventHub eventhub and authorization-rule

    """

helps['eh consumergroup'] = """
    type: group
    short-summary: Manage Azure EventHub consumergroup

    """

helps['eh alias'] = """
    type: group
    short-summary: Manage Azure EventHub Alias (Disaster Recovery Configuration)

    """

helps['eh namespace check-name-availability'] = """
    type: command
    short-summary: check for the availability of the given name for the Namespace
    examples:
        - name: Create a new topic.
          text: az eh namespace check_name_availability --name mynamespace

    """

helps['eh namespace create'] = """
    type: command
    short-summary: Creates the EventHub Namespace
    examples:
        - name: Create a new namespace.
          text: helps['az eh namespace create --resource-group myresourcegroup --name mynamespace --location westus
           --tags ['tag1: value1', 'tag2: value2'] --sku-name Standard --sku-tier Standard' --is-auto-inflate-enabled False --maximum-throughput-units 30]

    """

helps['eh namespace show'] = """
    type: command
    short-summary: shows the Namespace Details
    examples:
        - name: shows the Namespace details.
          text: helps['az eh namespace show --resource-group myresourcegroup --name mynamespace']

    """

helps['eh namespace list'] = """
    type: command
    short-summary: List the Namespaces by ResourceGroup or By subscription
    examples:
        - name: Get the Namespaces by resource Group.
          text: helps['az eh namespace list --resource-group myresourcegroup']
        - name: Get the Namespaces by Subscription.
          text: helps['az eh namespace list']

    """

helps['eh namespace delete'] = """
    type: command
    short-summary: Deletes the Namespaces
    examples:
        - name: Deletes the Namespace
          text: helps['az eh namespace delete --resource-group myresourcegroup --name mynamespace']

    """

helps['eh namespace authorizationrule create'] = """
    type: command
    short-summary: Creates Authorization rule for the given Namespace
    examples:
        - name: Creates Authorization rules
          text: helps['az eh namespace authorizationrule create --resource-group myresourcegroup --namespace-name mynamespace
           --name myauthorule --access-rights [Send, Listen]']

    """

helps['eh namespace authorizationrule get'] = """
    type: command
    short-summary: Shows the details of AuthorizatioRule
    examples:
        - name: Shows the details of AuthorizatioRule
          text: helps['az eh namespace authorizationrule show --resource-group myresourcegroup --namespace-name mynamespace
           --name myauthorule']

    """

helps['eh namespace authorizationrule list'] = """
    type: command
    short-summary: Shows the list of AuthorizatioRule by Namespace
    examples:
        - name: Shows the list of AuthorizatioRule by Namespace
          text: helps['az eh namespace authorizationrule show --resource-group myresourcegroup --namespace-name mynamespace']

    """

helps['eh namespace authorizationrule list-keys'] = """
    type: command
    short-summary: Shows the connectionstrings of AuthorizatioRule for the namespace
    examples:
        - name: Shows the connectionstrings of AuthorizatioRule for the namespace.
          text: helps['az eh namespace authorizationrule list-keys --resource-group myresourcegroup --namespace-name mynamespace
           --name myauthorule']

    """

helps['eh namespace authorizationrule regenerate-keys'] = """
    type: command
    short-summary: Regenerate the connectionstrings of AuthorizatioRule for the namespace.
    examples:
        - name: Regenerate the connectionstrings of AuthorizatioRule for the namespace.
          text: helps['az eh namespace authorizationrule regenerate-keys --resource-group myresourcegroup
           --namespace-name mynamespace --name myauthorule --key PrimaryKey']

    """

helps['eh namespace authorizationrule delete'] = """
    type: command
    short-summary: Deletes the AuthorizatioRule of the namespace.
    examples:
        - name: Deletes the AuthorizatioRule of the namespace.
          text: helps['az eh namespace authorizationrule delete --resource-group myresourcegroup --namespace-name mynamespace
           --name myauthorule']

    """

helps['eh eventhub create'] = """
    type: command
    short-summary: Creates the EventHub Eventhub
    examples:
        - name: Create a new Eventhub.
          text: helps['az eh eventhub create --resource-group myresourcegroup --namespace-name mynamespace --name myeventhub --message-retention-in-days 4 ---partition-count 15']

    """

helps['eh eventhub show'] = """
    type: command
    short-summary: shows the Eventhub Details
    examples:
        - name: Shows the Eventhub details.
          text: helps['az eh eventhub show --resource-group myresourcegroup --namespace-name mynamespace --name myeventhub']

    """

helps['eh eventhub list'] = """
    type: command
    short-summary: List the EventHub by Namepsace
    examples:
        - name: Get the Eventhubs by Namespace.
          text: helps['az eh eventhub list --resource-group myresourcegroup --namespace-name mynamespace']

    """

helps['eh eventhub delete'] = """
    type: command
    short-summary: Deletes the Eventhub
    examples:
        - name: Deletes the Eventhub
          text: helps['az eh eventhub delete --resource-group myresourcegroup --namespace-name mynamespace --name myeventhub']

    """

helps['eh eventhub authorizationrule create'] = """
    type: command
    short-summary: Creates Authorization rule for the given Eventhub
    examples:
        - name: Creates Authorization rules
          text: helps['az eh eventhub authorizationrule create --resource-group myresourcegroup --namespace-name mynamespace
           --event-hub-name myeventhub --name myauthorule --access-rights [Listen]']

    """

helps['eh eventhub authorizationrule show'] = """
    type: command
    short-summary: shows the details of AuthorizatioRule
    examples:
        - name: shows the details of AuthorizatioRule
          text: helps['az eh eventhub authorizationrule show --resource-group myresourcegroup --namespace-name mynamespace
           --event-hub-name myeventhub --name myauthorule']

    """

helps['eh eventhub authorizationrule list'] = """
    type: command
    short-summary: shows the list of AuthorizatioRule by Eventhub
    examples:
        - name: shows the list of AuthorizatioRule by Eventhub
          text: helps['az eh eventhub authorizationrule show --resource-group myresourcegroup --namespace-name mynamespace
           --event-hub-name myeventhub']

    """

helps['eh eventhub authorizationrule list-keys'] = """
    type: command
    short-summary: Shows the connectionstrings of AuthorizatioRule for the Eventhub.
    examples:
        - name: Shows the connectionstrings of AuthorizatioRule for the eventhub.
          text: helps['az eh eventhub authorizationrule list-keys --resource-group myresourcegroup --namespace-name mynamespace --event-hub-name myeventhub --name myauthorule']

    """

helps['eh eventhub authorizationrule regenerate-keys'] = """
    type: command
    short-summary: Regenerate the connectionstrings of AuthorizatioRule for the namespace.
    examples:
        - name: Regenerate the connectionstrings of AuthorizatioRule for the namespace.
          text: helps['az eh eventhub authorizationrule regenerate-keys --resource-group myresourcegroup --namespace-name mynamespace --event-hub-name myeventhub --name myauthorule --key PrimaryKey']

    """

helps['eh eventhub authorizationrule delete'] = """
    type: command
    short-summary: Deletes the AuthorizatioRule of the Eventhub.
    examples:
        - name: Deletes the AuthorizatioRule of the Eventhub.
          text: helps['az eh eventhub authorizationrule delete --resource-group myresourcegroup --namespace-name mynamespace --event-hub-name myeventhub --name myauthorule']

    """

helps['eh consumergroup create'] = """
    type: command
    short-summary: Creates the EventHub ConsumerGroup
    examples:
        - name: Create a new ConsumerGroup.
          text: helps['az eh consumergroup create --resource-group myresourcegroup --namespace-name mynamespace --event-hub-name myeventhub --name myconsumergroup']

    """

helps['eh consumergroup show'] = """
    type: command
    short-summary: Shows the ConsumerGroup Details
    examples:
        - name: Shows the ConsumerGroup details.
          text: helps['az eh consumergroup get --resource-group myresourcegroup --namespace-name mynamespace --event-hub-name myeventhub --name myconsumergroup']

    """

helps['eh consumergroup list'] = """
    type: command
    short-summary: List the ComsumerGroup by Eventhub
    examples:
        - name: Shows the ComsumerGroup by Eventhub.
          text: helps['az eh consumergroup get --resource-group myresourcegroup --namespace-name mynamespace --event-hub-name myeventhub']

    """

helps['eh consumergroup delete'] = """
    type: command
    short-summary: Deletes the ConsumerGroup
    examples:
        - name: Deletes the ConsumerGroup
          text: helps['az eh consumergroup delete --resource-group myresourcegroup --namespace-name mynamespace --event-hub-name myeventhub --name myconsumergroup']

    """

helps['eh alias check_name_availability'] = """
    type: command
    short-summary: Check the availability of the Alias (Geo DR Configuration) Name
    examples:
        - name: Check the availability of the Alias (Geo DR Configuration) Name
          text: helps['az eh alias check_name_availability --resource-group myresourcegroup --namespace-name primarynamespace
           --alias myaliasname']

    """

helps['eh alias create'] = """
    type: command
    short-summary: Creats Alias (Geo DR Configuration) for the give Namespace
    examples:
        - name: Creats Alias (Geo DR Configuration) for the give Namespace
          text: helps['az eh alias create  --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname --partner-namespace {id}']

    """

helps['eh alias show'] = """
    type: command
    short-summary: shows details of Alias (Geo DR Configuration) for Primay/Secondary Namespace
    examples:
        - name:  show details of Alias (Geo DR Configuration)  of the Primary Namespace
          text: helps['az eh alias show  --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname']
        - name:  Get details of Alias (Geo DR Configuration)  of the Secondary Namespace
           text: helps['az eh alias show  --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname']

    """

helps['eh alias break-pairing'] = """
    type: command
    short-summary: Disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces
    examples:
        - name:  Disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces
          text: helps['az eh alias break-pairing  --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname']

    """

helps['eh alias fail-over'] = """
    type: command
    short-summary: Envokes GEO DR failover and reconfigure the alias to point to the secondary namespace
    examples:
        - name:  Envokes GEO DR failover and reconfigure the alias to point to the secondary namespace
          text: helps['az eh alias fail-over  --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname']

    """

helps['eh alias delete'] = """
    type: command
    short-summary: Delete Alias(Disaster Recovery configuration) request accepted
    examples:
        - name:  Delete Alias(Disaster Recovery configuration) request accepted
          text: helps['az eh alias delete  --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname']

    """
