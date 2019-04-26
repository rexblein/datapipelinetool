import boto3
import click

aws_region='us-west-2'
aws_profile='pythonAutomation'

session = boto3.Session(profile_name=aws_profile, region_name=aws_region)
client = boto3.client('datapipeline')

# for some reason datapipline listings come 25 at a time.
# We have top make a superset of all of them.

# Assume there are more pipelines in the beginning, the flag to get more.
has_more_results = True
super_pipeline_list = []
m=''

while has_more_results:
    pipes = client.list_pipelines(marker=m)

    for p in pipes['pipelineIdList']:
        super_pipeline_list.append(p)

    has_more_results = pipes['hasMoreResults']

    if has_more_results:
        m = pipes['marker']


print(super_pipeline_list[1]['id'])
