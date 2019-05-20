#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Executable to test DataPipelineManager class."""

from pprint import pprint
from datapipeline import DataPipelineManager
import boto3
import click

session = None
client = None
dp_manager = None


@click.group()
@click.option('--profile', default=None, help="Use a given AWS profile.")
def cli(profile):
    """Methods in DataPipelineManager class."""
    global session, dp_manager

    session_cfg = {}
    if profile:
        session_cfg['profile_name'] = profile

    session = boto3.Session(**session_cfg)
    dp_manager = DataPipelineManager(session)


@cli.command('list-all-datapipelines')
def list_all_datapipelines():
    """Lists all datapipelines in a region."""
    pprint(dp_manager.super_pipeline_list)


@cli.command('describe-datapipelines')
@click.option('--id', default=None, help="Use given datapipeline id(s).")
def describe_datapipelines(id):
    """Lists datapipeline detail per describe function."""
    pprint(dp_manager.describe_datapipelines(id))


@cli.command('list-datapipeline-definitions')
@click.option('--id', default=None, help="Use given datapipeline id(s).")
def list_datapipeline_definitions(id):
    """Lists detail of datapipeline definitions."""
    pprint(dp_manager.list_datapipeline_definitions(id))


@cli.command('list-datapipeline-tags')
@click.option('--id', default=None, help="Use given datapipeline id(s).")
def list_datapipeline_tags(id):
    """Lists datapipeline tags."""
    pprint(dp_manager.list_datapipeline_tags(id))


if __name__ == '__main__':
    cli()
