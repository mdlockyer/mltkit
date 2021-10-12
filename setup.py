# -*- coding: utf-8 -*-
import shutil
from pathlib import Path

from setuptools import setup, find_packages
import src as mltkit

name = 'mltkit'
description = 'A toolkit for ML boilerplate.'
url = 'https://github.com/mdlockyer/mltkit'
author = 'Michael Lockyer'
author_email = 'mdlockyer@gmail.com'
version = src.__version__
license_type = 'MIT License'
classifiers = (
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: POSIX"
)
install_requires = ['PrintTags']
packages = find_packages()

proj_dir = Path(__file__).parent.resolve()
src_path = proj_dir.joinpath('src')
dest_path = proj_dir.joinpath(name)
try:
    shutil.copytree(src_path, dest_path)
    setup(name=name, description=description, version=version,
          url=url, author=author, author_email=author_email,
          license=license_type, classifiers=classifiers,
          packages=packages, python_requires='>=3.6')
finally:
    shutil.rmtree(dest_path)
