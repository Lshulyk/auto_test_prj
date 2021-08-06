# Lshulyk test project

###Dependencies:
```bash
Python3.9
pip
```
### Using pip install virtualenv tool for managing virtual environments
```bash
$ pip install virtualenv
```
####NOTE: If you don't have pip installed pleas follow next instraction: https://pip.pypa.io/en/stable/installing/


###Create virtual environment with local path to python3.9 
##### NOTE: make sure env directory exists in /home/<user_name> diretory, if it's not please create with command: "mkdir /home/<user_name>/env"
```bash
$ python3.9 -m venv env
```
###Activate virtual env
```bash
$ source /home/<user_name>/env/bin/activate
```
###Install project dependencies with requirements.txt
```bash
$ pip install -r requirements.txt
```
####Run one test with pytest command
```bash
$ cd <path_to_project>/tests
$ pytest test_amazon_card.py
```
####Run all tests with pytest command
```bash
$ cd <path_to_project>/tests
$ pytest test_*.py
```
####Browser logs outputting to <browser_name>.log file in test directory
