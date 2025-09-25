@echo off
echo Packaging the application into a single executable file...
echo This may take a few moments.

python -m PyInstaller --onefile --windowed Clicker.py

echo.
echo Packaging complete!
echo You can find the executable in the 'dist' folder that was just created.
pause