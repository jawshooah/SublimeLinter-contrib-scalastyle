SublimeLinter-contrib-scalastyle
================================

[![Build Status][travis-badge]][travis]
[![Codacy Badge][codacy-badge]][codacy]

This linter plugin for [SublimeLinter][docs] provides an interface to
[scalastyle][scalastyle]. It will be used with files that have the “scala”
syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter
3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `scalastyle` is installed on
your system. `scalastyle` is available as an executable `jar` file, which can
be downloaded [here][scalastyle-download].

### Linter configuration
In order for `scalastyle` to be executed by SublimeLinter, you must ensure that
`java`'s path is available to SublimeLinter. Before going any further, please
read and follow the steps in
[“Finding a linter executable”][finding-executable] through “Validating your
PATH” in the documentation.

Once you have installed and configured `scalastyle`, you can proceed to install
the SublimeLinter-contrib-scalastyle plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure
that the plugin will be updated when new versions are available. If you want to
install from source so you can modify the source code, you probably know what
you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`.
   Among the commands you should see `Package Control: Install Package`. If
   that command is not highlighted, use the keyboard or mouse to select it.
   There will be a pause of a few seconds while Package Control fetches the
   list of available plugins.

1. When the plugin list appears, type `scalastyle`. Among the entries you
   should see `SublimeLinter-contrib-scalastyle`. If that entry is not
   highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see
[Settings][settings]. For information on generic linter settings, please see
[Linter Settings][linter-settings].

In addition to the standard SublimeLinter settings,
SublimeLinter-contrib-scalastyle provides its own settings.

|Setting|Type|Description|
|:------|:---|:----------|
|jar_file|`str`|The path to the `scalastyle` `jar` file.|

By default, the linter plugin looks for a file called `scalastyle-config.xml`
in the current directory and its parents. To override the config file path, you
would add this to the linter settings:

```json
"scalastyle": {
    "args": ["--config", "path/to/config.xml"]
}
```

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `develop`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbrevations unless they are very
  well known.

##### IMPORTANT!
Also note that this repository uses [overcommit][overcommit] as a validation
tool. Before making any changes, please
[install overcommit][overcommit-install] in your local repository.

Thank you for helping out!

[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[codacy]: https://www.codacy.com/public/haginsjosh/SublimeLinter-contrib-scalastyle
[codacy-badge]: https://www.codacy.com/project/badge/6763b71dc0184aec875ab191cd9da3b8
[docs]: http://sublimelinter.readthedocs.org
[finding-executable]: http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[overcommit]: https://github.com/causes/overcommit
[overcommit-install]: https://github.com/causes/overcommit#installation
[pc]: https://sublime.wbond.net/installation
[scalastyle]: http://www.scalastyle.org
[scalastyle-download]: http://www.scalastyle.org/command-line.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[travis]: https://travis-ci.org/jawshooah/SublimeLinter-contrib-scalastyle
[travis-badge]: https://travis-ci.org/jawshooah/SublimeLinter-contrib-scalastyle.svg?branch=develop
