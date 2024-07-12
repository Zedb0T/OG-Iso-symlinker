@echo off
REM Get the current directory of the batch file
set "current_directory=%~dp0"

REM Get the current directory
set current_directory=%cd%

REM Get the location of the current script
set script_dir=%~dp0

REM Call the Python script with the full path to symlink.py
python "%script_dir%\symlink.py" %current_directory%
REM Pause to see output (optional)
pause
