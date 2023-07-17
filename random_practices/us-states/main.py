import turtle
import pandas
from text_model import Text

# reading the data from the csv file w pandas
data = pandas.read_csv(r'.\random_practices\us-states\50_states.csv')

# preparing the screen + adding the image
screen = turtle.Screen()
screen.title('US States Guesser')
image = r'.\random_practices\us-states\blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states_num = int(len(data.state)) # number of all states
correct_answers = 0 # tracking the score
guessed_states = [] # list of guesses for the if-else condition later

# creating a loop that runs untill the guesses num is equal to the states num
while states_num != correct_answers:
    title = f'{correct_answers}/{states_num} States Correct' # dynamic title of input
    state_names = data.state.to_list() # getting list of all state names

    answer_state = screen.textinput(title=title, prompt='What is another states name?')
    text = Text() # creating an instance of text class (empty for now)
    
    # secret input to create a file with all the non-guessed states:
    if answer_state.lower().strip() == 'exit':
        states_to_learn = [state for state in state_names if state.lower() not in guessed_states]
        # for state in state_names:
        #   if state.lower().strip() not in guessed_states:
        #     states_to_learn.append(state)
        learn_data = pandas.DataFrame(states_to_learn)
        learn_data.to_csv('states_to_learn.csv')
        break

    if answer_state.lower().strip() not in guessed_states: # block duplications
        for state in state_names:
            if state.lower().strip() == answer_state.lower().strip():
                correct_answers += 1
                guessed_states.append(answer_state.lower().strip())
                
                data_row = data[data.state == state] # getting the specific data row
                x = data_row['x'].values[0] # extracting the coordinates
                y = data_row['y'].values[0]
                text.set_text(state, x, y) # calling the text method and sending all the data
                    
# just a nice code that tells you the coodrinates or each click:

# def get_mouse_click_coor(x, y):
#   print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()