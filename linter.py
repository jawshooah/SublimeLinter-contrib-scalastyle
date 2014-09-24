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

import os
from SublimeLinter.lint import Linter, util


class Scalastyle(Linter):

    """Provides an interface to scalastyle."""

    syntax = 'scala'
    executable = 'java'
    config_file = ('--config', 'scalastyle_config.xml', '~')

    version_args = '--version'
    version_re = r'^scalastyle (?P<version>\d+\.\d+\.\d+)$'
    version_requirement = '>= 0.5'

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
        """
        Return the command line to execute.

        """

        command = [self.executable_path, '-jar']

        jarfile = self.get_jarfile_path()

        return command + jarfile


    def get_jarfile_path(self):
        """
        Return the absolute path to the scalastyle jarfile.

        Expand user shortcut (~) and environment variables.

        """

        settings = self.get_view_settings()
        jarfile = settings.get('jarfile')

        # Expand user directory shortcuts
        jarfile = os.path.expanduser(jarfile)

        # Expand environment variables
        jarfile = os.path.expandvars(jarfile)

        return jarfile
