import io
from os import path
from setuptools import setup, find_packages

MYDIR = path.abspath(path.dirname(__file__))

cmdclass = {}
ext_modules = []

setup(
    name='logging_basic_config',  
    version='1.4.3',
    author="Marcelo Santino",
    author_email="marcelo@santino.dev",
    description="Basic logging configurations to easily use in many projects",
    url='https://github.com/msantino/logging-basic-config',
    long_description=io.open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['tests']),
    include_package_data=False,
    zip_safe=False,
    setup_requires=[],
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )