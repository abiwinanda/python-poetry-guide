# Python Project Management with Poetry

## **1. Introduction**
Poetry is a dependency and package manager for Python that helps manage virtual environments and dependencies efficiently. This project is a sample project that is created using `poetry`. To setup `poetry` and understand how to use it, read-on.

## **2. Installation**
Install Poetry globally:
```sh
curl -sSL https://install.python-poetry.org | python3 -
```

## **3. Setting Up a Poetry Project**
Create a new project:
```sh
poetry new my_project
cd my_project
```
Or initialize an existing project:
```sh
poetry init
```

**Note:** `poetry init` initializes a new Poetry project inside an existing directory by creating a pyproject.toml file. It does not create a new folder (unlike `poetry new`).

## **4. Installing Dependencies**
```sh
poetry add requests  # Add a dependency
poetry install       # Install all dependencies
```
**Note:** By default `poetry add` will auto install the dependency. If you clone an existing project made with poetry then you could run `poetry install` to install the dependencies of the project.

`poetry` will install all dependencies in a virtual environment. If you want to check what dependencies or virtual environments are installed or created, you could use `poetry show`
```sh
poetry show            # List installed dependencies
poetry env info        # Show virtual environment details
```

## **5. Running the Project**
- **Recommended:** Use `poetry run`:
  ```sh
  poetry run python src/project_name/main.py
  ```
- **Activate the virtual environment manually**:
  ```sh
  poetry shell
  python src/project_name/main.py
  ```
**Note:** Notice that running `main.py` without using poetry command require you to start the virtual env manually. This means that if the `main.py` isn't run using `poetry run` the dependencies of the project are not installed. `poetry run` makes it seamless to run the project with the virtual env.

## **6. Running with a Custom Script**
If `main.py` is under `src/project_name/`, add this to `pyproject.toml`:
```toml
[tool.poetry]
packages = [{ include = "project_name", from = "src" }]

[tool.poetry.scripts]
project = "project_name.main:main"
```
Then run:
```sh
# make sure to run this every time poetry scripts are added or updated
poetry install
poetry run project
```

**Note:** `project_name.main:main` means that the script will run `main()` function inside `main.py` file under `src/project_name` directory. Therefore, ensure that the function `main()` exists in the `main.py`.

## **7. Conclusion**
Poetry simplifies dependency management and ensures a clean, isolated environment. Always use `poetry run` (recommended) or `poetry shell` to run your project inside the virtual environment.
