from __future__ import absolute_import
from __future__ import print_function
import json
import os
from datetime import datetime

import yaml
from awscli.customizations.datapipeline import translator

from .data_pipeline import DataPipelineClient


def deploy(config_file='config.yaml'):
    path_to_config_file = os.path.join(os.getcwd(), config_file)
    cfg = read_cfg(path_to_config_file)

    profile = cfg.get('aws_profile')
    access_key_id = cfg.get('aws_access_key_id')
    secret_access_key = cfg.get('aws_secret_access_key')
    region = cfg.get('region')

    client = get_client(access_key_id, secret_access_key, region, profile)

    name = cfg.get('name')
    unique_id = cfg.get('unique_id')
    description = cfg.get('description', '')

    create_response = client.create_pipeline(name, unique_id, description)

    pipeline_id = create_response.get('pipelineId')
    parameter_objects = translator.definition_to_api_parameters(read_json_file(cfg.get('parameter_objects')))
    parameter_values = translator.definition_to_parameter_values(read_json_file(cfg.get('parameter_values')))
    pipeline_definition = translator.definition_to_api_objects(read_json_file(cfg.get('pipeline_definition')))

    return client.put_pipeline_definition(pipeline_id, pipeline_definition, parameter_objects, parameter_values)


def start(config_file, start_timestamp):
    path_to_config_file = os.path.join(os.getcwd(), config_file)
    cfg = read_cfg(path_to_config_file)

    profile = cfg.get('aws_profile')
    access_key_id = cfg.get('aws_access_key_id')
    secret_access_key = cfg.get('aws_secret_access_key')
    region = cfg.get('region')

    client = get_client(access_key_id, secret_access_key, region, profile)

    start_timestamp_dt = datetime.strptime(start_timestamp, '%Y-%m-%dT%H:%M:%S')
    pipeline_id = get_pipeline_id_from_name(cfg.get('name'), client)

    return client.activate_pipeline(pipeline_id, start_timestamp_dt)


def stop(config_file, cancel_active):
    path_to_config_file = os.path.join(os.getcwd(), config_file)
    cfg = read_cfg(path_to_config_file)

    profile = cfg.get('aws_profile')
    access_key_id = cfg.get('aws_access_key_id')
    secret_access_key = cfg.get('aws_secret_access_key')
    region = cfg.get('region')

    client = get_client(access_key_id, secret_access_key, region, profile)

    pipeline_id = get_pipeline_id_from_name(cfg.get('name'), client)

    return client.deactivate_pipeline(pipeline_id, cancel_active)


def delete(config_file='config.yaml'):
    path_to_config_file = os.path.join(os.getcwd(), config_file)
    cfg = read_cfg(path_to_config_file)

    profile = cfg.get('aws_profile')
    access_key_id = cfg.get('aws_access_key_id')
    secret_access_key = cfg.get('aws_secret_access_key')
    region = cfg.get('region')

    client = get_client(access_key_id, secret_access_key, region, profile)

    pipeline_id = get_pipeline_id_from_name(cfg.get('name'), client)

    return client.delete_pipeline(pipeline_id)


def get_client(access_key_id, secret_access_key, region, profile):
    return DataPipelineClient(access_key_id, secret_access_key, region, profile)


def read_cfg(path_to_config_file):
    with open(path_to_config_file, 'r') as stream:
        try:
            cfg = yaml.load(stream)
            return cfg
        except yaml.YAMLError as exc:
            print(exc)


def read_json_file(path_to_json_file):
    with open(path_to_json_file, 'r') as stream:
        return json.load(stream)


def get_pipeline_id_from_name(name, client):
    pipelines = client.list_pipelines()
    return [p['id'] for p in pipelines if p['name'] == name][0]