# Vergel, Chean Bernard Villanueva
# Fan Class

from fan_greetings import Greeting
from fan_outputs import Outputs
from fan_user_interface import User_interface

greeting = Greeting()
ui = User_interface()
fan = Outputs()

greeting.print_welcome_message()

while True: 
    choice = ui.get_user_choice()
    if choice.upper() == "A":
        fan.runfan1_test()
    elif choice.upper() == "B":
        fan.runfan2_test()
    else:
        print("\U0001F6A7 \033[31mINVALID INPUT!\033[0m\U0001F6A7")
    if not ui.continue_calculation():
        print("\033[32mI hope this program helps and satisfy you.\033[0m")
        break
greeting.print_goodbye_message()

