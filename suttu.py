# Esimerkkejä päivämäärien, tiedostojen ja JSON-tiedostojen käytöstä

import datetime # Sisäänrakennettu kirjasto aikamääreille
import json # Sisäänrakennettu kirjasto JSON-objektien käsittelyä varten

# Päiväyksen muodostaminen

year = 2023
month = 2
day = 17

date = datetime.datetime(year, month, day)
print(date)

# Ajantasaisen päiväyksen ja kellonajan muodostaminen

just_now = datetime.datetime.now()
print(just_now)

# Aikaero päiväyksien välillä (ajantasaisen ajan mukaan)

difference = just_now - date
print(difference)

# Aikaero päiväyksien välillä (erikseen valitut päivämäärät)

def datediff(d1, d2):
    """Calculates the difference between two time values

    Args:
        d1 (str): time value in format yy-mm-dd
        d2 (str): time value in format yy-mm-dd

    Returns:
        float: time difference in years
    """
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    difference = abs((d2 - d1).days)
    return difference

ero = datediff('2023-03-17', '2023-01-20')
print(ero)

def timediff(t1, t2):
    """Calculates the difference between two time values

    Args:
        t1 (str): time value in format hh:mm:ss
        t2 (str): time value in format hh:mm:ss

    Returns:
        float: time difference in hours
    """
    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")
    seconds = abs((t2 - t1).seconds) # Vain sekunnit ja mikrosekunnit on tuettu timedeltassa
    hours = seconds / 3600
    return hours

kesto = timediff('10:00:00', '14:30:00')
print(kesto)

# Määritellään Python-sanakirja
jumppari = {'nimi': 'Erkki', 'Pituus': 171, 'Paino': 75.5}
jumppari2 = {'nimi': 'Aapo', 'Pituus': 180, 'Paino': 74.5}

# Luodaan JSON-merkkijono (objekti)
json_jumppari = json.dumps(jumppari)
print(jumppari)

# Luodaan tiedosto
file_to_use = open('kuntoilijat.json', 'x')
file_to_use.close() # Muista aina sulkea tiedosto operaation jälkeen

# Kirjoitetaan tiedostoon JSON-objekti
file_to_use = open('kuntoilijat.json','w')
json.dump(jumppari, file_to_use) # Muutetaan sanakirja JSON-muotoon ja tallennetaan
file_to_use.close() # Jälleen suljetaan tiedosto operaation jälkeen

# Luetaan JSON-objekti tiedostosta
file_to_use = open('kuntoilijat.json', 'r')
data = json.load(file_to_use)
file_to_use.close()
print(data)

# # Lisätään toinen JSON-objekti tiedoston loppuun
# file_to_use = open('kuntolijat.json', 'a')
# json.dump(jumppari2, file_to_use)
# file_to_use.close()