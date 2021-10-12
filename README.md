# OpenRobot-Packages
The base OpenRobot Package. This will be installed in all `OpenRobot-Packages` Packages.

# FaQ:
## How can I install a package from here?
You would do something like:
```
$ pip install git+https://github.com/OpenRobot-Packages/<Package Name>
```
(this may be differ from yours)

Any packages you install will automatically install this repository (https://github.com/OpenRobot-Packages/Python-OpenRobot-Packages) branch, `git+https://github.com/OpenRobot-Packages/Python-OpenRobot-Packages`. Note that this does not do anything and it has no code at all.

## Is OpenRobot Packages in PyPi?
No, and probably never will. We want to integrate packages in one organization, and publishing it in PyPi one by one will be a hard time and hard work to do.

## I failed to install a `OpenRobot-Packages` repo, what should I do?
- Make sure you already installed [Git](https://git-scm.com). You can check if you have git by just typing `git --version`. It should output something like `git version <Git Version>`.
- Make sure you do `OpenRobot-Packages` instead of `OpenRobot`. (`git+https://github.com/OpenRobot/<Package-Name>` = No. `git+https://github.com/OpenRobot-Packages/<Package-Name>` = Yes) and you have `git+` before using its url. If you still can't, feel free to make an Issue on the specific GitHub Repo, or try to clone the GitHub Repo, then trying to type `pip install .` (this may be differ from yours)

# License:
MIT
