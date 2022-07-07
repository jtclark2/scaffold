# Status Badge
This shows the status of the build actions. This is created under the
Actions tab, by selecting a specific action and clicking the `...` and 
selecting `Create Status Badge`. The contents are copied below.
[![Python application test with Github Actions](https://github.com/jtclark2/scaffold/actions/workflows/main.yml/badge.svg)](https://github.com/jtclark2/scaffold/actions/workflows/main.yml)

# scaffold
This is a project scaffold for python. We will create the basic files that form the foundation for most projects.
This file is based on the [Cloud Computing Foundations tutorial](https://www.coursera.org/learn/cloud-computing-foundations-duke/lecture/dxL50/constructing-a-python-project-scaffold) 

## Files required for best dev ops best practices

- Makefile: This file installs the environment, lints, formats, and tests code.
  - It is useful to for local setup, or as a commit hook for PRs.
  - Use tabs (not spaces)...This is not stylistic - some tools require tabs.
- [requirements.txt](https://pip.pypa.io/en/latest/user_guide/#requirements-files): pip's standard package definition file 
  - format is extremely simple, really just a list of the dependency and
  version pins
- [Actions / Workflows](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#viewing-the-activity-for-a-workflow-run): 
These are .yaml files that defines actions to be taken in response to 
various github events
  - In this project, actions are used as commit hooks `on: [push]`, though they can be quite flexible in generalcd sc
    - main.yml summary: install ubuntu virtual environment -> install python 
    -> install project's python dependencies -> run linter & black -> run tests 
  - Actions are saved in the project as yaml files in `.github/workflows/` 
- README: This markdown file explaining the basic idea and setup for a project
- .gitignore: Lists files to ignore during git commits
- source code (.py files): Pretty boring in this repo.
- test files (all test files, usually test_<sourcefile>.py)

## Local setup: 
1) Clone this repo
2) Create virtualenv / conda (referring to python env, not a container or virtual machine):
    - Syntax (in this example [repoName]=scaffold): 
        - Create env: `python3 -m venv ~/.[repoName]`
        - Activate env: `source ~/.[repoName]/bin/activate`
3) Run makefile:
   - Install and verify functionality:
     - `make install`
     - `make test`
