from setuptools import setup, find_packages
from typing import List

def getRequirements(file_path:str)-> List[str]:

    """
    This function will return the list of requirements
    """
    requirements = []

    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements =   [req.replace("\n", "") for req in requirements]
    
    return requirements








setup(
    name = "my_package",
    version= "0.0.1",
    author = "anurag singh bhagour",
    author_email = "singanurag46@gmail.com",
    description="pakage to test the setup.py file",
    install_requires=getRequirements("requirements.txt"),
)