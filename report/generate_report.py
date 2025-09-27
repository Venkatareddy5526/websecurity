from jinja2 import Template
import datetime
import os
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'template_report.html')
TEMPLATE = open(TEMPLATE_PATH, encoding='utf-8').read()

def create_report(findings, filename='report_output.html'):
    t = Template(TEMPLATE)
    out = t.render(date=datetime.datetime.now(), findings=findings)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(out)
    print('Report saved to', filename)

if __name__ == '__main__':
    findings = [
        {'id':1,'title':'Reflected XSS','severity':'High','url':'http://127.0.0.1:5001/','poC':'payload echoed (original)','fix':'Escape output'},
        {'id':2,'title':'SQL Injection (demo)','severity':'High','url':'http://127.0.0.1:5001/','poC':'bypass/login (original)','fix':'Use parameterized queries — Fixed in vuln_demo_fixed.py'},
    ]
    create_report(findings)
