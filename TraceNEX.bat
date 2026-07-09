@echo off

echo Starting TraceNEX System...

cd /d C:\Users\KS\Documents\Missing-Person-Detection-System-main\Missing-Person-Detection-System-main\core

start cmd /k C:\Users\KS\.conda\envs\faceenv\python.exe manage.py runserver

start "" "C:\Users\KS\Desktop\Loomix Studios Client Files\TraceNEX\index.html"

exit