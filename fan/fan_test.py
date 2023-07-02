# Vergel, Chean Bernard Villanueva
# Fan Class

from fan_greetings import Greeting
from fan_main import Fan
from fan_user_interface import User_interface

greeting = Greeting()
ui = User_interface()
fan = Fan()

greeting.print_welcome_message()

while True: 
    choice = ui.get_user_choice()
    if choice.upper() == "A":
        fan.runfan1()
    elif choice.upper() == "B":
        fan.runfan2() 
    if not ui.continue_calculation():
        print("\033[32mI hope this program helps and satisfy you.\033[0m")
        break
    else:
        print("\U0001F6A7 \033[31mINVALID INPUT!\033[0m\U0001F6A7")

greeting.print_goodbye_message()

