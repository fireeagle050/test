@echo off
echo Activating virtual environment and packaging the application...
call venv\Scripts\activate.bat

echo.
echo Running PyInstaller with version info and icon...

:: Use %~dp0 to get the script's directory, ensuring files are found
set SCRIPT_DIR=%~dp0
python -m PyInstaller --onefile --windowed --version-file "%SCRIPT_DIR%version_info.txt" --icon="%SCRIPT_DIR%icon.ico" Clicker.py

echo.
echo Packaging complete!
echo You can find the executable in the 'dist' folder.
pause