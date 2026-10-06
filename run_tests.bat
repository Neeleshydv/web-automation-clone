@echo off
title Automation Suite Demo Runner
echo ========================================================
echo    LightX Test Automation SUITE - INTERVIEW DEMO
echo ========================================================
echo 1. Activating Virtual Environment...
call venv\Scripts\activate.bat

echo 2. Running Automated Tests (Headed UI + REST API)...
pytest -v -s --html=reports/report.html --self-contained-html

echo ========================================================
echo 3. Opening HTML Test Report in Browser...
echo ========================================================
start reports\report.html
pause

