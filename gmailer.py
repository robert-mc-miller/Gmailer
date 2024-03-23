import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv
import time


def sendNow(to, name, subject):
    gmail_user = #enter gmail username as a string
    gmail_password = #enter gmail password as a string

    sent_from = gmail_user
    to = [to]
    html_content = '''
    <html>
    <body>
        <h1>Hello</h1>
        <p>This is the body of the email</p>
    </body>
    </html>
    ''' % (name)

    msg = MIMEMultipart()
    msg['From'] = sent_from
    msg['To'] = ', '.join(to)
    msg['Subject'] = subject

    # Attach HTML part
    html_part = MIMEText(html_content, 'html')
    msg.attach(html_part)




    # Attach file (optional, comment out if not needed)
########################################################################################################################
    filename = # Change this to your file name
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {filename}')

    msg.attach(part)
########################################################################################################################    


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, msg.as_string())
        server.quit()
        print('Email sent successfully to ', to)
    except Exception as e:
        print("Failed:", e)




def read_csv(file_path):
    names = []
    emails = []

    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header if present
            for row in reader:
                name, email = row
                names.append(name)
                emails.append(email)
    except Exception as e:
        print(f"Error reading CSV: {e}")

    return names, emails




names, emails = read_csv() #pass in the csv containing names and email addresses

subject = #enter your prefered subject line

for x in range(len(names)):
    sendNow(emails[x], names[x], subject)
    print(x+1)
    if (x+1)%50 == 0:
        time.sleep(120)



