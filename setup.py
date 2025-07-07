from setuptools import find_packages, setup
from typing import List
def get_requirements() -> List[str]:
    try:
        with open('requirements.txt', 'r') as file:
            requirement_list = [
                line.strip() for line in file.readlines()
                if line.strip() and line.strip() != '-e .'
            ]
        return requirement_list
    except FileNotFoundError:
        print("requirements.txt file not found. Make sure it exists!")
        return []

setup(
    name="ragster",
    version="0.0.1",
    author="Sreekanth Pogula",
    author_email="sreekanth.pogula2001@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires=">=3.10",  # Ensure compatible Python version
)