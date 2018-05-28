# Installation instructions

We will be using three main pieces of software for this course:

1. Git - a software version control tool

1. Conda - a package manager for installing Python libraries

1. LaTeX - a typesetting system for science, mathematics, and engineering

## 1. Git and GitHub

Git is a tool for managing software projects. It enables version control, meaning that (1) it is easy to collaborate with other people who are modifying the same files as you, and (2) you can choose snapshots of your work to revert back to when needed.

Github is a web-based hosting service for version control using git. While git is a tool that works locally on your machine, Github is a hosting service that allows to sync your projects to the internet. This is extra useful if you work on the same project across different machines, or if something happens to your development machine -- all material is stored in the cloud. Github is also useful as a resume tool for software engineers; recruiters can see your personal projects or your contributions to public projects.

### Getting set up

1. Follow the instructions under [Setting up Git](https://help.github.com/articles/set-up-git/) for setting up the git software and a GitHub account.

1. Now download the course materials by forking this repository. This means you will have a local copy (a fork) of everything maintained in this original repository, but you can make your own changes that will only be reflected in your local repository.

    1. Navigate to this github website [link](https://github.com/yanlisa/datasci-py) in your browser.

    1. In the top right, click ''Fork this repo.''

    1. Now, navigate to your own copy of the repo. It should be something like ```https://github.com/<your github username>/datasci-py```

    1. Click the green button that says ''Clone or download.''

    1.  Verify that the pop-up says ''Clone with HTTPS.'' If it says ''SSH'' switch to ''Use HTTPS.'' Copy the URL.

    1. Now, into your Git commandline tool, navigate to the workspace folder that you want to use for this course. Supposing that we want to develop in ```/Users/Lisa/Documents```:
    
    ```
    # change directories
    cd /Users/Lisa/Documents
    # move up one directory
    cd ..

    # list what's in the current directory
    # if on Mac or Linux:
    ls
    # if on Windows:
    dir

    # finally, create a folder and copy everything from the below git repository into your current folder
    git clone <the link that you copied ending .git>

    # you might have to enter your GitHub password
    # verify that the folder is there with ls (in Mac/Linux) or dir (in Windows)
    ```

### Submitting your assignment

Submitting your work is as easy as committing your changes to your fork. No need to submit pull requests; as long as your repository is public, the instructor will be able to see what you've done.

How to commit to github (note that in order to submit your work, you must perform steps 1, 2, 3 in that order):
```
# Step 1: Adds two files to be saved
git add file1.py file2.py

# Step 2: Writes a commit message and saves what you've done to your local repository
git commit -m "Updated exercises for week X"

# Step 3: Pushes and syncs so that github.com's repository also sees your new commit
git push origin master
```

Other commands to help you out:
```
#  Lists all files added, modified, or removed since your last commit
git status

# Lists all commit messages (type q to quit); you might not use this too much
git log

# Removes file from your local repository and removes it for your commit
git rm file1.py

# (more ideal) Removes file from the commit but does not remove the local copy
git rm --cached file1.py

# Drop all local changes for this file and get the version from the last commit
git checkout file1.py

```

### Downloading new material

Make commits to your local fork. When new material comes out, update your fork.

More description [here](https://reflectoring.io/github-fork-and-pull/):

```
# add the original repository as remote repository called "upstream"
git remote add upstream https://github.com/yanlisa/datasci-py.git
# if you messed up,
# git remote rm upstream
# and then add it again with the previous command

# fetch all changes from the upstream repository
git fetch upstream

# switch to the master branch of your fork
git checkout master

# merge changes from the upstream repository into your fork
git merge upstream/master
```

## 2. Conda

### Getting set up

1. Follow the instructions under [Regular installation](https://conda.io/docs/user-guide/install/index.html#regular-installation). We are using Python 3 for this course.

1. Once you have conda installed, open the ```anaconda prompt``` program.

1. Install some packages necessary for this course:

    ```
    conda install jupyter
    conda install numpy scipy matplotlib
    conda install scikit-learn
    ```

1. Verify that everything works. In one terminal, type in ```jupyter notebook``` and verify that it automatically starts something in your browser. In another terminal, type in ```python``` and verify that it can interpret simple addition, e.g., ```1 + 2<enter>```.

1. Note that in practice, you want to navigate to your desired folder (i.e., the one that has all the course materials in it) and then run ```jupyter notebook```. This saves you the navigation info. Then you keep your jupyter notebook running in a separate window.

## 3. LaTeX

This installation writeup will be updated at a later time.

## References
[Installing and maintaining Python 2.X and Python 3](https://stackoverflow.com/questions/30492623/using-both-python-2-x-and-python-3-x-in-ipython-notebook)

- To get the correct site-packages, copy a ```mymodule.pth``` file into ```/anaconda/<environment>/lib/python<ver>/site-packages/```with the single line of the ```/usr/local/lib/python<ver>/site-packages```
