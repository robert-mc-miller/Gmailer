# Gmailer
Sends emails via Gmail account to CSV list of emails

## Setup
1. Clone repository
2. Change html_content to the body of your email (in HTML form) 
3. Change filename to the attachment you wish to upload (or comment out that section of code if no attachment is required)
4. Enter the CSV filename into the parameters when read_csv() is called

**Note: The CSV file should be in this format (headers should be included)**

```
name, email
John, johndoe@example.com
Jane, janedoe@outlook.com
```

## How to run
Run gmailer.py with the command  `python gmailer.py` from the command line. It will output which of the emails are successful and which are not alongside the number of emails attempted. It will pause for 2 minutes every 50 emails to ensure Gmail does not temporarily revoke access. 
