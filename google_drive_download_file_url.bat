@echo off
mode con: cols=95 lines=20
Title google_drive_download_file_url
color A1
@echo on
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
@ Echo: Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ECHO off
set path=%~dp0
set py=%LocalAppData%\Programs\Python\Python39\python.exe

REM dir /b %path%\*.py*

REM set /p file_name=ENTER file name (not end py) ?:

%py% "%path%\google_drive_download_file_url.py" 

pause
cls
"google_drive_download_file_url.bat"
