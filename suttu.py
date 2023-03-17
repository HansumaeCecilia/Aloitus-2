# Esimerkkejä päivämäärien, tiedostojen ja JSON-tiedostojen käytöstä

import datetime

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
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

ero = datediff('2023-03-17', '2023-01-20')
print(ero)