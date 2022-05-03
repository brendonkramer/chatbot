#######################################################################################################################
# File: bot_engine.py
#
#######################################################################################################################

#imports
import threading
import time

from AIChatBot.bot import Bot
from numpy import *
import sys

user_input = []

def handle_input():
    time.sleep(2)
    while not user_input:
        time.sleep(2)

    ai.parse(user_input)

    # clear input array
    user_input.clear()

if __name__ == '__main__':
    name = "bot"
    if size(sys.argv) > 1:
        name = sys.argv[1]
    ai = Bot(str(name))

    bot_handle_input_thread = threading.Thread(target=handle_input)
    bot_handle_input_thread.daemon = True
    while True:
        user_input.append(input())
        if(bot_handle_input_thread.isAlive()):
            bot_handle_input_thread.exit()
            bot_handle_input_thread.run()