from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    """
    Read requirements from requirements.txt
    :param file_path: string path to requirements.txt
    :return: list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', ' ') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(name='MLproject',
      version='0.0.1',
      author='YLheureux',
      author_email='gayanekaraman@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
      )