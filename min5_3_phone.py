''' To check if phone format is correct'''

import re


number = str(input('Please, input your phone number:\n'))
result = re.search(r"^\([0-9]{3}\)[0-9]{3}-[0-9]{4}$", number)
if result:
    print('Your phone number format {} is correct.' .format(number))
else:
    print('Your phone number format is not correct.\n'
          'Input your phone number in format (xxx)xxx-xxxx')
