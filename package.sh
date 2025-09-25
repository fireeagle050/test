#!/bin/bash
echo "Activating virtual environment and packaging the application..."
source venv/bin/activate

echo ""
echo "Running PyInstaller with version info and icon..."

# Use absolute paths to ensure files are found
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
python3 -m PyInstaller --onefile --windowed --version-file "$SCRIPT_DIR/version_info.txt" --icon="$SCRIPT_DIR/icon.ico" Clicker.py

echo ""
echo "Packaging complete!"
echo "You can find the executable in the 'dist' folder."