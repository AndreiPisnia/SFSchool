''' To check if e-mail is correct'''

import re


email = str(input('Please, input your e-mail:\n'))
result = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9_.]+$", email)
if result:
    print('Your email address {} is correct.' .format(email))
else:
    print('Your email address {} is not correct.' .format(email))
