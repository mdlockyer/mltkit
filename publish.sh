#!/bin/bash
pip install -r requirements.txt
pip install wheel
python setup.py sdist bdist_wheel
twine upload dist/*