import random
from cv2 import threshold
import numpy as np
import flappy_bird
from IPython.display import clear_output
import help_functions
import sys
import keyboard 
from itertools import product
import pandas as pd
import os.path

df_states = help_functions.get_df_states()

#Wenn schon trainiert wurde, soll das entsprechende File geladen werden
#Falls nicht ein neues erstellt werden

file_exists = os.path.exists('trained_files/np_q_table.txt')
if file_exists: 
    np_q_table = np.loadtxt('trained_files/np_q_table.txt')
    print("load table")
else:
    np_q_table = help_functions.get_np_q_table(df_states) 

# Hyperparameters festlegen 
alpha = 0.1
gamma = 0.8
epsilon = 0.1

#Das Learning eine bestimmte Anzahl oft durchführen (hier 10000)
for i in range(1, 10000):
    epochs, reward = 0, 0
    done = False
    game_state = flappy_bird.FlappyBird()
    _, reward, done, pos = game_state.next_frame(0)
    state = help_functions.encode(pos[2], max(0, pos[0]), pos[1], df_states)
    while not done:
        
        #Beliebige Aktionen einstreuen 
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0,1)
        else:   
            if np_q_table[state][1] < np_q_table[state][2]:
                action = 1
            else: 
                action = 0

        _, reward, done, pos  = game_state.next_frame(action)
        
        next_state = help_functions.next_state(action, pos[2], max(0, pos[0]), pos[1], pos[3], df_states)
        old_value = np_q_table[state, action+1]
        next_max = max(np_q_table[next_state][2], np_q_table[next_state][1])
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        
        np_q_table[state, action+1] = new_value
        
        #print(f"New Value: {new_value}, Old Value: {old_value}, reward: {reward}, next_max: {next_max}, State: {state}, Next_State: {next_state}, action {action}")

        state = next_state
        epochs += 1
        if keyboard.is_pressed('Esc'):
            print("\nyou pressed Esc, so exiting...")
            np.savetxt('trained_files/np_q_table.txt', np_q_table)
            sys.exit(0)
    
    if keyboard.is_pressed('Esc'):
        np.savetxt('trained_files/np_q_table.txt', np_q_table)
        sys.exit(0)

np.savetxt('trained_files/np_q_table.txt', np_q_table)

