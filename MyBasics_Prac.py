# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:19:18 2021

@author: Dayanand
"""

# Some Mathematical Operation
3+4

#Creating Variables and assigning values

a=10
b=20
c=a+b
c=a*b
m=a*b
m
z=c*b

#String Variable

str_var="I am learning Python and working on Spyder"
b=" & Jupyter too"
str_var + b
#String variable allow  addition of two lines
str_var - b
str_var * b
str_var / b
# String Variable does not allow other mathematical operation like -,*,/

# Boolean variable
# Boolean variables gives output in the form of True or False
x = True
a=10
b=11
a>b
x>0
x

#Python is case sensitive
ABC=1000
#abc-error.it shows not defined

#------------------------------------------------------------

#Data Structures in Python

#-----------------------------------------------------
    
#List-It stores multiple values.It can be created using[].
#It is mutable.Value can be changed after creation also

myList1=[2,3,4,"ABC","DEF"]
myList1
myList2=[3,4,12,15,"BNM","APPLE","T"]
myList2
myList1+myList2
myList1[2]+myList2[3]
myNewList=[myList1[0:2]+myList2[0:3]]
myNewVar=(myList1[0:2]+myList2[0:3])
myNewVar
type(myNewVar)
type(myNewList)
type(myList2)#type tells the data type

#Tuple-It can also store multiple values of different data types.
#It can be created using small braces ().
#It's value can not be changed after creation.It is non mutable

myTuple1=(34,23,45,"Orange","Banana")
myTuple1
myTuple2=(23,34,56,"Name")
myTuple2
type(myTuple2)
myTuple1+myTuple2
myNewTuple1=myTuple1[2]+myTuple2[2]
myNewTuple1
type(myNewTuple1)
myNewTuple=[myTuple1[0:2]+myTuple2[0:2]]
myNewTuple
type(myNewTuple)
MyStrTuple = ("Apple")
MyStrTuple1 = (" Banana")
type(MyStrTuple + MyStrTuple1)

#If we add two tuples into a new variable.New variable becomes list/int/str

# Dictionery-{key:Value Pairs}-It can be created using middle braces{}.It is very
# useful from dataset point of view

Dic1={"Python":455,"Java":678,"R":235}
Dic1

Dic2={"facebook":4500000,"Google":6500000,"Amazon":8500000}
Dic2
# Dic1 + Dic2-We can not apply mathematical operator on dic

#Some very important datastructures through different libraries

import numpy as np

#numpy-its similar to list.However,numpy array can store elements of a single datatype. 

test_array1 = np.array([1,2,56,78])
test_array1

test_array2 = np.array([1,56,74,"Apple","Banana"])
test_array2
type(test_array2)

#numpy can be used without alias name too
#test_array2=numpy.array([234,345,567,78])
#test_array2

###Dataframe

#Step1:Set working directory
#Step2:Read External Files

#Set Working Directory
import os
#(os-operating system)
#get current working directory(cwd)
os.getcwd()
#change working directory(chdir)-single(/-forward slash)or double\\-backward slash)
os.chdir("C:\\Users\\tk\\Desktop\\DataScience\\Python Class Notes")
os.getcwd()

#READ FILE IN CURRENT DIRECTORY
# read_csv is method by which we can read files

import pandas as pd
MyData=pd.read_csv("Data_File.csv")
MyData

# Go to Variable Explore tab on the right side and double click 
# on "MyData" to view the dataset

#Extracting/Subsetting

#List subsetting using indexing

#Python list index starts from 0 from left to right

myList1[1]
myList1[0] 
myList2[-4]
#myListIndex=[0,1,2,3,4,5,......]
#MyListReverseIndex=[-1,-2,-3,-4,............]

myList3=[23,34,56,78,"Balsam","Marigold"]
myList3[0]
myList3[-1]
myList3[-5]
myList3[1:5]#It extracts continuous value

#Extracts elements opposite side.List indexing starts from -1 from right to left

myList3[-1:-5]# Reverse can not be done from -1 to -5

myList3[-5:-1]
myList3[-3:-1]
myList3[-1:-3]#It returns blank/empty.
myList3[2,4,-1]#It does not extract non continuous elements.Error
#myList3[2,4]
#way to extract non continuous elements-We can extract separately writing one by one

[myList3[-1],myList3[3],myList3[0]]#It gives output as List
myList3[-1],myList3[3]#It gives output as tuple
[myList3[-5],myList3[-4],myList3[0:4]]

#If we do not put big braces outside,it will show result in the 
# form of tuple

myList3[-1],myList3[3],myList3[0]
myList3[-5],myList3[-4],myList3[0:4]

#Excluding elements -It can be done Using : 
myList4=["Hi","Hello","Fine","Bye"]
myList4[:2]# 0 to (index-1)
myList4["Hi"]
#excludes elements from given index to rest of the elements

#myList4[0:2]=myList[:2]

myList4[2:]#Prints from index to rest of all elements
#excludes all elements before indexing

#Value based susetting-it does not support value based subsetting
myList3[myList3>7]#error

#Subsetting for Tuple-It follows all properties of list for indexing

myTuple1=(23,34,56,"Banana","Facebook","Google")
myTuple1[2]
myTuple1[0]
myTuple1[3]
myTuple1[-2]
myTuple1[-3]
myTuple1[1:4]#It provides continuous elements subsetting

myTuple1[-4:0]#it returns blank
myTuple1[-4:-1]

#It does not support non continuous extraction of elements
myTuple1[-2,-4,3]

#It does not support value based subsetting
myTuple1[myTuple1>10]

#Extracting elements in between-It can be using :

myTuple1[:3]   #0 to (index-1) 
#myTuple1[0:3]=myTuple1[:3]
myTuple1[3:]# 3 to all rest of elements

#Numpy Array
import numpy as np
Num_Array=np.array([23,345,456,"Google","Amazon","facebook"])
Num_Array
Num_Array["Google"]
Num_Array[2]
Num_Array[7]#Index out of size
Num_Array[0]
Num_Array[-1]        
Num_Array[0:7]#It runs in the continuous cases
Num_Array[-4:-1]
Num_Array[[1,-2,3]]#It supports non continous extraction
Num_Array[:4]#It prints from 0 to 3 index elements
Num_Array[4:]#It prints from 4th index to rest of all
Num_Array2=np.array([23,45,56])
Num_Array+Num_Array2#it throws error
Num_Array[3:]+Num_Array[:3]#It throws error

np.delete(Num_Array,[4])#It deletes/removes 4th element from starting or 0 index 

#Value based subsetting-It supports value based subsetting

Num_Array1=np.array([5,8,4,9,10])
Num_Array1[Num_Array1>8]#returns value
Num_Array1>9 #returns true or false .True value for given condtion

np.where(Num_Array1>7)#It gives the index where this condition becomes true

#Dictionery

Test_Dic={"Python":456,"JAVA":789,"R":895,"Sigmoid":657}
Test_Dic
Test_Dic[0]#Dic can not be accessed by indexing.Since it is unordered

Test_Dic["Python"]#Dic elements can be accessed using keys

Test_Dic["Python","JAVA"]#More than one element can not be accessed

#DataFrame
import numpy as np
MyData=np.array([124,345,678,980])
MyData

import os
os.getcwd()
os.chdir("C:\\Users\\tk\\Desktop\\DataScience\\Python Class Notes")
os.getcwd()
import pandas as pd
Myfile=pd.read_csv("Data_File.csv")
Myfile

#Index based subsetting

Myfile[1]#Throwing error
#can not be accessed dataframes using single indexes
#Subsetting based on coulumn name
#Can be accessed using column names
Myfile["Variable_A"]
Myfile[["Variable_A","Variable_B"]]
#Multiple column names can be accessed

#Extract using row numbers-Multiple rows can be accessed

Myfile[2:4]#extract rows 2 to 3
Myfile[2:3]#Extract only one row
Myfile[2:]#It will fetch all rows from given index
Myfile[:5]#It will fetch all rows before indexing

#Extract using R,C format(iloc method)-Index based subsetting
Myfile.iloc[1]
Myfile.iloc[0]
Myfile.iloc[2:4]#It will extract rows from 2 to 3
Myfile.iloc[[2,5,0]]#It will extract rows 2 ,5 & 0 index
#it allows non continuous subsetting

#Subsetting rows and columns using iloc method
# comma operator(,) separates between rows and columns
# colon (:) is for rows and cols indexes fetching

Myfile.iloc[2:4,1:2]#it will fetch first column with 2 rows 2 & 3
Myfile.iloc[3:5,2:4]#it will fetch 2nd &3rd columns with 3 & 4 rows
Myfile.iloc[:,0:3]#It will fetch all rows with 0,1,2nd column
#Myfile.iloc[,0:3]#Error-Python does not allow to keep rows blank
Myfile.iloc[1:3,]#We can keep blank column side

#Extract using loc (Name based subsetting)
Myfile.loc[:,["Variable_A","Variable_B"]]#it will fetch all rows and mentioned columns
Myfile.loc[2:5,["Variable_C","Variable_D"]]
#It will fetch rows from 2 to 5 and mentioned columns
#Here it fetched rows from 2 to 5.
#It did not fetch from 2 to 4 as per python standard
#When we use .loc subsets it extracts from start:end 

#We can not use R-Rows,C-Columns formating without using iloc & loc functionality
Myfile[2:4,1:2]#Error
Myfile[:,"Variable_A"]#Error

#Column name within iloc
Myfile.iloc[1:3,"Variable_A"] #Error

#Rows name within loc
Myfile.loc[2:3,1:3]#Error

#From above examples it shows that
# index based subsetting is done using iloc in R,C format
#Name based subsetting is done using loc in R,C format

####################################################
###################################################

###Value based subsetting
Myfile
#Variable_A greater than 5
Myfile[Myfile["Variable_A"]>5]
Myfile.loc[Myfile["Variable_A"]>5,:]
#Myfile.iloc[:,Myfile["Variable_A"]>5]#iloc can not be used
#Myfile[1]#Using index it can not be accessed

abc=Myfile.loc[Myfile["Variable_A"]>5,:]
abc
pqr=Myfile.loc[Myfile.Variable_A>5,:]
pqr
##Subsetting using categorical variable

Myfile.loc[Myfile["Variable_E"]=="B",:]
Myfile.loc[Myfile.Variable_E=="B",:]

#All rows where Var_A>5 and Var_E has "B"
Myfile.loc[(Myfile["Variable_A"]>5) & (Myfile["Variable_E"]=="B"),:]
Myfile.loc[(Myfile["Variable_A"]>5) | (Myfile["Variable_E"]=="B"),:]
#Traditional or Conditioning
Myfile.loc[(Myfile["Variable_E"]=="A") | (Myfile["Variable_E"]=="B"),:]
Myfile.loc[Myfile["Variable_E"].isin(["A","B"]),:]

#.isin is used when we have multiple conditions associated with one variable
myList=["A","B"]
Myfile.loc[Myfile["Variable_E"].isin(myList),:]
#Some not conditions
Myfile.loc[(Myfile.Variable_E!="B") & (Myfile.Variable_E!="E"),:]
Myfile.loc[~(Myfile.Variable_E=="B") & ~(Myfile.Variable_E=="E"),:]
#You can also use ~ negate conditions
Myfile.loc[~(Myfile.Variable_E=="B")| (Myfile.Variable_E=="E"),:]

#--------------------------------------------------------------------------------

#Some useful functions used in data frame

#-------------------------------------------------------------------------------

# To see the supported methods of a function use dir()

MyList=[67,2,89]
dir(MyList)
MyList.append(876)#append a new element
MyList
MyList.pop()#remove the last element
MyList
MyList.reverse()#reverse the order
MyList
MyList.clear()#removes all elements
MyList

#Some built in functions(Built in functions do not require 
# any library/variable)
len(MyList)
sorted(MyList)#it sorts out in ascending order
sorted(MyList,reverse=True)
#sorted with arguement reverse=True sorts in descending order
range(1,5,1)
range(1,10,3)
range(10)
list(range(10))#to see/print the output use list()
range(2,5)
list(range(2,5))
list(range(1,5,1))
list(range(1,5,2))#Last arguement gives gap of 2(we can write any no)

# Check this link for a list of builtin functions: https://docs.python.org/3.10/library/functions.html

# # Accessing multiple elements in a list like structure 

# Convert to numpy array and perform all operations on the numpy
# array and finally convert it back to a list using list() function)
# import numpy as np
# Test_List
# Test_List_Np_Array = np.array(Test_List)
# Test_List_Np_Array
# Temp_Np_Array = Test_List_Np_Array[[0,3,2]] # Access multiple elements in a numpy array
# Temp_Np_Array
# Temp_List = list(Temp_Np_Array)
# Temp_List

#Tuple
Temp_Tuple=("234","ABC","456","DEF",789,198)
Temp_Tuple
type(Temp_Tuple)
dir(Temp_Tuple)
len(Temp_Tuple)

#Dictionary

Temp_dic={"Rishabh":8,"Dayanand":39,"Rachit":2,"Rachna":31}
Temp_dic
dir(Temp_dic)
len(Temp_dic)
Temp_dic.pop("Rachit")
Temp_dic
Temp_dic.update({"Rachit":2})
Temp_dic
Temp_dic.keys()#provides keys info
Temp_dic.values()#provides values info
Temp_dic.items()#provides keys & values both
Temp_dic.update({"Dayanand":38})
#update the value if keys are existed otherwise add new key with values
Temp_dic
Temp_dic.update({"Job":"Google"})
Temp_dic
Temp_dic.pop("Job")
Temp_dic

#Dataframe
import os
os.getcwd()
os.chdir("C:/Users/tk/Desktop/DataScience/Python Class Notes")

import pandas as pd
MT_Cars=pd.read_csv("Mtcars.csv")
dir(MT_Cars)

#Some attributs:Attributes do not allow to pass agruement
MT_Cars.shape#It provides no of rows and no of columns.It is an attribute
MT_Cars.dtypes#It provides data types of each column variables.it is an attribute
MT_Cars.columns#It provides columns info.It is an attribute
list(MT_Cars)#this way we can now the columns info

#Some Methods
#Methods or function has bracet ()

MT_Cars.describe()#descibe shows the statistics for continuous elements
MT_Cars.head()#head provides info of first 5 elements
MT_Cars.tail()#tail provides info of last 5 elements
MT_Cars.boxplot()#draws boxplot

#----------------------------------------------------------------------
###Basics Plotting using Seaborn------------------------------------
##---------------------------------------------------------------------
import seaborn as sns
iris=sns.load_dataset("Iris")
iris.head()

#Scatter plot
sns.scatterplot(iris["sepal_length"],iris["petal_length"])

#Line Plot
sns.lineplot(iris["sepal_length"],iris["petal_length"])

#histogram-distplot() is the function to draw histogram
sns.distplot(iris["sepal_length"])
sns.distplot(iris["petal_length"],kde=False)#kde-kernel distribution estimator.in simpler terms its shape/distribute the data

#Barplot-countplot() is the function to draw barplot()
sns.countplot(iris["species"])

#pairplot
sns.pairplot(iris)

#boxplot
sns.boxplot(iris["petal_length"])

#piechart-seaborn doesnot piechart.We can draw piechart using pandas
#pie chart takes count/frequency as input.so value.counts() will provide us input
iris["species"].value_counts().plot(kind="pie")
iris["sepal_length"].value_counts().plot(kind="line")
#value_counts(iris["sepal_length"]).plot(kind="line")
###--------------------------------------------------------------------------
###Basics Statistics---------------------------------------------------------
####-------------------------------------------------------------------------

#Central Tendency-Mean,Median,Mode

iris["sepal_length"].mean()
type(iris["petal_length"].mean())
round(iris["petal_width"].mean())


iris["petal_width"].median()
type(iris["petal_width"].median())
dir(list)
###------------------------------------------------------------
####- for my experiemnt with different darta types----------------------
####--------------------------------------------------------------------

import numpy as np
myArray=np.array([2,1,1,1,2,2,3,4])
myArray.mean()
#myArray.median()
#myArray.mode()
dir(myArray)
#nump array does not have method median & mode

#List(),tuple(),dir() has no mean,median,mode


listMode=[2,1,1,3,2,1,1,1,5]
listMode.mean()

#--------------------------------------------------------------------------

import pandas as pd
DataSet=pd.read_csv("C:\\Users\\tk\\Desktop\\DataScience\\Python Class Notes\\Data_File1.csv")
DataSet
DataSet["Variable_E"].mode()[0]
#-------------------------------------------------------------------------------
iris["species"].mode()
type(iris["species"].mode())
iris["sepal_length"].mode()
iris["species"].mode()[0]#to get the exact category name from mode output
iris["sepal_length"].mode()[0]


#Spread/dispersion-range,standard deviation
# Range
iris["sepal_length"].max()-iris["sepal_length"].min()
round(iris["sepal_length"].max()-iris["sepal_length"].min())
round(max(iris["petal_width"])-min(iris["petal_width"]))

iris["sepal_length"].std()
round(iris["petal_width"].std())

### Outliers: Detection

iris.describe()

#iris.describe(include = 'all') # Gives stats for categorical columns as well

# For lower side outliers, look for "relatively higher magnitude" jump values 
# between 0th percentile (Min) and 25th percentile (Q1) [0 to Q1] 
# compared to jump between Q1 to Q2 and Q2 to Q3

# For higher side outliers, look for "relatively higher magnitude" jump values between 75th percentile (Q3) and 
# 100th percentile (Max) [Q3 to Max] compared to jump between Q1 to Q2 and Q2 to Q3

# Cutoff Points (Lower Bound & Upper Bound) Identification Methods are provided below:

## IMPORTANT Pointer to keep in mind:
## If you are using pandas quantile or numpy quantile, then values should be 
# between [0,1]
## If you are using numpy percentile, then percentile values should 
#  be between [0,100]
# Example 
#pandas has only quantile

iris["sepal_length"].quantile(0.5)#pandas quantile

#numpy has both function quantile and percentile
import numpy as np
np.quantile(iris["sepal_length"],q=0.43)
np.percentile(iris["sepal_length"],q=43)

#Option 1.Percentile method

np.percentile(iris["sepal_length"],q=[0,25,50,75,100])

lower_bound=np.percentile(iris["sepal_length"],q=1)
lower_bound
upper_bound=np.percentile(iris["sepal_length"],q=99)
upper_bound

#------------------------------------------------------------------------
#----Another example of outlier--------------------------------------

Data_Set2=pd.read_csv("C:\\Users\\tk\\Desktop\\DataScience\\Python Class Notes\\Data_File2.csv")
Data_Set2
dir(Data_Set2)
#Lower_Bound=pd.quantile(Data_Set2["Variable_G"],q=0.1)
Lower_Bound=Data_Set2["Variable_G"].quantile(q=0.1)
Lower_Bound
#Lower_Bound=Data_Set2["Variable_G"].quantile(q=0)#chacking min valueof the dataset


Upper_Bound=Data_Set2["Variable_G"].quantile(q=.99)
Upper_Bound

# Boxplot using pandas
Data_Set2.boxplot(column="Variable_G",grid=False)

####--------------------------------------------------------------------

#option 2- Mean +- 3*sd


lower_bound=iris["sepal_length"].mean()-3*(iris["sepal_length"].std())
lower_bound
upper_bound=iris["sepal_length"].mean()+3*(iris["sepal_length"].std())
upper_bound

##########################################################################
#### Another example of boxplot-----------------------------------------

lower_bound=Data_Set2["Variable_G"].mean()-3*(Data_Set2["Variable_G"].std())
lower_bound
upper_bound=Data_Set2["Variable_G"].mean()+3*(Data_Set2["Variable_G"].std())
upper_bound

#trying to find boxplot graph using seaborn library 

import seaborn as sns

DataFile2=sns.load_dataset("C:\\Users\\tk\\Desktop\\DataScience\\Python Class Notes\\Data_File2.csv")

#Above way of loading data base is showing errors that it is not of example

#-------------------------------------------------------------------------------
#option 3-Boxplot-IQR=Q3-Q1;
#sns.boxplot(y=iris["sepal_length"])

IQR=np.percentile(iris["sepal_length"],q=75)-np.percentile(iris["sepal_length"],q=25)
IQR

# Lower bound- Q1-3*IQR
lower_bound=np.percentile(iris["sepal_length"],q=25)-3*IQR
lower_bound

upper_bound=np.percentile(iris["sepal_length"],q=75)+3*IQR
upper_bound

#-----------Another method of finding boxplot----------------------------
IQR=np.percentile(Data_Set2["Variable_G"],q=75)-np.percentile(Data_Set2["Variable_G"],q=25)
IQR
lower_bound1=np.percentile(Data_Set2["Variable_G"],q=25)-3*IQR
lower_bound1

upper_bound1=np.percentile(Data_Set2["Variable_G"],q=75)+3*IQR
upper_bound1

#------------------------------------------------------------------------
#-----Some Operations in Pandas------------------------------------------
#-----------------------------------------------------------------------
import os
import pandas as pd
os.getcwd()
# read a csv file
MyData=pd.read_csv("C:/Users/tk/Desktop/DataScience/Python Class Notes/Data_File.csv")
MyData

# To see the column names
MyData.columns
[MyData.columns]

#rename the columns
#Option 1
MyData= MyData.rename(columns = {"Variable_A":"Variable_A_New","Variable_B":"Variable_B_New"})
MyData.columns

#Option 2
MyData.rename(columns={"Variable_C":"Variable_C_New","Variable_D":"Variable_D_New"},inplace=True)
MyData.columns
#inplace=True-we do not require to store the changes in MyData.It will automaticaly do

#Option 3
MyData.columns=["Variable_A","Variable_B","Variable_C","Variable_D","Variable_E_New"]
MyData.columns

#Option 3 does not allow slicing.We can not pick columns and slice it
#MyData.columns[0:2]=["Variable_A","Variable_B_New","Variable_C_New"]#Error

#Columns creation in dataframe

MyData["Variable_F"]=MyData["Variable_D"]*2
MyData.columns
#Another way to create new columns in data frame
MyData["Variable_G"]=MyData.loc[:,"Variable_B"]*2
MyData.columns

#MyData.rename(columns={"Variable_E_New":"Variable_E"},inplace=True)
#MyData.columns
MyData.head()#display the first five rows of the dataframe

pd.set_option("display.max_rows",500)
pd.set_option("display.max_columns",500)
pd.set_option("display.width",500)

#Delete the column
MyData.columns

# Option 1
MyData3=MyData.drop(["Variable_F","Variable_F"],axis=1)
MyData3
MyData4=MyData.drop(["Variable_G"],axis=1)#axis=1:columns wise deletion
MyData4

#Option 2
MyData.drop(["Variable_D"],axis=1,inplace=True)
MyData
#inplace=True will delete the data from actual table

#Option 3
del MyData["Variable_G"]
MyData

# To check Null values
MyData.isnull()
#Checking null/missing values element wise

MyData.isnull().sum()
#checking null value element wise and sum the total null values columnwise
MyData.isna().sum()#same as above

#Aggregation of data using groupby method
#groupby("Variable_to_group_by_with-categorical variable")["Variable_on_which_groupby_will_happen"]
MyData.columns
MyData.groupby("Variable_E")["Variable_B"].mean()
MyData.groupby("Variable_E")["Variable_B"].sum()
MyData.groupby("Variable_E")["Variable_C"].std()

# Multiple aggregate functions in a single groupby
abc=MyData.groupby("Variable_E")[["Variable_C","Variable_D"]].agg({"Variable_C":["min","max"],"Variable_D":"std"})
abc
#def=MyData.groupby("Variable_E")[["Variable_C","Variable_D"]].agg({"Variable_C":["min","max"],"Variable_D":"std"})
xyz=MyData.groupby("Variable_E")["Variable_A","Variable_B"].agg({"Variable_A":["min","max"],"Variable_B":"std"})
xyz

#### A pointer to keep in mind while creating copy of the dataframe
MyData_copy=MyData
MyData["Variable_X"]=MyData["Variable_C"]*2
MyData
MyData_copy
# What we observe is that we created colmumn in MyData.But column is also reflected in MyData_copy too
# To avoid this issue use copy() function

MyData_New=MyData.copy()
MyData_New
MyData["Variable_Y"]=MyData["Variable_A"]*2
MyData
MyData_New

# Combine datasets in python(as rbind,cbind of R)
import pandas as pd
MyData1=pd.read_csv("C:/Users/tk/Desktop/DataScience/Python Class Notes/Data_File.csv")
MyData2=pd.read_csv("C:/Users/tk/Desktop/DataScience/Python Class Notes/Data_File.csv")

Row_Wise_Combine=pd.concat([MyData1,MyData2],axis=0)#axis=0 for row wise data bind
Row_Wise_Combine.shape

Column_Wise_Combine=pd.concat([MyData1,MyData1],axis=1)#axis=1 for column wise data bind
Column_Wise_Combine.shape

#####-------------------------------------------------------------------------
# for loop,if else structure-control structure
#####-------------------------------------------------------------------------

#---------------------------------------------------------------------------
#if and else structure
#---------------------------------------------------------------------------

x = 7
y = 10

if ( x > y):
    x=x+1
    print("x is greater than y")
else:
    x=x-1
    print("X is smaller than y")

#---Scalar sentence comparison
x = 5

if ( x == 5):
    print(1)
else:
    print(0)


#-----------------------------------------------------------------------
 # R syntax for scalar variable comparison---------------------------
 # x = 7
 # y = 1
 # ifelse(x>y,x,y)
 #-------------------------------------------------------------------
 
 # Nested ifs (if within if whitin if else construct)
 #if(x<y):
  #   if(y<7):
   #      x = x+1
   
 #ifelse construct in R for USING np.where()
 x=7
 y=np.array([5,10,15])#This has to be array.It can not be a list.
 # Vectorization(ifelse works with array)
 import numpy as np
np.where(x>y,x,y)#np.where is ifelse of R
np.where(x>y,x+1,y+1)

#-------------------------------------------------------------------------
#----------------------------------------------------------------------------
#-- for loop---------------------------------------------------------------
#---------------------------------------------------------------------------

# Ex-Print the values from 0 to 9

for i in range(10):
    print(i)
 
# Ex-Cancatnate strings within for loop

My_string=["Appple","Banana","Orange"] 

for j in My_string:
    my_print_statement= "Fruits Name - " + j
    print(my_print_statement)

for i in range(10):
    #print(i + "Fruits") 
    stringVar= str(i) + " - Number"
    print(stringVar)
    
# Break statement : to stop any iteration and step outside of the loop

for i in range(10):
    if(i==5):
        break
    else:
        print(i) 

#continue statement :to skip any iteration without terminating a loop

for i in range(10):
    if(i==5):
        continue
    else:
        print(i)
 
# np.where use with list

temp_var=[[1,2],[5,6],[8,9]]  
   
for i in temp_var:  
    np.where(np.array(i)==np.where([1,2]),0,1)
    print(i)
 
###########################################
####### While loop ######################## 
###########################################

start=0
while(start<5):
    print(start)
    start=start+1
    
#############################################################################
####### List Comprehension #############
#############################################################################

# List comprehension is an elegant way to define and create lists based on
# existing/new/empty lists

## Ex 1- Create a list of all values from 0 to 9

# Using traditional for loop
abc=[]

for i in range(10):
    abc.append(i)
    print("inside loop",abc)
print("Outside loop",abc)
    
# Traditional for loop can be used as List comprehension
# which automatically "append" elements as it runs through loops
#<[what_you_want_to_store]> for i in <[loop_range]>

[i for i in range(10)]

# Example 2:Create a list of values using some condition

# Traditional for Loop
xyz=[]
for i in range(10):
    if(i<5):
        xyz.append(i)
xyz        
    
MyNewListWithComprehension=[i for i in range(10) if(i<5)]
#--------------------------<i=value store>(for i in range(10)-condition with loop)><if(i<5)-extra condition]
                            
MyNewListWithComprehension

#########

#Ex-3 : Select multiple non continuous elements from the list(which is not possible with list[2,3,5])

MyList=[24,6,28,19,234]
index_to_pick=[0,2,4]
subset_list=[]

for i in range(len(MyList)):
#    print(i)
    if(i in index_to_pick):
 #       print(i)
        subset_list.append(MyList[i])
  #      print(subset_list)
print(subset_list)

#Same example with list comprehension
Subset_List=[MyList[i] for i in range(len(MyList)) if(i in index_to_pick)]   
Subset_List

# Ex-4: Exclude multiple non continuous elements

MyTestList=[123,234,56,89,90,12]
index_to_exclude=[1,4,0]
subset_test_list=[]

for i in range(len(MyTestList)):
    #print(i)
    if(i not in index_to_exclude):
        subset_test_list.append(MyTestList[i])
print(subset_test_list)

# Same example with List Comprehension

[MyTestList[i] for i in range(len(MyTestList)) if(i not in index_to_exclude)]

#Ex 5: print if else statement using for loop

MyListStr=["Apple","Banana","Orange","Papaya","Carrot"]
MyFruits=[]
for i in range(len(MyListStr)):
    if(MyListStr[i]=="Apple"):
        MyFruits.append(MyListStr[i])
#print(MyFruits)
    else:
        print("Not my fruits available")
print(MyFruits)  

# Same examples using List Comprehension

 ["Apple is there" if MyListStr[i]=="Apple" else "MyFruits Not available" for i in range(len(MyListStr)) ]
MyNum=["odd" if num%2!=0 else "even" for num in range(10)]
MyNum
# in List comprehension if lese condition is wrtitten first then followed by for loop
#[MyListStr[i] for i in range(len(MyListStr)) if MyListStr[i]=="Apple" else "MyFruits Not available"]

# It is throwing errors in the bove way
# create a list of values with multiple conditions

MyListNew=[12,23,34,45,56]
MyAppendList=[]
for i in range(len(MyListNew)):
    if((MyListNew[i]>25) & (MyListNew[i]<57)):
        MyAppendList.append(MyListNew[i])
print(MyAppendList)

# same examples with List Comprehension
[MyListNew[i] for i in range(len(MyListNew)) if((MyListNew[i]>25) & (MyListNew[i]<57))]

################################################################
##### User Defined Functions
################################################################

# This is a function definition(which needs tobe created before calling/using function)

def MySquareFunction(x):#def is an keyword used to create a function
    Output=x*x
    return Output # return is needed to return an output when we call the function
# This is a function call
a=MySquareFunction(5)
a
# without return keyword it will not show the output

#Ex-2: Multiple functions

def MyNewfunction(x):
    square=x*x
    cube=x*x*x
    return{"Square":square,"Cube":cube}

MyNewfunction(15)


def MyNewFunction1(y,z):
    add=y+z
    multiply=y*z
#    return add,multiply#it returns tuple
    #return [add,multiply]# it returns list
    return{"add":add,"multiply":multiply}#it returns the value as dictionary
MyNewFunction1(45,56)

###################################################################
#### Apply method in function ########
##################################################################

# apply() method in pandas is the same as apply() function of R
# it recursively applies on rows & columns

#Apply() function of pandas work on columns in python by default axis=0
#if want to apply onrows change the axis=1 

import seaborn as sn
Iris=sn.load_dataset("Iris")
Iris
# Traditional for loop over a dataframe
for colname in Iris.columns[:4]:
    print(colname)
    print(colname,":",Iris[colname].mean())
    
# above examples using apply() using the method np.mean
import numpy as np
Iris.iloc[:,0:4].apply(np.mean,axis=0)# by default column wise
Iris.iloc[:,0:4].apply(np.mean,axis=1) # row wise

#using user defined function within apply method
Iris.iloc[:,0:4].apply(MyNewfunction,axis=0)

# R syntax for apply function
#apply(df,2,mean)