@echo off
rem Fafa - lancador do desktop. Abre o Fafa por voz na janela propria.
title Fafa
chcp 65001 >nul
set PYTHONUTF8=1
cd /d "%~dp0backend"
if not exist ".venv\Scripts\python.exe" (
  echo Ambiente nao encontrado. Rode primeiro: python -m venv .venv ^&^& .venv\Scripts\pip install -e ".[all,dev]"
  pause
  exit /b 1
)
if not exist ".env" (
  echo Falta o arquivo backend\.env. Copie .env.example para .env e preencha a ANTHROPIC_API_KEY.
  pause
  exit /b 1
)
".venv\Scripts\python.exe" -m fafa voz %*
if errorlevel 1 pause
