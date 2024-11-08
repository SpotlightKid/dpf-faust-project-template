# copier-dpf-faust

A [copier] project template for DISTRHO Plugin Framework ([DPF]) audio
effect plugins using [FAUST] for the implementation of the DSP pipeline.

[![quickstart asciicast](https://asciinema.org/a/355004.svg)](https://asciinema.org/a/355004?speed=2&&theme=monokai&autoplay=1&size=medium)

## Quickstart

To create a DPF effect plugin using this template, install copier (see
the [installation instructions]) and then run:

```console
$ copier copy --trust gh:SpotlightKid/copier-dpf-faust <my-project>
```

where `<my-project>` should be the path to a non-existing directory where
your new project will be created.

**Note:** The `--trust` option is necessary because the project template
runs some additional tasks after the project generation and is this considered
"unsafe". These tasks are simple shell commands to set up a git repository with
a sub module etc. You can have a look at the [copier.yml](./copier.yml) file to
review these commands beforehand.

Enter the plugin name and other info at the prompts. (See the
[copier documentation] on how to change the default values for these prompts.)

Here is an example (some output abbreviated for clarity):

```console
$ copier copy --trust gh:SpotlightKid/copier-dpf-faust dpffaustgain
🎤 project_name
   DPF FAUST Gain
🎤 plugin_description
   A simple audio volume gain plugin
🎤 author_name
   Joe Doe
🎤 domain
   example.com
🎤 github_username
   joe.doe
🎤 email
   joe.doe@example.com
🎤 plugin_brand
   example.com
🎤 The plugin name, which can be used as an identifier in source code
   DPFFAUSTGain
🎤 repo_name
   dpffaustgain
🎤 plugin_uri
   https://example.com/plugins/dpffaustgain
🎤 project_license
   MIT
🎤 version
   0.1.0
🎤 year
   2024
🎤 num_inputs (int)
   1
🎤 num_outputs (int)
   1

Copying from template version 0.2.0.post3.dev0+213caa6
    create  .
    create  Makefile
    create  README.md
    create  plugins
    [...]

 > Running task 1 of 11: echo 'Running post-project-generation hook...'
Running post-project-generation hook...
 > Running task 2 of 11: echo 'Initializing new Git repository:'
Initializing new Git repository:
 > Running task 3 of 11: git init
Initialized empty Git repository in .../dpffaustgain/.git/
 > Running task 4 of 11: git remote add origin git@github.com:joe.doe/dpffaustgain
 > Running task 5 of 11: echo 'Adding Git submodule for DPF library:'
Adding Git submodule for DPF library:
 > Running task 6 of 11: git submodule add https://github.com/DISTRHO/DPF.git dpf
Cloning into '.../dpffaustgain/dpf'...
[...]
 > Running task 7 of 11: echo 'Checking out submodules:'
Checking out submodules:
 > Running task 8 of 11: git submodule update --init --recursive
Submodule 'dgl/src/pugl-upstream' (https://github.com/DISTRHO/pugl.git) registered for path 'dpf/dgl/src/pugl-upstream'
Cloning into '.../dpffaustgain/dpf/dgl/src/pugl-upstream'...
Submodule path 'dpf/dgl/src/pugl-upstream': checked out 'e33b2f6b0cea6d6263990aa9abe6a69fdfba5973'
 > Running task 9 of 11: echo 'Making initial Git commit:'
Making initial Git commit:
 > Running task 10 of 11: git add -A
 > Running task 11 of 11: git commit -m 'Initial commit'
[master (root-commit) 4696c9d] Initial commit
[...]

Your DPF/FAUST audio effect plugin project is now ready!
To compile it, change into the 'dpffaustgain' directory and type 'make'.
The plugin binaries and bundles will be placed in the 'bin' subdirectory.
Have fun!
```

A directory named after the second argument you gave to `copier` will be
created and initialized as a Git repository and DPF added as a Git submodule.

Enter the directory and run `make`:

```console
$ cd dpffaustgain
$ make
```

The resulting plugin binaries will be placed in the `bin` sub-directory of your
project.

The FAUST DSP implementation will be in in the `faust` sub-directory, in a file
named `<plugin_name>.dsp` (in all lower-case). Adapt it as you see fit and run
`make` again to re-generate the C++ source code from the the FAUST source and
to rebuild the binaries. The second compilation will be much faster, because
the DPF library has already been built.

The static and generated source code for your plugin is in a sub-directory of
the `plugins` directory named after the value you specified for `plugin_name`
(again in all lower-case).

See the `README.md` file in your generated project for more information on
compiling, prerequisites and how to install the finished plugin(s).


## Requirements

To create a project using this cookie cutter template you need:

* Python
* Git
* [copier]

To build the generated project, you need additional development tools. See the
`README.md` file in your generated project for more information.


## License

This copier template is released under MIT license. See the
[LICENSE.md](./LICENSE.md) file for more information.

When generating a project using this template, you may choose any license for the
resulting files which is compatible with the license of DPF and the plugin
formats you want to distribute.

The `faustpp` architecture files in the `faust/arch` directory of generated
projects are distributed under the Boost Software License 1.0 and come with a
special license exception, which can be found in the `LICENSE-EXCEPTION.md`
file in the same dierctory.


## Authors

* Christopher Arndt ([@SpotlightKid])
* Jean Pierre Cimalando ([@jpcima]) - [faustpp] architecture files


[copier]: https://github.com/copier-org/copier
[copier documentation]: https://copier.readthedocs.io/en/stable
[dpf]: https://github.com/DISTRHO/DPF
[installation instructions]: https://copier.readthedocs.io/en/stable/#installation
[faust]: https://faust.grame.fr/
[faustpp]: https://github.com/jpcima/faustpp
[@jpcima]: https://github.com/jpcima
[@spotlightkid]: https://github.com/SpotlightKid
