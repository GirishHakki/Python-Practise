# pre-requisites

# 1) letters a-z(small letters)
# 2) 0-9
# 3) . _ (only one . & _ req)
# 4) only one @ req
# 5) . should be 2nd or 3rd position (email not shart with .)

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input('Enter your Email : ')

if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")
