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

def btn_advanced():
    def get_news(location):
        print("yes i got that!")
    def make_kernel():
        kernel_root2 = Tk()
        screen_width2 = kernel_root2.winfo_screenwidth()
        screen_height2 = kernel_root2.winfo_screenheight()
        kernel_root2.geometry('%dx%d' % (screen_width2, screen_height2))
        kernel_root2.title('Daily News!')
        return generate_frames2(kernel_root2,screen_width2)

    def generate_frames2(kernel_root2, screen_width2):
        Tops2= Frame(kernel_root2, bg='powder blue', height=50, width=screen_width, relief=SUNKEN)
        Tops2.pack(side=TOP)

        Low_Tops2 = Frame(kernel_root2, bg='red', height=30, width=screen_width, relief=SUNKEN)
        Low_Tops2.pack(side=TOP)

        Left2 = Frame(kernel_root2, bg='green', height=700, width=663, relief=SUNKEN)
        Left2.pack(side=TOP)

        Right2 = Frame(kernel_root2, bg='red', height=700, width=663, relief=SUNKEN)
        Right2.pack(side=RIGHT)
        location = StringVar()
        txtLabel_loc = Label(Tops2, font=('arial', 16,
                                         'bold'),text='Enter Location', bd=8, bg='powder blue',
                            justify=RIGHT)
        txtLabel_loc.grid(row=0, column=0)

        txtLocation = Entry(Tops2,  font = ('arial', 16,
                                      'bold'), textvariable = location, bd = 10, insertwidth = 4, bg = 'powder blue',
                                                                                                      justify = RIGHT)
        txtLocation.grid(row=0, column=1)
        btn_loc = Button(Tops2, text="CLICK", bd=10,
                          padx=12, pady=12, fg='white', font=('arial', 12, 'bold'), bg='blue',
                          command=lambda : get_news(txtLocation.get())
                          )
        btn_loc.grid(row=0,column=2)


        def get_news(location):
            print(location)
            return extract_city_news("https://timesofindia.indiatimes.com/city",location)

        def extract_city_news(main_url,location):
            print(main_url)
            import requests
            from bs4 import BeautifulSoup
            title_list = []
            pg_list = []
            nav_link_list = []
            # manual_city = input("Enter city name: ")
            # manual_city = manual_city.lower()

            main_url = main_url + '/' + location

            content = requests.get(main_url)
            html_content = content.text
            soup = BeautifulSoup(html_content, "html.parser")
            print(main_url)
            req_content = soup.find('script', {'type': 'application/ld+json'})
            r_c = soup.find('ul', {'class': 'top-newslist clearfix'})
            data = req_content.text

            for x in r_c.findAll('li'):
                for y in x.findAll('a'):
                    inner_link = y.get('href')
                    pg = y.get('pg')
                    title = y.get('title')
                    link = inner_link
                    if link.__contains__('/city'):
                        link_list = link.split('/')
                        link_list = link_list[3:]
                        new_link = '/'.join(link_list)
                        main_url = main_url + '/'
                        upd_link = main_url + new_link
                        inner_link = upd_link

                    title_list.append(title)
                    nav_link_list.append(inner_link)
                    pg_list.append(pg)

            return new_pre_labels(title_list, nav_link_list, Tops2, Low_Tops2, Left2, Right2)


    def new_pre_labels(title_list, nav_link_list,Tops2,Low_Tops2,Left2,Right2):
        lbl_main_title2 = Label(Tops2,text='DAILY NEWS!',font=('arial',40,'bold'),
                            bg='powder blue',fg='Steel Blue',bd=10,anchor='w')
        lbl_main_title2.grid(row=0,column=0)


        lbl_topstories2 = Label(Low_Tops2,text='TOP STORIES!',font=('arial',20,'bold'),
                               bd=10,fg='PURPLE',anchor='w',bg='red')
        lbl_topstories2.grid(row=0, column=0)
        lbl_top_ex2 = Label(Low_Tops2, text='THIS SECTION GIVES COMPLETE LIST OF TOP STORIES TODAY!'+
                                          'HAVE A GREAT DAY ASHEAD SIR!', font=('arial', 10, 'bold'),
                               bd=10, fg='PURPLE', anchor='w',bg='red')
        lbl_top_ex2.grid(row=1, column=1)

        localtime = get_localtime()

        lbl_time2 =  Label(Tops2,text=localtime,font=('arial',20,'bold'),
                               bd=5,fg='Black',anchor='w')
        lbl_time.grid(row=1, column=0)

        lbl_latest2 = Label(Left2, text='LATEST NEWS!', font=('arial', 19, 'bold'),
                               bd=10, fg='green',anchor='w')
        lbl_latest2.grid(row=0, column=0)


        lbl_loc_news2 = Label(Right2, text='IN CHENNAI TODAY!', font=('arial', 25, 'bold'),
                           bd=10, fg='Steel Blue', anchor='w')
        lbl_loc_news2.grid(row=0, column=0)

        lbl_loc_ex2 = Label(Right2, text='HELLO @ENC0DED_VIP !THIS SECTION GIVES YOU THE LATEST NEWS OF YOUR LOCATION!',
                              font=('arial', 10, 'bold'),
                              bd=10, fg='green', anchor='w')
        lbl_loc_ex2.grid(row=1, column=0)
        return populate_location_stories(title_list, nav_link_list,Tops2,Low_Tops2,Left2,Right2)

    def populate_location_stories(title_list, link_list,Tops2,Low_Tops2,Left2,Right2):
        # main_list, url_list = extract_city_news("https://timesofindia.indiatimes.com/city")
        x = len(title_list)
        print(x)
        latest_box2 = Listbox(Low_Tops2, width=663, bd=10, cursor='dotbox', selectmode=SINGLE,
                             font=('comic sans', 8, 'italic'), height=10)  # use height =16

        latest_box2.grid(row=0, column=1)
        i = 1
        for t in title_list:
            temp_title = str(t)
            l =title_list.index(t)
            temp_link = link_list[l]
            latest_box2.insert(END, 'News' + ' ' + temp_title)
            latest_box2.insert(END, 'Link' + ' ' + (temp_link))

        return general_extraction("https://timesofindia.indiatimes.com/",Tops2, Low_Tops2, Left2, Right2)

    def general_extraction(main_url, Tops2, Low_Tops2, Left2, Right2):
        ac_title = []
        ac_link = []
        # print('ACROSS INDIA TODAY :' + '\n')
        soup = BeautifulSoup(requests.get(main_url).text, 'html.parser')
        req_content = soup.findAll('ul', {'data-vr-zone': 'across_toi'})
        for x in req_content:
            r_c = x.findAll('li')
            for y in r_c:
                r1_c = y.findAll('a')
                for z in r1_c:
                    title = z.get('title')
                    pg = z.get('pg')
                    link = z.get('href')
                    if not link.__contains__(main_url):
                        if link[0] == '/':
                            link = link[1:]
                            link = main_url + link

                    else:
                        if link[0] == '/':
                            link = link[1:]
                            link = main_url + link
                    # link = build_link(link, main_url)
                    # dispatch_op(title, link, pg)
                    ac_title.append(title)
                    ac_link.append(link)


        return new_pre_labels_latest(ac_title, ac_link, Tops2, Low_Tops2, Left2, Right2)

    def new_pre_labels_latest(title_list, nav_link_list, Tops2, Low_Tops2, Left2, Right2):
        lbl_main_title2 = Label(Tops2, text='DAILY NEWS!', font=('arial', 40, 'bold'),
                                bg='powder blue', fg='Steel Blue', bd=10, anchor='w')
        lbl_main_title2.grid(row=0, column=0)

        lbl_topstories2 = Label(Low_Tops2, text='TOP STORIES!', font=('arial', 20, 'bold'),
                                bd=10, fg='PURPLE', anchor='w', bg='red')
        lbl_topstories2.grid(row=0, column=0)
        lbl_top_ex2 = Label(Low_Tops2, text='THIS SECTION GIVES COMPLETE LIST OF TOP STORIES TODAY!' +
                                            'HAVE A GREAT DAY ASHEAD SIR!', font=('arial', 10, 'bold'),
                            bd=10, fg='PURPLE', anchor='w', bg='red')
        lbl_top_ex2.grid(row=1, column=1)

        localtime = get_localtime()

        lbl_time2 = Label(Tops2, text=localtime, font=('arial', 20, 'bold'),
                          bd=5, fg='Black', anchor='w')
        lbl_time.grid(row=1, column=0)

        lbl_latest2 = Label(Left2, text='LATEST NEWS!', font=('arial', 19, 'bold'),
                            bd=10, fg='green', anchor='w')
        lbl_latest2.grid(row=0, column=0)

        lbl_loc_news2 = Label(Right2, text='IN CHENNAI TODAY!', font=('arial', 25, 'bold'),
                              bd=10, fg='Steel Blue', anchor='w')
        lbl_loc_news2.grid(row=0, column=0)

        lbl_loc_ex2 = Label(Right2, text='HELLO @ENC0DED_VIP !THIS SECTION GIVES YOU THE LATEST NEWS OF YOUR LOCATION!',
                            font=('arial', 10, 'bold'),
                            bd=10, fg='green', anchor='w')
        lbl_loc_ex2.grid(row=1, column=0)
        return populate_across_stories(title_list, nav_link_list, Tops2, Low_Tops2, Left2, Right2)

    def populate_across_stories(title_list, link_list, Tops2, Low_Tops2, Left2, Right2):
        # main_list, url_list = extract_city_news("https://timesofindia.indiatimes.com/city")
        x = len(title_list)
        print(x)
        latest_box3 = Listbox(Left2, width=663, bd=10, cursor='dotbox', selectmode=SINGLE,
                             font=('comic sans', 8, 'italic'), height=18)  # use height =16

        latest_box3.grid(row=0, column=1)
        i = 1
        for t in title_list:
            temp_title = str(t)
            l = title_list.index(t)
            temp_link = link_list[l]
            latest_box3.insert(END, 'News' + ' ' + temp_title)
            latest_box3.insert(END, 'Link' + ' ' + (temp_link))


    return make_kernel()



def btn_fuel():
    def make_kernel_part3():
        kernel_root3 = Tk()
        kernel_root3.title('Petrol Prices in different cities')
        scw = kernel_root3.winfo_screenwidth()
        sch = kernel_root3.winfo_screenheight()
        kernel_root3.geometry('%dx%d' % (scw, sch))
        kernel_root3.mainloop()
        return make_new_frames(kernel_root3, scw)
    # return make_kernel_part3()


    def make_new_frames(kernel_root3,scw):
        Topnew = Frame(kernel_root3, bg='powder blue', height=50, width=screen_width, relief=SUNKEN)
        Topnew.pack(side=TOP)

        lbl_fuel = Label(Topnew, text='Enter Location', font=('arial', 40, 'bold'),
                                bg='powder blue', fg='Steel Blue', bd=10, anchor='w')
        lbl_fuel.grid(row=0, column=0)
        location = StringVar()
        txtLocation = Entry(Topnew, font=('arial', 16,
                                         'bold'), textvariable=location, bd=10, insertwidth=4, bg='powder blue',
                            justify=RIGHT)
        txtLocation.grid(row=0, column=1)

        btn_loc = Button(Topnew, text="CLICK", bd=10,
                         padx=12, pady=12, fg='white', font=('arial', 12, 'bold'), bg='blue',
                         command=lambda: get_loc(txtLocation.get())
                         )
        btn_loc.grid(row=0, column=2)
        LowTop_new = Frame(kernel_root3, bg='powder blue', height=50, width=screen_width, relief=SUNKEN)
        Topnew.pack(side=TOP)

        def get_loc(location):
            print(location)
            manual_city = location.lower()
            main_url = "https://timesofindia.indiatimes.com/city"
            main_url = main_url + '/' + manual_city
            return scrape_content(main_url,manual_city)

        def scrape_content(main_url,manual_city):
            soup = BeautifulSoup(requests.get(main_url).text, "html.parser")
            req_content = soup.find('div', {'id': 'fuelList'})
            r_c = req_content
            for x in r_c:
                link = x.find('li').find('a').get('href')
                generated_link = main_url + '/' + '/'.join(link.split('/')[3:])

                new_soup = BeautifulSoup(requests.get(generated_link).text, 'html.parser')
                required = new_soup.find('div', {'class': 'Normal'}).text

            return new_pre_labels3(generated_link,manual_city,required,LowTop_new)

    def new_pre_labels3(generated_link, manual_city,required,LowTop_new):



        lbl_topstories2 = Label(LowTop_new,text='TOP STORIES!',font=('arial',20,'bold'),
                               bd=10,fg='PURPLE',anchor='w',bg='red')
        lbl_topstories2.grid(row=0, column=0)
        lbl_top_ex2 = Label(LowTop_new, text='THIS SECTION GIVES COMPLETE LIST OF TOP STORIES TODAY!'+
                                          'HAVE A GREAT DAY ASHEAD SIR!', font=('arial', 10, 'bold'),
                               bd=10, fg='PURPLE', anchor='w',bg='red')
        lbl_top_ex2.grid(row=1, column=1)

        return populate_petrol_prices(generated_link,manual_city,required,LowTop_new)

    def populate_petrol_prices(generated_link,manual_city,required,LowTop_new):
        link_list = []
        title_list = []
        link_list.append(generated_link)
        title_list.append(required)
        # main_list, url_list = extract_city_news("https://timesofindia.indiatimes.com/city")
        x = len(title_list)
        print(x)
        latest_box3 = Listbox(LowTop_new, width=663, bd=10, cursor='dotbox', selectmode=SINGLE,
                             font=('comic sans', 8, 'italic'), height=10)  # use height =16

        latest_box3.grid(row=0, column=1)
        i = 1
        for t in title_list:
            temp_title = str(t)
            l =title_list.index(t)
            temp_link = link_list[l]
            latest_box3.insert(END, 'News' + ' ' + temp_title)
            latest_box3.insert(END, 'Link' + ' ' + (temp_link))

    return make_kernel_part3()








def button_handler():
    btn_more = Button(Tops,text="CLICK HERE FOR MORE NEWS",bd=10,
                      padx=12, pady=12, fg='white', font=('arial',12, 'bold'), bg='blue',
                      command=btn_advanced
                      )
    btn_more.grid(row=1,column=1)
    btn_more = Button(Tops, text="CHECK FUEL PRICES", bd=10,
                      padx=12, pady=12, fg='white', font=('arial', 12, 'bold'), bg='red',
                      command=btn_fuel
                      )
    btn_more.grid(row=1, column=2)

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

        lbl_loc_news = Label(Right, text='IN CHENNAI TODAY!', font=('arial', 25, 'bold'),
                           bd=10, fg='Steel Blue', anchor='w')
        lbl_loc_news.grid(row=0, column=0)

        lbl_loc_ex = Label(Right, text='HELLO @ENC0DED_VIP !THIS SECTION GIVES YOU THE LATEST NEWS OF YOUR LOCATION!',
                              font=('arial', 10, 'bold'),
                              bd=10, fg='green', anchor='w')
        lbl_loc_ex.grid(row=1, column=0)

        return Tops,Low_Tops,Left,Right,lbl_main_title,lbl_time,lbl_topstories,lbl_top_ex,lbl_latest,lbl_loc_news,lbl_loc_ex

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

    populate_top_stories(Tops,Low_Tops,Left,Right)

    button_handler()
    run(kernel_root)

