# GET BASIC INFORMATION ABOUT AN ATHLETE AND CREATE ATHLETE OBJECTS
# -------------------------------------------------------

# LIBRARIES AND MODULES
import kuntoilija
import questions



# Ask a question and convert the answer to float


# Enter information about an athlete
name = input('Anna nimesi: ')

# Ask details about him/her
question = questions.Question('Anna painosi (kg): ')
weight = question.ask_user_float(True)[0]
question = questions.Question('Anna pituutesi (cm): ')
height = question.ask_user_float(True)[0]
question = questions.Question('Anna ikäsi: ')
age = question.ask_user_integer(True)[0]
question = questions.Question('Sukupuoli: mies(1), nainen(0): ')
gender = question.ask_user_integer(True)[0]
question = questions.Question('Anna niskasi ympärysmitta: ')
neck = question.ask_user_float(True)[0]
question = questions.Question('Anna vyötärösi ympärysmitta: ')
waist = question.ask_user_float(True)[0]
if gender == 0:
    question = questions.Question('Lantiosi ympärysmitta: ')
    hips = question.ask_user_float(True)[0]

# Create an athlete object from Kuntoilija class
athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender)

#Print some information about the athlete
text_to_show = f'Terve {athlete.nimi}, painoindeksisi tänään on: {athlete.bmi}'
print(text_to_show)
fat_percentage = athlete.rasvaprosentti()
if gender == 1:
    usa_fat_percentage = athlete.usa_rasvaprosentti_mies(height, waist, neck)
else:
    usa_fat_percentage = athlete.usa_rasvaprosentti_nainen(height, waist, hips, neck)

text_to_show = f'Suomalainen rasva-% on {fat_percentage} ja amerikkalainen rasva-% on {usa_fat_percentage}'
print(text_to_show)