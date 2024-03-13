from setuptools import find_packages,setup
from typing import List

HYPHEN_e='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this func will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_e in requirements:
            requirements.remove(HYPHEN_e)

    return requirements
setup(
    name='MLProject',
    version='0.0.1',
    author='Aniket',
    author_email='aniketgupta89611@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)