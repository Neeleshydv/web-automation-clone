# LightX Web & API Test Automation Framework

A production-grade, scalable End-to-End Test Automation Framework for **LightX** implementing **Page Object Model (POM)** for Web UI automation using **Playwright** and an independent **REST API Testing Engine** with automated CI/CD integration (**GitHub Actions** & **Jenkins**).

---

## 🏗️ Architecture & Directory Structure

```
automation-suite-python/
│
├── config/
│   └── config.py               # Central environment configuration (.env reader)
│
├── pages/                      # Page Object Model (POM)
│   ├── base_page.py            # Reusable actions, explicit waits, screenshot helpers
│   ├── login_page.py           # Encapsulated locators & user flows for Login
│   └── inventory_page.py       # Encapsulated locators & flows for Dashboard/Cart
│
├── api/                        # REST API Automation Engine
│   ├── api_client.py           # Reusable session client (GET, POST, PUT, DELETE, auth)
│   └── endpoints.py            # Centralized API route contracts
│
├── tests/                      # Automated Test Scenarios
│   ├── conftest.py             # Global Pytest fixtures & HTML report screenshot hooks
│   ├── test_ui.py              # Web UI automation test scenarios
│   └── test_api.py             # REST API automation test scenarios
│
├── reports/                    # Auto-generated HTML execution reports & failure screenshots
│   ├── report.html             # Standalone interactive HTML report dashboard
│   └── screenshots/            # Automated failure capture
│
├── .github/workflows/          # CI/CD Workflows
│   └── test-pipeline.yml       # Push, PR, Nightly Cron, & Manual dispatch triggers
│
├── Jenkinsfile                 # Enterprise Declarative Jenkins CI/CD pipeline
├── Dockerfile                  # Containerized test runner
├── docker-compose.yml          # Multi-container orchestration
├── pytest.ini                  # PyTest configuration & test markers
├── requirements.txt            # Python dependencies
└── run_tests.bat               # 1-Click local test execution runner
```

---

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.10+ (Tested on Python 3.13)
* Git

### 2. Installation
```powershell
# Clone the repository
git clone https://github.com/Neeleshydv/web-automation-clone.git
cd web-automation-clone

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Install Playwright browser binaries
playwright install chromium
```

---

## 🧪 Executing Tests

### Quick Execution
Double-click `run_tests.bat` or run via PowerShell:
```powershell
.\run_tests.bat
```

### Targeted Execution via Pytest Markers
```bash
# Run only Smoke tests
pytest -m smoke -v

# Run Web UI tests with browser visible (Headed Mode)
pytest -m ui -v --headed

# Run REST API tests
pytest -m api -v

# Run full Regression suite
pytest -m regression -v
```

---

## 🔄 CI/CD Automation & Pipeline Triggers

The framework is configured for continuous testing across multiple pipeline triggers:

1. **Pull Request & Push Trigger**:
   * Automatically executes on pushes to `main`, `master`, and `develop`.
   * Gates feature branches by running the Smoke & API suites to catch regressions early.

2. **Nightly Scheduled Execution (Cron)**:
   * Configured via cron expression (`0 2 * * *`) in GitHub Actions and Jenkins.
   * Executes the full Regression suite overnight against staging environments.

3. **Manual Workflow Dispatch**:
   * Enables team members to trigger pipeline runs on-demand with custom inputs (selecting browser engines and test markers).

---

## 📊 Test Reporting & Failure Diagnosis

* **Interactive HTML Report**: Generates a self-contained HTML report at `reports/report.html` containing execution timelines, environment metadata, and pass/fail metrics.
* **Automatic Failure Screenshots**: Implemented via custom PyTest hook `pytest_runtest_makereport` in `tests/conftest.py`—captures full-page screenshots on any test failure and attaches them directly inside the HTML report for instant root-cause analysis.
