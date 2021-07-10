#! bin/sh

python -m pip install --upgrade pip build
python -m pip install wheel bdist_wheel
python setup.py bdist_wheel
python -m build
