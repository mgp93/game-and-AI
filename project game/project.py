
import random
import time
print("hi welcome to our minigames!!!!!!!")
time.sleep(3)
print("you have to win all the games and even the boss to win a trophy!!!!!")
print("but if you lose the game will stop ")
o = input("are you ready?(yes/no)")
if o == "yes" or o == "y":
    print("ok than lets go!!!!!!!!")
    print("for the first game you have to say the answer")
    time.sleep(2)
    print("minigame (1)")
    time.sleep(2)
    question = ["2*2=?", "8*8=?", "9*5=?", "25*36=?", "4*2=?", "80*3=?", "3*3=?"]
    print(random.choices(question,k=1))
    p = input("enter>>>")
    if p == "4" or p == "64" or p == "45" or p == "900" or p == "8" or p == "240" or p == "9":
        print("that's right!")
        time.sleep(2)
        print("so for the next game you have to fix the sentence ")
        time.sleep(3)
        print("minigame (2)")
        time.sleep(2)
        sentence = ["hello how___you?(did/are)","are___okay?(you/brothers)","hi mo_!(mom/mohammad)"]
        print(random.choices(sentence, k=1))
        r = input("enter>>>")
        if r =="are" or r =="you" or r =="mom":
            print("that's right!!!!")
            time.sleep(2)
            print("for the next game you have to translate the word to a different language")
            print("hint:{word}(language to translate)")
            time.sleep(3)
            print("minigame (3)")
            word = ["hello(germany)", "hallo(english)", "ish(english)"]
            print(random.choices(word, k=1))
            b = input("enter>>>")
            if b == "me"  or b == "hallo" or b == "hello":
                print("that's right")
                time.sleep(2)
                print("you have to answer question! ")
                time.sleep(2)
                print("minigame (4)")
                y = input("who write sahname(ferdosi or sadi)")
                if y == "ferdosi":
                    print("that's right!!!!")
                    time.sleep(2)
                    print("ohh there's an other question!")
                    time.sleep(2)
                    print("minigame (5)")
                    time.sleep(2)
                    print("What is the capital of Iran?(tabriz-tehran)")
                    t = input("enter>>>")
                    if t == "tehran":
                        print("that's right")
                        time.sleep(2)
                        print("you have to answer a math question!")
                        time.sleep(2)
                        print("minigame (6)")
                        time.sleep(2)
                        i = input("What is 245 + 378?(623- 700)")
                        if i == "623":
                            print("boss:how did you reach here?")
                            time.sleep(2)
                            print("boss:ahh ok you can fight me")
                            time.sleep(2)
                            print("congrats you are now on boss level!!!!")
                            print("for this part you have to guess logo")
                            time.sleep(2)
                            print("you have 10 attempt")
                            time.sleep(2)
                            print("Boss Level!!!")
                            for i in range(1, 10):
                                print("logos:nokia-apple-samsung-asus-hp-lenovo-windows-linux")

                                brand = ["nokia", "apple", "samsung", "asus", "hp", "lenovo", "windows", "linux"]
                                w = random.choice(brand)
                                e = input("enter>>>")
                                if w == e:
                                    print("you win!!!!!!!!!!!!!!")
                                    print("congrats bro")
                                    print("your trophy  is on game file")
                                    exit()

                                else:
                                    print(w)
                                    print("you lost this round:(")





else:
    print("ok! have a nice day :)")

