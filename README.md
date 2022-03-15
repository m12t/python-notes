## About
I created these notes for my own use but decided to make them public just in case they can help someone else :)

### The Only Code in Here:
There is a hastily-written command line script in here called `strip_pip_reqs.py` that will take a pip requirements file as-is from `pip freeze > requirements.txt` and will remove all version info (eg. `numpy==11.22.3` -> `numpy`) such that calls to `pip install -r requirements.txt` should get the latest version of each of those packages.
