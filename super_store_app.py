import csv
from SuperStore import SuperStore
from Client import Client
from Product import Product
from Laptop import Laptop
from Smartphone import Smartphone
from Shirts import Shirts
from Order import Order

from tkinter import *
from tkinter import ttk
from tkinter import messagebox



class SuperStoreApp:
    def __init__(self, window):


        window.title("The best app ever!")
        window.geometry("900x900")


        lbl = Label(window, text="SuperStore", font=("Ariel bold", 40), fg="blue")
        lbl.grid(column=0, row=0)

        lbl2 = Label(window, text="Product", font=("Ariel bold", 20), fg="blue")
        lbl2.grid(row=1, column=0)

        self.c_product = ttk.Combobox(window, values=["All product", "Laptops", "Smartphone", "Shirt"])
        self.c_product.grid(row=2, column=0)

        self.products = Listbox(window, width=45, height=4)
        self.products.grid(row=2, column=2)

        btn = Button(window, text="Display products", width=14, height=4, command=self.handel_click)
        btn.grid(row=2, column=1)

        lbl3 = Label(window, text="Create New Product", font=("Ariel", 20), fg="blue")
        lbl3.grid(row=8, column=0)

        current_row = 9

        self.status_lbl = Label(window, text="",font=("Ariel bold", 15), fg="red")
        self.status_lbl.grid(row=current_row, column=1)

        current_row+=1

        id_c = Label(window, text="id", font=("Ariel", 10), fg="black")
        id_c.grid(row=current_row, column=0)
        self.enter_id = Entry(window, width=20)
        self.enter_id.grid(row=current_row+1, column=0)

        price = Label(window, text="price", font=("Ariel", 10), fg="black")
        price.grid(row=current_row, column=1)
        self.enter_price = Entry(window, width=20)
        self.enter_price.grid(row=current_row+1, column=1)


        brand = Label(window, text="Brand", font=("Ariel", 10), fg="black")
        brand.grid(row=current_row, column=2)
        self.enter_brand = Entry(window, width=20)
        self.enter_brand.grid(row=current_row+1, column=2)

        model = Label(window, text="Model", font=("Ariel", 10), fg="black")
        model.grid(row=current_row, column=3)
        self.enter_model = Entry(window, width=20)
        self.enter_model.grid(row=current_row+1, column=3)

        current_row+=2

        self.year = Label(window, text="Year", font=("Ariel", 10), fg="black")
        self.year.grid(row=current_row, column=0)

        self.com_year = ttk.Combobox(window, values=self.year_v())
        self.com_year.grid(row=current_row+1, column=0)

        current_row+=2

        self.product_t = StringVar()
        self.product_type = {
            "Laptop": "L",
            "Smartphone": "S"}

        current_row+=1
        for text, value in self.product_type.items():
            r = Radiobutton(window,
                            text=text,
                            value=value,
                            variable=self.product_t, command=self.l_or_s)
            r.grid(sticky=W, column=0, row=current_row)
            current_row += 1

        CPU = Label(window, text="CPU", font=("Ariel", 10), fg="black")
        CPU.grid(row=14, column=1)
        self.enter_CPU = Entry(window, width=20)
        self.enter_CPU.grid(row=15, column=1)

        hard_disk = Label(window, text="Hard disk", font=("Ariel", 10), fg="black")
        hard_disk.grid(row=14, column=2)
        self.enter_hard_disk = Entry(window, width=20)
        self.enter_hard_disk.grid(row=15, column=2)

        screen = Label(window, text="Screen", font=("Ariel", 10), fg="black")
        screen.grid(row=14, column=3)
        self.enter_screen = Entry(window, width=20)
        self.enter_screen.grid(row=15, column=3)

        cellular_net = Label(window, text="Cellular Network", font=("Ariel", 10), fg="black")
        cellular_net.grid(row=16, column=1)
        self.enter_cellular_net = Entry(window, width=20)
        self.enter_cellular_net.grid(row=17, column=1)

        number_of_cores = Label(window, text="Number of cores", font=("Ariel", 10), fg="black")
        number_of_cores.grid(row=16, column=2)
        self.enter_number_of_cores = Entry(window, width=20)
        self.enter_number_of_cores.grid(row=17, column=2)

        camera_resulution = Label(window, text="Camera Resulution", font=("Ariel", 10), fg="black")
        camera_resulution.grid(row=16, column=3)
        self.enter_camera_resulution = Entry(window, width=20)
        self.enter_camera_resulution.grid(row=17, column=3)

        self.current_row = 40
        self.create = Button(window, text="Create", width=14, height=4, fg="blue", command=self.red_entry)
        self.create.grid(row=self.current_row, column=3)
        self.current_row += 1



        self.store = SuperStore('products_supply.csv', 'clients.csv', 'shirts.csv', 'orders.csv')

    def year_v(self):
        v = ["1970"]
        a = 1970
        while a < 2023:
            a += 1
            v.append(str(a))
        return v


    def handel_click(self):
        self.products.delete(0, END)
        list_p = []
        product = self.c_product.get()
        if product == "All product":
            list_p = self.store.product_list
        elif product == "Laptops":
            list_p = self.store.get_all_laptop()
        elif product == "Smartphone":
            list_p = self.store.get_all_phones()
        elif product == "Shirt":
            list_p = self.store.list_shirts()
        for i in list_p:
            self.products.insert(END, str(i))



    def l_or_s(self):
        if self.product_t.get() == "L":
            self.enter_cellular_net["state"] = "disabled"
            self.enter_camera_resulution["state"] = "disabled"
            self.enter_number_of_cores["state"] = "disabled"
            self.enter_CPU["state"] = "normal"
            self.enter_hard_disk["state"] = "normal"
            self.enter_screen["state"] = "normal"

        elif self.product_t.get() == "S":
            self.enter_CPU["state"] = "disabled"
            self.enter_hard_disk["state"] = "disabled"
            self.enter_screen["state"] = "disabled"
            self.enter_cellular_net["state"] = "normal"
            self.enter_camera_resulution["state"] = "normal"
            self.enter_number_of_cores["state"] = "normal"

    def red_entry(self):
        if self.enter_id.get() == "":
            self.enter_id.configure(bg="red")
        else:
            self.enter_id.configure(bg="white")

        if self.enter_price.get() == "":
            self.enter_price.configure(bg="red")
        else:
            self.enter_price.configure(bg="white")

        if self.enter_brand.get() == "":
            self.enter_brand.configure(bg="red")
        else:
            self.enter_brand.configure(bg="white")

        if self.enter_model.get() == "":
            self.enter_model.configure(bg="red")
        else:
            self.enter_model.configure(bg="white")
        a = self.enter_CPU.get()
        if a == "":
            self.enter_CPU.configure(bg="red")
        else:
            self.enter_CPU.configure(bg="white")
        b = self.enter_hard_disk.get()
        if b == "":
            self.enter_hard_disk.configure(bg="red")
        else:
            self.enter_hard_disk.configure(bg="white")
        c = self.enter_screen.get()
        if c == "":
            self.enter_screen.configure(bg="red")
        else:
            self.enter_screen.configure(bg="white")

        d = self.enter_cellular_net.get()
        if d == "":
            self.enter_cellular_net.configure(bg="red")
        else:
            self.enter_cellular_net.configure(bg="white")
        e = self.enter_number_of_cores.get()
        if e == "":
            self.enter_number_of_cores.configure(bg="red")
        else:
            self.enter_number_of_cores.configure(bg="white")

        f = self.enter_camera_resulution.get()
        if f == "":
            self.enter_camera_resulution.configure(bg="red")
        else:
            self.enter_camera_resulution.configure(bg="white")
        list = [self.enter_id, self.enter_price, self.enter_brand, self.enter_model, self.com_year.get(), a, b, c, d, e, f]
        p = 0
        for i in list:
            if i != "":
                p += 1
        if p == 8:
            self.add_new_product()


    def add_new_product(self):
        id = self.enter_id.get()
        if not id.isnumeric():
            self.status_lbl.configure(text=f'The ID:{id} \n is not int')
        elif self.store.get_product(id) is not None:
            self.status_lbl.configure(text=f'The ID:{id} \nThe product already exists')
        elif self.store.get_product(id) is None:
            brand = self.enter_brand.get()
            year = self.com_year.get()
            price = self.enter_price.get()
            model = self.enter_model.get()
            if not price.isnumeric():
                self.status_lbl.configure(text=f'The price:{price} \nis not int')
            elif self.product_t.get() == 'L':
                product_type = 'laptpo'
                CPU = self.enter_CPU.get()
                hard_disk = self.enter_hard_disk.get()
                screen = self.enter_screen.get()
                if not screen.isnumeric():
                    self.status_lbl.configure(text=f'The screen:{screen} \nis not int')
                else:
                    new_product = Laptop(id, product_type, brand, model, year, price, CPU, hard_disk, screen)
                    if self.store.add_product(new_product) == True:
                        messagebox.showinfo(message=f'The product added:{new_product}')
                        self.delete_entry()
            elif self.product_t.get() == "S":
                product_type = 'smartphone'
                cell_net = self.enter_cellular_net.get()
                num_cores = self.enter_number_of_cores.get()
                cam_res = self.enter_camera_resulution.get()
                if not num_cores.isnumeric():
                    self.status_lbl.configure(text=f'The num_cores: {num_cores} \nis not int')
                elif not cam_res.isnumeric():
                    self.status_lbl.configure(text=f'The cam res:{cam_res} \nis not int')
                else:
                    new_product = Smartphone(id, product_type, brand, model, year, price, cell_net, num_cores, cam_res)
                    if self.store.add_product(new_product) == True:
                        messagebox.showinfo(message=f'The product added: {new_product}')
                        self.delete_entry()


    def delete_entry(self):
        self.enter_id.delete(0, END)
        self.enter_brand.delete(0, END)
        self.enter_price.delete(0, END)
        self.enter_model.delete(0, END)
        self.com_year.delete(0, END)
        self.enter_CPU.delete(0, END)
        self.enter_hard_disk.delete(0, END)
        self.enter_screen.delete(0, END)
        self.enter_cellular_net.delete(0, END)
        self.enter_number_of_cores.delete(0, END)
        self.enter_camera_resulution.delete(0, END)




window = Tk()
SuperStoreApp(window)
window.mainloop()



import numpy as np
from matplotlib import pyplot as plt

np.set_printoptions(suppress=True)  # כדי לא לקבל תוצאות ברישום מדעי ( scientific notation)

# 1-	צרו מילון שמכיל כמפתח את מספר הארץ וכערך את שמה
# Q1
countries = {
    1: 'Australia',
    2: 'Canada',
    3: 'China',
    4: 'France',
    5: 'Germany',
    6: 'Greece',
    7: 'India',
    8: 'Italy',
    9: 'Japan',
    10: 'New Zealand',
    11: 'Norway',
    12: 'Russian Federation',
    13: 'Singapore',
    14: 'South Africa',
    15: 'United Kingdom',
    16: 'United States'
}

# 2-	תצרו מערך numpy  בשם gdp
# Q2
gdp = np.genfromtxt('gdp.csv', delimiter=',', skip_header=1)
print(gdp)

# 3-	כמה שורות ועמודות יש במערך
# Q3
# shape[0] is the number of rows , shape[1] is the number of columns

print(f'The number of rows is {gdp.shape[0]} and the number of columns is {gdp.shape[1]}')

# 4-	הוסף עמודה למערך שמציגה עבור כל ארץ את ממוצע ה- gdp  לכל השנים . תעגלו את הממוצע לשתי ספרות אחרי הנקודה
# Q4
# gdp[:,1:12]
# מכיל את כל השורות והעמודות מהעמודה עם אינדקס 1 (עמודה שניה ) עד העמודה  עם האינדקס 11 (עמודה אחרונה)

# mean(axis=1)
# : מחשב את הממוצע של העמודות 1 עד 11 עבור כל שורה

x = gdp[:, 1:12].mean(axis=1)  # מקבלים מערך עם שורה 1 ו-16 ערכים
x = np.around(x, 2)  # מעוגל לשתי ספרות אחרי הנקודה
x = x.reshape(16, 1)  # מקבלים מערך עם 16 שורות ועמודה 1
gdp = np.hstack([gdp, x])   # מחברים בין המערך gdp לעמודה החדשה שיצרנו
print(gdp)

# 5-	לאיזה ארץ יש gdp  הכי נמוך ב- 2022 . הציגו את שם הארץ ואת ה- gdp
# Q5
min2022 = gdp[:, 11].min()  # מינימום עבור 2022 (עמודה עם אינדקס 11 )
print(min2022)
x = int(gdp[gdp[:, 11] == min2022, 0])  # מספר הארץ הנמצא בעמודה 0
print(countries[x])  # שם הארץ מהמילון

# 6-	הציגו את כל השורות שיש להם ב- 2020  gdp  גבוה יותר מממוצע ה- gdp  של אותה שנה.
# Q6
avg = gdp[:, 9].mean()
print(gdp[gdp[:, 9] > avg])

# 7-	הוסיפו עמודה המציגה את גידול ה- gdp  של 5 שנים אחרונות (בין 2017 ל- 2022)
# Q7
x = gdp[:, 11] - gdp[:, 7]  # חישוב ההפרש בין שתי השנים
x = x.reshape(16, 1)
gdp = np.hstack([gdp, x])
print(gdp)

# 8-	לאיזה ארצות יש גידול שלילי. הצג את שם הארץ  ואת ה- gdp  ב- 2017 וב- 2022
# בניית מעדך של שורות עם גידול על פי העמודה החדשה
gdp_negative = gdp[gdp[:, 13] < 0]

print(gdp_negative)
for x in gdp_negative:
    country_id = x[0]  # מספר הארץ
    country_name = countries[country_id]  # שם הארץ על פי המילון
    print(country_name, x[7], x[11])    # x[7] - 2017 | x[11] - 2022

# 9-	בנה דיאגרמת מקלות (bar) שמציגה עבור כל ארץ את ה- gdp  של 2022  ואת ה- gdp  של 2021 באותו גרף (שני מקלות עבור כל ארץ כל אחר בצבע אחר). הצג בציר ה- x את שם הארץ.
# Q9
lx = list(countries.values())
ly1 = list(gdp[:, 11])
ly2 = list(gdp[:, 10])

x_axis = np.arange(len(lx))
plt.xticks(rotation=90)  # Rotates X-Axis Ticks by 90-degrees
# בכדי ליצור הפרדה ביו העמודות את הנתונים של הגרף הראשון נוריד ב 0.2 והגרף השני נעלה ב0.2
# כך יווצר רווח בתצוגה שלהם
# אם נוריד את ההפרשים האלו העמודות יהיו אחת על השנייה
plt.bar(x_axis - 0.2, ly1, color='red', width=0.25, label='2022')
plt.bar(x_axis + 0.2, ly2, color='blue', width=0.25, label='2021')
plt.legend()

plt.show()