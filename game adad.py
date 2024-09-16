import random

adad_tasadofi = random.randint(1,15)
for i in range(3):
    user_input = int(input("adad ro entekhab kon(1,15):"))

    if user_input < adad_tasadofi:
        print("adad shoma kocactar ast")
    elif adad_tasadofi < user_input:
        print("adad shoma bozorgtar ast")

print(adad_tasadofi)