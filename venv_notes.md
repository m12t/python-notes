* all virtual environments are stored in the hidden directory: ".venv" in /Users/mike
	> this is not the right way to do it... they should be project-level...
* to access these hidden folders, click 'mike' in finder and type: <command> <shift> <.> (command + shift + period). this will show all hidden files.
* to activate an environment, due to it being in a hidden folder, you must run:
	". ~/.venv/<env_name>/bin/activate"
  So to activate ibenv, for example:
	". ~/.venv/ibenv/bin/activate"
* deactivation is simple. Directory doesn't matter, simply type: "deactivate".
* To create a virtual environment, cd in .venv and then type:
	python -m venv <env_name>
* to write all dependencies/requirements for the environment, it is recommended to write this file  into the root project folder and not to write this inside of envs.
* to actually create the command, type: pip freeze > requirements.txt
* then if moving to production or make a new virtualenv for whatever reason and want it to have the same packages, type "pip install -r requirements.txt".

the package `virtualenv` is used to manage python environments.
envs should be project level and `.gitignore`d. Simply document the packages in the environment with `pip freeze > requirements.txt` within the root project directory to be able to recreate the environment elsewhere with the command `pip install -r requirements.txt`. The script `~/python-notes/strip_pip_reqs.py` can be used to list the general packages without versions.
1. to use it, `cd` into your project directory
1. type `virtualenv env` to create and environment named `env` in an eponymous directory within the project directory. This is only done once.
1. then, to activate the environment, cd into the `env` directory and type `. bin/activate` or `source bin/activate`. The environment is now active.
1. now, python packages can be downloaded via pip into the environment and won't appear globally within python.
1. to deactivate an env, simply type `deactivate` into the terminal.


debugging virtualenv:

- a bug I encountered when trying to use virtualenv was repeated errors with `ERROR: virtualenv is not compatible with this system or executable`.
	- The traceback also showed virtualenv pointing to python 3.7 instead of 3.10, which is correctly symlinked and calling `which python3` correctly points to `3.10.2`.
	- The issue was that older versions of python had been installed without homebrew and had virtualenv packages within `/bin` that were being used instead of the instace tied to the homebrew installation of python. The solution was to simply clear out the old versions nad move them to the trash. Then, ensuring that python was unaffected by moving the old versions from `../Library/Frameworks/Python.framework/Versions/`. NOTE: you could have simply deleted the virtualenv executables exclusively, but there's no point to having those old versions of python outside of brewl. After clearing out those versions of python, run `which virtualenv` and `pip show virtualenv` to ensure it's pointing to the right place and installed as expected.

a useful source regarding clearing out old versions of python can be found [here](https://faun.pub/the-right-way-to-set-up-python-on-your-mac-e923ffe8cf8e). Be careful using the command given `sudo rm -Rf /Library/Frameworks/Python.framework/Versions/*` as if you don't know what you're doing you can recursively delete all your files permanently! It's best to just move the versions into the trash individually as this also allows you to put them back before deleting permanently.
