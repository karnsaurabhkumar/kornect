#Build the project
python setup.py bdist_wheel

#Run the test
twine check dist/*

#Push to repository
python3 -m twine upload --repository testpypi dist/*