#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Josh Hagins
# Copyright (c) 2014 Josh Hagins
#
# License: MIT
#

"""This module exports the Scalastyle plugin class."""

from os import path
from SublimeLinter.lint import Linter, util


class Scalastyle(Linter):

    """Provides an interface to scalastyle."""

    syntax = 'scala'
    executable = 'java'
    cmd = None
    config_file = ('--config', 'scalastyle-config.xml')

    regex = (
        r'^(?:(?P<error>error)|(?P<warning>warning)) '
        r'(?:file=(?P<file>.+?)) '
        r'(?:message=(?P<message>[^\r\n]+)) '
        r'(?:line=(?P<line>\d+)) '
        r'(?:column=(?P<col>\d+))$'
    )

    multiline = False
    line_col_base = (1, 0)
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = r'^([-\w]+|([\'"])[-\w ]+\2)'
    defaults = {
        'jarfile': ''
    }
    inline_settings = None
    inline_overrides = None
    comment_re = None

    def cmd(self):
        """Return the command line to execute."""

        jarfile = self.get_jarfile_path()
        return [self.executable_path, '-jar', jarfile]

    def get_jarfile_path(self):
        """
        Return the absolute path to the scalastyle jarfile.

        Expand user shortcut (~) and environment variables.

        """

        settings = self.get_view_settings()
        jarfile = settings.get('jarfile')

        # Expand user directory shortcuts
        jarfile = path.expanduser(jarfile)

        # Expand environment variables
        jarfile = path.expandvars(jarfile)

        return jarfile
