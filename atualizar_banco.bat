@echo off
echo ==========================================
echo      ATUALIZANDO BANCO DE DADOS
echo ==========================================
echo.

echo 1. Criando arquivos de migracao...
python manage.py makemigrations core

echo.
echo 2. Aplicando alteracoes no banco de dados...
python manage.py migrate

echo.
echo ==========================================
echo      TUDO PRONTO! PODE FECHAR.
echo ==========================================
pause