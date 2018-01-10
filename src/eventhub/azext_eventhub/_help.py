# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

helps['eventhubs'] = """
    type: group
    short-summary: Manage Azure EventHub namespace, eventhub, consumergroup and Geo Disaster Recovery configuration - Alias

    """

helps['eventhubs namespace'] = """
    type: group
    short-summary: Manage Azure EventHub namespace and authorization-rule

    """

helps['eventhubs eventhub'] = """
    type: group
    short-summary: Manage Azure EventHub eventhub and authorization-rule

    """

helps['eventhubs consumergroup'] = """
    type: group
    short-summary: Manage Azure EventHub consumergroup

    """

helps['eventhubs georecovery-alias'] = """
    type: group
    short-summary: Manage Azure EventHub Geo Disaster Recovery configuration - Alias

    """

helps['eventhubs namespace check-name-availability'] = """
    type: command
    short-summary: check for the availability of the given name for the Namespace
    examples:
        - name: Create a new topic.
          text: az eh namespace check_name_availability --name mynamespace

    """

helps['eventhubs namespace create'] = """
    type: command
    short-summary: Creates the EventHub Namespace
    examples:
        - name: Create a new namespace.
          text: helps['az eh namespace create --resource-group myresourcegroup --name mynamespace --location westus
           --tags ['tag1: value1', 'tag2: value2'] --sku-name Standard --sku-tier Standard' --is-auto-inflate-enabled False --maximum-throughput-units 30]

    """

helps['eventhubs namespace show'] = """
    type: command
    short-summary: shows the Namespace Details
    examples:
        - name: shows the Namespace details.
          text: helps['az eh namespace show --resource-group myresourcegroup --name mynamespace']

    """

helps['eventhubs namespace list'] = """
    type: command
    short-summary: List the Namespaces by ResourceGroup or By subscription
    examples:
        - name: Get the Namespaces by resource Group.
          text: helps['az eh namespace list --resource-group myresourcegroup']
        - name: Get the Namespaces by Subscription.
          text: helps['az eh namespace list']

    """

helps['eventhubs namespace delete'] = """
    type: command
    short-summary: Deletes the Namespaces
    examples:
        - name: Deletes the Namespace
          text: helps['az eh namespace delete --resource-group myresourcegroup --name mynamespace']

    """

helps['eventhubs namespace authorizationrule create'] = """
    type: command
    short-summary: Creates Authorization rule for the given Namespace
    examples:
        - name: Creates Authorization rules
          text: helps['az eh namespace authorizationrule create --resource-group myresourcegroup --namespace-name mynamespace
           --name myauthorule --access-rights [Send, Listen]']

    """

helps['eventhubs namespace authorizationrule get'] = """
    type: command
    short-summary: Shows the details of AuthorizatioRule
    examples:
        - name: Shows the details of AuthorizatioRule
          text: helps['az eh namespace authorizationrule show --resource-group myresourcegroup --namespace-name mynamespace
           --name myauthorule']

    """

helps['eventhubs namespace authorizationrule list'] = """
    type: command
    short-summary: Shows the list of AuthorizatioRule by Namespace
    examples:
        - name: Shows the list of AuthorizatioRule by Namespace
          text: helps['az eh namespace authorizationrule show --resource-group myresourcegroup --namespace-name mynamespace']

    """

helps['eventhubs namespace authorizationrule list-keys'] = """
    type: command
    short-summary: Shows the connectionstrings of AuthorizatioRule for the namespace
    examples:
        - name: Shows the connectionstrings of AuthorizatioRule for the namespace.
          text: helps['az eh namespace authorizationrule list-keys --resource-group myresourcegroup --namespace-name mynamespace
           --name myauthorule']

    """

helps['eventhubs namespace authorizationrule regenerate-keys'] = """
    type: command
    short-summary: Regenerate the connectionstrings of AuthorizatioRule for the namespace.
    examples:
        - name: Regenerate the connectionstrings of AuthorizatioRule for the namespace.
          text: helps['az eh namespace authorizationrule regenerate-keys --resource-group myresourcegroup
           --namespace-name mynamespace --name myauthorule --key PrimaryKey']

    """

helps['eventhubs namespace authorizationrule delete'] = """
    type: command
    short-summary: Deletes the AuthorizatioRule of the namespace.
    examples:
        - name: Deletes the AuthorizatioRule of the namespace.
          text: helps['az eh namespace authorizationrule delete --resource-group myresourcegroup --namespace-name mynamespace
           --name myauthorule']

    """

helps['eventhubs eventhub create'] = """
    type: command
    short-summary: Creates the EventHub Eventhub
    examples:
        - name: Create a new Eventhub.
          text: helps['az eh eventhub create --resource-group myresourcegroup --namespace-name mynamespace --name myeventhub --message-retention-in-days 4 ---partition-count 15']

    """

helps['eventhubs eventhub show'] = """
    type: command
    short-summary: shows the Eventhub Details
    examples:
        - name: Shows the Eventhub details.
          text: helps['az eh eventhub show --resource-group myresourcegroup --namespace-name mynamespace --name myeventhub']

    """

helps['eventhubs eventhub list'] = """
    type: command
    short-summary: List the EventHub by Namepsace
    examples:
        - name: Get the Eventhubs by Namespace.
          text: helps['az eh eventhub list --resource-group myresourcegroup --namespace-name mynamespace']

    """

helps['eventhubs eventhub delete'] = """
    type: command
    short-summary: Deletes the Eventhub
    examples:
        - name: Deletes the Eventhub
          text: helps['az eh eventhub delete --resource-group myresourcegroup --namespace-name mynamespace --name myeventhub']

    """

helps['eventhubs eventhub authorizationrule create'] = """
    type: command
    short-summary: Creates Authorization rule for the given Eventhub
    examples:
        - name: Creates Authorization rules
          text: helps['az eh eventhub authorizationrule create --resource-group myresourcegroup --namespace-name mynamespace
           --event-hub-name myeventhub --name myauthorule --access-rights [Listen]']

    """

helps['eventhubs eventhub authorizationrule show'] = """
    type: command
    short-summary: shows the details of AuthorizatioRule
    examples:
        - name: shows the details of AuthorizatioRule
          text: helps['az eh eventhub authorizationrule show --resource-group myresourcegroup --namespace-name mynamespace
           --event-hub-name myeventhub --name myauthorule']

    """

helps['eventhubs eventhub authorizationrule list'] = """
    type: command
    short-summary: shows the list of AuthorizatioRule by Eventhub
    examples:
        - name: shows the list of AuthorizatioRule by Eventhub
          text: helps['az eh eventhub authorizationrule show --resource-group myresourcegroup --namespace-name mynamespace
           --event-hub-name myeventhub']

    """

helps['eventhubs eventhub authorizationrule list-keys'] = """
    type: command
    short-summary: Shows the connectionstrings of AuthorizatioRule for the Eventhub.
    examples:
        - name: Shows the connectionstrings of AuthorizatioRule for the eventhub.
          text: helps['az eh eventhub authorizationrule list-keys --resource-group myresourcegroup --namespace-name mynamespace --event-hub-name myeventhub --name myauthorule']

    """

helps['eventhubs eventhub authorizationrule regenerate-keys'] = """
    type: command
    short-summary: Regenerate the connectionstrings of AuthorizatioRule for the namespace.
    examples:
        - name: Regenerate the connectionstrings of AuthorizatioRule for the namespace.
          text: helps['az eh eventhub authorizationrule regenerate-keys --resource-group myresourcegroup --namespace-name mynamespace --event-hub-name myeventhub --name myauthorule --key PrimaryKey']

    """

helps['eventhubs eventhub authorizationrule delete'] = """
    type: command
    short-summary: Deletes the AuthorizatioRule of the Eventhub.
    examples:
        - name: Deletes the AuthorizatioRule of the Eventhub.
          text: helps['az eh eventhub authorizationrule delete --resource-group myresourcegroup --namespace-name mynamespace --event-hub-name myeventhub --name myauthorule']

    """

helps['eventhubs consumergroup create'] = """
    type: command
    short-summary: Creates the EventHub ConsumerGroup
    examples:
        - name: Create a new ConsumerGroup.
          text: helps['az eh consumergroup create --resource-group myresourcegroup --namespace-name mynamespace --event-hub-name myeventhub --name myconsumergroup']

    """

helps['eventhubs consumergroup show'] = """
    type: command
    short-summary: Shows the ConsumerGroup Details
    examples:
        - name: Shows the ConsumerGroup details.
          text: helps['az eh consumergroup get --resource-group myresourcegroup --namespace-name mynamespace --event-hub-name myeventhub --name myconsumergroup']

    """

helps['eventhubs consumergroup list'] = """
    type: command
    short-summary: List the ComsumerGroup by Eventhub
    examples:
        - name: Shows the ComsumerGroup by Eventhub.
          text: helps['az eh consumergroup get --resource-group myresourcegroup --namespace-name mynamespace --event-hub-name myeventhub']

    """

helps['eventhubs consumergroup delete'] = """
    type: command
    short-summary: Deletes the ConsumerGroup
    examples:
        - name: Deletes the ConsumerGroup
          text: helps['az eh consumergroup delete --resource-group myresourcegroup --namespace-name mynamespace --event-hub-name myeventhub --name myconsumergroup']

    """

helps['eventhubs georecovery-alias check_name_availability'] = """
    type: command
    short-summary: Check the availability of the Geo Disaster Recovery configuration - Alias Name
    examples:
        - name: Check the availability of the Geo Disaster Recovery configuration - Alias Name
          text: helps['az eh alias check_name_availability --resource-group myresourcegroup --namespace-name primarynamespace
           --alias myaliasname']

    """

helps['eventhubs georecovery-alias create'] = """
    type: command
    short-summary: Creats Geo Disaster Recovery configuration - Alias for the give Namespace
    examples:
        - name: Creats Geo Disaster Recovery configuration - Alias for the give Namespace
          text: helps['az eh alias create  --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname --partner-namespace {id}']

    """

helps['eventhubs georecovery-alias show'] = """
    type: command
    short-summary: shows details of Geo Disaster Recovery configuration - Alias for Primay/Secondary Namespace
    examples:
        - name:  show details of Geo Disaster Recovery configuration - Alias  of the Primary Namespace
          text: helps['az eh alias show  --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname']
        - name:  Get details of Geo Disaster Recovery configuration - Alias  of the Secondary Namespace
           text: helps['az eh alias show  --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname']

    """

helps['eventhubs georecovery-alias break-pairing'] = """
    type: command
    short-summary: Disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces
    examples:
        - name:  Disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces
          text: helps['az eh alias break-pairing  --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname']

    """

helps['eventhubs georecovery-alias fail-over'] = """
    type: command
    short-summary: Envokes Geo Disaster Recovery configuration - Alias to point to the secondary namespace
    examples:
        - name:  Envokes GEO DR failover and reconfigure the alias to point to the secondary namespace
          text: helps['az eh alias fail-over  --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname']

    """

helps['eventhubs georecovery-alias delete'] = """
    type: command
    short-summary: Delete Geo Disaster Recovery configuration - Alias
    examples:
        - name:  Delete Geo Disaster Recovery configuration - Alias
          text: helps['az eh alias delete  --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname']

    """
