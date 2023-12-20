
# greet:

  Die Methode beginnt damit, den Benutzer mit der freundlichen Frage "Hello, do you need help or just want to speak?" zu begrüßen.
  Sie wartet auf die Benutzerantwort durch die input-Funktion.
  Anschließend ruft sie die Methode greet_answer mit der Benutzerantwort als Argument auf, um auf die Benutzerantwort zu reagieren und weitere Schritte einzuleiten.

# can_help:

  Diese Methode überprüft, ob der Benutzer weiteren Hilfebedarf hat.
  Standardmäßig wird die Frage "Can I help you with something else?" gestellt, aber es kann auch eine benutzerdefinierte Frage übergeben werden.
  Sie ruft die Methode confirm auf, um die Benutzerantwort zu überprüfen.
  Abhängig von der Benutzerantwort wird entweder erneut die Begrüßung (greet_answer) angezeigt oder eine Unterhaltung gestartet (speak).

# confirm:

  Diese Methode nimmt eine benutzerdefinierte Frage entgegen und erwartet eine einfache Bestätigung ("yes" oder "no").
  Die Benutzerantwort wird über die input-Funktion eingelesen und in Kleinbuchstaben umgewandelt.
  Es wird überprüft, ob die Antwort eine positive oder negative Bestätigung ist.
  Falls die Antwort ungültig ist, wird eine entsprechende Meldung ausgegeben, und die Methode wird rekursiv aufgerufen, um eine gültige Antwort zu erhalten.

# greet_answer:

  Diese Methode analysiert die Benutzerantwort auf Schlüsselwörter wie "speak" oder "help".
  Wenn das Schlüsselwort "speak" erkannt wird, ruft sie die Methode speak auf, um eine Unterhaltung zu beginnen.
  Wenn das Schlüsselwort "help" erkannt wird, werden Informationen zu verfügbaren Themen angezeigt. Der Benutzer wird aufgefordert, ein Thema auszuwählen, und es wird die entsprechende mathematische Operation  durchgeführt.
  Nach der Verarbeitung wird die Methode can_help aufgerufen, um festzustellen, ob der Benutzer weiteren Hilfebedarf hat.

# speak:

  Die Methode fordert den Benutzer mit einer standardmäßigen Frage ("then I want to know how do you feel") auf.
  Die Benutzerantwort wird über die input-Funktion eingelesen.
  Anschließend wird die Methode update_intent aufgerufen, um die Benutzerantwort zu analysieren und die Intention zu aktualisieren.
  Dann ruft sie die Methode get_response auf, um eine Antwort auf die Benutzerantwort zu erhalten.
  Schließlich wird die Methode speak rekursiv aufgerufen, um die erhaltenen Chat-Antworten anzuzeigen und eine neue Benutzerantwort zu erhalten.

# get_response:

  Diese Methode nimmt die Benutzerantwort als Eingabe und durchläuft die in der Datei "intents.json" definierten Intents.
  Sie überprüft, ob eines der Muster (patterns) in der Benutzerantwort enthalten ist.
  Wenn ein passendes Intent gefunden wird, wird eine zufällige Antwort aus den vordefinierten Antworten zurückgegeben.

# update_intent:

  Die Methode durchsucht die vorhandenen Intents in der Datei "intents.json" nach Ähnlichkeiten zwischen den Benutzereingaben und den Intent-Patterns.
  Wenn eine Ähnlichkeit gefunden wird, wird die Intention aktualisiert, und die Benutzerantwort wird zurückgegeben.
  Wenn keine Übereinstimmung gefunden wird, wird der Benutzer nach seiner Hilfe gefragt, um eine neue Intention hinzuzufügen.
  Falls der Benutzer zustimmt, wird ein neues Intent-Objekt erstellt und zur Liste der Intents hinzugefügt. Die Änderungen werden in der Datei "intents.json" gespeichert.

# write_to_intents:

  Die Methode schreibt die aktualisierten Intent-Daten in die Datei "intents.json".
  Falls erforderlich, wird auch eine neue Intention hinzugefügt.
  Die Datei wird mit der json.dump-Funktion aktualisiert, um die Änderungen zu speichern.

# Wo Sie noch Fragen haben können

  json.dump() - https://www.geeksforgeeks.org/json-dump-in-python/

  open() - https://www.w3schools.com/python/ref_func_open.asp

  enumerate() - https://www.w3schools.com/python/ref_func_enumerate.asp

  any() - https://www.geeksforgeeks.org/python-any-function/

