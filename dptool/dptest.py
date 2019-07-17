#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Executable to test DataPipelineManager class."""

from pprint import pprint
from datapipeline import DataPipelineManager
import click

# client = None
dp_manager = None


@click.group()
@click.option('--profile', default=None, help="Use a given named AWS profile.")
@click.option('--region', default=None, help="Use a given named AWS region.")
def cli(profile, region):
    """Methods in DataPipelineManager class."""
    global dp_manager

    """session_cfg = {}
    if profile:
        session_cfg['profile_name'] = profile

    session = boto3.Session(**session_cfg)"""
    dp_manager = DataPipelineManager(profile, region)


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


@cli.command('set-datapipeline-tags')
@click.option('--id', default=None, help="Use given datapipeline id(s).")
@click.option('--tagstring', default=None, help="Set given datapipeline tag(s).")
def set_datapipeline_tags(id, tagstring):
    """Sets datapipeline tags."""
    pprint(dp_manager.set_datapipeline_tags(id, tagstring))


if __name__ == '__main__':
    cli()
