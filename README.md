# Status Badge
This shows the status of the build actions.
[![Python application test with Github Actions](https://github.com/jtclark2/scaffold/actions/workflows/main.yml/badge.svg)](https://github.com/jtclark2/scaffold/actions/workflows/main.yml)

# scaffold
This is a project scaffold for python. We will create the basic files that form the foundation for most projects.
This file follows the [Cloud Computing Foundations tutorial](https://www.coursera.org/learn/cloud-computing-foundations-duke/lecture/dxL50/constructing-a-python-project-scaffold) 

- Makefile: use tabs in makefile (instead of spaces)
- requirements.txt   
- script(s): The project code (eg: the .py files)
- test files (for testing the scripts)
- virtualenv:
    - Syntax (in this example [repoName]=scaffold): 
        - Create env: `python3 -m venv ~/.[repoName]``
        - Activate env: `source ~/.[repoName]/bin/activate`
