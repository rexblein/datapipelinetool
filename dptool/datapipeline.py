# -*- coding: utf-8 -*-
"""Classes for datapipelines."""

from pprint import pprint

class DataPipelineManager:
    """Manage datapipelines."""

    def __init__(self, session):
        self.session = session
        self.dp_client = self.session.client('datapipeline')
        self.super_pipeline_list = self.get_all_datapipelines()

    def get_all_datapipelines(self):
        """Refreshes datapipelines info into self.super_pipeline_list."""

        has_more_results = True
        self.super_pipeline_list = []
        m=''

        while has_more_results:
            pipes = self.dp_client.list_pipelines(marker=m)

            for p in pipes['pipelineIdList']:
                self.super_pipeline_list.append(p)

            has_more_results = pipes['hasMoreResults']

            if has_more_results:
                m = pipes['marker']

        return self.super_pipeline_list

    def list_datapipeline_tags(self, id):
        """Lists tags associated with datapipeline 'id'."""

        tags = None

        for dp in self.super_pipeline_list:
            if dp['id'] == id:
                tags = self.dp_client.describe_pipelines(pipelineIds=[id])\
                ['pipelineDescriptionList'][0]['tags']

        return tags
