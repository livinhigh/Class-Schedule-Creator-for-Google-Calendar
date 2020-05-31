import csv
from datetime import datetime, timedelta
x = datetime(2020, 6, 1)
#do not change this
days=['mon','tue','wed','thur','fri','sat']
huge_list=[]
#do not change this
huge_list.append(['Subject','Start Date','Start Time','End Date','End Time','All Day Event' ,'Description', 'Location','Private'])
k=1

for i in days:# loop days
    
    for j in range(0,4):# loop hour
        #Change the subject names
        opt=input("Enter the "+str(j+1)+ " hour on "+i+":")
        if opt==1:
            sub="Computer Oriented Numerical Analysis"
        elif opt==2:
            sub="Formal Languages and Automaton Theory"
        elif opt==3:
            sub="Internet of Things"
        elif opt==4:
            sub="Design and Analysis of Algorithms"
        elif opt==5:
            sub="Software Engineering"
        elif opt==6:
            sub="Internet and Web Programming"
        if j==3 and i=='mon':
            j+=2
        for o in range(6): #change the number of weeks here
            huge_list.append([sub,x.strftime("%d")+"-"+x.strftime("%m")+"-"+x.strftime("%Y"),str(9+j)+":00 ",sub,x.strftime("%d")+"-"+x.strftime("%m")+"-"+x.strftime("%Y"),str(10+j)+":00 ","FALSE","Online class","","FALSE"])
            x=x+timedelta(7)
        x=x-timedelta(42)
    k+=1
    x = datetime(2020, 6,k)
    
print huge_list

                    
while True:  
    try:
        with open('IMPORT THIS.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(huge_list)
        break
    except:
        continue
