import subprocess
import click


@click.command()
@click.argument('path', default='snakeeyes')
def cli(path):
    """
    Run a test coverage report
    :param path:
    :return:
    """
    cmd = f'pytest --cov {path}'
    return subprocess.call(cmd, shell=True)
