import pandas as pd
from itertools import product

# Funktion um die Zahl für jeden Zustand anzugeben 
def encode(vogel_hoehe, abstand, pipe_hoehe, df_states): 
    sol = df_states.loc[(df_states.vogel_hoehe ==vogel_hoehe) & (df_states.abstand == abstand) & (df_states.pipe_hoehe == pipe_hoehe)]
    return sol.iloc[0]["state"]

# Funktion um den nächste Zustand (State) anzugeben 
def next_state(action, vogel_hoehe, abstand, pipe_hoehe, current_velocity_y, df_states):
    if action == 1:
        current_velocity_y = -9
           
    elif current_velocity_y < 10 and not action:
            current_velocity_y += 1
    vogel_hoehe+= min(current_velocity_y, vogel_hoehe - current_velocity_y - 24)
    if vogel_hoehe < 0:
        vogel_hoehe = 0
    new_abstand = abstand - 4
    new_pipe_hoehe = pipe_hoehe
    state = encode(vogel_hoehe, max(0,new_abstand), new_pipe_hoehe, df_states)
    return state

# Dataframe erstellen, in dem jedem möglichen Zustand(state) eine Zahl zugeordnet wird 
def get_df_states():
    vogel = list(range(0, 400))  #=> 380
    abstand = list(range(0, 292, 4))      #=> 72
    y_lowerpipe = list(range(200, 280, 10)) #=> 7
    values = [vogel, abstand, y_lowerpipe]
    states = []

    for pair in product(*values):
        states.append(pair)

    df_states = pd.DataFrame(states)
    df_states ["state"] = df_states.index
    df_states.columns = ["vogel_hoehe", "abstand", "pipe_hoehe", "state"]
    return df_states 

# Ein Q-Table in Form eines numpy arrays erstellen 
def get_np_q_table(df_states):
    q_table = pd.DataFrame() 
    q_table["state"] = df_states ["state"]
    q_table["nothing"] = 0.0
    q_table["press"] = 0.0
    np_q_table = q_table.to_numpy()
    return np_q_table
