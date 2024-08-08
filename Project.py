from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from datetime import datetime
from timezonefinder import TimezoneFinder
import requests
import pytz

root=Tk()
root.title("Whether App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()
 
        geolocator=Nominatim(user_agent="geoapiExersises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
 
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #WEATHER
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=60b895dd13588b6fdee6fa796c441fd5"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']


        t.config(text=(temp,"°"))
        c.config( text=(condition,"|","FEELS","LIKE",temp,"°"))
 
        w.config(text=wind)
        h.config(text=humidity)
      
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")



#Logo
Logo_image=PhotoImage(file="rain.png")
logo=Label(image=Logo_image)
logo.place(x=30,y=30)


#search box
Search_image=PhotoImage(file="search.png") 
myimage=Label(image=Search_image)
myimage.place(x=40,y=10)

textfield=tk.Entry(root,justify="center",width=15,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=70,y=30)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=25)



 
#Bottom Box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#Time
name=Label(root,font=("areal",20,"bold"))
name.place(x=100,y=30)
clock=Label(root,font=("Helvetica",20))
clock.place(x=650,y=70)
          

#label
label1=Label(root,text="WIND",font=("Helvetica",20,'bold'),fg="White",bg="#1ab5ef")
label1.place(x=220,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",20,'bold'),fg="White",bg="#1ab5ef")
label2.place(x=500,y=400)



t=Label(font=("areal",90,"bold"),fg="#ee666d")
t.place(x=600,y=150)

c=Label(font=("areal",15,"bold"))
c.place(x=600,y=280)


w=Label(text="...",font=("areal",20,"bold"),bg="#1ab5ef")
w.place(x=550,y=430)

h=Label(text="...",font=("areal",20,"bold"),bg="#1ab5ef")
h.place(x=230,y=430)


root.mainloop()
