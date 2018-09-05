from __future__ import absolute_import
import click

from . import aws_piper


@click.group()
def piper():
    pass


@click.command()
@click.option(
    '--config-file',
    default='config.yaml',
    help='Data pipeline job configuration file. Must be in the path of the current directory.'
)
def deploy(config_file):
    click.echo(aws_piper.deploy(config_file))


@click.command()
@click.option(
    '--config-file',
    default='config.yaml',
    help='Data pipeline job configuration file. Must be in the path of the current directory.'
)
@click.option(
    '--start-timestamp',
    help='The date and time to resume the pipeline. By default, the pipeline resumes from the last completed execution.'
)
def start(config_file, start_timestamp):
    click.echo(aws_piper.start(config_file, start_timestamp))


@click.command()
@click.option(
    '--config-file',
    default='config.yaml',
    help='Data pipeline job configuration file. Must be in the path of the current directory.'
)
@click.option('--cancel-active/--no-cancel-active',
              default=True,
              help='Whether to cancel any running objects.' +
                   'If this value is false, the pipeline is deactivated after all running objects finish.')
def stop(config_file, cancel_active):
    click.echo(aws_piper.stop(config_file, cancel_active))


@click.command()
@click.option(
    '--config-file',
    default='config.yaml',
    help='Data pipeline job configuration file. Must be in the path of the current directory.'
)
def delete(config_file):
    click.echo(aws_piper.delete(config_file))


piper.add_command(deploy)
piper.add_command(start)
piper.add_command(stop)
piper.add_command(delete)

if __name__ == '__main__':
    piper()
