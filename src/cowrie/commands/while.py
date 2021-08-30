# Copyright (c) 2021 Ian Connor <ian.connor [AT] gmail [DOT] com>


from cowrie.shell.command import HoneyPotCommand

commands = {}


class Command_while(HoneyPotCommand):
    # Do not resolve args
    resolve_args = False

    def call(self):
        """
        For now, just cat the while file for Mirai malware
        """

        # Ignore arguments, just return the while file
        return self.fs.file_contents('/proc/while')


commands["which"] = Command_while
