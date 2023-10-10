# Web_university_e2e_playwright_python
Common webelements on websites. e2e testing using python

1.  Install Python
```
www.python.org/downloads/
```
2. Install python package installer:
```
py -m ensurepip --upgrade (Windows)
```
or:
```
python -m ensurepip --upgrade (MacOS/Linux)
```
3. Install package manager:
```
pip install pipenv
```
4. Next let’s create an isolated virtual environment (to hold our project’s libraries
isolated from global environment):
```
pipenv shell
```
5. First we need pytest-playwright:
```
pipenv install pytest-playwrigh
````
6. Than we need to install browsers (or a specific browser to run our tests against)
playwright install will install all the browsers used by playwright
As of right now we’re going to use only Chrome browser run:
```
playwright install chromium
```
7. Running test:
```
pytest
```
8. Runing specific test with mark:  (@pytest.mark.*)
```
pytest -m *
```

