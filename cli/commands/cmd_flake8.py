import subprocess
import click


@click.command()
@click.option('--skip-init', default=True, help='Skip __init__.py files')
@click.argument('path', default='snakeeyes')
def cli(skip_init, path):
    """
    Run a test coverage report
    :param path:
    :return:
    """
    arg = None
    if skip_init:
        arg = '--exclude __init__.py'

    cmd = f'flake8 {path} {arg}'
    return subprocess.call(cmd, shell=True)
