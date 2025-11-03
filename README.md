1. add this to your pyproject.toml file,  after the `dependencies` variable

[tool.poetry] 
package-mode = false



poetry install

eval $(poetry env activate)

poetry run python your_script.py

