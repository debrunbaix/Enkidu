#!/bin/bash

# Variables
REQUIRED_PYTHON_VERSION="3.9"
GHIDRA_VERSION="10.1.5"
GHIDRA_URL="https://ghidra-sre.org/ghidra_${GHIDRA_VERSION}_PUBLIC_20210928.zip"
GHIDRA_DIR="ghidra_${GHIDRA_VERSION}"
GHIDRA_INSTALL_PATH="./ghidra"

# Function to compare Python versions
version_gt() { test "$(echo "$@" | tr " " "\n" | sort -V | tail -n 1)" == "$1"; }

# Check if the correct Python version is installed
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
if version_gt $REQUIRED_PYTHON_VERSION $PYTHON_VERSION || version_gt $PYTHON_VERSION $REQUIRED_PYTHON_VERSION; then
    echo "Correct Python version ($REQUIRED_PYTHON_VERSION) is already installed."
else
    echo "Installing Python $REQUIRED_PYTHON_VERSION..."
    sudo apt-get update
    sudo apt-get install python${REQUIRED_PYTHON_VERSION}
fi

# Create and activate virtual environment
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate

# # Install required Python packages
# pip install -r requirements.txt

# # Download and install Ghidra
# if [ ! -d "$GHIDRA_INSTALL_PATH" ]; then
#     echo "Downloading Ghidra $GHIDRA_VERSION..."
#     wget $GHIDRA_URL -O ghidra.zip
#     unzip ghidra.zip -d .
#     mv $GHIDRA_DIR $GHIDRA_INSTALL_PATH
#     rm ghidra.zip
# fi

# # Add Ghidra path to .env file
# echo "GHIDRA_PATH=$GHIDRA_INSTALL_PATH" > .env

# # Notify user of successful installation
# echo "Installation completed successfully."
# echo "To activate the virtual environment, run: source venv/bin/activate"
