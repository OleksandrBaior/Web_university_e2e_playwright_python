# Web_university_e2e_playwright_python
Common webelements on websites. e2e testing using python

1. If you receive “no module named pip” error you probably do not have pip installed. Run this command:
py -m ensurepip --upgrade (Windows)
or:
```
python -m ensurepip --upgrade (MacOS/Linux)
```
3. Install package manager:
```
pip install
```
5. Next let’s create an isolated virtual environment (to hold our project’s libraries
isolated from global environment):
```
pipenv shell
```
7. First we need pytest-playwright:
```
pipenv install pytest-playwrigh
````
9. Than we need to install browsers (or a specific browser to run our tests against)
playwright install will install all the browsers used by playwright
As of right now we’re going to use only Chrome browser run:
```
playwright install chromium
```
11. Running test:
```
pytest
```
12. Runing specific test with mark:  (@pytest.mark.*)
```
pytest -m *
```

