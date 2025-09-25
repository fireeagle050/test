#!/bin/bash
# Author: Fire Eagle
# This script packages the Auto-Clicker application into a single executable file.

echo "Packaging the application into a single executable file..."
echo "This may take a few moments."

python3 -m PyInstaller --onefile --windowed Clicker.py

echo ""
echo "Packaging complete!"
echo "You can find the executable in the 'dist' folder that was just created."