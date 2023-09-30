# Web_university_e2e_playwright_python
Common webelements on websites. e2e testing using python

1. If you receive “no module named pip” error you probably do not have pip installed. Run this command:
py -m ensurepip --upgrade (Windows)
or:
python -m ensurepip --upgrade (MacOS/Linux)
2. Install package manager:
pip install
3. Next let’s create an isolated virtual environment (to hold our project’s libraries
isolated from global environment):
pipenv shel
4. First we need pytest-playwright. We can skip ==<VERSION> part as this project
does not require any specific version installed:
pipenv install pytest-playwrigh
5. Than we need to install browsers (or a specific browser to run our tests against)
playwright install will install all the browsers used by playwright
As of right now we’re going to use only Chrome browser run:
playwright install chromiu
6. Running test:
pytest
