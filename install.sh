#!/bin/bash

# Installation script for the Stadium Crowd Behavior Detection System
# This script installs all required dependencies and sets up the environment

echo "Installing Stadium Crowd Behavior Detection System..."
echo "===================================================="

# Check Python version
python3 --version

# Install required packages
echo "Installing required packages..."
pip3 install tensorflow opencv-python pillow matplotlib numpy tqdm

# Create necessary directories if they don't exist
echo "Setting up directory structure..."
mkdir -p stadium_dataset/images
mkdir -p stadium_dataset/annotations
mkdir -p models
mkdir -p alerts/images
mkdir -p test_results

echo "Installation complete!"
echo "To run the system, use: python3 main.py --mode [image|video|live] --input [path]"
echo "For more information, see README.md"
