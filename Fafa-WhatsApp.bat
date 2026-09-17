@echo off
rem Fafa no WhatsApp: sobe o webhook e o tunel publico. Deixe esta janela aberta.
title Fafa - WhatsApp
chcp 65001 >nul
set PYTHONUTF8=1
cd /d "%~dp0backend"
".venv\Scripts\python.exe" -m fafa whatsapp %*
pause
