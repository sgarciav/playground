#!/usr/bin/env python3

# pylint: disable=C0103

# See (gmail): https://medium.com/testingonprod/how-to-send-text-messages-with-python-for-free-a7c92816e1a4
# See (yahoo): https://stackoverflow.com/questions/16381527/sending-e-mails-using-yahoo-account-in-python

import sys
import smtplib
import argparse
from email.mime.text import MIMEText

USERNAME = "sergiodotgarcia"
EMAIL_FROM = USERNAME + "@yahoo.com"
CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtex.com",
    "sprint": "@page.nextel.com"
}

MSG_TEMPLATE = """
Hello!
A member of the RIF team has been alerted of your presence.
You may be shortly receiving a follow-up message.
Thank you for your patience.
"""


def main():
    parser = argparse.ArgumentParser(description = 'Send a txt message.')
    parser.add_argument('-n', '--phone-number',
                        type=str,
                        default=None,
                        help='Recepient phone number without extra characters.')
    parser.add_argument('-c', '--carrier',
                        type=str,
                        default="att",
                        help='Phone carrier of the recepient.')
    parser.add_argument('-p', '--password',
                        type=str,
                        default=None,
                        help='One-time password of sender`s account.')

    args = parser.parse_args()

    # TODO: protect against incorrect carrier
    EMAIL_TO = args.phone_number + CARRIERS[args.carrier]

    print("email: {}".format(EMAIL_TO))

    msg = MIMEText(MSG_TEMPLATE)
    msg['Subject'] = "SOMEONE AT THE BOOTH"
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    server = smtplib.SMTP("smtp.mail.yahoo.com", 587)

    try:
        server.starttls()
        server.login(USERNAME, args.password)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        server.quit()
        print('Txt Sent')
    except:
        print('Oops. Something went wrong.')

if __name__ == "__main__":
    sys.exit(main())
