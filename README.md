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

### Edit

Durch das Anpassen der Reward Funktion konnte eine Verbesserung im Trainingsprozess erzielt werden. Hierbei wurden 0.2 Punkte für jeden Zug mehr vergeben, wenn sich der Vogel im mittleren Teil und nicht an den Rändern befand. Hierdurch wurde das Ursprüngliche Problem beseitigt. Jedoch ist auffällig, dass der Vogel trotz des besseren Trainingsprozesses weiterhin viele ZUstände lernen muss, und zwar mittiger fliegt, jedoch immernoch sehr selten durch die Rohre durchkommt. 

### User-Story
Eine direkte User-Story kann für dieses Projekt nicht verfasst werden, da es keine Anwendung im realen Umfeld für einen Nutzer gibt und es somit keinen Mehrwert bietet. Jedoch konnte in der Präsentation gezeigt werden, dass durch die Anwendung von Machine Learning Methoden bei verschiedenen Spielen wie Schach oder Go wichtige Erkenntnisse über die Technologie gewonnen werden konnten. Das führte beispielsweise dazu, dass in der Biologie nun anhand von künstlicher Intelligenz Proteinfaltungen ermittelt werden. Daher handelt es sich hierbei eher um ein Forschungsprojekt, um die neue Technologie zu verstehen und im weiteren Verlauf auf wichtige Anwendungen anzuwenden, die einen Mehrwert für die Menschheit bieten.

### Fazit zu Flappy Bird und Reinfocement Learning
Als Erkenntnis dieses explorativen Projektes lässt sich festhalten, dass bei unserer Vorgehensweise der Einsatz von Reinfocement Learning nur bedingt Sinn macht. Eine algorithmisch programmierte Lösung, die Flappy Bird spielt, ist dennoch effizienter. Spiele, die komplexer sind und dadurch größere Abhängigkeiten und Folgen von getätigten Entscheidungen besitzen, kommen für den Reinfocement Ansatz mehr in Frage. 

### Ausblick
Häufig fokusieren sich Projekte und Entwicklungen im Reinforcementbereich auf die Aufgabenstellung an sich. Dabei ist es sinnvoll, sich aus dem rein wirtschaftlichen Kontext zu lösen und Algorithmen und Modelle auch etwas spielerischer auszuprobieren. Die aus dem Gamingbereich entstandenen Erkenntnisse können dann auf andere Felder wieder angewendet werden (vgl. Alpha Fold).
Für die Zukunft dieses Projektes schlagen wir vor, die Reinfocementstrategie weiter zu verfolgen und mit mehr Ressourcen über einen längeren Zeitraum zu trainieren. Weitere Spiele mit mehr als 2 Aktionen, die beim Spielen getätigt werden müssen, können in diesem Kontext weiterhin sehr interessant sein. Vor allem der Übergang von hard gecodeten Spiellösungen zu KI-basierten ist höchstinteressant und sollte weiter untersucht werden.
