#!/bin/bash
echo "Activating virtual environment and packaging the application..."
source venv/bin/activate

echo ""
echo "Running PyInstaller..."
python3 -m PyInstaller --onefile --windowed --version-file version_info.txt Clicker.py

echo ""
echo "Packaging complete!"
echo "You can find the executable in the 'dist' folder."