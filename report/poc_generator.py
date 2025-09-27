# report/poc_generator.py
import csv
from datetime import datetime

POC_FILE = 'report/poc_output.txt'

vulns = [
    {"ID":1,"Title":"Reflected XSS","Payload":"<script>alert(1)</script>"},
    {"ID":2,"Title":"SQL Injection","Payload":"' OR '1'='1"}
]

with open(POC_FILE, 'w', encoding='utf-8') as f:
    f.write(f"PoC Report - {datetime.now()}\n\n")
    for v in vulns:
        f.write(f"ID: {v['ID']}\nTitle: {v['Title']}\nPayload: {v['Payload']}\n\n")

print(f"PoC saved in {POC_FILE}")
