import pyowm # import module
from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

owm = pyowm.OWM("9837beed96baf69bfaa64cf456a1d42f", language = "ru") # api + ru

print(Fore.BLACK) # module colorama
print(Back.GREEN) # module colorama

print("For the application to work, make sure you have an Internet connection!")

place = input("In which city do you want to know the weather?: ")

try: # exceptions
    observation = owm.weather_at_place(place) # location indication
    w = observation.get_weather()
    temp = w.get_temperature("celsius")["temp"] # temperature centigrade

    print(Fore.BLACK) # module colorama
    print(Back.CYAN) # module colorama

    print("In the city " + place + " now " + w.get_detailed_status()) # conclusion
    print("Temperature in the area " + str(temp) + " °C") # conclusion

    if temp < 10: # wishes

        print(Fore.BLACK) # module colorama
        print(Back.RED) # module colorama
 
        print("It's cold outside, you should dress warmly!")
    elif temp < 20: # wishes

        print(Fore.BLACK) # module colorama
        print(Back.MAGENTA) # module colorama

        print("It's cool outside, dress warmer!")
    else: # wishes

        print(Fore.BLACK) # module colorama
        print(Back.YELLOW) # module colorama

        print("The weather is good outside, you can dress easily!")


except pyowm.exceptions.api_response_error.NotFoundError: # exceptions

    print(Fore.BLACK) # module colorama
    print(Back.RED) # module colorama
    print("You have entered a city that does not exist!")

input()
