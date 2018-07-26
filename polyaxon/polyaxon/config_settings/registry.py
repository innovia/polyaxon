from polyaxon.config_manager import config

REGISTRY_USER = config.get_string('POLYAXON_REGISTRY_USER', is_optional=True)
REGISTRY_PASSWORD = config.get_string('POLYAXON_REGISTRY_PASSWORD', is_optional=True)
REGISTRY_HOST_NAME = config.get_string('POLYAXON_REGISTRY_HOST', is_optional=True)
REGISTRY_PORT = config.get_string('POLYAXON_REGISTRY_PORT', is_optional=True)
REGISTRY_NODE_PORT = config.get_string('POLYAXON_REGISTRY_NODE_PORT', is_optional=True)
REGISTRY_HOST = '{}:{}'.format('127.0.0.1', REGISTRY_NODE_PORT)
#PRIVATE_REGISTRIES = config.get_string('POLYAXON_PRIVATE_REGISTRIES', is_optional=True)
ECR_REGION = config.get_string('POLYAXON_ECR_REGION', is_optional=True)
ECR_ACCOUNT_ID = config.get_string('POLYAXON_ECR_ACCOUNT_ID', is_optional=True)
