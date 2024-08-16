from tkinter import *
from PIL import Image,ImageTk
from random import randint

#main window
def gameloop():
    root = Tk()
    root.title ("Rock Paper Scissor")
    root.configure(background ="#5833ea")
    

    #pictures
    rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
    paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
    scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
    rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
    paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
    scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

    #insert picture
    user_label = Label(root,image=scissor_img_comp,bg ="#5833ea")
    comp_label = Label(root,image = scissor_img,bg ="#5833ea")
    comp_label.grid(row=1,column=0)
    user_label.grid(row=1,column=4)

    #scores
    PlayerScore = Label(root,text = 0, font = 100, bg = "#5833ea",fg ="white")
    ComputerScore = Label(root,text = 0,font = 100, bg = "#5833ea",fg ="white")
    ComputerScore.grid(row=1,column=1 )
    PlayerScore.grid(row=1,column=3)

    #indicators
    user_indicator = Label(root,font=70, text = "User", bg = "#38b6ff",fg ="white")
    comp_indicator = Label(root,font=70, text = "Computer", bg = "#38b6ff",fg ="white")
    user_indicator.grid(row=0,column = 3)
    comp_indicator.grid(row=0,column = 1)

    #messages
    msg = Label(root,font=50, bg = "#40b8f5",fg ="white",text = "Start Game")
    msg.grid(row=1,column = 2)

    #update message 
    def updatemessage(x):
        msg ["text"] = x

    #update score
    #update user score
    def updateuserscore():
        score = int(PlayerScore["text"])
        score += 1
        PlayerScore["text"] = str(score)
    #update computer score
    def upadatecompscore():
        score = int(ComputerScore["text"])
        score += 1
        ComputerScore["text"] = str(score)


    #check winner
    def checkwin(player,computer):
        if player == computer:
            updatemessage("Its A Tie")
        elif player == "rock":
            if computer == "paper":
                updatemessage("You Lose")
                upadatecompscore()
            else:
                updatemessage("You Win")
                updateuserscore()
        elif player == "paper":
            if computer=="scissors":
                updatemessage("You Lose")
                upadatecompscore()
            else:
                updatemessage("You Win")
                updateuserscore()
        elif player == "scissors":
            if computer == "rock":
                updatemessage("You Lose")
                upadatecompscore()
            else:
                updatemessage("You Win")
                updateuserscore()
        else:
            pass

    #update choice
    choices = ["rock","paper","scissor"]

    def updatechoice(x):
    #for computer
        compchoice = choices[randint(0,2)]
        if compchoice == "rock":
            comp_label.configure(image=rock_img_comp)
        elif compchoice == "paper":
            comp_label.configure(image=paper_img_comp)
        else:
            comp_label.configure(image=scissor_img_comp)



    #for user
        if x == "rock":
            user_label.configure(image=rock_img)
        elif x == "paper":
            user_label.configure(image=paper_img)
        else:
            user_label.configure(image=scissor_img)
        
        checkwin(x,compchoice)

    #buttons
    rock = Button(root,width = 20,height = 2, text = "Rock", bg = "blue",fg = "white",command = lambda:updatechoice("rock")).grid(row =2, column = 1)
    paper = Button(root,width = 20,height = 2, text = "Paper", bg = "#6866e1",fg = "white",command = lambda:updatechoice("paper")).grid(row =2, column =2)
    scissor = Button(root,width = 20,height = 2, text = "Scissor", bg = "red",fg = "white",command = lambda:updatechoice("scissor")).grid(row = 2, column = 3)

    def close_window():
        root.destroy()

    # Create a button to exit the game
    exit_button = Button(root, text="Exit", command=close_window,bg="red",fg="white")
    exit_button.grid(row=4,column=2)

    root.mainloop()
gameloop()


# #start game function
# import tkinter as tk
# import tkinter.font as font
# from tkinter import messagebox

# tk.Tk.report_callback_exception = lambda *args: None
# win = tk.Tk()
# win.geometry("700x400")
# win.title("Snake Game by PESU Students")
# Title_Font = font.Font(family="Comic Sans MS", size=50, weight="bold")
# Font2 = font.Font(family="Impact", size=20, weight="bold")

# # Create a variable to track the selected speed
# selected_speed = tk.StringVar()
# selected_speed.set("15")  # Default speed

# # TITLE TEXT
# title_text = Label(win,text = "Rock Paper Scissors",fg = "#00FFFF")
# title_text['font'] = Title_Font
# title_text.pack()
# caption = Label(win,text = "By PESU Students",fg = "Blue")                  
# caption['font'] = Font2
# caption.pack()


# # Create a button to start the game
# start_button = tk.Button(win, text="Start Game", command=gameloop)

# start_button.pack(pady=10)

# # To collect Username
# username=Label(win, text = "Username").pack()
# E1 = Entry(win,width=20).pack()

# # Function to show information about the game
# def show_info():
#     info = "Snake Game\n\nUse arrow keys to control the snake.\nEat the fruit to grow and score points.\nAvoid collisions with walls and yourself."
#     messagebox.showinfo("Game Info", info)

# # Create a button to show game information
# info_button = tk.Button(win, text="Game Info", command=show_info)
# info_button.pack(pady=10)

# # # Option menu to select the speed level
# # speed_label = tk.Label(win, text="Select Speed Level:")
# # speed_label.pack()

# # speed_menu = tk.OptionMenu(win, selected_speed, *map(str, range(10, 100, 10)))
# # speed_menu.pack(pady=10)

# # Function to close the window
# def close_window():
#     win.destroy()

# # Create a button to exit the game
# exit_button = tk.Button(win, text="Exit", command=close_window)
# exit_button.pack(pady=10)

# # Run the GUI
# win.mainloop()
