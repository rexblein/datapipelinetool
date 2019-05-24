# datapipelinetool

Painless management of AWS data-pipeline assets in AWS

# configuration

Setup credentials/config files in your ~/.aws directory or use IAM roles.

## dptool

Creates and manages data-pipeline assets inside AWS

## Usage

Usage: dptest.py [OPTIONS] COMMAND [ARGS]...

  Methods in DataPipelineManager class.

Options:
  --profile TEXT  Use a given named AWS profile.
  --region TEXT   Use a given named AWS region.
  --help          Show this message and exit.

Commands:
  describe-datapipelines         Lists datapipeline detail per describe...
  list-all-datapipelines         Lists all datapipelines in a region.
  list-datapipeline-definitions  Lists detail of datapipeline definitions.
  list-datapipeline-tags         Lists datapipeline tags.

## example
dptest.py list-datapipeline-definitions --id <pipeline ids>

### Features

- list pipelines
- list pipeline tags
- list full pipeline descriptions
- list full pipeline definitions
- create a pipeline (coming soon)
- delete a pipeline (coming soon)
- activate a pipeline (coming soon)
