# UCR-Club-Search

## Setup dev environment

* Install `uv`. [Follow the steps here](https://github.com/astral-sh/uv#installation)
* Create a Virtual Python environment: `uv venv`
* Enter the virtual python environment: `source .venv/bin/activate`
  * Note: you can exit by just typing out `deactivate` inside of the terminal
* Now you can `uv sync` the project to download all of the dependencies
  * Note: you can add new dependencies to the project using `uv add <package-name>`
* Run the project `uv run main.py`
* You can learn more about `uv` [here](https://docs.astral.sh/uv/)
