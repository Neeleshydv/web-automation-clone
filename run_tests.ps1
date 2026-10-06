Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "      LIGHTX WEB AND API AUTOMATION SUITE" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan

& .\venv\Scripts\Activate.ps1
python -m pytest -v -s --html=reports/report.html --self-contained-html

Write-Host "`nTest Execution Finished! Opening Report..." -ForegroundColor Green
Start-Process "reports/report.html"
