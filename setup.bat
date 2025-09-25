@echo off
echo Setting up Python virtual environment...
python -m venv venv

echo.
echo Activating virtual environment and installing dependencies...
call venv\Scripts\activate.bat
pip install -r requirements.txt

echo.
echo Setup complete. You can now run the packaging script.
pause