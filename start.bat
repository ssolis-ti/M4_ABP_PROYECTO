@echo off
echo Starting Gestor Inteligente de Clientes...
python run.py
if %ERRORLEVEL% NEQ 0 (
    echo Application exited with error.
    pause
)
