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
    Tops  = Frame(kernel_root,bg='powder blue',height=70,width=screen_width,relief=SUNKEN)
    Tops.pack(side=TOP)

    Low_Tops = Frame(kernel_root,bg='red',height=100,width=screen_width,relief=SUNKEN)
    Low_Tops.pack(side=TOP)

    lbl_topstories = Label(Tops, text='Fuel Prices', font=('arial', 20, 'bold'),
                           bd=10, fg='PURPLE', anchor='w', bg='red')
    lbl_topstories.grid(row=0, column=0)

    localtime = get_localtime()

    lbl_time = Label(Tops, text=localtime, font=('arial', 20, 'bold'),
                     bd=5, fg='Black', anchor='w')
    lbl_time.grid(row=0, column=1)

    location= StringVar()
    txtLabel_loc = Label(Tops, font=('arial', 16,
                                      'bold'), text='Enter Location', bd=8, bg='powder blue',
                         justify=RIGHT)
    txtLabel_loc.grid(row=1, column=0)

    txtLocation = Entry(Tops, font=('arial', 16,
                                     'bold'), textvariable=location, bd=10, insertwidth=4, bg='powder blue',
                        justify=RIGHT)
    txtLocation.grid(row=1, column=1)
    btn_loc = Button(Tops, text="Get Price Details", bd=10,
                     padx=12, pady=12, fg='white', font=('arial', 12, 'bold'), bg='blue',
                     command=lambda: get_loc(txtLocation.get())
                     )
    btn_loc.grid(row=1, column=2)

    def get_loc(manual_city):
        print(manual_city)
        manual_city = manual_city.lower()
        main_url = "https://timesofindia.indiatimes.com/city"
        main_url = main_url + '/' + manual_city
        return scrape_content(main_url, manual_city)

    def scrape_content(main_url, manual_city):
        soup = BeautifulSoup(requests.get(main_url).text, "html.parser")
        req_content = soup.find('div', {'id': 'fuelList'})
        r_c = req_content
        cont = []
        link_list = []
        for x in r_c:
            link = x.find('li').find('a').get('href')
            generated_link = main_url + '/' + '/'.join(link.split('/')[3:])

            new_soup = BeautifulSoup(requests.get(generated_link).text, 'html.parser')
            required = new_soup.find('div', {'class': 'Normal'}).text

            cont.append(required)
            link_list.append(generated_link)
        return pre_labels(link_list, manual_city, cont, Low_Tops)

    def pre_labels(generated_link, manual_city, required, Low_Tops):
        #HEre no pre labels , they are already defined above
        return Populate_Fuel_Price_Details(Tops,Low_Tops,required,generated_link,manual_city)




def Populate_Fuel_Price_Details(Tops,Low_Tops,required,generated_link,manual_city):
    # print('Valued work')
    x = len(required)
    print(x)
    latest_box3 = Listbox(Low_Tops, width=663, bd=10, cursor='dotbox', selectmode=SINGLE,
                          font=('comic sans', 8, 'italic'), height=10)  # use height =16

    latest_box3.grid(row=0, column=1)
    i = 1
    for t in required:
        temp_title = str(t)
        l = required.index(t)
        temp_link = generated_link[l]
        y = temp_title.split('.')
        latest_box3.insert(END, 'News')
        for x in y:
            latest_box3.insert(END,x)
        latest_box3.insert(END, 'Link' + ' ' + (temp_link))

if __name__ == '__main__':
    kernel_root,screen_height,screen_width = set_window()
    generate_frames(kernel_root,screen_width)

    run(kernel_root)




