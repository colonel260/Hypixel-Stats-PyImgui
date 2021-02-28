from dearpygui import core, simple


core.set_main_window_size(500, 500)
with simple.window("Hypixel Stats"):
    core.add_input_text("Player name", hint="Player name")
    core.add_checkbox("Sample Settings")
    core.add_checkbox("Sample Settings1")
    core.add_checkbox("Sample Settings2")
    core.add_checkbox("Sample Settings3")
    core.add_checkbox("Sample Settings4")
    core.add_checkbox("Sample Settings5")

core.start_dearpygui(primary_window="Hypixel Stats")
