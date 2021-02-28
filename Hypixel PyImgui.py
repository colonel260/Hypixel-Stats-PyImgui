from dearpygui import core, simple


def Settings(sender, callback):
    Stats = ("Imagine that this is " +
             core.get_value("Player name") + "'s stats")
    core.add_input_text("Stats", readonly=True, multiline=True,
                        default_value=Stats, parent="Hypixel Stats")


core.set_main_window_size(500, 500)
core.set_main_window_title("Hypixel Stats")
core.set_style_frame_rounding(4)
with simple.window("Hypixel Stats"):
    core.add_input_text("Player name", hint="Player name")
    core.add_checkbox("Sample Settings")
    core.add_checkbox("Sample Settings1")
    core.add_checkbox("Sample Settings2")
    core.add_checkbox("Sample Settings3")
    core.add_checkbox("Sample Settings4")
    core.add_checkbox("Sample Settings5")
    core.add_spacing(count=20)
    core.add_button("Lookup", callback=Settings, width=140, height=25)

core.start_dearpygui(primary_window="Hypixel Stats")
