import tkinter as tk
from PIL import ImageTk, Image
import requests


# key 0e9132f430fbb665e205970becb02636
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}


HEIGHT = 700
WIDTH = 800

root = tk.Tk()
root.title("Weather App")


# function define
def action(a):
    print(f"button clicked {a}")


def format(weather):
    try:
        CName = weather['sys']['country']
        CityName = weather['name']
        des = weather['weather'][0]['description']
        temp = weather['main']['temp']
        loc = weather['coord']
        final_msg = f'Coutry: {CName} \n City: {CityName} \n Weather: {des} \n Temperature: {temp}F \n Location: {loc}'
    except:
        final_msg = 'problem retrieving data'
    return final_msg


def getWeather(city):
    key = '0e9132f430fbb665e205970becb02636'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'appid': key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params, )
    weather = response.json()
    label['text'] = format(weather)


canvas = tk.Canvas(root, height=650, width=750)
canvas.pack()

bg_img = ImageTk.PhotoImage(Image.open('weather.png'))
bg_label = tk.Label(root, image=bg_img)
bg_label.place(relheight=1, relwidth=1)

frame = tk.Frame(root, bg='#495e80', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, text='this is entry area')
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Get Weather Update', bg='black', fg='green', font=40,
                   command=lambda: getWeather(entry.get()))

button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#495e80", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, text='', font=40, anchor='nw', justify='left')
label.place(relwidth=1, relheight=1)

root.mainloop()
