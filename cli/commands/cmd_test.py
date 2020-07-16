import subprocess
import click
import os


@click.command()
@click.argument('path', default=os.path.join('snakeeyes', 'tests'))
def cli(path):
    """
    Run a test coverage report
    :param path:
    :return:
    """
    cmd = f'pytest {path}'
    return subprocess.call(cmd, shell=True)
