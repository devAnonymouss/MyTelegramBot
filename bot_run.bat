@echo off

call %~dp0MyTelegramBot\venv\Scripts\activate.ps1

cd %~dp0MyTelegramBot

set TOKEN=5666389838:AAFXr1a46OfXhRS0wq03uXmogRd4aFhEjZY

python telebot_marsian.py
pause