#!/usr/bin/python
# -*- coding: utf-8 -*-

import boto3
import click
from pprint import pprint

from datapipeline import DataPipelineManager

session = None
client = None
dp_manager = None


@click.group()
@click.option('--profile', default=None,
    help="Use a given AWS profile.")
def cli(profile):
    """dptest tests methods in DataPipelineManager class."""
    global session, dp_manager

    session_cfg = {}
    if profile:
        session_cfg['profile_name'] = profile

    session = boto3.Session(**session_cfg)
    dp_manager = DataPipelineManager(session)


@cli.command('list-datapipelines')
def list_all_datapipelines():
    """Lists all datapipelines in a region"""
    #dp_manager.get_all_datapipelines()
    pprint(dp_manager.super_pipeline_list)


@cli.command('list-datapipeline-tags')
@click.option('--id', default=None,
    help="Use a given datapipeline id.")
def list_datapipeline_tags(id):
    print(id)
    pprint(dp_manager.list_datapipeline_tags(id))

if __name__ == '__main__':
    cli()