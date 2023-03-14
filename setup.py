# it is basically a meta data file 
# providing information about the project


from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'        # constant

def get_requirements(file_path:str)->List[str]:
    # this function will return a list of requirements 
    
    requirements = []
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()       # reads the file line by line

        # as the file is getting read line by line the \n needs to be eliminated 
        requirements = [req.replace("\n","") for req in requirements]    # for loop 

        # while installing the packages the -e . should not get executed hence we done this
        # -e .  is present in requirements.txt bcoz whenever the requirements.txt is executed 
        # then simalteneously setup.py should also get executed  
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Harshal',
    author_email='harshal7757@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)



# 1. 
# find_packages() --> it identifies folders that we want to serve as a packaage 
# suppose we have folder xyz which we want to treat as a package then just create 
# a file named __init__.py 
# In which ever folder the __init__.py file is present the find packages()
# will consider that folder as a package


# 2. 
# install_requires=['pandas','numpy','seaborn']
# will install all the required packages 
# but when number of packages increase it is not feasible to write them over here
# hence we use the requirements.txt file. where we can mention all the required packages
# we can achieve this by writing a function as done above.