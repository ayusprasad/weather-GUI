from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=99bcfbb010d36965e5fe840e95a7ff2f")

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        label_blank_w.config(text=data["weather"][0]["main"])
        wb_label_blank.config(text=data["weather"][0]["description"])
        wb_label_temp.config(text=str(data["main"]["temp"] - 273.15))
        wb_label_pressure.config(text=data["main"]["pressure"])
    else:
        label_blank_w.config(text="Error fetching data")
        wb_label_blank.config(text="")
        wb_label_temp.config(text="")
        wb_label_pressure.config(text="")


win = Tk()
win.title("Weather App")
win.config(background='gray')
win.geometry('540x570')
name_label = Label(win, text="weather app", font=("arial", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=350)
city_name = StringVar()
list_name = ["Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
             "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
             "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
             "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
             "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
             "National Capital Territory of Delhi", "Puducherry"]

com = ttk.Combobox(win, values=list_name, font=("arial", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

w_label = Label(win, text="Weather Climate ", font=("arial", 12))
w_label.place(x=25, y=260, height=50, width=210)

label_blank_w = Label(win, text=" ", font=("arial", 12))
label_blank_w.place(x=250, y=260, height=50, width=210)

wb_label = Label(win, text="weather Description", font=("arial", 12))
wb_label.place(x=25, y=330, height=50, width=210)

wb_label_blank = Label(win, text=" ", font=("arial", 12))
wb_label_blank.place(x=250, y=330, height=50, width=210)

temp_label = Label(win, text="Temperature", font=("arial", 12))
temp_label.place(x=25, y=400, height=50, width=210)

wb_label_temp = Label(win, text=" ", font=("arial", 12))
wb_label_temp.place(x=250, y=400, height=50, width=210)

pressure_label = Label(win, text="Pressure", font=("arial", 12))
pressure_label.place(x=25, y=470, height=50, width=210)

wb_label_pressure = Label(win, text=" ", font=("arial", 12))
wb_label_pressure.place(x=250, y=470, height=50, width=210)

done_button = Button(win, text="Done", font=("arial", 20, "bold"), command=data_get)
done_button.place(y=190, height=50, width=100, x=200)

win.mainloop()
