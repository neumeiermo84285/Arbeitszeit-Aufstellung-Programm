from datetime import datetime, timedelta

def generate_work_schedule(name, s_date, e_date, s_time, e_time, selected_weekdays, file_path):
    # Startdatum und Enddatum für das Jahr 2023
    start_date = datetime(int(s_date.split(".")[2]), int(s_date.split(".")[1]), int(s_date.split(".")[0]))
    end_date = datetime(int(e_date.split(".")[2]), int(e_date.split(".")[1]), int(e_date.split(".")[0])) 

    day_amp = {"0": "Montag", "1": "Dienstag", "2": "Mittwoch", "3": "Donnerstag", "4": "Freitag", "5": "Samstag", "6": "Sonntag"}
    arbeitsage = "" 
    for day in selected_weekdays:
        arbeitsage += day_amp[str(day)] + ", "

    # Erzeuge den vollständigen Dateipfad
    file_name = f"Arbeitszeittabelle_{name}_{start_date.year}.csv"
    full_file_path = f"{file_path}/{file_name}"

    # Öffne eine Textdatei zum Schreiben
    with open(full_file_path, "w") as file:
        # Schreibe die Kopfzeile
        file.write(f"Name: {name}\n\n")
        file.write(f"Arbeitstage {arbeitsage}\n\n")
        file.write("Datum;Uhrzeit – Beginn;Uhrzeit – Ende;Arbeitszeit in Stunden\n")

        # Schreibe die Arbeitszeiten für die ausgewählten Wochentage im angegebenen Zeitraum
        current_date = start_date
        while current_date <= end_date:
            if current_date.weekday() in selected_weekdays:
                start_time = current_date.replace(hour=int(s_time.split(":")[0]), minute=int(s_time.split(":")[1]))
                end_time = current_date.replace(hour=int(e_time.split(":")[0]), minute=int(e_time.split(":")[1]))
                work_hours = (end_time - start_time).seconds / 3600

                # Schreibe die Zeile in die Datei
                file.write(f"{current_date.strftime('%d.%m.%Y')};{start_time.strftime('%H:%M')};{end_time.strftime('%H:%M')};{work_hours:.1f}\n")

            # Gehe zum nächsten Tag
            current_date += timedelta(days=1)

if __name__ == "__main__":
    # Frage nach dem Namen
    name = input("Bitte geben Sie Ihren Namen ein: ")

    # Frage name start Datum
    start_date = input("Bitte geben Sie das Startdatum ein (Format: DD.MM.JJJJ --> z.B.: 1.1.2023): ")
    # Frage nach end Datum
    end_date = input("Bitte geben Sie das Enddatum ein (Format: DD.MM.JJJJ --> z.B.: 31.12.2023): ")

    #Frage nach startzeit Arbeitszeit
    start_time = input("Bitte geben Sie die Arbeits-Startzeit ein (Format: HH:MM --> z.B.: 10:00): ")
    end_time =  input("Bitte geben Sie die Arbeits-Endzeit ein (Format: HH:MM --> z.B.: 11:30): ")

    # Frage nach den ausgewählten Wochentagen
    weekdays_input = input("Bitte geben Sie die ausgewählten Wochentage ein (Komma getrennt, 0 für Montag, 1 für Dienstag, usw.): ")
    selected_weekdays = [int(day) for day in weekdays_input.split(',')]

    # Frage nach dem Speicherpfad für die Datei
    file_path = input("Bitte geben Sie den Speicherpfad für die Datei ein: ")

    # Generiere die Arbeitszeittabelle mit dem eingegebenen Namen und Pfad
    generate_work_schedule(name, start_date, end_date, start_time, end_time, selected_weekdays, file_path)

    print(f"Arbeitszeittabelle wurde erfolgreich erstellt für {name} und gespeichert unter {file_path}.")
