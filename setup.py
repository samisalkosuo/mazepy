# -*- coding: utf-8 -*-
 
 
"""setup.py: setuptools control."""
 
 
import re
from setuptools import setup

projectName="mazepy"
scriptFile="%s/%s.py" % (projectName,projectName)
description="Setuptools setup.py for mazepy."


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open(scriptFile).read(),
    re.M
    ).group(1)
 
 
with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")
 
 
setup(
    name = projectName,
    packages = [projectName],
    #add required packages to install_requires list
    #install_requires=["package","package2"]
    entry_points = {
        "console_scripts": ['%s = %s.%s:main' % (projectName,projectName,projectName)]
        },
    version = version,
    description = description,
    long_description = long_descr,
    author = "Sami Salkosuo",
    author_email = "dev@rnd-dev.com",
    url = "https://github.com/samisalkosuo/mazepy",
    license='MIT',
#list of classifiers: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=['Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
 'License :: OSI Approved :: MIT License',
 'Topic :: Software Development :: Libraries :: Python Modules',
 'Natural Language :: English',
 'Operating System :: OS Independent',
 'Programming Language :: Python :: 3.4',
 'Programming Language :: Python :: 3.5',
 'Programming Language :: Python :: 3 :: Only']
    )
