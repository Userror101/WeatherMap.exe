import pyowm # import module
from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

owm = pyowm.OWM('9837beed96baf69bfaa64cf456a1d42f', language = 'ru') # api + ru

print(Fore.BLACK) # module colorama
print(Back.GREEN) # module colorama

print('Для работы приложения, убедитесь что установлено интернет соединение!')

place = input('В каком городе хотите узнать погоду?: ')

try: # exceptions
    observation = owm.weather_at_place(place) # location indication
    w = observation.get_weather()
    temp = w.get_temperature('celsius')['temp'] # temperature centigrade

    print(Fore.BLACK) # module colorama
    print(Back.CYAN) # module colorama

    print('В городе ' + place + ' сейчас ' + w.get_detailed_status()) # conclusion
    print('Температура в районе ' + str(temp) + ' °C') # conclusion

    if temp < 10: # wishes

        print(Fore.BLACK) # module colorama
        print(Back.RED) # module colorama
 
        print('На улице холодно, стоит одеться тепло!')
    elif temp < 20: # wishes

        print(Fore.BLACK) # module colorama
        print(Back.MAGENTA) # module colorama

        print('На улице прохладно, одевайтесь теплее!')
    else: # wishes

        print(Fore.BLACK) # module colorama
        print(Back.YELLOW) # module colorama

        print('На улице хорошая погода, можно одеться легко!')


except pyowm.exceptions.api_response_error.NotFoundError: # exceptions

    print(Fore.BLACK) # module colorama
    print(Back.RED) # module colorama
    print('Вы ввели несуществующий город!')

input()