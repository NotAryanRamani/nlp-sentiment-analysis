# This file creates this project as a package
# which can be accessed by anyone by downloading it

from setuptools import find_packages, setup
from typing import List

def get_requirements(file:str)->List[str]:
    requirements = []
    with open(file) as file_:
        requirements = file_.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        print(requirements)
        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(
    name = 'NLP_Sentiment_Analysis',
    version = '1.0.0',
    author = 'Aryan Ramani',
    author_email = 'aryanramani67@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)