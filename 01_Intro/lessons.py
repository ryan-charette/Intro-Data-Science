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
