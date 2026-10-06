Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "   LightX Test Automation SUITE - INTERVIEW DEMO" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan

& .\venv\Scripts\Activate.ps1
pytest -v -s --html=reports/report.html --self-contained-html

Write-Host "`nTest Execution Finished! Opening Report..." -ForegroundColor Green
Start-Process "reports/report.html"

