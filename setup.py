from setuptools import find_packages,setup # type: ignore
from typing import List

def get_Requirements(path:str)->List[str]:
    '''
        importing all the required packages from file
    '''
    requirements:List[str] = []
    HYPEN_E_DOT:str = "-e ."
    with open(path) as file:
        requirement = file.readlines()
        requirement = [req.replace("\n","") for req in requirement]            
        requirements.extend(requirement)
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="ML",
    version="0.0.1",
    author="Mohamed Aklamaash",
    author_email="aklamaash78@gmail.com",
    packages=find_packages(),
    install_requires = get_Requirements("requirements.txt")
)