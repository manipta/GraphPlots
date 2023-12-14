import matplotlib.pyplot as plt
import csv
labels=[]
values=[]
with open('vaccine.csv','r') as file:
    next(file)
    csvreader=csv.reader(file,delimiter=";")
    for each in csvreader:
        if 4==csvreader.line_num:
            break
        labels.append(each[0])
        values.append(each[1])
    print(labels)
    print(values)
plt.pie(values,labels=labels,shadow=True,autopct='%.2f',explode=[0,0.25,0])
plt.title("Covid Vaccine Fear Among People(in India)")
plt.legend(title="People's Response",bbox_to_anchor=(1,1))
plt.show()

# Source: https://www.cureus.com/articles/192893-quantification-of-covid-19-vaccine-coercion-in-india-a-survey-study#!/media