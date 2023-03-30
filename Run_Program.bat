@echo off
start cmd /k python lib/db/seed.py
mode con: cols=80 lines=24
/k python lib/cli.py

@REM Testing to see if I can generate a batch file that will create a fixed cli file
@REM so that we can do "screens" and art and actually fit them on the page