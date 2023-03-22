# this setup file will be responsible in using ML application as a package
# that is it can be used in another file/packages
from setuptools import find_packages, setup
from typing import List


HYPEN_DOT_E = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function returns list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        
        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)
            
    return requirements
        
    

setup(
    name='ML Project',
    version='0.0.1',
    author='Krishna Mohan',
    author_email='gollapalli.k@northeastern.edu',
    packages = find_packages(), 
    install_requires = get_requirements('requirements.txt')
)