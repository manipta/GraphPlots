import matplotlib.pyplot as plt
import csv
#Extracting Data
years=['2017','2018','2019','2020','2021','2022','2023']
deaths={
    i:[0 for j in range(1,55)] for i in years
}
with open('covid_deaths.csv','r') as file:
    next(file)
    csvreader=csv.reader(file,delimiter=";")
    for each in csvreader:
        y=each[1].split("-")[0]
        w=int(each[1].split("-")[1])
        deaths[y][w]=float(each[6])
    
#plotting
weeks=[i for i in range(1,55)]
for i in years:
    plt.plot(weeks,deaths[i],label=i)
plt.legend()
plt.title("Excess Deaths in Europe\n")
plt.xlabel("week")
plt.xlabel("Death Count")
plt.xticks([i for i in range(0,55,5)])
plt.savefig("CovidDeathsEurope.png")
plt.show()

# Source: https://www.euromomo.eu/graphs-and-maps