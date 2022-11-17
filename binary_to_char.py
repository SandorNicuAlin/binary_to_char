import dearpygui.dearpygui as dpg

WIDTH = 600
HEIGHT = 300
APP_NAME = "Binary To Char"

dpg.create_context()
dpg.create_viewport(title=APP_NAME, width=WIDTH, height=HEIGHT)

def on_convert_handler(sender, app_data):
    print(app_data)

with dpg.window(label=APP_NAME, width=WIDTH, height=HEIGHT):
    dpg.add_input_text(label="Binary")
    dpg.add_button(label="Convert", callback=on_convert_handler)
    dpg.add_text()
    
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()