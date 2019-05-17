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

        tags = []
        super_id_list = []
        valid_id_list = []
        passed_id_list = []

        if id:
            passed_id_list = id.split()
        else:
            passed_id_list = None

        for i in self.super_pipeline_list:  # just want the existing ids
            super_id_list.append(i['id'])

        if not passed_id_list:   # no ids passed - select all from super_id_list
            valid_id_list = super_id_list
        else:
            for i in passed_id_list:   #iterate over each id
                if i in super_id_list:
                    valid_id_list.append(i)

        for i in valid_id_list:
            tag = [i]
            tag.append(self.dp_client.describe_pipelines(pipelineIds=[i])
                ['pipelineDescriptionList'][0]['tags'])

            tags.append(tag)

        #for i in id_list:   #iterate over each id
        #    for dp in self.super_pipeline_list:
        #        if dp['id'] == i:
        #            tags.append(
        #            self.dp_client.describe_pipelines(pipelineIds=[i])
        #            ['pipelineDescriptionList'][0]['tags']
        #            )

        return tags
