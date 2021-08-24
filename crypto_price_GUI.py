import tkinter as tk
import tkinter.font as TkFont
import requests
from datetime import datetime

# definisanje parametara za citanje API vrednosti
parameters = {
  'start':'1',
  'limit':'7', # broj kriptovaluta za prikazivanje
  'convert':'USD'
}
headers = {
  'X-CMC_PRO_API_KEY': '<<API KLJUC>>', # univerzalni kljuc
  'Accepts': 'application/json'
}

def trackPrice():
    # definisanje vrednosti za citanje i ispisivanje u GUI-u
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    json = requests.get(url, params = parameters, headers = headers).json()
    time = datetime.now().strftime("%H:%M:%S") # formatiranje vremena
    valute = json['data'] # lista sa vrednostima

    for coin in valute:
    # defninisanje vrednosti za popunjavanje label-a
        if coin['symbol'] == 'BTC':
            labelPrice1.config(text = str(coin['name']) + " " + str("{:.2f}".format((coin['quote']['USD']['price']))))

        if coin['symbol'] == 'ETH':
            labelPrice2.config(text = str(coin['name']) + " " + str("{:.2f}".format((coin['quote']['USD']['price']))))

        if coin['symbol'] == 'ADA':
            labelPrice3.config(text = str(coin['name']) + " " + str("{:.2f}".format((coin['quote']['USD']['price']))))

        if coin['symbol'] == 'BNB':
            labelPrice4.config(text = str(coin['name']) + " " + str("{:.2f}".format((coin['quote']['USD']['price']))))

        if coin['symbol'] == 'USDT':
            labelPrice5.config(text = str(coin['name']) + " " + str("{:.2f}".format((coin['quote']['USD']['price']))))

        if coin['symbol'] == 'XRP':
            labelPrice6.config(text = str(coin['name']) + " " + str("{:.2f}".format((coin['quote']['USD']['price']))))  

        if coin['symbol'] == 'DOGE':
            labelPrice7.config(text = str(coin['name']) + " " + str("{:.2f}".format((coin['quote']['USD']['price']))))

        labelTime.config(text = "Last refresh time: " + time) 

    root.after(1000, trackPrice) # refresovanje citanja nakon 1 sekunde

# definisanje izgleda glavnog prozora grafickog interfejsa
root = tk.Tk()
root.geometry("700x800") # velicina prozora
root.title("BTC/ETH price tracker") # ime prozora

# definisanje PNG slike koja je na pozadini glavnog prozora
filename = tk.PhotoImage(file = "C:\\Users\<<PUTANJA DO FOLDERA SA SLIKOM POZADINE>>\\background.png")
background_label = tk.Label(root, image = filename)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# definisanje fontova
font1 = TkFont.Font(family = "Herculanum", size = 24, weight = "bold")
font2 = TkFont.Font(family = "Helvetica", size = 22, weight = "bold")
font3 = TkFont.Font(family = "Helvetica", size = 18, weight = "normal")

# definisanje vrednosti ispisanih na glavnom prozoru
label = tk.Label(root, text = "Live Price Tracker", font = font1)
label.pack(pady = 60)

# label za vrednosti 
labelPrice1 = tk.Label(root, font = font2)
labelPrice1.pack(pady = 10)

 # label za vrednosti 
labelPrice2 = tk.Label(root, font = font2) 
labelPrice2.pack(pady = 10)

# label za vrednosti 
labelPrice3 = tk.Label(root, font = font2)
labelPrice3.pack(pady = 10)

 # label za vrednosti 
labelPrice4 = tk.Label(root, font = font2) 
labelPrice4.pack(pady = 10)

# label za vrednosti 
labelPrice5 = tk.Label(root, font = font2)
labelPrice5.pack(pady = 10)

# label za vrednosti 
labelPrice6 = tk.Label(root, font = font2)
labelPrice6.pack(pady = 10)

# label za vrednosti 
labelPrice7 = tk.Label(root, font = font2)
labelPrice7.pack(pady = 10)

# label za vrednosti trenutnog vremena
labelTime = tk.Label(root, font = font3) 
labelTime.pack(pady = 80)

# definisanje main funkcije
if __name__ == "__main__":

    trackPrice()
    root.mainloop()
