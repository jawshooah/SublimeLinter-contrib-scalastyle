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
        r'^(?:(?P<error>error)|(?P<warning>warning))'
        r'(?: file=(?P<file>.+?))'
        r'(?: message=(?P<message>.+?))'
        r'(?: line=(?P<line>\d+))?'
        r'(?: column=(?P<col>\d+))?$'
    )

    multiline = False
    line_col_base = (1, 0)
    tempfile_suffix = 'scala'
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = r'^([-\w]+|([\'"])[-\w ]+\2)'
    defaults = {
        'jar_file': ''
    }
    inline_settings = None
    inline_overrides = None
    comment_re = None

    def cmd(self):
        """Return the command line to execute."""

        jar_file = self.get_jarfile_path()

        return [self.executable_path, '-jar', jar_file]

    def get_jarfile_path(self):
        """
        Return the absolute path to the scalastyle jar file.

        Expand user shortcut (~) and environment variables.

        """

        settings = self.get_view_settings()
        jar_file = settings.get('jar_file')

        # Expand user directory shortcuts
        jar_file = path.expanduser(jar_file)

        # Expand environment variables
        jar_file = path.expandvars(jar_file)

        # Get canonical path
        jar_file = path.realpath(jar_file)

        return jar_file

    def split_match(self, match):
        """
        Return the components of the match.

        We override this method so that errors with no line number can be displayed.

        """

        match, line, col, error, warning, message, near = super().split_match(match)

        if line is None and message:
            line = 0

        return match, line, col, error, warning, message, near
