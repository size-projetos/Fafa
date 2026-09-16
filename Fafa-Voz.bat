@echo off
rem Fafa no terminal, por voz (Enter para falar). Alternativa ao painel.
title Fafa - voz
chcp 65001 >nul
set PYTHONUTF8=1
cd /d "%~dp0backend"
".venv\Scripts\python.exe" -m fafa voz %*
if errorlevel 1 pause
