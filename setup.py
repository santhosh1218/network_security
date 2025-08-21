"""
The setup.py file is an essential part of packaging and distributing python projects.
It is used by setuptools(or distutils in older Python versions) to define the configuration
of your projects, such as its metadata, dependencies, and more..

"""
from setuptools import find_packages,setup

def get_requirements():
    """
    this function will return list of requirements
    """
    requirements_list=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            # process each line
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print('requirements file not found')
    
    return requirements_list

setup(
    name='NetworkSecurity',
    version='0.0.0.1',
    author='santhosh reddy',
    author_email='santhoshkommula98@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()

)
