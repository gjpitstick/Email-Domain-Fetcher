import os
import re
import pandas as pd

def capture_emails(csv, domain, output):
  try:
    df = pd.read_csv(csv)
    headers = df.columns
    emails = []
    count = 0
    email_column = ''
    for header in headers:
      if re.match(r'email', header, re.IGNORECASE):
        email_column = df[header]
    for email in email_column:
      if re.match(fr'[a-zA-Z0-9][a-zA-Z0-9._%+-]+[^._%+\-@ ]@{domain}$', email):
        emails.append(email)
        count += 1
    print(f'Emails Matched:{count}')
    with open(output, 'w') as f:
      for email in emails:
        f.write(f'{email}\n')
      f.close()
    print(f"List has been written to {output}")
  except pd.errors.ParserError as e:
    print(f'Parser error: {e}')


def capture_emails_inv(csv, domain, output):
  try:
    df = pd.read_csv(csv)
    headers = df.columns
    emails = []
    count = 0
    email_column = ''
    for header in headers:
      if re.match(r'email', header, re.IGNORECASE):
        email_column = df[header]
    for email in email_column:
      if not re.match(fr'[a-zA-Z0-9][a-zA-Z0-9._%+-]+[^._%+\-@ ]@{domain}$', email):
        emails.append(email)
        count += 1
    print(f'Emails Matched:{count}')
    with open(output, 'w') as f:
      for email in emails:
        f.write(f'{email}\n')
      f.close()
    print(f"List has been written to {output}")
  except pd.errors.ParserError as e:
    print(f'Parser error: {e}')
