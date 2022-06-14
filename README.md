# FlappyBird_Abgabe
Diese Abgabe verfolgt das Ziel, tieferes Verständnis über das Reinforcement-Learning zu erhalten. 
Hierzu wurde sich zum Ziel gesetzt, das Spiel Flappy Bird dem Computer beizubringen. 

Die Datei flappy_bird.py enthält das Spiel an sich und wurde in folgenden GitHub Repo erstellt.
https://github.com/uvipen/Flappy-bird-deep-Q-learning-pytorch/blob/master/src/flappy_bird.py

Darauf aufbauend wurde die Datei algorithmische_loesung.py implementiert. Hierbei wird dem Vogel explizit gesagt, wann er welche Aktion durchführen soll. 
Diese Datei ist ausführbar und zeigt den Vogel wie er meist durch die Rohren fliegt. 

Die Datei reinforcement_loesung.py implementiert den Q-Learning Algorithmus, sodass das Programm sich das Spiel selbst beibringt. 
Hierzu wird die Datei help_fuctions.py benötigt, welche wichtige Methoden aus Übersichtlichkeitsgründen ausgelagert hat.
reinforcement_loesung.py ist ebenfalls ausführbar und zeigt den Vogel beim lernen. 

Der Lernfortschritt wir im Ordner trained_files gespeichert. Hier ist eine Datei nach 10000 Trainings und eine mit wenigen Trainings vorhanden. 
Welche für das Programm verwendet werden soll kann durch die Änderung des Paths in reinforcement_loesung.py angegeben werden.      
