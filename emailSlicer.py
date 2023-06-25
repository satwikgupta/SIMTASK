# Take email address from the user
email = input('Enter your email address : ')

#Slice and store the username and domain
username = email[:email.index('@')]
domain = email[email.index('@')+1:]

#make output result

result = "Your username is {} & domain is {}".format(username, domain)

#print the result
print(result)