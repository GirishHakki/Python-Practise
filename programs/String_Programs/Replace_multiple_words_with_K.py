# Python3 code to demonstrate working of
# Replace multiple words with K
# Using join() + split() + list comprehension

# initializing string
test_str = 'LinkedIn is best for Freshers and Experienced'

# printing original string
print("The original string is : " + str(test_str))

# initializing word list
word_list = ["best", 'Experienced', 'for']

# initializing replace word
repl_wrd = 'GH'

# Replace multiple words with K
# Using join() + split() + list comprehension
res = ' '.join([repl_wrd if idx in word_list else idx for idx in test_str.split()])

# printing result
print("String after multiple replace : " + str(res))
