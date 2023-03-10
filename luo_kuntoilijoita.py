# GET BASIC INFORMATION ABOUT AN ATHLETE AND CREATE ATHLETE OBJECTS
# -------------------------------------------------------

# LIBRARIES AND MODULES
import kuntoilija
import questions



# Ask a question and convert the answer to float


# Enter information about an athlete
nimi = input('Nimi: ')

# Ask details about him/her
question1 = questions.Question('Kuinka paljon painat (kg): ')
weight = question1.ask_user_float(True)
question2 = questions.Question('Kuinka pitkä olet (cm): ')
height = question2.ask_user_float(True)
question3 = questions.Question('Minkä ikäinen olet: ')
age = question3 = question3.ask_user_integer(True)
question4 = questions.Question('Sukupuoli: mies(1), nainen(0): ')
gender = question4.ask_user_integer(True)
question5 = questions.Question('Niskasi ympärysmitta: ')
neck = question5.ask_user_float(True)
question6 = questions.Question('Vyötärösi ympärysmitta: ')
waist = question6.ask_user_float(True)
question7 = questions.Question('Lantiosi ympärysmitta: ')
hips = question7.ask_user_float(True)