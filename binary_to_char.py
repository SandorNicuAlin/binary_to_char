"""
01010011 01101111 00100000 01101001 01110100 00100000 01100010 01100101 01100111 01101001 01101110 01110011 00100000 00101110 00101110 00101110 00101110 00101110 00100000 01010100 01110010 01110101 01101101 01110000 00100000 00110010 00110000 00110010 00110100
"""

import dearpygui.dearpygui as dpg
import re

WIDTH = 854
HEIGHT = 480
APP_NAME = "Binary To Char"

dpg.create_context()
dpg.create_viewport(title=APP_NAME, width=WIDTH, height=HEIGHT)

def on_convert_handler():
    # get the input
    binary = dpg.get_value("binary")
    
    #validate input
    if not binary:
        return dpg.set_value('result', 'Please provide an input.')
    regex_pattern = '([0-1]{8}[ |\n]*)*'
    if not re.fullmatch(regex_pattern, binary):
        return dpg.set_value('result', 'Invalid input. Please provide only 8 digits values that contains 0s and 1s.\nSeparate the values by spaces or new lines (RETURN).')
    
    #split the binary codes into a list
    binary_list = re.split("[ |\n]+", binary)
    if "" in binary_list:
        binary_list.remove("")
        
    #convert every item in the list into a character and append them into a result string variable
    result = ""
    for data in binary_list:
        binary_data = int(data, 2)
        char_data = chr(binary_data)
        result += char_data
        
    #output the result
    dpg.set_value("result", result)

with dpg.window(label=APP_NAME, width=WIDTH, height=HEIGHT):
    dpg.add_input_text(tag="binary", multiline=True)
    dpg.add_button(label="Convert", callback=on_convert_handler)
    dpg.add_text(label="Result", tag="result")
    
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()