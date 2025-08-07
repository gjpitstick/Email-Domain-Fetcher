import os
import sys
from argparse import ArgumentParser
from proj import capture_emails
from proj import capture_emails_inv

sys.tracebacklimit = 0

def main():
  parser = ArgumentParser(description='Email Parser Script')

  parser.add_argument('csv', help='The csv file that will be scanned to pull email addresses with a specified domain and list them in a text file. Ensure the column with emails has "email" (case insensitive) somewhere in the column name')
  parser.add_argument('--domain', help='The domain name you want to search for. Ex: gmail.com', required=True)
  parser.add_argument('--output', help='Filepath that you would like the output to be created at', required=True)
  parser.add_argument('--inverse', help='Will pull all the email addresses that dont contain the specified domain', action="store_true")

  args = parser.parse_args()

  if not os.path.isfile(args.csv):
    print(f'File was not found: {args.csv}')
    raise FileNotFoundError
  if not os.path.isdir(os.path.dirname(args.output)):
    print(f'Directory was not found: {os.path.dirname(args.output)}')
    raise NotADirectoryError


  if not args.inverse:
    capture_emails(args.csv, args.domain, args.output)
  else:
    capture_emails_inv(args.csv, args.domain, args.output)

if __name__ == '__main__':
  main()
