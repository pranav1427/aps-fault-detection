from setuptools import find_packages ,setup

from typing import List

REQUIREMENTS_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->list[str]:
    
    with open(REQUIREMENTS_FILE_NAME) as reqirement_file:
        requirement_list =reqirement_file.readline()
    requirement_list=[reqiurement_name.replace("\n","") for requirement_name in requirement_list]
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list

setup(name="sensor" ,
    version="0.0.1" ,
    author="pranav_v",
    author_email="pranavvanage@gmail.com",
    packages= find_packages()
    install_requires=get_requirements(),
)