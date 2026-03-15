from tkinter import *

root = Tk()
root.config(background="#8bfab4")
root.geometry("800x800")
root.title("GTN")

title=Label(root,text="Welcome to GTN",font=("Arial",30,"bold"),bg="#8bfab4",fg="white")
title.grid(column=0,row=0,padx=250,pady=50)

nameget=Frame(root)
nameget.grid(column=0,row=1,padx=30,pady=200)

name=Label(nameget,text="What is your name?",font=("Arial",20),bg="#8bfab4",fg="white")
name.grid(column=0,row=0)

nameentry=Entry(nameget)
nameentry.grid(column=0,row=1)

mainloop()