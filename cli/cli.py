import click
import os

cmd_folder = os.path.join(os.path.dirname(__file__), 'commands')
cmd_prefix = 'cmd_'


class CLI(click.MultiCommand):

    def list_commands(self, ctx):
        commands = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and filename.startswith(cmd_prefix):
                commands.append(filename[4:-3])
        commands.sort()
        return commands

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(cmd_folder, cmd_prefix + name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']


cli = CLI(help='This tool\'s subcommands are loaded from a '
                 'commands folder dynamically.')

if __name__ == '__main__':
    cli()
