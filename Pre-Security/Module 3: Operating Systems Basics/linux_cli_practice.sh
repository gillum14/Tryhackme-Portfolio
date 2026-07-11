#!/bin/bash

# Linux CLI Basics Practice Script
# This script supports my Linux CLI Basics notes by safely demonstrating
# common beginner Linux commands.

echo "Linux CLI Basics Practice"
echo "========================="
echo

echo "Current working directory:"
pwd
echo

echo "Current user:"
whoami
echo

echo "Operating system name:"
uname
echo

echo "Kernel and system information:"
uname -a
echo

echo "Files and folders in the current directory:"
ls
echo

echo "Detailed file listing:"
ls -l
echo

echo "All files, including hidden files:"
ls -al
echo

echo "Disk usage:"
df -h
echo

echo "Searching for README files from the current directory:"
find . -name "README.md" 2>/dev/null
echo

echo "Practice complete."
