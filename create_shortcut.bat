@echo off
:: Author: Fire Eagle
:: This script creates a shortcut on the desktop for the Auto-Clicker application.

echo Creating Desktop Shortcut...

set SCRIPT_DIR=%~dp0
set TARGET_EXE=%SCRIPT_DIR%dist\Clicker.exe
set SHORTCUT_NAME=Auto-Clicker

powershell.exe -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%USERPROFILE%\Desktop\%SHORTCUT_NAME%.lnk'); $s.TargetPath = '%TARGET_EXE%'; $s.Save()"

echo Shortcut created successfully on your Desktop.