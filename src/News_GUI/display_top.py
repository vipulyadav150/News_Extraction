import tkinter
from tkinter import *
from tkinter import *
from tkinter import messagebox
import random
import time
from tkinter import scrolledtext
from tkinter import Menu
from src.top_stories.extract_headlines import *


def top_stories():
    kernel_root = Tk()
    screen_height = kernel_root.winfo_screenheight()
    screen_width = kernel_root.winfo_screenwidth()
    kernel_root.geometry('%dx%d' % (screen_width, screen_height))
    kernel_root.title('Daily News!')
    localtime = time.asctime(time.localtime(time.time()))

    text_input = StringVar()
    operator = ''



    Tops = Frame(kernel_root, width=screen_width, height=50, bg='powder blue', relief=SUNKEN)
    Tops.pack(side=TOP)

    Left = Frame(kernel_root, width=800, height=700, relief=SUNKEN)
    Left.pack(side=LEFT)

    Right = Frame(kernel_root, width=300, height=700, relief=SUNKEN)
    Right.pack(side=RIGHT)

    title_label = Label(Tops, bg='powder blue', text='DAILY NEWS!', font=('arial', 20, 'bold'),
                                     anchor='w',  bd=10,justify='center')
    title_label.grid(row=0, column=0)
    main_list, url_list = extraction_top_stories(n=0, main_url='https://timesofindia.indiatimes.com/')

    def getTopContents():
        for t in main_list:
            title = StringVar()
            link = StringVar()
            title_left = t
            title = (title_left)
            print(title_left)
            i = main_list.index(t)

            link = url_list[i]
            link_left = link
            link = (title_left)
            print(link_left)
            content =  Entry(Left,font=('arial',8,'bold'),textvariable=title,bd=10,insertwidth=4,bg='powder blue',
                justify=RIGHT).grid(row=i,column=0)
            url  =Entry(Right,font=('arial',8,'bold'),textvariable=link,bd=10,insertwidth=4,bg='powder blue',
                justify=RIGHT).grid(row=i,column=0)

    getTop = Button(Left, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='Get', bg='powder blue',
                  command=getTopContents)
    getTop.grid(row=9, column=0)

    mainloop()
    #self.title_label = Label(self.Tops, bg='powder blue', text='DAILY NEWS!', font=('arial', 20, 'bold'),
    #                                  anchor='w',  bd=10,justify='center')
    #         self.title_label.grid(row=0, column=0)
    #
    #         self.top_story_label = Label(self.LowerTop, bg='red', text='TOP STORIES', anchor='w',
    #                                font=('arial', 10, 'bold'), bd=10,justify='left')
    #         self.top_story_label.grid(row=1,column=0)
    #
    #         self.left_story_label = Label(self.Left, bg='green', text='LATEST', anchor='w',
    #                                      font=('arial', 10, 'bold'), bd=10, justify='left')
    #         self.left_story_label.grid(row=0,column=1)
    #         explain_text_left = 'Happy to see you here! This section contains the latest news for today' + self.localtime+'@Encoded'
    #         self.left_story_label = Label(self.Left, bg='purple', text=explain_text_left, anchor='w',
    #                                       font=('arial', 10, 'bold'), justify='left')
    #         self.left_story_label.grid(row=1, column=1)
    #
    #         self.right_story_label = Label(self.Right, bg='purple', text='NEWS @ YOUR LOCATION:CHENNAI', anchor='w',
    #                                       font=('arial', 10, 'bold'), bd=10, justify='left')
    #         self.right_story_label.grid(row=0, column=1)
    #         explain_text_left = 'Happy to see you here! This section contains the latest news for specific to your location'+'@Enc0ded_Vip'
    #         self.right_story_label = Label(self.Right, bg='green', text=explain_text_left, anchor='w',
    #                                       font=('arial', 10, 'bold'), justify='left')
    #         self.right_story_label.grid(row=1, column=1)
    #



top_stories()

