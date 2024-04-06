@echo off
set CONDA_DIR=%~dp0conda\
set CONDA=%CONDA_DIR%condabin\conda.bat

if exist %CONDA_DIR% goto :end

curl -Lk https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe --output setup.exe
start /wait "" setup.exe /InstallationType=JustMe /RegisterPython=0 /S /D=%~dp0conda
del /Q /F setup.exe
%CONDA% env create -f environment.yml
:end