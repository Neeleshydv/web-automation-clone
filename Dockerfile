FROM mcr.microsoft.com/playwright/python:v1.42.0-jammy

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV HEADLESS=True
ENV BROWSER=chromium

CMD ["pytest", "--html=reports/report.html", "--self-contained-html"]
