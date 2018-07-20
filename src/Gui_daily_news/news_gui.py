import tkinter as tk
from tkinter import *
from tkinter import Button,Label,Frame,Entry
from tkinter import messagebox
import time
from tkinter import Tk
import time

from src.top_stories.extract_headlines import *
from src.Latest_News.extract_latest import *

def set_window():
    kernel_root = Tk()
    screen_width = kernel_root.winfo_screenwidth()
    screen_height = kernel_root.winfo_screenheight()
    kernel_root.geometry('%dx%d'%(screen_width,screen_height))
    kernel_root.title('Daily News!')
    return kernel_root,screen_height,screen_width

def run(kernel_root):
    kernel_root.mainloop()

def get_localtime():
    localtime = time.asctime(time.localtime(time.time()))
    return localtime

def generate_frames(kernel_root,screen_width):
    Tops  = Frame(kernel_root,bg='powder blue',height=50,width=screen_width,relief=SUNKEN)
    Tops.pack(side=TOP)

    Low_Tops = Frame(kernel_root,bg='red',height=30,width=screen_width,relief=SUNKEN)
    Low_Tops.pack(side=TOP)


    Left = Frame(kernel_root,bg='green',height=700,width=663,relief=SUNKEN)
    Left.pack(side=TOP)

    Right = Frame(kernel_root, bg='red', height=700, width=663, relief=SUNKEN)
    Right.pack(side=RIGHT)
    def pre_labels():
        lbl_main_title = Label(Tops,text='DAILY NEWS!',font=('arial',40,'bold'),
                            bg='powder blue',fg='Steel Blue',bd=10,anchor='w')
        lbl_main_title.grid(row=0,column=0)


        lbl_topstories = Label(Low_Tops,text='TOP STORIES!',font=('arial',20,'bold'),
                               bd=10,fg='PURPLE',anchor='w',bg='red')
        lbl_topstories.grid(row=0, column=0)
        lbl_top_ex = Label(Low_Tops, text='THIS SECTION GIVES COMPLETE LIST OF TOP STORIES TODAY!'+
                                          'HAVE A GREAT DAY ASHEAD SIR!', font=('arial', 10, 'bold'),
                               bd=10, fg='PURPLE', anchor='w',bg='red')
        lbl_top_ex.grid(row=1, column=1)

        localtime = get_localtime()

        lbl_time =  Label(Tops,text=localtime,font=('arial',20,'bold'),
                               bd=5,fg='Black',anchor='w')
        lbl_time.grid(row=1, column=0)

        lbl_latest = Label(Left, text='LATEST NEWS!', font=('arial', 19, 'bold'),
                               bd=10, fg='green',anchor='w')
        lbl_latest.grid(row=0, column=0)
        # lbl_latest_ex = Label(Left, text='HELLO @ENC0DED_VIP !'+'\n'
        #                                  'THIS SECTION GIVES YOU'+'\n'
        #                                  ' THE LATEST NEWS AROUND THE WORLD!', font=('arial', 10, 'bold'),
        #                    bd=10, fg='green', anchor='w')
        # lbl_latest_ex.grid(row=1, column=0)



        lbl_loc_news = Label(Right, text='IN CHENNAI TODAY!', font=('arial', 25, 'bold'),
                           bd=10, fg='Steel Blue', anchor='w')
        lbl_loc_news.grid(row=0, column=0)

        lbl_loc_ex = Label(Right, text='HELLO @ENC0DED_VIP !THIS SECTION GIVES YOU THE LATEST NEWS OF YOUR LOCATION!',
                              font=('arial', 10, 'bold'),
                              bd=10, fg='green', anchor='w')
        lbl_loc_ex.grid(row=1, column=0)

        return Tops,Low_Tops,Left,Right,lbl_main_title,lbl_time,lbl_topstories,lbl_top_ex,lbl_latest,lbl_loc_news,lbl_loc_ex
        # , lbl_latest_ex before lbl_loc_news
    return pre_labels()


def populate_top_stories(Tops,Low_Tops,Left,Right):
    #Remember to delete the unused arguments at the end of the section!
    def top_stories():
        main_list,url_list = extraction_top_stories(n=0,main_url='https://timesofindia.indiatimes.com/')
        x=len(main_list)
        print(x)
        story_list_box = Listbox(Low_Tops, width=screen_width,bd=10,cursor='dotbox',selectmode=SINGLE,
                                 font=('comic sans',8,'italic'),height=14,selectbackground='green')

        story_list_box.grid(row=0, column=1)
        i=1
        for t in main_list:
            temp_title=str(t)
            l = main_list.index(t)
            temp_link = url_list[l]
            story_list_box.insert(END,'News'+' '+temp_title)
            story_list_box.insert(END, 'Link'+' '+(temp_link))

        return latest_news()

    def latest_news():
        main_list, url_list = extract_latest_stories(n=0,main_url='https://timesofindia.indiatimes.com/')
        x = len(main_list)
        print(x)
        latest_box = Listbox(Left, width=663, bd=10, cursor='dotbox', selectmode=SINGLE,
                                  font=('comic sans', 8, 'italic'),height=18)  # use height =16

        latest_box.grid(row=0, column=1)
        i = 1
        for t in main_list:
            temp_title = str(t)
            l = main_list.index(t)
            temp_link = url_list[l]
            latest_box.insert(END, 'News' + ' ' + temp_title)
            latest_box.insert(END, 'Link' + ' ' + (temp_link))




    return top_stories()


if __name__ == '__main__':
    kernel_root,screen_height,screen_width = set_window()
    Tops,Low_Tops,Left,Right,lbl_main_title, lbl_time, lbl_topstories, lbl_top_ex, lbl_latest, lbl_loc_news, lbl_loc_ex=generate_frames(kernel_root,screen_width)
    #, lbl_latest_ex before lbl_loc_news
    populate_top_stories(Tops,Low_Tops,Left,Right)
    # , lbl_latest_ex before lbl_loc_news
    run(kernel_root)

