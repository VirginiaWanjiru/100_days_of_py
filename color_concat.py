#Adding color to a program

print("===Your Adventure Simulator===")
print("""You'll be asked a bunch of questions then a story will be made with you as the main character """)

print()
name=input("What is your name ?")
enemy=input("Whats your worst enemys name ?")
superPower=input("Your super power ?")

print()

print("Our story begins as out hero approaches a foreboding castle")
print("The suddenly a bold ot lightening striked the ground at the feet","\033[32m", name, "\033[0m]")
print("'Our Final battle begins' shout the evil", enemy,"clearly missing out the fact that ", name, "has the power of", superPower,"\033[35m","which means they'll win quite easily","\033[0m")


