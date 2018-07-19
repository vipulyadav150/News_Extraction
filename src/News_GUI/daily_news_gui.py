import tkinter
from tkinter import *
from tkinter import *
from tkinter import messagebox
import random
import time
from tkinter import scrolledtext
from tkinter import Menu
from src.top_stories.extract_headlines import *

#
# class main_display:
#     def __init__(self):
#         self.kernel_root = Tk()
#         self.screen_height = self.kernel_root.winfo_screenheight()
#         self.screen_width = self.kernel_root.winfo_screenwidth()
#         self.kernel_root.geometry('%dx%d'%(self.screen_width,self.screen_height))
#         self.kernel_root.title('Daily News!')
#         self.localtime = time.asctime(time.localtime(time.time()))
#
#
#
#     def run(self):
#         self.kernel_root.mainloop()
#
#     def set_frames(self):
#         self.Tops = Frame(self.kernel_root, width=self.screen_width, height=50,
#                           bg='powder blue', relief=SUNKEN,bd=10)
#         self.Tops.pack(side=TOP)
#
#         self.LowerTop =Frame(self.kernel_root, width=self.screen_width,height=200,
#                           bg='red', relief=SUNKEN,bd=10)
#         self.LowerTop.pack(side=TOP)
#
#
#         self.Left = Frame(self.kernel_root, width=(self.screen_width/2.0), height=1000,
#                           bg='green', relief=SUNKEN,bd=10)
#         self.Left.pack(side=LEFT)
#
#         self.Right = Frame(self.kernel_root, width=((self.screen_width / 2.0)), height=1000,
#                           bg='purple', relief=SUNKEN,bd=10)
#         self.Right.pack(side=RIGHT)
#
#     def set_pre_labels(self):
#
#         self.title_label = Label(self.Tops,bg='powder blue',text='DAILY NEWS!',font=('arial', 20, 'bold'),
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
#
#     def dispatch_top(self,top_title,top_link):
#         self.top_tile = top_title
#         self.top_link = top_link
#         self.title_top_text = Entry(self.LowerTop, font=('arial', 7, 'bold'), textvariable=self.top_title, insertwidth=4,
#                                bg='red',
#                                justify=RIGHT)
#         self.title_top_text.grid(row=0, column=1)
#
#
#
#     # def set_scrollbar(self):
#     #     self.scrollbar = Scrollbar(self.kernel_root)
#     #     self.scrollbar.pack(side=RIGHT,fill=Y)
#     #     self.bullet_list = Listbox(self.kernel_root,width=1, yscrollcommand=self.scrollbar.set)
#     #     for line in range(1000):
#     #         self.bullet_list.insert(END,"")
#     #
#     #     self.bullet_list.pack(side=RIGHT, fill=BOTH)
#     #     self.scrollbar.config(command=self.bullet_list.yview)
#
#
# game = main_display()
# game.set_frames()
# game.set_pre_labels()
# # game.set_scrollbar()
# game.title_top,game.link_top = extraction_top_stories()
# game.dispatch_top(game.title_top,game.link_top)
# game.run()
#
#


import requests
from bs4 import BeautifulSoup
from src.top_stories.build_link import *
from src.top_stories.dispatch_op import *
# from src.News_GUI.daily_news_gui import *


def extraction_top_stories(n,main_url):
    content = requests.get(main_url)  # Returns status
    html_content = content.text
    soup = BeautifulSoup(html_content, 'html.parser')

    requested_content = soup.find('ul', {'data-vr-zone': 'top_stories'})

    for x in requested_content.findAll('li'):
        for y in x.findAll('a'):
            links = y.get('href')
            title =y.get('title')
            # print(title)
            # print(links)

            links =  build_link(links,main_url)

            dispatch(title,links)






if __name__=='__main__':
    title,links = extraction_top_stories(n=0,main_url='https://timesofindia.indiatimes.com/')


