import turtle
import pandas
from text_model import Text

data = pandas.read_csv(r'.\random_practices\us-states\50_states.csv')
print(data.columns)

screen = turtle.Screen()
screen.title('US States Guesser')
image = r'.\random_practices\us-states\blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states_num = int(len(data.state))
correct_answers = 0
guessed_states = []

while states_num != correct_answers:
    title = f'{correct_answers}/{states_num} States Correct'
    state_names = data.state.to_list()

    answer_state = screen.textinput(title=title, prompt='What is another states name?')
    text = Text()

    if answer_state.lower().strip() not in guessed_states:
        for state in state_names:
            if state.lower().strip() == answer_state.lower().strip():
                correct_answers += 1
                guessed_states.append(answer_state.lower().strip())
                print(guessed_states)
                
                data_row = data[data.state == state]
                x = data_row['x'].values[0]
                y = data_row['y'].values[0]
                text.set_text(state, x, y)
                
# just a nice code that tells you the coodrinates or each click:
# def get_mouse_click_coor(x, y):
#   print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()