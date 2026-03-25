 # later we can use this project as package and install them

from setuptools import find_packages , setup
from typing import List
HYPEN_E_DOT ='-e .'
def get_requirements(file_path: str) -> List[str]: # file_path: str it tell it should be string not other and List[str]: it tell this return list of string
    """
    this function will return the list of requirement
    """

    requirements = [] # create emty list
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements   # ✅ properly aligned
      
   





setup(
name='mlproject',
version='0.0.1',
author='chetan',
install_requires=get_requirements('requirements.txt'), 
packages=find_packages()

)

