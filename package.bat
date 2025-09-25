@echo off
echo Activating virtual environment and packaging the application...
call venv\Scripts\activate.bat

echo.
echo Running PyInstaller...
python -m PyInstaller --onefile --windowed --version-file version_info.txt Clicker.py

echo.
echo Packaging complete!
echo You can find the executable in the 'dist' folder.
pause