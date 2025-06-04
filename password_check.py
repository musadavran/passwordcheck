password_uncomp = ["No uppercase letters","No lowercase letters","No number","No special characters","Too short",]
password_strength = 0
weakest_pas = ["123","abc","password","qwerty","letmein","iloveyou","admin","welcome","monkey","dragon","sunshine","trustno1","12345678","123456789","1234567","1234567890","password1","qwertyuiop","123123","1q2w3e4r5t","111111","123321","abc123","password123","qwerty123","1qaz2wsx","qazwsx","zxcvbnm","asdfghjkl","qwertyuiop123","123qwe","1qazxsw2cde3vfr4tgb5yhn6ujm7ik8ol9p0","1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0p","1qazxsw23edcvfr45tgbnhy67ujmiko89olp0"]
password_file = "passwords.txt"
password = input("Text your password: ")
print("checking your password please wait...")
has_upper = False
has_lower = False
has_digit = False
has_special = False
if len(password) >= 8: 
    password_strength += 20
    password_uncomp.remove ("Too short")
for char in password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
    if not char.isalnum():
        has_special = True
if has_upper:
    password_strength += 20
    password_uncomp.remove ("No uppercase letters")
if has_lower:
    password_strength += 20
    password_uncomp.remove ("No lowercase letters")
if has_digit:
    password_strength += 20
    password_uncomp.remove ("No number")
if has_special:
    password_strength += 20
    password_uncomp.remove ("No special characters")

for char in set (password):
    if password.count(char) >= 3:
        password_strength -= 20
        print("Your password has too many repeated letters.")

for weak in weakest_pas:
    if weak in password:
        password_strength -= 20
        print("Your password is too weak, it contains a common password.")
        
if password_strength < 40:
    print("""
Your password its weak
    """,password_uncomp)
elif password_strength < 80:
    print("Your password its medium",password_uncomp)
else:
    print("Your password its strong")

        
        

    