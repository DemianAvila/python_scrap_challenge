#!/bin/bash

#CHECK IF WE HAVE PYTHON IN PATH, AT LEAST V3
python_path=$(command -v python3 || command -v python ) && \
echo "INFO: Python installed and in path"|| \
echo "ERROR: There is no python instalation on the path" && >&2

python_v=$(${python_path} --version)

if echo ${python_v} |  awk '/^Python[python] [3]\.(3|[4-9]|[1-9][0-9])/' > /dev/null; then
    echo "INFO: Python has a 3.1 version, right for run the project"
else
    echo "ERROR: Python version is lower than 3.1."  && >&2
fi

#CHECK IF WE HAVE VENV, IF SO CREATE A VENV AND INSTALL REQUIREMENTS 
eviron_path=$(pwd)/build/no_docker/environment
${python_path} -m virtualenv -h > /dev/null &&\
echo "INFO: virtualenv module is installed"|| \
echo "ERROR: virtaulenv module is not installed, install it via your package manager or via pip"  && >&2

${python_path} -m virtualenv ${eviron_path} && \
echo "INFO: Environment created correctly" ||
echo "ERROR: Couldn't create environment"  && >&2

#INSTALL REQUIREMENTS
src_path=$(pwd)/src
challenge1_path=${src_path}/first_challenge
challenge2_path=${src_path}/second_challenge
pip_path=${eviron_path}/bin/pip3
python_env_path=${eviron_path}/bin/python3

${pip_path} install -r ${challenge1_path}/requirements.txt
${pip_path} install -r ${challenge2_path}/requirements.txt
