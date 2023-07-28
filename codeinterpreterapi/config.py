from pydantic import BaseSettings
from dotenv import load_dotenv
from typing import Optional

# .env file
load_dotenv(dotenv_path="./.env")


class CodeInterpreterAPISettings(BaseSettings):
    """
    CodeInterpreter API Config
    """

    VERBOSE: bool = False

    CODEBOX_API_KEY: Optional[str] = None
    
    IMPLEMENTATION: Optional[str] = None
    AI_API_MODEL: Optional[str] = None 
    AI_API_KEY: Optional[str] = None
    AZURE_API_BASE: Optional[str] = None
    AZURE_API_VERSION: Optional[str] = None



settings = CodeInterpreterAPISettings()
