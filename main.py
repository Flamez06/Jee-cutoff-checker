import csv
def scan():
    a=input("Enter the type of institute you want to view from the following:\nIIT\nNIT\nIIIT\nGFTI\n \n").lower()
    print()
    with open(a+'s','r')as f:
        for i in f.readlines():print(i.rstrip('\n'))
    clg=input('\nEnter the names of the institute whose cutoffs you want to see (use ; to seperate): ').split(';')
    course=input('Enter the names of your courses (use ; to seperate): ').split(';')
    quota=input('Enter the category you belong to (OPEN for general): ')
    gender=input('Enter your gender (female or neutral): ')


    l1=[];l2=[];l3=[]

    with open('clgdata.csv','r')as f:
        data=csv.reader(f)
        for i in data:
            if quota.lower() in i[3].lower() and gender.lower() in i[4].lower():
                for j in clg:
                    if j==i[0]:
                        for k in course:
                            if k.lower() in i[1].lower():
                                if i[2]=="AI":l1.append(i)
                                elif i[2]=="OS":l2.append(i)
                                else:l3.append(i)
    l=l1+l2+l3

    if len(l)!=0:
        with open('info.csv','w',newline="")as f:
            writer=csv.writer(f)
            writer.writerow(['Name','Course','Quota','Seat type','Opening rank','Closing rank'])
            for i in l:writer.writerow([i[0],i[1],i[3],i[2],i[5],i[6]])


scan()
