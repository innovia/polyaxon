DEFAULT_PORT = 2222
ENV_VAR_TEMPLATE = '{name: "{var_name}", value: "{var_value}"}'
VOLUME_CLAIM_NAME = 'plx-pvc-{vol_name}'
CONFIG_MAP_NAME = 'plx-config-{uuid}'
SECRET_NAME = 'plx-secret-{uuid}'  # noqa, secret
CONFIG_MAP_CLUSTER_KEY_NAME = 'POLYAXON_CLUSTER'
CONFIG_MAP_DECLARATIONS_KEY_NAME = 'POLYAXON_DECLARATIONS'
CONFIG_MAP_EXPERIMENT_INFO_KEY_NAME = 'POLYAXON_EXPERIMENT_INFO'
CONFIG_MAP_JOB_INFO_KEY_NAME = 'POLYAXON_JOB_INFO'
CONFIG_MAP_TASK_INFO_KEY_NAME = 'POLYAXON_TASK_INFO'
CONFIG_MAP_LOG_LEVEL_KEY_NAME = 'POLYAXON_LOG_LEVEL'
CONFIG_MAP_REFS_OUTPUTS_PATHS_KEY_NAME = 'POLYAXON_REFS_OUTPUTS_PATHS'
CONFIG_MAP_RUN_OUTPUTS_PATH_KEY_NAME = 'POLYAXON_RUN_OUTPUTS_PATH'
CONFIG_MAP_RUN_LOGS_PATH_KEY_NAME = 'POLYAXON_LOGS_PATH'
CONFIG_MAP_RUN_DATA_PATHS_KEY_NAME = 'POLYAXON_DATA_PATHS'
SECRET_USER_TOKEN = 'POLYAXON_USER_TOKEN'  # noqa, secret
EXPERIMENT_JOB_NAME = 'plxjob-{task_type}{task_idx}-{experiment_uuid}'
JOB_NAME = 'plx-{name}-{job_uuid}'

REPOS_VOLUME = 'repos'
DOCKER_VOLUME = 'docker'
