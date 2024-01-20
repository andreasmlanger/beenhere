from airtable import Airtable
import os
from dotenv import dotenv_values
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

config = {
    **dotenv_values(Path(BASE_DIR, '.env')),
    **os.environ
}

BASE_ID = config.get('AIRTABLE_BASE_ID')
TABLE_NAME = config.get('AIRTABLE_TABLE_NAME')
TOKEN = config.get('AIRTABLE_TOKEN')

AIRTABLE = Airtable(BASE_ID, TABLE_NAME, TOKEN)
