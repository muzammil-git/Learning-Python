# SIGN UP AND LOGIN

print("Signup Page")
email1 = input("What is your email:")
password1 = input("What is your password:")


print("Account Created Successfully")

print("\n")
print("------x------")
print("\nLogin Page")

email2 = input("What is your email:")
password2 = input("What is your password:")

if(email2 == email1 and password2 == password1):
    print("Logged In!!!")

else:
    print("Incorrect Credential")

