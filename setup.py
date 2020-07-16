from setuptools import setup

setup(
    name="SnakeEyes Cli",
    version="1.0.0",
    packages=['cli', 'cli.commands'],
    include_package_data=True,
    entry_points="""
    [console_scripts]
    mysite=cli.cli:cli
    """,
)
