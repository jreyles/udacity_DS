#!/bin/bash

#Makes python code easy-to-read. Dependency: autopep8 (Install by typing: 'pip install autopep8')

echo -n "Enter Project Directory Folder (Either subfolder from working directory or full directory path): "
read project_dir

autopep8 $project_dir --recursive --in-place --pep8-passes 2000 --verbose
