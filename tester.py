import matplotlib.pyplot as plt
import numpy as np

file = open("/Users/jerryxia/Downloads/data.csv", "r")
line = file.readline().strip().split(",")
stats_gender = {"f": 0, "m": 0, "x": 0}

while line != [""]:
    gender = line[3]
    stats_gender[gender] += 1
    line = file.readline().strip().split(",")

print(stats_gender)

plt.bar(['f','m','x'], list(stats_gender.values()))
plt.title('COVID 19 Vax Data')
plt.xlabel('Gender')
plt.ylabel('Number of vaccines')
plt.show()

file.close()