import matplotlib.pyplot as plt
import csv

male=[]
female=[]
total=[]
year_start=[]
year_end=[]
interval=int(input("Enter Interval Size You Want?\nHint:(like for 1950-1959 it's 10)\n"))
labeling_opt=int(input("Labeling Format?\n1.Intevals(1950-1960) 2.Absolute(1950)\n"))
data_opt=input("Wanna print data as well?(y/n)\n")
save_opt=input("Wanna save the bargraph as well?(y/n)\n")
complete_interval=True
with open('germany_birth.csv','r') as file:
    csvreader=csv.reader(file,delimiter=';')
    # below are temp vals for making intervals
    m=0
    f=0
    t=0
    c=0
    ys=""
    ye=""
    for each in csvreader:
        if c==0:
            ys=int(each[0])
        m+=int(each[1])
        f+=int(each[2])
        t+=int(each[3])
        ye=each[0]
        c=c+1
        if c==interval:
            male.append(m)
            female.append(f)
            total.append(t)
            year_start.append(ys)
            year_end.append(ye)
            c=0
            m=0
            f=0
            t=0
    if c!=0:
        male.append(m)
        female.append(f)
        total.append(t)
        year_start.append(ys)
        year_end.append(ye)
        complete_interval=False
    if(data_opt=="y"):
        print("---------------------------------")
        print("MALE:")
        print(male)
        print("FEMALE:")
        print(female)
        print("TOTAL:")
        print(total)
        print("YEAR START:")
        print(year_start)
        print("YEAR END:")
        print(year_end)
        print("---------------------------------")
    if ~complete_interval:
        print("Last interval is not complete!")
        print("Ends at "+ ye)
# Plotting
if labeling_opt==1:
    years=[str(year_start[i])+"-"+str(year_end[i]) for i in range(0,len(year_end))]
else:
    years=year_start
total=[i/1000000 for i in total]
upper_limit=round(max(total))+1

plt.bar(years,total,color="red")
plt.title("Germany Birth-Rate Declines")
plt.xticks(years)
plt.yticks(range(0,upper_limit,1))
plt.xlabel("Time\n(in Years)")
plt.ylabel("Count\n(in Millions)")
if save_opt=="y":
    plt.savefig("BirthRateDecline.png")
plt.show()

#Source: https://www-genesis.destatis.de/genesis/online?operation=abruftabelleBearbeiten&levelindex=1&levelid=1702595031386&auswahloperation=abruftabelleAuspraegungAuswaehlen&auswahlverzeichnis=ordnungsstruktur&auswahlziel=werteabruf&code=12612-0001&auswahltext=&werteabruf=Werteabruf#abreadcrumb