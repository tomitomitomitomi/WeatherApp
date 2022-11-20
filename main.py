import requests
from tkinter import *

api = '88231e840f02fbfe64b9e74454d91e89'

syote = input("Anna kaupunki: ")

saa_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={syote}&units=metric&APPID={api}")
print(saa_data.json())

saa = saa_data.json()['weather'][0]['main']   #uudelleen tähän, koska toinen aliohjelma ei voi noutaa alemmasta iffistä
saakuvaus = saa_data.json()['weather'][0]['description']
lampotila = round(saa_data.json()['main']['temp'])
sijainti = saa_data.json()['coord']

if saa_data.json()['cod'] == '404':
    print("Kaupunkia ei löytynyt")
else:
    saa = saa_data.json()['weather'][0]['main']
    saakuvaus = saa_data.json()['weather'][0]['description']
    lampotila = round(saa_data.json()['main']['temp'])
    sijainti = saa_data.json()['coord']

    print(f"Sää paikassa {syote} on: {saa}")
    print(f"Sään tarkempi kuvaus: {saakuvaus} ")
    print(f"Lämpötila paikassa {syote} on: {lampotila}°C")
    print(f"Kaupungin {syote} koordinaatit ovat: {sijainti}")


root = Tk()
root.geometry("350x350")
root.title("Sääseuranta - " + f'{syote}')

def nayta_kaupungin_nimi(syote):
    kaupunki_label = Label(root, text=f"{syote}")
    kaupunki_label.config(font=("Consolas", 28))
    kaupunki_label.pack(side='top')

def nayta_statistiikat(saa, saakuvaus, lampotila, sijainti):

    saa = Label(root, text=f"{saa}")
    saakuvaus = Label(root, text=f"{saakuvaus}")
    lampotila = Label(root, text=f"{lampotila} °C")
    sijainti = Label(root, text=f"{sijainti}")



    saa.config(font=("Consolas", 22))
    saakuvaus.config(font=("Consolas", 22))
    lampotila.config(font=("Consolas", 22))
    sijainti.config(font=("Consolas", 22))


    saa.pack(side='top')
    saakuvaus.pack(side='top')
    lampotila.pack(side='top')
    sijainti.pack(side='top')


nayta_kaupungin_nimi(syote)
nayta_statistiikat(saa, saakuvaus, lampotila, sijainti)

mainloop()