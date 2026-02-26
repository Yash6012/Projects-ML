from setuptools import find_packages, setup
from typing import List

HYPHEN_E = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Returns the list of Requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)
    return requirements


setup(
    name='Project - ML',
    version='0.0.1',
    author='Yash',
    author_email='yash7singh3@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)