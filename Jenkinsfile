pipeline {
    agent any

    // Triggers: Run on code push AND on nightly cron schedule at 2:00 AM
    triggers {
        pollSCM('H/5 * * * *')     // Poll Git every 5 mins OR trigger via GitHub Webhook
        cron('H 2 * * *')          // Nightly Scheduled Run at 02:00 AM
    }

    environment {
        HEADLESS = 'True'
        BROWSER = 'chromium'
    }

    stages {
        stage('1. Checkout') {
            steps {
                echo 'Checking out automation repository...'
                checkout scm
            }
        }

        stage('2. Prepare Environment') {
            steps {
                echo 'Setting up Python virtual environment and dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    playwright install --with-deps chromium
                '''
            }
        }

        stage('3. Run Smoke & API Tests') {
            steps {
                echo 'Executing Smoke & API automated tests...'
                sh '''
                    . venv/bin/activate
                    pytest -m "smoke or api" --html=reports/report.html --self-contained-html
                '''
            }
        }

        stage('4. Run Full Regression') {
            when {
                // Run full regression only on scheduled nightly runs or main branch
                anyOf {
                    branch 'main'
                    triggeredBy 'TimerTrigger'
                }
            }
            steps {
                echo 'Executing Full Regression Suite...'
                sh '''
                    . venv/bin/activate
                    pytest --html=reports/report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            echo 'Archiving test results and HTML reports...'
            archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
            
            // If Jenkins HTML Publisher plugin is installed:
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Automation Test Execution Report'
            ])
        }
        failure {
            echo 'Test suite completed with failures! Alerting team via Slack / Email...'
        }
        success {
            echo 'All automated test scenarios passed successfully!'
        }
    }
}
