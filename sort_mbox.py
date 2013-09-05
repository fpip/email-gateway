"""
Process an mbox file, sorting contact form messages into spam/ham folders for
further training of the spam filter.

Messages look like:

from python import podcast contact form:

name: Mike Pirnat
email: mpirnat@gmail.com
message: Testing 123 your podcast rules, dudes.
"""
import sys
from hashlib import md5
from mailbox import mbox

hams = 0
spams = 0

box = mbox(sys.argv[-1])
for index, message in box.items():
    if 'contact form' not in message['subject']:
        continue
    full_message = message.get_payload()
    print "* * * * *"
    print full_message
    print "* * * * *"
    response = raw_input("Is it spam? [Y]: ")
    if not response.strip() or response.strip().lower() == 'y':
        is_spam = True
        spams += 1
    else:
        is_spam = False
        hams += 1
    if 'message: ' in full_message:
        message = full_message.split('message: ')[-1]
    else:
        message = full_message
    filename = md5(message).hexdigest()
    if is_spam:
        filename = "./spam/" + filename
    else:
        filename = "./ham/" + filename
    open(filename, 'wb').write(message)
