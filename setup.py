from setuptools import setup
from setuptools import find_packages

with open(file="README.md", mode="r", encoding="utf=8") as fh:
    long_description = fh.read()

setup(

    # this will be my Library name.
    name='python-bea',

    # Want to make sure people know who made it.
    author='Alex Reed',

    # also an email they can use to reach out.
    author_email='coding.sigma@gmail.com',

    # I'm in alpha development still, so a compliant version number is a1.
    # read this as MAJOR VERSION 0, MINOR VERSION 1, MAINTENANCE VERSION 0
    version='0.1.1',
    description='A python API client library for the US Bureau of Economic Analysis',

    # I have a long description but that will just be my README file.
    long_description=long_description,

    # want to make sure that I specify the long description as MARKDOWN.
    long_description_content_type="text/markdown",

    # here is the URL you can find the code.
    url='https://github.com/areed1192/python-bureau-economic-analysis-api-client.git',

    # there are some dependencies to use the library, so let's list them out.
    install_requires=[
        'requests'
    ],

    # here are the packages I want "build."
    packages=find_packages(include=['pybea']),

    # additional classifiers that give some characteristics about the package.
    classifiers=[

        # I want people to know it's still early stages.
        'Development Status :: 3 - Alpha',

        # My Intended audience is mostly those who understand finance.
        'Intended Audience :: Financial and Insurance Industry',

        # My License is MIT.
        'License :: OSI Approved :: MIT License',

        # I wrote the client in English
        'Natural Language :: English',

        # The client should work on all OS.
        'Operating System :: OS Independent',

        # The client is intendend for PYTHON 3
        'Programming Language :: Python :: 3'
    ],

    # you will need python 3.8 to use this libary.
    python_requires='>3.8'
)
