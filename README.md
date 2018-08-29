# aws-piper
CLI tool to simplify AWS DataPipeline deployment and management

### Description

> [AWS Data Pipeline](https://aws.amazon.com/datapipeline) is a web service that you can use to automate the movement and transformation of data. With AWS Data Pipeline, you can define data-driven workflows, so that tasks can be dependent on the successful completion of previous tasks.

The Data Pipeline service is quite powerful and allows you to only define the logic and parameters of your pipeline and let the service implement it for you.
Use cases include moving data from / to S3, executing SQL queries on Redshift, launching EMR clusters and executing arbitrary shell scripts.

However, with that power and flexibility comes a rather complicated pipeline management lifecyle. This project aims to simplify that.


### Key Features

- A single configuration file to manage the pipeline
- A reduced number of simple steps to manage the pipeline (deploy, start, stop, delete)
- A streamlined python CLI that can easily be integrated in other projects

### Installation

Until the project is available on PyPi, you can simply run:

```shell
pip install git+https://github.com/heetch/aws-piper
```

### Configuration properties

```yaml
aws_access_key_id: # the iam user managing the pipeline access key

aws_secret_access_key: # the iam user managing the pipeline secret access key

aws_profile: # the name of your aws profile as defined in your credentials file, see: https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html

name: # the name for the pipeline as displayed in the aws console

unique_id: # the unique id for the pipeline

region: # the aws account region

description: # a description for the pipeline (optional)

parameter_objects: # the path to the json file containing your pipeline objects parameters

parameter_values: # the path to the json file containing the values of your pipeline objects parameters

pipeline_definition: # the path to the json file containing your pipeline objects
```

**Note:** You only need to define either your aws profile name _or_ your access key / secret key pair.

### Lifecycle management

#### Deploying a pipeline

To deploy a pipeline simply run:

```shell
piper deploy --config-file config.yaml
```

This command will:
1. Create the pipeline
2. Validate the pipeline definition
3. Upload the pipeline definition

**Important:** This command allows you to both deploy and update a given pipeline. As long as you keep the same pipeline name / pipeline id combination (`name` and `unique_id` in the configuration file), it will create the pipeline at the first run and modify it for the subsequent ones.

#### Starting a pipeline

```shell
piper start --config-file config.yaml
```

This will start (activate) the pipeline deployed in the previous step. There's an optional `--start-timestamp` flag to specify when should the pipeline start from.

```shell
piper start --config-file config.yaml --start-timestamp 2018-08-23T23:00:00
```

#### Stopping a pipeline

```shell
piper stop --config-file config.yaml
```

This will stop the specified pipeline executions.
Stopping a pipeline execution can be used when the pipeline definition needs to be updated.
You stop the pipeline, deploy a new configuration and start it again.
When stopping, you can either interrupt the current execution or wait for it to finish thanks to the `--cancel-active/--no-cancel-active` flags.

#### Deleting a pipeline

```shell
piper delete --config-file config.yaml
```

This will completely remove the pipeline from your list of pipelines.

### Help

You can get some help about the commands and the available flags through

```shell
piper --help
```

or 

```shell
piper [command] --help
```

### Contributions

At Heetch, we are heavy users of Data Pipeline as a data engineering tool.
Although similar libraries exists to simplify the management of other AWS services, we couldn't find one for Data Pipeline.
This project initiated from the need to simplify the access to the service internally and allow a more streamlined and integrated management of our Data Pipeline definitions.

This project so far only represents a rough first version and the bare minimum to allow us to start reaching that goal.

Therefore, we warmly welcome and encourage contributions in the form of issues, patches, tests, requests through this github project.


### Inspirations

- [nficano/python-lambda](https://github.com/nficano/python-lambda)
- [fabfuel/ecs-deploy](https://github.com/fabfuel/ecs-deploy)
