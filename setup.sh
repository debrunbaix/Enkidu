#!/bin/bash

# Variables
REQUIRED_PYTHON_VERSION="3.9"
GHIDRA_VERSION="10.1.5"
GHIDRA_URL="https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.4_build/ghidra_10.4_PUBLIC_20230928.zip"
GHIDRA_DIR="ghidra_10.4_PUBLIC"
GHIDRA_INSTALL_PATH="$(pwd)/ghidra"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Function to print messages with colors
function print_info {
    echo -e "${BLUE}[INFO]${NC} $1"
}

function print_success {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

function print_warning {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

function print_error {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to compare Python versions
version_gt() { test "$(echo "$@" | tr " " "\n" | sort -V | tail -n 1)" == "$1"; }

# Check if the correct Python version is installed
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
if version_gt $REQUIRED_PYTHON_VERSION $PYTHON_VERSION || version_gt $PYTHON_VERSION $REQUIRED_PYTHON_VERSION; then
    print_success "Correct Python version ($REQUIRED_PYTHON_VERSION) is already installed."
else
    print_info "Installing Python $REQUIRED_PYTHON_VERSION..."
    sudo apt-get update
    sudo apt-get install python${REQUIRED_PYTHON_VERSION}
fi

# Ensure pip is installed
if ! python3 -m ensurepip &> /dev/null; then
    print_info "Installing pip..."
    sudo apt-get install -y python3-pip
fi

# Install the venv module if not present
if ! dpkg -s python3-venv &> /dev/null; then
    print_info "Installing python3-venv..."
    sudo apt-get install -y python3-venv
fi

# Create and activate virtual environment
if [ ! -d "venv" ]; then
    print_info "Creating virtual environment..."
    python3 -m venv venv
fi

if [ -d "venv/bin" ]; then
    print_info "Activating virtual environment..."
    source venv/bin/activate
else
    print_error "Virtual environment not found."
    exit 1
fi

print_info "Installing required packages and libraries..."
sudo apt-get install libc6-i386 -y
sudo apt install checksec -y
sudo apt-get install openjdk-11-jre -y
sudo apt-get install openjdk-17-jdk -y

# Install required Python packages
pip install -r requirements.txt

# Download and install Ghidra
if [ ! -d "$GHIDRA_INSTALL_PATH" ]; then
    print_info "Downloading Ghidra $GHIDRA_VERSION..."
    wget $GHIDRA_URL -O ghidra.zip
    unzip ghidra.zip -d .
    mv $GHIDRA_DIR $GHIDRA_INSTALL_PATH
    rm ghidra.zip
fi

# Add Ghidra path to .env file
echo "GHIDRA_HEADLESS_PATH=$GHIDRA_INSTALL_PATH/support/analyzeHeadless" > app/decompile_zone/.env

# Notify user of successful installation
print_success "Installation completed successfully."
print_info "To activate the virtual environment, run: source venv/bin/activate"