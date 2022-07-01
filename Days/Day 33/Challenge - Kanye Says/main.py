from tkinter import *
import requests
# CHALLENGE: Make a get() request to the Kanye Rest API ✔
#            Raise an exception if the request returned an unsuccessful status code ✔
#            Parse the JSON to obtain the quote text ✔
#            Display the quote in the canvas' quote_text widget ✔


def get_quote():
    api_response = requests.get(url="https://api.kanye.rest")
    api_response.raise_for_status()
    quote = api_response.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="Days\\Day 33\\Challenge - Kanye Says\\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="Days\\Day 33\\Challenge - Kanye Says\\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
