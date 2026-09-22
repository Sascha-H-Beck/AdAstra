import os
import sys
from dotenv import load_dotenv
load_dotenv()

with open("shb.inc", "r") as f:
    ascciart = f.read()


def main() -> None:
    application_name = os.getenv("APPLICATION_NAME", "Nicht gefunden")
    application_version = os.getenv("APPLICATION_VERSION", "Nicht gefunden")
    application_date = os.getenv("APPLICATION_DATE", "Nicht gefunden")    
    db_name = os.getenv("POSTGRES_DB", "Nicht gefunden").capitalize()
    print(f"You are running {application_name} - Version: {application_version} Created on: {application_date}\n")
    print(ascciart)
    print(f"\nRunning.... (Database System: {db_name})")