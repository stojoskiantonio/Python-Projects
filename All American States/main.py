import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
correct = 0
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
guessedStates = []

t = turtle.Turtle()
t.hideturtle()
t.penup()
turtle.shape(img)

while correct != 50:
    answerState = screen.textinput(title=f"States correct {correct}/50", prompt="Which state are you guessing?").title()
    if answerState == "Exit":
        break

    if answerState in states:
        if answerState not in guessedStates:
            correct += 1
            stateData = data[data.state == answerState]
            guessedStates.append(answerState)
            t.goto(stateData.x.item(), stateData.y.item())
            t.write(answerState)

notGuessedStates = []
for state in states:
    if state not in guessedStates:
        notGuessedStates.append(state)
new_data = pandas.DataFrame(notGuessedStates)
new_data.to_csv("States To Learn.csv")
def getMouseClick(x, y):
    print(x, y)

print(f"States that you missed are {notGuessedStates}")

turtle.onscreenclick(getMouseClick)

turtle.mainloop()
