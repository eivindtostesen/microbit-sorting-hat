def on_button_pressed_a():
    global counter
    if mode == "ceremony":
        for seat in history:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                """)
            basic.show_string("" + (seat))
            basic.pause(700)
        basic.clear_screen()
    elif mode == "settings":
        if seat2 == "G":
            seat2 = "S"
            basic.show_string("S")
        elif seat2 == "S":
            seat2 = "H"
            basic.show_string("H")
        elif seat2 == "H":
            seat2 = "R"
            basic.show_string("R")
        elif seat2 == "R":
            seat2 = "G"
            basic.show_string("G")
        counter = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def think_and_decide():
    for index2 in range(2):
        basic.show_leds("""
            . . . . .
            . # . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . # .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . # .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . # . . .
            . . . . .
            """)
    basic.show_string("" + (seat2))
    basic.pause(2000)
    basic.clear_screen()

def on_gesture_shake():
    global index, seat2
    if mode == "ceremony":
        if len(available) == 0:
            basic.show_icon(IconNames.YES)
        else:
            index = randint(0, len(available) - 1)
            seat2 = available[index]
            think_and_decide()
            if available.remove_at(index):
                history.append(seat2)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global mode
    if mode == "settings":
        mode = "ceremony"
        basic.show_icon(IconNames.TRIANGLE)
    else:
        mode = "settings"
        basic.show_icon(IconNames.SQUARE)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global counter
    if mode == "ceremony":
        basic.show_string("" + (seat2))
        basic.pause(500)
        basic.clear_screen()
    elif mode == "settings":
        counter += 1
        basic.show_number(counter)
        available.append(seat2)
input.on_button_pressed(Button.B, on_button_pressed_b)

index = 0
counter = 0
seat2 = ""
mode = ""
history: List[str] = []
available: List[str] = []
available = []
history = []
mode = "settings"
seat2 = "G"
basic.show_string("G")
