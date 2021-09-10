from django.core.management.commands.shell import Command as ShCommand
import os

class Command(ShCommand):
    shells = ShCommand.shells.append("ptpython")

    def ptpython(self):
        try:
            from prompt_toolkit.contrib.repl import embed
        except ImportError:
            from ptpython.repl import embed

        history_filename = os.path.expanduser("~/.ptpython_history")
        embed(globals(), locals(), vi_mode=True, history_filename=history_filename)

