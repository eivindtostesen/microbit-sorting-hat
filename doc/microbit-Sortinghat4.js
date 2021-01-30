input.onButtonPressed(Button.A, function () {
    if (mode == "ceremony") {
        for (let seat of history) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                `)
            basic.showString("" + (seat))
            basic.pause(700)
        }
        basic.clearScreen()
    } else if (mode == "settings") {
        if (seat == "G") {
            seat = "S"
            basic.showString("S")
        } else if (seat == "S") {
            seat = "H"
            basic.showString("H")
        } else if (seat == "H") {
            seat = "R"
            basic.showString("R")
        } else if (seat == "R") {
            seat = "G"
            basic.showString("G")
        }
        counter = 0
    }
})
function think_and_decide () {
    for (let index2 = 0; index2 < 2; index2++) {
        basic.showLeds(`
            . . . . .
            . # . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . # .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . # .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . # . . .
            . . . . .
            `)
    }
    basic.showString("" + (seat))
    basic.pause(2000)
    basic.clearScreen()
}
input.onGesture(Gesture.Shake, function () {
    if (mode == "ceremony") {
        if (available.length == 0) {
            basic.showIcon(IconNames.Yes)
        } else {
            index = randint(0, available.length - 1)
            seat = available[index]
            think_and_decide()
            if (available.removeAt(index)) {
                history.push(seat)
            }
        }
    }
})
input.onButtonPressed(Button.AB, function () {
    if (mode == "settings") {
        mode = "ceremony"
        basic.showIcon(IconNames.Triangle)
    } else {
        mode = "settings"
        basic.showIcon(IconNames.Square)
    }
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    if (mode == "ceremony") {
        basic.showString("" + (seat))
        basic.pause(500)
        basic.clearScreen()
    } else if (mode == "settings") {
        counter += 1
        basic.showNumber(counter)
        available.push(seat)
    }
})
let index = 0
let counter = 0
let seat = ""
let mode = ""
let history: string[] = []
let available: string[] = []
available = []
history = []
mode = "settings"
seat = "G"
basic.showString("G")

