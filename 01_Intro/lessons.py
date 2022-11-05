# Lesson 3
libraries = ["NumPy", "SciPy", "Pandas", "Matplotlib", "Seaborn"]
completion = [100, 100, 96, 0, 0]

libraries.append("scikit-learn")
completion.append(0)

gradebook = list(zip(libraries, completion))

print("Lesson Completion Rates:")
print(gradebook)
print("\n")

# What's next?

# gradebook.append(("BeautifulSoup", 0))
# gradebook.append(("Tensorflow", 0))

# Lesson 4
import pandas as pd
import codecademylib3_seaborn

# Load data
df = pd.read_csv('page_visits.csv')

# Display data
print(df.head())

# Lesson 5
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

plt.title("Codecademy Learners Time Series")

plt.xlabel("Hour")
plt.ylabel("Viewers")

plt.plot(hour, viewers_hour)

plt.legend(['2015-01-01'])

ax = plt.subplot()

ax.set_facecolor('seashell')

ax.set_xticks(hour)
ax.set_yticks([0, 20, 40, 60, 80, 100, 120])

y_upper = [i + (i*0.15) for i in viewers_hour]
y_lower = [i - (i*0.15) for i in viewers_hour]

plt.fill_between(hour, y_lower, y_upper, alpha=0.2)

plt.show()

# Lesson 6

import random
#Simulate a room with a certain number of people
def simulate(num_people):
  birthdays = []
  print("Here's what our room looks like:\n")
  months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	#Assign a random birthday to each person
  for i in range(0, num_people):
    #Choose a random month
    month_choice = random.choice(months)
    #Choose a random day based on month
    if month_choice == "February":
      day = random.randint(1, 29)
    elif month_choice == "April" or month_choice == "June" or month_choice == "September" or month_choice == "November":
      day = random.randint(1, 30)
    else:
      day = random.randint(1, 31)
    birthday = month_choice + " " + str(day)
    #Store the birthday
    birthdays.append(birthday)
    print("Person {0}'s birthday: {1}".format(i + 1, birthday))
  calculate_probability(num_people)
  match = False
  #Check for matching birthdays
  for i in range(len(birthdays)):
    if find_duplicates(birthdays, birthdays[i], i):
      match = True
      break
  if not match:
    print("\n\nIn our simulation, no two people have the same birthday")

#Calculate the probability of there being 2 people with the same birthday
def calculate_probability(num_people):
  #Check there is at least 2 people in the room
  if num_people < 2:
    print("\n\nNot enough people in the room!")
    return
  else:
    #Calculate the probability
    numerator = 365
    countdown = 364
    for i in range(2, num_people + 1):
      numerator = numerator * countdown
      countdown -= 1
    denominator = 365 ** num_people
    probability = 1 - numerator/float(denominator)
    #Change probability to percentage
    rounded = round(probability*100, 2)
    print("\n\nThe probability that two people in a room of {0} people have the same birthday is nearly {1}%".format(num_people, rounded))

    
#Find the same birthday within our list of birthdays
def find_duplicates(birthdays_list, birthday, index):
  people = []
  for i in range(len(birthdays_list)):
    if birthdays_list[i] == birthday and i != index:
      people.append(i + 1)
  if people:
    people.append(index + 1)
    print("\n\nIn our simulation, the following people have the same birthdays: ")
    for person in people:
      print("Person {0}".format(person))
    return True
  else:
    return False
  
def main():  
  num_people_in_room = 2 			#Change This Number (keep it smaller than 100 to save processing power)

  simulate(num_people_in_room) 
main()
