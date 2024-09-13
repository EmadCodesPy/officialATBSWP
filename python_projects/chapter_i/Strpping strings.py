spam = '   SpamSpamHelloSpamWorldSpamSpam   '

print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())
print(spam.strip().strip('Spam'))