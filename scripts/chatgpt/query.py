from chatgpt_wrapper import ChatGPT
from text2audio import text_to_audio

bot = ChatGPT()
# response = bot.ask("Hello, world!")
response = bot.ask("Imagine we are working with a household robot. The job of this robot is to make an omelette. The objects available around are: fridge, bowl, pan, oil, stove The main functions you can use are: locate_object(object_name): Returns the XYZ coordinates of an object of interest. go_to_location(object_name): Moves robot to a location specified by XYZ coordinates. Returns nothing. pick_up(object_name): Picks up the object of interest. Returns nothing. use_item(object_name): Takes the name of an object as input. Performs an appropriate action on the object at hand (pour oil, crack eggs). Returns nothing. Can you make use of these to write code to go to the kitchen and make an omelette? Try to use these low level functions to construct more high level behaviors and then solve the task using those high level primitives.")

# Open a file for writing
with open('test.txt', 'w') as f:
    # Write a string to the file
    f.write(response)

print(response)  # prints the response from chatGPT

text_to_audio(response)  # converts the response to audio and plays it