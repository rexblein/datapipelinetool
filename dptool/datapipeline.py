# -*- coding: utf-8 -*-
"""Classes for datapipelines."""

import boto3
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

    @staticmethod
    def listify_passed_ids(self, id):
        """Takes id string and returns a python list."""

        super_id_list = []
        valid_id_list = []
        passed_id_list = []

        if id:
            id = id.replace(',',' ')
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

        return valid_id_list


    def list_datapipeline_tags(self, id):
        """Lists tags associated with datapipeline 'id'."""

        tags = []
        super_id_list = []
        valid_id_list = []
        passed_id_list = []

        valid_id_list = self.listify_passed_ids(self, id)

        for i in valid_id_list:
            tag = [i]
            tag.append(self.dp_client.describe_pipelines(pipelineIds=[i])
                ['pipelineDescriptionList'][0]['tags'])

            tags.append(tag)

        return tags

    def describe_datapipelines(self, id):
        """Gets datapipeline(s) description data."""

        descriptions = []
        #super_id_list = []
        valid_id_list = []
        #passed_id_list = []

        valid_id_list = self.listify_passed_ids(self, id)

        for i in valid_id_list:
            desc = [i]
            desc.append(self.dp_client.describe_pipelines(pipelineIds=[i])
                ['pipelineDescriptionList'][0])

            descriptions.append(desc)

        return descriptions

    def list_datapipeline_definitions(self, id):
        """Lists datapipeline detail per definition function."""

        definitions = []
        valid_id_list = []

        valid_id_list = self.listify_passed_ids(self, id)

        for i in valid_id_list:
            defn = [i]
            defn.append(self.dp_client.get_pipeline_definition(pipelineId=i))

            definitions.append(defn)

        return definitions
