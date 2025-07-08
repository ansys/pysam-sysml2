@REM This section install VSCode extensions for PySam Developers
call code --install-extension donjayamanne.python-extension-pack
call code --install-extension ms-python.black-formatter
call code --install-extension ms-python.flake8
call code --install-extension ms-python.isort
call code --install-extension sonarsource.sonarlint-vscode
@REM This section install Python dependencies for PySam developers
pip install -r requirements.txt
