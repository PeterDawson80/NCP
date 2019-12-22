from django.apps import AppConfig


class CustomerRelationshipManagementConfig(AppConfig):
    name = 'customer_relationship_management'

INSTALLED_APPS = [
    'text_query.apps.TextQueryConfig',
    # ...
]
