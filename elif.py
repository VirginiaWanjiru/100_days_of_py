print("SECURE LOGIN SYSTEM")

username = input("Username >")
password = input("Password>")
myOrder= input("What will you order today ?")

if username == "mark" and password == "password":
  print("Why hello there ", username,"What a wonderful aura you have.")
  print("One",myOrder,"coming up for you")
  
elif username == "Virginia" and password == "V1rg1n1a":
 print("Welcome", username ,"How can I serve you today?")
  
elif username == "Suzzane" and password == "password":
 print("Welcome Suzzanne.One", myOrder,"coming up for you")
  
else:
 print("Hello there. You're credentials are not available in our database or are invalid. Please try again or consider registering an account. Thank you")
  
