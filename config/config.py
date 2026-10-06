import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Config:
    """Centralized framework configuration loaded from environment variables."""
    BASE_URL: str = os.getenv("BASE_URL", "https://www.saucedemo.com")
    API_BASE_URL: str = os.getenv("API_BASE_URL", "https://reqres.in/api")
    HEADLESS: bool = os.getenv("HEADLESS", "TRUE").lower() in ("true", "1", "yes")
    BROWSER: str = os.getenv("BROWSER", "chromium")
    DEFAULT_TIMEOUT: int = int(os.getenv("DEFAULT_TIMEOUT", "30000"))

    # Test Credentials
    STANDARD_USER: str = os.getenv("STANDARD_USER", "standard_user")
    LOCKED_OUT_USER: str = os.getenv("LOCKED_OUT_USER", "locked_out_user")
    DEMO_PASSWORD: str = os.getenv("DEMO_PASSWORD", "secret_sauce")
