@echo off

WHERE pyinstaller
IF %ERRORLEVEL% NEQ 0 pip install pyinstaller

pyinstaller --onefile -w app.py