from setuptools import Require, setup 
from typing import List

# declaring variables for the setup.py

PROJECT_NAME =  "Housing price prediction"
VERSION = "0.0.2"
AUTHOR = "PK"
DESCRIPTION = "Housing price prediction"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_PATH = "requirements.txt"

def get_requirements() ->List[str]:
    """ 
    Description: This function is going to return list of requirement 
    mention in requirements.txt file
    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_PATH) as requirements_file:
        return requirements_file.readlines()


setup( 
      name = PROJECT_NAME,
      Version = VERSION,
      author= AUTHOR,
      description= DESCRIPTION,
      packages= PACKAGES, 
      install_requires = get_requirements(),
      
)


          