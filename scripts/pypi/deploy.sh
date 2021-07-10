#! bin/sh

# Deploy build to PyPi, pypi.org
python -m pip install --upgrade twine
python -m twine upload dist/*
