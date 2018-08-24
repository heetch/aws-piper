from boto3.session import Session


class DataPipelineClient(object):
    def __init__(self, access_key_id=None, secret_access_key=None, region=None, profile=None):
        session = Session(aws_access_key_id=access_key_id,
                          aws_secret_access_key=secret_access_key,
                          region_name=region,
                          profile_name=profile)
        self.boto = session.client(u'datapipeline')

    def create_pipeline(self, name, unique_id, description):
        return self.boto.create_pipeline(
            name=name,
            uniqueId=unique_id,
            description=description
        )

    def put_pipeline_definition(self, pipeline_id, pipeline_definition, parameter_objects, parameter_values):
        return self.boto.put_pipeline_definition(
            pipelineId=pipeline_id,
            pipelineObjects=pipeline_definition,
            parameterObjects=parameter_objects,
            parameterValues=parameter_values
        )

    def activate_pipeline(self, pipeline_id, start_timestamp=None):
        if start_timestamp:
            return self.boto.activate_pipeline(
                pipelineId=pipeline_id,
                startTimestamp=start_timestamp
            )
        else:
            return self.boto.activate_pipeline(
                pipelineId=pipeline_id
            )

    def deactivate_pipeline(self, pipeline_id, cancel_active):
        return self.boto.deactivate_pipeline(
            pipelineId=pipeline_id,
            cancelActive=cancel_active
        )

    def list_pipelines(self):
        has_more_results = True
        pipelines = []
        marker = ''

        while has_more_results:
            response = self.boto.list_pipelines(marker=marker)
            pipelines += response['pipelineIdList']
            marker = response.get('marker', '')
            has_more_results = response['hasMoreResults']

        return pipelines

    def delete_pipeline(self, pipeline_id):
        return self.boto.delete_pipeline(
            pipelineId=pipeline_id
        )
