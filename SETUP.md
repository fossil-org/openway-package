This file contains instructions
on how to set up a Git repository
from the openway-package template.

Step 1:
Make sure Openway is installed
```commandline
gavel install openway --get-packages
```
Note: The `get-packages` option is required as openway operates as a module.
Note: `gavel` is required to install Openway. You can run these commands to get `gavel` if you don't have it:
```commandline
git clone https://github.com/fossil-org/gavel
pipx install ./gavel
rm ./gavel
```

Step 2:
Add a license to the LICENSE file.
Go to [choosealicense.com](https://choosealicense.com/) for help choosing a license for your project.

Step 3:
Write information about your project in README.md

Step 4:
Start coding! There is a main file in package/init/main.py and an entrypoint test file in tests/main.py