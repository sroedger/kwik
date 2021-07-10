#! bin/sh

# Deploy build to the PyPI test site
# test.pypi.org
python -m pip install --upgrade twine
python -m twine upload --repository testpypi dist/*
