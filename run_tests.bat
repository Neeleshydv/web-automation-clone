@echo off
title LightX Web and API Test Runner
echo ========================================================
echo       LIGHTX WEB AND API AUTOMATION SUITE
echo ========================================================
echo 1. Activating Virtual Environment...
call venv\Scripts\activate.bat

echo 2. Running Automated Tests (Headed UI + REST API)...
python -m pytest -v -s --html=reports/report.html --self-contained-html

echo ========================================================
echo 3. Opening HTML Test Report in Browser...
echo ========================================================
start reports\report.html
pause
