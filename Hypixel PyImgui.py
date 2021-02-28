from dearpygui import core, simple


def save_callback(sender, data):
    print('Settings are still in developpement and not available.')


with simple.window("Hypixel Stats", width=500, height=500):
    core.add_checkbox("Settings", callback=save_callback)
    core.add_input_text("Player name", hint="Player name")

core.start_dearpygui(primary_window="Hypixel Stats")
