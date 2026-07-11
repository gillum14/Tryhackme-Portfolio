# Windows CLI Basics Practice Script
# This script supports my Windows CLI Basics notes by demonstrating
# basic file navigation, file searching, and system information collection.

Write-Host "Windows CLI Basics Practice"
Write-Host "==========================="
Write-Host ""

Write-Host "Current directory:"
Get-Location
Write-Host ""

Write-Host "Files and folders in the current directory:"
Get-ChildItem
Write-Host ""

Write-Host "All files and folders, including hidden items:"
Get-ChildItem -Force
Write-Host ""

Write-Host "Current user:"
whoami
Write-Host ""

Write-Host "Basic system information:"
Get-ComputerInfo | Select-Object CsName, WindowsProductName, WindowsVersion, OsArchitecture
Write-Host ""

Write-Host "Network configuration:"
Get-NetIPConfiguration
Write-Host ""

Write-Host "Searching for README.md files from the current directory:"
Get-ChildItem -Path . -Recurse -Filter "README.md" -ErrorAction SilentlyContinue | Select-Object FullName
Write-Host ""

Write-Host "Practice complete."
