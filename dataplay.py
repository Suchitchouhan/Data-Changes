import pandas as pd
import numpy as np
import time as t
import matplotlib.pyplot as plt
print("Please select data Format ".title())
print("1.csv")
print("2.table")
print("3.fwf")
print("4.clipboard")
print("5.excel")
print("6.hdf")
print("7.html")
print("8.json")
print("9.msgpack")
print("10.pickle")
print("11.sas")
print("12.sql")
print("13.stata")
print("14.feather")

while True:
    try:
        i22=int(input("Enter number of the data format [Number] > "))
        break
    except:
        print("Please choose right option ")
data=(input("Enter the path of data > "))
if i22==1:
    p=pd.read_csv(data)
elif i22==2:
    p=pd.read_table(data)
elif i22==3:
    p=pd.read_fwf(data)
elif i22==4:
    p=pd.read_clipboard(data)
elif i22==5:
    p=pd.read_excel(data)
elif i22==6:
    p=pd.read_hdf(data)
elif i22==7:
    p=pd.read_html(data)
elif i22==8:
    p=pd.read_json(data)
elif i22==9:
    p=pd.read_msgpack(data)
elif i22==10:
    p=pd.read_pickle(data)
elif i22==11:
    p=pd.read_sas(data)
elif i22==12:
    p=pd.read_sql(data)
elif i22==13:
    p=pd.read_stata(data)
elif i22==14:
    p=pd.read_feather(data)
p1=pd.DataFrame(p)
p2=p1.columns
def details():
    print('===================================================================')
    print("Columns in your data")
    print('===================================================================')
    for x in p2:
        print(x)
    print('===================================================================')
    print("this is basic information".title())
    print(p1.describe())
    print('===================================================================')
    print('Columns names : non-empty values')
    print(p1.count())
    print('===================================================================')
    print('Columns names : empty values ')
    a=[]
    for x in p2:
        count=0
        b=p1[x][p1[x].isnull()].values
        for y in b:
            count=count+1
        print(x,'  :   ',count,'empty values')
        
def dataclean():
    print('====================================================================')
    print('Columns        :    non-empty values ')
    print(p1.count())
    print('====================================================================')
    a=[]
    for x in p2:
        count=0
        b=p1[x][p1[x].isnull()].values
        for y in b:
            count=count+1
        print(x,'  :   ',count,'empty values')
        if count > 0:
            a.append(x)
        else:
            print("the data is already clean")
        
            
    print('=====================================================================')      
    for x in a:
        try:
            print('replaceing values in ',x,'columns')
            if p1[x].dtype==object:
                rep=input("Enter [string] replaceing values > ")
            elif p1[x].dtype==float:
                rep=float(input("Enter [float] replaceing values > "))
            else:
                rep=int(input("Enter [integer] replaceing values > "))
        except:
                rep=np.nan
        
        p1[x]=p[x].replace(np.nan,rep)
     
    
        
def view():
          print("1.view in list format")
          print("2.view in simple format")
          
          while True:
                try:
                    i23=int(input("Enter view format number > "))
                    break
                except:
                    print("please choose right number ")
          if i23==1:
                for x in p1.values:
                    print(x)
          else:
             pd.set_option('display.max_rows', p1.shape[0]+1)
             print(p1)   
def insertnewvalue():
    p=pd.read_csv(data)
    p1=pd.DataFrame(p)
    p2=p1.columns
    p3=list(p2)
    b=[]
    for x in p3:
        print('=====================insert value in ',x,'===============================')
        try:
                if p1[x].dtype==object :
                    x=input('Enter the [string] value > ')
                elif p1[x].dtype==float:
                    x=float(input('Enter the [float] value > '))
                else:
                    x=int(input('Enter the [int] value > '))
        except: 
              x=np.nan
        b.append(x)
    y=pd.Series(b,index=p3)
    p1=p1.append(y,ignore_index=True)
    print('===========================Inserted values===============================')
    print(p1[p1[p3[0]]==b[0]])
    print('=========================================================================')
def drop():
    try:
        p1=p1.drop_duplicates()
        print("Duplicate rows has been deleted")
        print("===========================================================================")
    except:
        print("there is not duplicate ")

def search():
    p6=list(p2)
    print("======================================================================================")
    for x,y in enumerate(p6):
        print(x,".",y)
    while True:
         try:
            indexcolumns=int(input("Enter the choice for index column [number] > "))
            print("Selected index column is ",p6[indexcolumns])           
            break
         except:
             print("please enter right choice")
    print("========================================================================================")                
    while True:
         try:
                print("please enter the value of ==",p6[indexcolumns],"==carefully")
                if p1[p6[indexcolumns]].dtype==object :
                    x=input('Enter the [string] value > ')
                elif p1[p6[indexcolumns]].dtype==float:
                    x=float(input('Enter the [float] value > '))
                else:
                    x=int(input('Enter the [int] value > '))
                break    
         except: 
               print("select",p6[indexcolumns]," value care fully ")
    print("=========================================================================================")            
    srea=p1[p1[p6[indexcolumns]]==x].values
    for x in srea:
         print(x)
import matplotlib.pyplot as plt
def plotgraph():
    p12=list(p2)
    for x,y in enumerate(p12):
        print(x,".",y)
    print("=======================================================================================")    
    while True:
        try:
            i12=int(input("choose X-axis columns [number] > "))
            break
        except:
            print("please enter right choice number ")
    print("=======================================================================================")        
    while True:
        try:
            i13=int(input("choose Y-axis columns [number] > "))
            break
        except:
            print("please enter right choice number ")
    print("==========================================================================================")        
    i15=plt.style.available
    i16=list(i15)
    for x,y in enumerate(i16):
        print(x,".",y)
    print("==========================================================================================")        
    try:
        i14=int(input("plaese chose the style [number] > "))
    except:
        print("default we use this ",i16[3])
        i14=3
    print("==========================================================================================")        

    try:
        i18=input("enter the name [deflaut title name is NOTHING] > ")
    except:
        i18="NOTHING"
    print("==========================================================================================")        

    try:
        i20=input("Enetr the label name  > ")
    except:
        i20="no label"
    print("==========================================================================================")        
    
    plt.style.use(i16[i14])        
    plt.plot(p1[p12[i12]],p1[p12[i13]],color="blue",label=i20)
    plt.xlabel(p12[i12])
    plt.ylabel(p12[i13])
    plt.title(i18)
    plt.legend()
    plt.show()
    print("if you want to save then [press1] or not then [press 2]")
    while True:
        try:
            i19=int(input("ENTER YOUR CHOICE > "))
            break
        except:
            print("PLAESE CHOOSE CORRECT NUMBER")
    if i19==1:
        plt.savefig(i17,".png")
def scatterplot():
    p12=list(p2)
    for x,y in enumerate(p12):
        print(x,".",y)
    print("=======================================================================================")    
    while True:
        try:
            i12=int(input("choose X-axis columns [number] > "))
            break
        except:
            print("please enter right choice number ")
    print("=======================================================================================")        
    while True:
        try:
            i13=int(input("choose Y-axis columns [number] > "))
            break
        except:
            print("please enter right choice number ")
    print("==========================================================================================")        
    i15=plt.style.available
    i16=list(i15)
    for x,y in enumerate(i16):
        print(x,".",y)
    print("==========================================================================================")        
    try:
        i14=int(input("plaese chose the style [number] > "))
    except:
        print("default we use this ",i16[3])
        i14=3
    print("==========================================================================================")        

    try:
        i18=input("enter the name [deflaut title name is NOTHING] > ")
    except:
        i18="NOTHING"
    print("==========================================================================================")        

    try:
        i20=input("Enetr the label name  > ")
    except:
        i20="no label"
    print("==========================================================================================")        
    
    plt.style.use(i16[i14])        
    plt.scatter(p1[p12[i12]],p1[p12[i13]],color="blue",label=i20)
    plt.xlabel(p12[i12])
    plt.ylabel(p12[i13])
    plt.title(i18)
    plt.legend()
    plt.show()
    print("if you want to save then [press1] or not then [press 2]")
    while True:
        try:
            i19=int(input("ENTER YOUR CHOICE > "))
            break
        except:
            print("PLAESE CHOOSE CORRECT NUMBER")
    if i19==1:
        plt.savefig(i17,".png")
def savethedata():
    print("===========================================================================")
    print("please choose your the data format in which data would we save ")
    print("1.csv")
    print("2.clipboard")
    print("3.html")
    print("4.excel")
    print("5.hdf")
    print("6.json")
    print("7.feather")
    print("8.msgpack")
    print("10.pickle")
    print("11.sas")
    print("12.sql")
    print("9.stata")
    print("7.feather")
    while True:
        try:
            a=int(input("Enter the file [format] > "))
            break
        except:
            print("please choose right format ")
    print("please enter  path locatation where you wanna save the data .then after write the [=filename=] ")
    print("window users will have to put backslash[ \ ] between the path and file ")
    print("linux/mac users will have to put forwrdslash[ / ] between the path and file ")

    while True:
        try:
            b=input("Enter the path with file name > ")
            break
        except:
            print("enter right file name")
    if a==1:
        p1.to_csv(b)
    elif a==2:
        p1.to_clipboard(b)
    elif a==3:
        p1.to_html(b)
    elif a==4:
        p1.to_excel(b)
    elif a==5:
        p1.to_hdf(b)
    elif a==6:
        p1.to_json(b)
    elif a==7:    
        p1.to_feather(b)
    elif a==8:
        p1.to_msgpack(b)
    elif a==9:
        p1.to_stata(b)
    elif a==10:
        p1.to_pickle(b)
    elif a==11:
        p1.to_sql(b)
    print("your data has been saved")
    print("==============================================================================")
while True:
        try:    
                print("===========================================================================================")
                print("1.data details".title())
                print("2.view data".title())         
                print("3.date clean".title())
                print("4.Insert new value ".title())
                print("5.Search rows values in data according to columns ")
                print("6.Delete all duplicate row in data")
                print("7.Plot a graph ")
                print("8.plot a scatter graph ")   
                print("9.Saving the data")
                print("10.Exit")
                print("==========================================================================================")
                while True:
                    try:
                        chose=int(input("choose the option [enter the number ] > "))
                        break
                    except:
                        print("please enter correct choice")
                if chose==1 :
                    details()
                elif chose==2 :
                         view()    
                elif chose==3 :
                        dataclean()    
                elif chose==4 :
                     insertnewvalue()
                elif chose==5 :
                     search()
                elif chose==6 :    
                    drop()
                elif chose==7 :
                    plotgraph()
                elif chose==8:
                    scatterplot()
                elif chose==9:
                    savethedata()
                else:
                    break
        except:
            print("something worng")
