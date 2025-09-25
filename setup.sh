#!/bin/bash
echo "Setting up Python virtual environment..."
python3 -m venv venv

echo ""
echo "Activating virtual environment and installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt

echo ""
echo "Setup complete. You can now run the packaging script."