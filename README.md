# LightX Test Automation Framework (Python + PyTest + Playwright)

A production-grade, scalable End-to-End Test Automation Framework implementing **Page Object Model (POM)** for Web UI automation and an independent **REST API Testing Engine** with CI/CD integration (**GitHub Actions** & **Jenkins**).

---

## ðŸ—ï¸ Framework Architecture

```
automation-suite-python/
â”‚
â”œâ”€â”€ config/
â”‚   â””â”€â”€ config.py               # Central environment configuration (.env reader)
â”‚
â”œâ”€â”€ pages/                      # Page Object Model (POM)
â”‚   â”œâ”€â”€ base_page.py            # Reusable actions, explicit waits, screenshot helpers
â”‚   â”œâ”€â”€ login_page.py           # Encapsulated locators & user flows for Login
â”‚   â””â”€â”€ inventory_page.py       # Encapsulated locators & flows for Dashboard/Cart
â”‚
â”œâ”€â”€ api/                        # REST API Automation Engine
â”‚   â”œâ”€â”€ api_client.py           # Reusable session client (GET, POST, PUT, DELETE, auth)
â”‚   â””â”€â”€ endpoints.py            # Centralized API route contracts
â”‚
â”œâ”€â”€ tests/                      # Test Scenarios
â”‚   â”œâ”€â”€ conftest.py             # Global Pytest fixtures & HTML report screenshot hooks
â”‚   â”œâ”€â”€ test_ui.py              # Web UI automation test scenarios
â”‚   â””â”€â”€ test_api.py             # REST API automation test scenarios
â”‚
â”œâ”€â”€ reports/                    # Auto-generated HTML reports & failure screenshots
â”‚   â”œâ”€â”€ report.html             # Standalone interactive HTML report dashboard
â”‚   â””â”€â”€ screenshots/            # Failure screenshots
â”‚
â”œâ”€â”€ .github/workflows/          # CI/CD Workflows
â”‚   â””â”€â”€ test-pipeline.yml       # Push, PR, Nightly Cron, & Manual triggers
â”‚
â”œâ”€â”€ Jenkinsfile                 # Enterprise Declarative Jenkins CI/CD pipeline
â”œâ”€â”€ Dockerfile                  # Containerized test runner
â”œâ”€â”€ pytest.ini                  # PyTest configuration & markers (smoke, regression, etc.)
â”œâ”€â”€ requirements.txt            # Python dependencies
â””â”€â”€ run_tests.bat               # 1-Click execution script for live demonstration
```

---

## ðŸš€ How to Run Tests Locally

### 1. One-Click Demo
Double-click `run_tests.bat` or run:
```powershell
.\run_tests.bat
```
This executes the test suite and automatically opens `reports/report.html` in your default browser.

### 2. Run by Markers
```bash
# Run only Smoke tests
pytest -m smoke

# Run only UI tests (Headed mode with browser visible)
pytest -m ui

# Run only API tests
pytest -m api

# Run comprehensive Regression suite
pytest -m regression
```

---

## ðŸ”„ CI/CD Automation Triggers Explained

### 1. Developer Push / PR Trigger
- **Event**: A developer pushes code or creates a Pull Request.
- **Action**: GitHub Actions / Jenkins automatically triggers the **Smoke Test Suite**.
- **Outcome**: Protects main branch by failing the build if existing features break (preventing regression bugs).

### 2. Scheduled Nightly Runs (Cron)
- **Event**: Configured cron schedule (`0 2 * * *` - 2:00 AM UTC).
- **Action**: Runs the **Full Regression Suite** overnight.
- **Outcome**: The team arrives in the morning with an updated HTML report detailing application health.

### 3. Manual Workflow Dispatch
- **Event**: QA or Lead triggers pipeline on-demand from GitHub/Jenkins UI.
- **Action**: Can dynamically select test marker (`smoke`, `regression`, `api`) and browser (`chromium`, `firefox`, `webkit`).

---

## ðŸŽ¯ Interview Talking Points & NDA Presentation Script

### Question 1: *"Can you show us your work from your current or past company?"*
> **Answer**:  
> *"Due to company confidentiality and NDA, I cannot share my previous employer's proprietary source code or internal application URLs. However, to demonstrate my technical approach, I built this LightX Test Automation framework. It mirrors the exact production architecture I work with: Page Object Model with Playwright, a dedicated REST API client, PyTest fixtures, and CI/CD pipelines in Jenkins and GitHub Actions."*

### Question 2: *"Why did you choose Playwright over Selenium?"*
> **Answer**:  
> *"Playwright provides native auto-waiting (eliminating flaky `Thread.sleep` or complex explicit waits), fast headless execution via Chrome DevTools Protocol, built-in network interception, trace recording, and native support for multi-tab and iframe handling out-of-the-box."*

### Question 3: *"How do you handle test flakiness and failure diagnosis?"*
> **Answer**:  
> *"1. We use Playwright's auto-wait on actionability states (visible, stable, enabled).*  
> *2. In `tests/conftest.py`, we implement a custom PyTest hook `pytest_runtest_makereport` that automatically captures full-page screenshots on any test failure and attaches them directly inside the HTML report for instant RCA (Root Cause Analysis).*  
> *3. In CI, we archive Playwright traces which allow stepping through test execution with DOM snapshots, console logs, and network calls."*

