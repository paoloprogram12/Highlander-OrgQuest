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

## Run with docker

* `docker compose up -d --build`
  * please comment out nvidia gpu in the docker-compose.yml file if your
    computer does not have one.
* The webapp port will be avaliable at 8000


## Push and Pull code

* Clone the code to your IDE: git clone https://github.com/paoloprogram12/Highlander-OrgQuest.git
* Pull recent changes: git pull

### All commands needed before Pushing back into github

* Create a branch and checkout to that branch: git checkout -b "branchName"
* (Optional)Create a branch: git branch "branchName"
* (Optional)Go to a branch: git checkout "branchName"
* Stage all changes: git add . 
* (Optional)Stage specific changes: git add "fileName" 
* Commit changes: git commit -m "description of changes"
* Push changes to remote: git push origin "branchName"
