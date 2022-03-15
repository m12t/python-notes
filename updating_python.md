# Tips & Tricks for updating/installing Python globally on macOS.

### Steps
0. Run `pip freeze > requirements.txt` (more on this later)
1. Use homebrew (seriously important!). Open up Terminal.
	a. run `brew upgrade && brew update` | `brew install python` (if not installed)
2. Once the new version python is downloaded, create the symlinks to point to it and unlink other versions, if applicable.
	a. Run `brew link python@<latest version>`
	b. If conflicting symlinks exist, follow the instructions spit out by brew, or unlink the others and try again.
3. At this stage, running `python3 -V` should display the latest version just downloaded. If it displays python 2.x, quickly `vim .zshrc` and add `alias python=python3` to the top of the file. This reference is only effective within Terminal.
4. By now, the new version of python should be linked, but pip is not yet linked. All pip packages must also be migrated over. This is where the pip freeze call from (0) comes in. Double check that `requirements.txt` matches `pip list` before proceeding.
5. Add an alias for pip if `pip -V` points to a location within an older version of python. Make the alias in the same file as (3) with `alias pip=pip3`. Check that it works by running `pip -V` and `pip3 -V`, ensuring that they both point to the newest version of python.
6. Now that pip is migrated as well, type `pip list`. This should be quite sparse as most packages are in the older version of python. If this is the case, the old requirements can be installed into the new version. Before installation, a choice must be made:
	a. if you want all the newest versions of each package (which will help with support for the new versions), run `/python-notes/strip_pip_reqs.py`. This script will strip the version info from `requirements.txt` such that pip will install the newest possible version.
	b. Otherwise, leave `requirements.txt` as-is and manually remove versions for packages that have issues with compatibility.
To install the packages, run `python3 -m pip install -r requirements.txt` (ensuring pip is correctly aliased from (5)). the `python3 -m` prefix ensures that pip is tied to the latest version of python.
	> running `pip show <package>` will show the location of and other info for a package. Use this to ensure that the correct version of python is used and other details are as expected.
7. That's all there is to it. Check one last time that the version of python is as expected by running `python -V` and `pip -V`, then start hacking away with your fresh install of Python!

debugging:
after updating globally, is virtualenvs give bad interpreter errors when running `pip show`, for example: [stackoverflow](https://stackoverflow.com/questions/51373063)/pip3-bad-interpreter-no-such-file-or-directory. Run ` rm /usr/local/bin/pip3` within the activated virtualenv, then run `brew link python`. Now try `python -V` and `pip -V` again, they should work.
