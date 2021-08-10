import tkinter as tk
import requests
import time

canva = tk.Tk() #creating a window
canva.geometry("600x500")  # scale of window
canva.title("Weather App") #title 

#weather function
def weather(canva):
   city = text.get() #city name as enterd by the user
   api = "https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=e86f15e621e016803f649c751635f685"
   json_data = requests.get(api).json()  #getting jason data from api
   condition = json_data['weather'][0]['main'] #conditions are from weather dictionary in main placed at 0th position
   temperature = int(json_data['main']['temp'] - 273.15) #according to the api temperature is in main and it has temp
   min_temperature = int(json_data['main']['temp_min'] - 273.15)
   max_temperature = int(json_data['main']['temp_max'] - 273.15)
   pressure = json_data['main']['pressure']
   humidity = json_data['main']['humidity']
   wind = json_data['wind']['speed']
   sunrise = time.strftime("%I:%M:%S %p", time.gmtime(json_data['sys']['sunrise'] - 21600)) # gmt is used for convrting from seconds and 21600 is for varying timezone
   sunset = time.strftime("%I:%M:%S %p", time.gmtime(json_data['sys']['sunset'] - 21600))

   #setting strings to carryon the data
   final1 = condition + "\n" + str(temperature) + "°C"
   final2 = "\n" + "Maximum Temperature: " + str(max_temperature) + "\n" + "Minimum Temperature: " + str(min_temperature) + "\n" + "Pressure: " +str(pressure) +"\n"+ "Humidity: "+str(humidity) +"\n"+"Wind Speed: "+str(wind)
   final3 = "\n"+"Sunrise: "+sunrise + "\n"+"Sunset: "+sunset

   #adding the styles i.e fonts
   label1.config(text = final1)
   label2.config(text = final2)
   label3.config(text = final3)


font1 = ("poppins",13,"bold") #font style
font2 = ("poppins", 25,"bold")
font3 = ("ds-digital",18,"bold")

text = tk.Entry(canva,justify='center', font = font2) #accepts single line words entered by the user
text.pack(pady = 20) #position 
text.focus() #focusing the canvas 
text.bind("<Return>",weather) #deals with the weather function

# creating a form like attributes
label1 = tk.Label(canva, font = font2)
label1.pack()
label2 = tk.Label(canva, font = font1)
label2.pack()
label3 = tk.Label(canva,font = font3)
label3.pack()

canva.mainloop()

