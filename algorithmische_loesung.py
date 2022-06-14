import flappy_bird
import time

#Spiel erstellen 
game_state = flappy_bird.FlappyBird()

#Nach welcher Zeit soll das Spiel wieder aufhören?
end_time = time.time() + 200

#Das Spiel starten und die Position abfragen
_, _, _, pos = game_state.next_frame(0)

while time.time() < end_time:
    # Wenn der Vogel (pos[2]) höher ist (< aufgrund verdrehter Skala), dann nichts machen (0)
    if(pos[2] + 40 < pos[1]):
        _, _, _, pos = game_state.next_frame(0) 
    # Sonst ist der Vogel zu niedrig und muss hoch (1)
    else:
        _, _, _, pos = game_state.next_frame(1)

