import time
import sys
import getpass


def delay_print(s):
    for c in s :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)
def delayer_print(s):
    for c in s :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.75)
            
            
class Vote:    
    def run(self):
        book_recs = 0
        voters = 0
        book_num = 1
        voter_num = 1
        books = []
        winning_score = 1
        
        print("*" * 80)
        print("*" * 80 + "\n\n")
        
        delay_print("Gooooooooooooood morning, bookworms! 🤓 I will be your polling companion today.\n")
        time.sleep(1)
        delay_print("I am the one... ")
        time.sleep(.6)
        delay_print("and only... ")
        time.sleep(.6)
        delay_print("EXTRAORDINARY VOTING APPARATUS FOR NOVELS!!! ")
        time.sleep(1)
        delay_print("v.1.0\n")
        time.sleep(2)
        delay_print("But you can all just call me E.V.A.N. for short! 😎\n")
        time.sleep(0.5)
        delay_print("\nToday we will be voting on your book for the month of December.\n")
        time.sleep(0.5)
        delay_print("I just need to get everything calibrated first. Let's see here.")
        time.sleep(1) 
        delayer_print("..")
        time.sleep(0.5)
        delay_print("\n\nHow many voters do we have present today?  ")
        
        voters = int(input())
        
        print("\n" + "*" * 80 + "\n")
        delay_print("I see, I see. " + str(voters) + " of you. Noted! And how many books recs in total? 🤨  ")
        book_recs = int(input())
        
        print("\n" + "*" * 80 + "\n")
        delay_print("Phenomenal!! Please list them now:\n\n")
        
        while (book_recs > 0 and book_num <= book_recs) :
            name = input("Book " + str(book_num) + ": ")
            books.append({ "name" : name, "ref" : book_num , "score" : 0})
            print()

            book_num += 1

        print("*" * 80 + "\n")
        delay_print("All set! On to the good part now: ")
        time.sleep(0.5)
        delay_print("the voting!! 😄\n\n")
        print("*" * 80 + "\n")

        while (voters > 0) :
            if voter_num == 1:
                delay_print("Voter #" + str(voter_num) + ", please approach!\nPress enter when you are ready.")
            elif voters == 1 :
                delay_print("And last but not least, Voter #" + str(voter_num) + "!\nPress enter when you are ready.")
            else :
                delay_print("Hello, Voter #" + str(voter_num) + "!\nPress enter when you are ready.")
            input()
            delay_print("\n\nHere are your options:\n\n")
            for book in books :
                print(str(book["ref"]) + ") " + str(book["name"]) + "\n")
            time.sleep(1.5)
            delay_print("\nNow tell me, which book is your first choice? Don't worry, I won't tell. 🤫\n")
            time.sleep(0.1)
            delay_print("Simply type the book's associated number from the list above. ")
            num = getpass.getpass(" ")
            for book in books :
                if int(num) == int(book["ref"]) :
                    book["score"] += 3
                    break

            delay_print("\nOhohohoo~ excellent choice! What's your second favorite option? ")
            num = getpass.getpass(" ")
            for book in books :
                if int(num) == int(book["ref"]) :
                    book["score"] += 2
                    break

            delay_print("\nThat's a good one too. And finally, your third choice? ")
            num = getpass.getpass(" ")
            for book in books :
                if int(num) == int(book["ref"]) :
                    book["score"] += 1
                    break
            
            if voters == 1 :
                delay_print("\nVery good! Thank you for your input, Voter #" + str(voter_num) + "!\n\n")
            else :    
                delay_print("\nVery good! Thank you for your input, Voter #" + str(voter_num) + "! Please send the next voter over.\n\n")
            print("*" * 80 + "\n")
            
            voter_num += 1
            voters -= 1

        delay_print("That concludes our voting! 👏\n\n")
        print("*" * 80 + "\n")
        for book in books :
            if book["score"] > winning_score :
                winning_score = book["score"]
                winner = book["name"]
                
        time.sleep(1.5)       
        delay_print("Thank you for your patience in this process, dear readers. ")
        time.sleep(0.2)
        delay_print("\nI'll just need a moment to tally up the votes!!\n")
        delayer_print("\n...\n")
        delay_print("Oh this is so exciting~\n")
        delayer_print("...\n...\n")
        delay_print("One more here, two for this one...\n")
        delayer_print("...\n...\n...\nO.M.G 😲")
        time.sleep(3)
        delay_print("\n\nAhem, you'll have to excuse me. The results are in!!!\nAnd what incredible results they are!!!!!!\n\n")
        print("*" * 80)
        time.sleep(1.5)
        delay_print("\nEsteemed readers! I give you...")
        time.sleep(1.5)
        delay_print(" Your December 2022 Book of the Month!")
        time.sleep(1.5)
        delay_print("\n\nDrumroll pleaseee!! 🥁\n\n\n")
        time.sleep(3)
        print("🎉🎈✨" * 13)
        print("\n\n" + " " * 25 + winner.upper() + "!!!!!\n\n" + " " * 25)
        print("🎉🎈✨" * 13)
        time.sleep(5)
        print("\n\n\nFinal Results:\n")
        for book in books :
            print(book["name"] + ": " + str(book["score"]) + " points")
        delay_print("\n\nThank you for participating! Until next time! Happy reading! 👋\n")
v = Vote()
v.run()
print("\n\n\n" + "*" * 80)
print("*" * 80)
