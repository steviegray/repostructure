# repostructure
Playing with repo structure and imports, packages and modules.

My attempt at tryng to figure out how imports work with packages when you have multiple directories and are trying to follow 
http://python-guide-pt-br.readthedocs.io/en/latest/writing/structure/

# Tests
To run the tests do one of the following 

1. Run them via nose
```
$ nosetests
```
2. Install package as developer
```
$ pip install -e .
$ python -m tests/test_hello
```

# Notes
* The following is a good read for packaging https://python-packaging.readthedocs.io/en/latest/index.html
