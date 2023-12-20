# themes:

Diese Methode fordert den Benutzer auf, eine mathematische Operation auszuwählen (Addition, Subtraktion, Division, Multiplikation oder Wahrscheinlichkeit).
Die ausgewählte Operation wird als Zeichenkette zurückgegeben.

# list_of_ints:

Diese Methode fordert den Benutzer auf, mindestens zwei Zahlen einzugeben, die durch Leerzeichen getrennt sind.
Die eingegebenen Zeichenketten werden in eine Liste von Ganzzahlen konvertiert, und nur gültige Ganzzahlen werden in der Liste berücksichtigt.

# chooseOperation:

Diese Methode nimmt das ausgewählte Thema als Argument entgegen und ruft dann die entsprechende mathematische Operation auf, abhängig von der ausgewählten Option.
Je nach ausgewähltem Thema werden die entsprechenden Methoden wie add, subtruct, divide, multiply oder probability aufgerufen.
Das Ergebnis der Operation wird zurückgegeben.

# Mathematische Operationen (add, subtruct, multiply, divide):

Diese Methoden führen die grundlegenden mathematischen Operationen auf einer Liste von Zahlen durch, indem sie die reduce-Funktion und die entsprechenden Operatoren (__add__, __sub__, __mul__, __truediv__) verwenden.

# probability:

Diese Methode ist derzeit nicht implementiert (#not done). Es gibt jedoch einen Platzhalter, der für zukünftige Implementierungen von Wahrscheinlichkeitsberechnungen vorgesehen ist.

# Hauptprogramm:

Der Benutzer wird aufgefordert, eine mathematische Operation auszuwählen und dann die erforderlichen Zahlen einzugeben.
Das Programm ruft die entsprechende Methode auf und gibt das Ergebnis aus.