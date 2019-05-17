import boto3
import click

client = boto3.client('datapipeline')

@click.group()
def cli():
    "dptool operates on the datapiplines in AWS"
    pass


@cli.command('list-data-pipelines')
def list_data_pipelines():
    "Lists all datapipelines in a region"

    # for some reason datapipline listings come 25 at a time.
    # We have top make a superset of all of them.
    # Assume there are more than one page of pipelines, set this flag to get more.
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

    for p in super_pipeline_list:
        print(p)

    return


@cli.command('list-data-pipeline-tags')
def list_data_pipelines_tags():
    "Lists all datapipelines in a region and their tags"

    # for some reason datapipline listings come 25 at a time.
    # We have top make a superset of all of them.
    # Assume there are more than one page of pipelines, set this flag to get more.
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

    for p in super_pipeline_list:
        print(p)

    return


if __name__ == '__main__':
    cli()
