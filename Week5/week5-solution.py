import csv

with open('student.csv','w',newline='') as d :
    w=csv.writer(d)
    fields=['S_ID','S_NAME','CITY','CONTACT']
    w.writerow(fields)
    rows=[[1,'Ishu','surat',757508],
    [2,'Kishu','bardoli',658790],
    [3,'Sai','navsari',476879],
    [4,'Om','vyra',586998],
    [5,'Perarna','surat',376586]]
    w.writerows(rows)

#INSERT INPUT OF 5 RECORDS THROUGH USER:    
from csv import writer
with open('student.csv','a',newline='') as d :
    w=csv.writer(d)
    l=[]
    for i in range(5):
        s_id=int(input("ENTER STUDENT ID:"))
        s_name=input("ENTER STUENT NAME:")
        city=input("ENTER CITY:")
        contact=input("ENTER STUDENT CONTACT NUMBER:")
        t=(s_id, s_name,city,contact)
        l.append(t)
    w.writerows(l)
    
#READ THIS FILE USING CSV MODULE AND PRINTING IT:
from csv import reader
with open('student.csv','r',newline='') as d:
    w=reader()
    for row in w:
        print(row)
