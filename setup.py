from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Remove newline and extra spaces

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)  # Remove '-e .' if present

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Pratham',
    author_email='prathmesh123k@gmail.com',  # Corrected argument name
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  # Ensure this returns a clean list
)
