"""Project name= megamind: the memory game

Created by= Ruhan Saad Dave & Rushil Vishwakarma

Description=
This project is a game that aims to deliver a fun experience to the player and aims to 
improve the players observation and memory skills, while also not being addictive like many other games.

Class= XII-B
	
Year=2022~23
"""
import random
import json #it is used to fix a list error
import mysql.connector
from tkinter import *   #Importing both of these so that we 
import tkinter as tk    #do not have to write ".tkinter" everytime.
import time#Time for timer and ending loops at specific time


def gennew(digit_len=4):
        """generates 3 random numbers for the new game

        This function generates 3 random number for the new game, the random number will be taken from the range of min_no to max_no(defination given below), then the 3 numbers will be stored in a list to return itself out of function easily.

        identifier meanings:
        digit_len: number of digits present in the random number
        max_no: the maximum number from which the random number will be chosen 
        min_no: the minimum number from which the random number will be chosen
        num_list: it is a list which stores 3 random numbers that are generated and will return itself out of the function
        """
        max_no="9"*digit_len
        max_no=int(max_no)
        min_no=10**(digit_len-1)
        a=random.randint(min_no,max_no)
        return a


def rule_check(digit_len=4):
        """checks if the entered answer of the user(input_no) is a number and of the required length(deault is 4). 

        this function checks if the input of the user is in correct format, if not it will display the designed reply and the function will loop again till the input is in correct format(format given above).

        identifier meanings:
        rule_pass: this makes a loop when the user inserts a wrong input, the program will loop again till it is in correct format.
        input_no: the input entered by the user.
        digit_len: number of digits required for the number
        """     
        rule_pass=0
        while rule_pass==0:
                input_no=input("Please enter the number=")
                if input_no.isdigit()==False:
                        print("Enter only numbers!")
                elif len(input_no)!=digit_len:
                        print("Enter a number of", digit_len, "digits")
                else:
                        input_no=int(input_no)
                        rule_pass=1
                        return input_no

def display1(no_list):
        """
        displays the numbers using tkinter
        
        displays the 3 numbers one by one with time delay inside a window created by tkinter, and after 3.5 seconds the window gets destroyed and displays the next number. The is a bug where the windows wont pop up untill input is required, so between each number the user need to press enter to continue.

        identifier meanings:
        no_list= the list containing the 3 rabdonly generated numbers of desired length
        """
        win1=Tk() #creats a window win1
        win1.geometry('600x120') #deciding the size of the window
        win1.title("number") #title of the window
        label1 = tk.Label(win1, text= no_list[0], font=("Arial Black", 70)) #displaying the text in the window
        label1.grid(row=0, column=1) #position of the text
        win1.after(3500, lambda: win1.destroy())
       
def display2(no_list):
        #the function of each line is explained above
        win2=Tk()
        win2.geometry('600x120') 
        win2.title("number")
        label2 = tk.Label(win2, text= no_list[1], font=("Arial Black", 70))
        label2.grid(row=0, column=1)
        win2.after(3500, lambda: win2.destroy()) 

def display3(no_list):
        win3=Tk()
        win3.geometry('600x120')
        win3.title("number")
        label3 = tk.Label(win3, text= no_list[2], font=("Arial Black", 70))
        label3.grid(row=0, column=1)
        win3.after(3500, lambda: win3.destroy())



#variables
player_name='default'
player_id=0     
digit_len=4 #length of the number to be displayed
total_play=0 #no of games played
total_score=0 #total score earned
easy_win=0 #no of wins in easy mode
medium_win=0 #no of wins in medium mode
hard_win=0 #no of wins in hard mode
total_error=0 #total no of mistakes done


###############################################################
#Mysql database related(comment all of the part once the database is created)
con=mysql.connector.connect(host="localhost", user="root", password="Admin2003", auth_plugin = "mysql_native_password")
cur=con.cursor()

query="create database megamind;"
cur.execute(query)
query="use megamind;"
cur.execute(query)
query="create table login_details(serial_no int, account_name varchar(20), password varchar(20))"
cur.execute(query)
query="create table score_details(serial_no int, account_name varchar(20), total_score int, total_games_played int, total_no_of_wins int, wins_of_easymedhard varchar(30), average_mistake float);"
cur.execute(query)
con.commit()
query="insert into login_details values(1, 'bow', 'wob')"
cur.execute(query)
query="insert into login_details values(2, 'arrow', 'worra')"
cur.execute(query)
query="insert into score_details values(1, 'bow', 1234, 234, 100, '[50,30,20]', 1.0)"
cur.execute(query)
query="insert into score_details values(2, 'arrow', 5678, 678, 300, '[150,100,50]', 1.5)"
cur.execute(query)
con.commit() #permanently save data in mysql
print("Database created successfully")
###################################################################   


#connecting to database for every time use
con=mysql.connector.connect(host="localhost", user="root", password="Admin2003", database="megamind")
cur=con.cursor()


#__main__
while True:     
        print("*"*30)
        print("\t Welcome to")
        print("\t  Megamind")
        print("*"*30)

        print("Where would you like to go?")     
        print("1→Play") #line 154
        print("2→How to play") #line 219
        print("3→Difficulty") #line 260
        print("4→Accounts") #line 277
        print("5→Score board") #line 417
        print("6→Exit") #line 458
        main_choice=input("Enter your choice:")
        print("\n"*3)

        if main_choice=='1': #Play option from main menu
                print("Help tip: go to how to play option in main menu before playing a new game, if you didnt you can just type 1234 for five(5) times.")
                print("Please execute this program in .exe version (put the file in desktop and run directly without viewing the code) or else the numbers wont be shown/ removed from output screen. ")
                ch=input("Continue?") #this is for user to read previous line.
                one=gennew(digit_len)
                two=gennew(digit_len)
                three=gennew(digit_len)
                no_list=[one,two,three]
                question=random.randint(0,2) #for selecting one of the three numbers as question
                question=int(question)

                print("\n")
                print("Ready!")
                time.sleep(1) #timer of 1 second
                print("Steady!")
                time.sleep(1) #timer of 1 second
                print("Go!")
                time.sleep(1) #timer of 1 second
                display1(no_list)
                next=input("Press ENTER to see next number")
                display2(no_list)
                next=input("Press ENTER to see next number")
                display3(no_list)
                print("\n")
                answer=no_list[question] #storing the correct answer
                if question==0: #these are for the displaying the question
                        position="1st"
                elif question==1:
                        position="2nd"
                else:
                        position="3rd"
                tries=1 
                while tries<=5: #check if player done 5 mistakes or not
                        print("\n"*5)
                        print("What is the", position , "number")
                        guess_no=rule_check(digit_len)
                        if guess_no!=answer:
                                print("Wrong answer! Try again")
                                print("You have", 5-tries, "tries left")
                                tries+=1
                                if tries>5:
                                        print("Sorry, you lost the game")
                                        print("The correct answer was", answer)
                                        win=0
                                        break
                        else:
                                print("Congratulations!")
                                print("You made it in", tries, "try!")
                                win=1
                                break
                #calculating the score and saving it
                total_play+=1
                new_score=digit_len*(5-tries)
                total_score+=new_score
                print("You have earned", new_score, "score")
                exit=input("Press enter to continue.") #this is for user to read the score before going to main menu
                print("\n"*5)
                if digit_len==4:
                        easy_win+=1
                elif digit_len==6:
                        medium_win+=1
                else:
                        hard_win+=1
                total_error+=tries-1

        elif main_choice=='2': #how to play option
                print("What information would you like to know?")
                print("1» The game") #line 227
                print("2» Score system") #line 236
                print("3» Accounts") #line 246
                choice=input("Select option:")
                print("\n"*3)

                if choice=="1": #To know about the game, just messages
                        print("\n"*3)
                        print("The player will see a few numbers on the Screen one at a time.")
                        print("The user/player must remember those numbers with their corresponding position before those numbers disappear")
                        print("and then input the required numbers asked in the appropriate text fields.")
                        print(" If the input numbers match the Shown numbers, the player wins.")
                        print("But if the player input number is mismatched, and the player enters wrong for 5 times, then the player loses. ")
                        ch=input("Press enter to return")

                elif choice=='2': #To know about the score system, just messages
                        print("The score is determined by the hardness of the level")
                        print("and the number of tries the player has used to guess the correct answer.")
                        print("For example, if the player wins the easy mode in 3 tries, he will earn:")
                        print(" 4*(5-3)=8 points")
                        print("Suppose the player doesnt guess the correct answer for all 5 times,")
                        print("their score will be reduced for 4/6/8 for easy/medium/hard mode repectively")
                        ch=input("Press enter to return")
                        print("\n"*3)

                elif choice=='3': #to know about accounts, just messages
                        print("An account is necessary if the player wants to store their data.")
                        print("For that the user must login in the ACCOUNTS menu from main menu.")
                        print("In case the user does not want to login and wants to see their score, they can check for it.")
                        print("All the score earned will be stored in a TEMPORARY account and pushed to the actual account when closing the program. ")
                        print("But still the user can go to SCORE BOARD option in main menu.")
                        ch=input("Press enter to return")
                        print("\n"*3)

                else:
                        print("Invalid input, please try again!")
                        ch=input("Press enter to return")
                        print("\n"*3)

        elif main_choice=='3': #difficulty option
                print("Which difficulty do you want?")
                print("1» Easy (4 digits)")
                print("2» Medium (6 digits)")
                print("3» Hard (8 digits)")
                choice=input("Enter your choice:")
                if choice=='1':
                        digit_len=4
                elif choice=='2':
                        digit_len=6
                elif choice=='3':
                        digit_len=8
                else:
                        print("Invalid input, please try again")
                        ch=input("Press enter to return")
                        print("\n"*3)

        elif main_choice=='4': #accounts option
                con=mysql.connector.connect(host="localhost", user="root", password="Admin2003", database="megamind")
                cur=con.cursor()
                print("What action would you like to do?")
                print("1» Create account") #line 289
                print("2» Login account") #line 316
                print("3» Delete account") #line 347
                print("4» Refresh current account (need login, else chance of crash)") #line 371
                print("5» Change password") #line 386
                choice=input("Enter your choice:")

                if choice=='1': #create account option
                        con=mysql.connector.connect(host="localhost", user="root", password="Admin2003", database="megamind")
                        cur=con.cursor()
                        query="select * from login_details"
                        cur.execute(query)
                        data=cur.fetchall()
                        row=len(data)
                        user_name=input("Enter user_name:")
                        user_password=input("Enter password:")
                        confirm_password=input("Enter confirmed password:") #this part is inspired by all internet website when creating account
                        if user_password!=confirm_password:
                                print("Sorry, wrong password, please try again!")
                                ch=input("Press enter to return")
                                print("\n"*3)   
                        else:
                                #creating an account and save it in the database
                                query="insert into login_details values({}, '{}','{}')".format(row+1,user_name,user_password)
                                cur.execute(query)
                                query="insert into score_details values({},'{}',{},{},{},'{}',{})".format(row+1,user_name,total_score,total_play,easy_win+medium_win+hard_win,[easy_win,medium_win,hard_win],total_error/total_play)
                                cur.execute(query)
                                con.commit() #permanently saving the information in mysql
                                print("Account succefully created, please login to you account!")
                                print("Your ID is:",row+1)
                                ch=input("Press enter to return")
                                print("\n"*3)
                                
                elif choice=='2': #login account option
                        con=mysql.connector.connect(host="localhost", user="root", password="Admin2003", database="megamind")
                        cur=con.cursor()
                        user_name=input("Please enter user_name:")
                        user_password=input("Please enter password:")
                        query="select * from login_details where account_name='{}' and password='{}'".format(user_name, user_password)
                        cur.execute(query)
                        data=cur.fetchall()
                        row=len(data)
                        if row==0: #checks if account exists
                                print("Sorry, no matching account found.")
                                ch=input("Press enter to return")
                                print("\n"*3)
                        else:
                                player_name=user_name
                                query="select * from score_details where account_name='{}'".format(player_name)
                                cur.execute(query)
                                data=cur.fetchall()
                                row=list(data[0])
                                emh=json.loads(row[5]) #to convert list in form of string back into list
                                #adding the past record to default account
                                total_play+=row[3]
                                total_score+=row[2]
                                easy_win+=int(emh[0])
                                medium_win+=int(emh[1])
                                hard_win+=int(emh[2])     
                                total_error+=total_play*row[-1]
                                con.commit() #permanently save data in mysql
                                print("Account login succesfully")
                                ch=input("Press enter to return")
                                print("\n"*3)

                elif choice=='3': #delete account option
                        con=mysql.connector.connect(host="localhost", user="root", password="Admin2003", database="megamind")
                        cur=con.cursor()
                        confirm=input("Are you sure to delete the account? (y/n):")
                        if confirm.lower()=='y':
                                user_name=input("Please enter user_name:")
                                user_password=input("Please enter password:")
                                query="select * from login_details where account_name='{}' and password='{}'".format(user_name, user_password)
                                cur.execute(query)
                                data=cur.fetchall()
                                row=len(data)
                                if row==0: #checks if account exists
                                        print("Sorry, no matching account found.")
                                else:
                                        #deleting the account
                                        query="delete from login_details where account_name='{}'".format(user_name)
                                        cur.execute(query)
                                        query="delete from score_details where account_name='{}'".format(user_name)
                                        cur.execute(query)
                                        con.commit() #permanently save data on mysql
                                        print("Account deleted successfully!")
                                        ch=input("Press enter to return")
                                        print("\n"*3)

                elif choice=='4': #refresh account option
                        con=mysql.connector.connect(host="localhost", user="root", password="Admin2003", database="megamind")
                        cur=con.cursor()
                        #this option saves all the data into the database so that in case the system crashes no data will be lost, inspired by many offline games.
                        query="select * from score_details where account_name='{}'".format(player_name)
                        cur.execute(query)
                        data=cur.fetchall()
                        #puting all the current scores and other data into the database
                        query="update score_details set total_score={}, total_games_played={}, total_no_of_wins={},wins_of_easymedhard='{}', average_mistake={} where account_name='{}'".format(total_score, total_play, easy_win+medium_win+hard_win, [easy_win, medium_win, hard_win], total_error/total_play, player_name
                                                                                                                                                                                                      )
                        cur.execute(query)
                        con.commit() #permanently save data on mysql
                        print("Account refresh successfully!")
                        ch=input("Press enter to return")
                        print("\n"*3)

                elif choice=='5': #change password option
                        con=mysql.connector.connect(host="localhost", user="root", password="Admin2003",database="megamind")
                        cur=con.cursor()
                        confirm=input("Are you sure to change password? (y/n):")
                        if confirm.lower()=='y':
                                user_name=input("Please enter user_name:")
                                user_password=input("Please enter password:")
                                query="select * from login_details where account_name='{}' and password='{}'".format(user_name, user_password)
                                cur.execute(query)
                                data=cur.fetchall()
                                row=len(data)
                                if row==0: #check if account exists
                                        print("Sorry, no matching account found.")
                                        ch=input("Press enter to return")
                                        print("\n"*3)
                                else:
                                        new_password=input("Enter new password:")
                                        confirm_password=input("Enter confirmed password:") #tgis part is inspired by many internet website when changing password
                                        if confirm_password!=new_password:
                                                print("Sorry, you have entered wrong password. Please try again.")
                                                ch=input("Press enter to return")
                                                print("\n"*3)
                                        else:
                                                #changing password and save into the databass
                                                query="update login_details set password='{}' where account_name='{}'".format(confirm_password, user_name)
                                                cur.execute(query)
                                                con.commit() #permanently save data in mysql                            
                                                print("Password changed successfully!")
                                                ch=input("Press enter to return")
                                                print("\n"*3)

        elif main_choice=='5': #score board option
                print("Displaying current account score:")
                print("\n"*3)
                print("User name » ", player_name)
                print("User ID » ", player_id)
                print("Total games played » ", total_play)
                print("Total score earned » ", total_score)
                print("Total games won » ", easy_win+medium_win+hard_win)
                print("Number of wins in easy mode » ", easy_win)
                print("Number of wins in medium mode » ", medium_win)
                print("Number of wins in hard mode » ", hard_win)
                print("Number of wrong answers made » ", total_error)
                if total_play<=0:
                        print("Average mistakes made » 0\n")
                else:
                	print("Average mistakes made » ", total_error/total_play, "\n")

                #this part is to give ranking based on the score, just for decorration purpose
                if total_score<=0:
                        rank='F'
                elif total_score<=10:
                        rank='E'
                elif total_score<=50:
                        rank='D'
                elif total_score<=100:
                        rank='C'
                elif total_score<=200:
                        rank='B'
                elif total_score<=500:
                        rank='A'
                elif total_score<=1000:
                        rank='S'
                else:
                        rank='LEGENDARY'
                print("Rank » ", rank)
                print("NOTE: Try getting more than 1000 score") #motivating the player to reach a target 
                ch=input("Press enter to return")
                print("\n"*3)
                
        elif main_choice=='6': #exit option
                choice=input("Are you sure you want to exit? (y/n):")
                if choice.lower()=='y':
                        break
#storing all score and other data into database
if player_name!='default':
        query="update score_details set total_score={}, total_games_played={}, total_no_of_wins={}, wins_of_easymedhard='{}', average_mistake={} where account_name='{}'".format(total_score, total_play, easy_win+medium_win+hard_win, [easy_win, medium_win, hard_win], total_error/total_play, player_name)
        cur.execute(query)
        con.commit() #permanently save data in mysql
        print("All your data has been automatically saved.")
choice=input("Thanks for playing!")

#THE END OF PROGRAM
