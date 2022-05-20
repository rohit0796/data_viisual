import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
w=0.25
maxi=[]

data1 = pd.read_csv("APPENDICITIS/AverageIter10001.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data2 = pd.read_csv("APPENDICITIS/AverageIter10002.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data3 = pd.read_csv("APPENDICITIS/AverageIter10003.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data4 = pd.read_csv("APPENDICITIS/AverageIter10004.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data5 = pd.read_csv("APPENDICITIS/AverageIter10005.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})

sum1=data1[0].sum()
avg1=sum1/100
sum2=data2[0].sum()
avg2=sum2/100
sum3=data3[0].sum()
avg3=sum3/100
sum4=data4[0].sum()
avg4=sum4/100
sum5=data5[0].sum()
avg5=sum5/100
max1= data1[0].max()
max2= data2[0].max()
max3= data3[0].max()
max4= data4[0].max()
max5= data5[0].max()
min1= data1[0].min()
min2= data2[0].min()
min5= data5[0].min()
min3= data3[0].min()
min4= data4[0].min()
fig, axs = plt.subplots(nrows=2,ncols=2)
f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[0][0])
ax.set(ylabel="ACCURACY")
ax.set(ylim=(80,90))
ax.set(xlabel=" ")




maxi=[]
sum1=data1[1].sum()
avg1=sum1/100
sum2=data2[1].sum()
avg2=sum2/100
sum3=data3[1].sum()
avg3=sum3/100
sum4=data4[1].sum()
avg4=sum4/100
sum5=data5[1].sum()
avg5=sum5/100
max1= data1[1].max()
max2= data2[1].max()
max3= data3[1].max()
max4= data4[1].max()
max5= data5[1].max()

min1= data1[1].min()
min2= data2[1].min()
min5= data5[1].min()
min3= data3[1].min()
min4= data4[1].min()

f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[0][1])
ax.set(ylabel="ERROR")
ax.set(ylim=(10,20))
ax.set(xlabel=" ")
plt.suptitle("appendicitis")



maxi=[]
sum1=data1[2].sum()
avg1=sum1/100
sum2=data2[2].sum()
avg2=sum2/100
sum3=data3[2].sum()
avg3=sum3/100
sum4=data4[2].sum()
avg4=sum4/100
sum5=data5[2].sum()
avg5=sum5/100
max1= data1[2].max()
max2= data2[2].max()
max3= data3[2].max()
max4= data4[2].max()
max5= data5[2].max()

min1= data1[2].min()
min2= data2[2].min()
min5= data5[2].min()
min3= data3[2].min()
min4= data4[2].min()

f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[1][0])
ax.set(ylabel="SENSITIVITY")
ax.set(ylim=(0.5,1.2))
ax.set(xlabel=" ")



maxi=[]
sum1=data1[3].sum()
avg1=sum1/100
sum2=data2[3].sum()
avg2=sum2/100
sum3=data3[3].sum()
avg3=sum3/100
sum4=data4[3].sum()
avg4=sum4/100
sum5=data5[3].sum()
avg5=sum5/100
max1= data1[3].max()
max2= data2[3].max()
max3= data3[3].max()
max4= data4[3].max()
max5= data5[3].max()

min1= data1[3].min()
min2= data2[3].min()
min5= data5[3].min()
min3= data3[3].min()
min4= data4[3].min()

f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[1][1])
ax.set(ylabel="SPECIFICITY")

ax.set(ylim=(0.5,1.2))
ax.set(xlabel=" ")








data1 = pd.read_csv("BREAST_CANCER/AverageIter10001.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data2 = pd.read_csv("BREAST_CANCER/AverageIter10002.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data3 = pd.read_csv("BREAST_CANCER/AverageIter10003.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data4 = pd.read_csv("BREAST_CANCER/AverageIter10004.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data5 = pd.read_csv("BREAST_CANCER/AverageIter10005.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})

sum1=data1[0].sum()
avg1=sum1/100
sum2=data2[0].sum()
avg2=sum2/100
sum3=data3[0].sum()
avg3=sum3/100
sum4=data4[0].sum()
avg4=sum4/100
sum5=data5[0].sum()
avg5=sum5/100
max1= data1[0].max()
max2= data2[0].max()
max3= data3[0].max()
max4= data4[0].max()
max5= data5[0].max()

min1= data1[0].min()
min2= data2[0].min()
min5= data5[0].min()
min3= data3[0].min()
min4= data4[0].min()
fig, axs = plt.subplots(nrows=2,ncols=2)
f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[0][0])
ax.set(ylabel="ACCURACY")
plt.suptitle("breast cancer")
ax.set(ylim=(95,100))
ax.set(xlabel=" ")



maxi=[]
sum1=data1[1].sum()
avg1=sum1/100
sum2=data2[1].sum()
avg2=sum2/100
sum3=data3[1].sum()
avg3=sum3/100
sum4=data4[1].sum()
avg4=sum4/100
sum5=data5[1].sum()
avg5=sum5/100
max1= data1[1].max()
max2= data2[1].max()
max3= data3[1].max()
max4= data4[1].max()
max5= data5[1].max()

min1= data1[1].min()
min2= data2[1].min()
min5= data5[1].min()
min3= data3[1].min()
min4= data4[1].min()

f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[0][1])
ax.set(ylabel="ERROR")
ax.set(ylim=(1,5))
ax.set(xlabel=" ")



maxi=[]
sum1=data1[2].sum()
avg1=sum1/100
sum2=data2[2].sum()
avg2=sum2/100
sum3=data3[2].sum()
avg3=sum3/100
sum4=data4[2].sum()
avg4=sum4/100
sum5=data5[2].sum()
avg5=sum5/100
max1= data1[2].max()
max2= data2[2].max()
max3= data3[2].max()
max4= data4[2].max()
max5= data5[2].max()

min1= data1[2].min()
min2= data2[2].min()
min5= data5[2].min()
min3= data3[2].min()
min4= data4[2].min()

f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[1][0])
ax.set(ylabel="SENSITIVITY")
ax.set(ylim=(0.9,1))
ax.set(xlabel=" ")




maxi=[]
sum1=data1[3].sum()
avg1=sum1/100
sum2=data2[3].sum()
avg2=sum2/100
sum3=data3[3].sum()
avg3=sum3/100
sum4=data4[3].sum()
avg4=sum4/100
sum5=data5[3].sum()
avg5=sum5/100
max1= data1[3].max()
max2= data2[3].max()
max3= data3[3].max()
max4= data4[3].max()
max5= data5[3].max()

min1= data1[3].min()
min2= data2[3].min()
min5= data5[3].min()
min3= data3[3].min()
min4= data4[3].min()

f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[1][1])
ax.set(ylabel="SPECIFICITY")
ax.set(ylim=(0.9,1.1))
ax.set(xlabel=" ")




data1 = pd.read_csv("HEPATITIS/AverageIter10001.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data2 = pd.read_csv("HEPATITIS/AverageIter10002.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data3 = pd.read_csv("HEPATITIS/AverageIter10003.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data4 = pd.read_csv("HEPATITIS/AverageIter10004.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data5 = pd.read_csv("HEPATITIS/AverageIter10005.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})

sum1=data1[0].sum()
avg1=sum1/100
sum2=data2[0].sum()
avg2=sum2/100
sum3=data3[0].sum()
avg3=sum3/100
sum4=data4[0].sum()
avg4=sum4/100
sum5=data5[0].sum()
avg5=sum5/100
max1= data1[0].max()
max2= data2[0].max()
max3= data3[0].max()
max4= data4[0].max()
max5= data5[0].max()

min1= data1[0].min()
min2= data2[0].min()
min5= data5[0].min()
min3= data3[0].min()
min4= data4[0].min()
fig, axs = plt.subplots(nrows=2,ncols=2)
f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[0][0])
ax.set(ylabel="ACCURACY")
ax.set(ylim=(50,90))
plt.suptitle("hepatitis")
ax.set(xlabel=" ")
maxi=[]
sum1=data1[1].sum()
avg1=sum1/100
sum2=data2[1].sum()
avg2=sum2/100
sum3=data3[1].sum()
avg3=sum3/100
sum4=data4[1].sum()
avg4=sum4/100
sum5=data5[1].sum()
avg5=sum5/100
max1= data1[1].max()
max2= data2[1].max()
max3= data3[1].max()
max4= data4[1].max()
max5= data5[1].max()

min1= data1[1].min()
min2= data2[1].min()
min5= data5[1].min()
min3= data3[1].min()
min4= data4[1].min()

f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[0][1])
ax.set(ylabel="ERROR")
ax.set(xlabel=" ")

maxi=[]
sum1=data1[2].sum()
avg1=sum1/100
sum2=data2[2].sum()
avg2=sum2/100
sum3=data3[2].sum()
avg3=sum3/100
sum4=data4[2].sum()
avg4=sum4/100
sum5=data5[2].sum()
avg5=sum5/100
max1= data1[2].max()
max2= data2[2].max()
max3= data3[2].max()
max4= data4[2].max()
max5= data5[2].max()

min1= data1[2].min()
min2= data2[2].min()
min5= data5[2].min()
min3= data3[2].min()
min4= data4[2].min()

f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[1][0])
ax.set(ylabel="SENSITIVITY")
ax.set(xlabel=" ")

maxi=[]
sum1=data1[3].sum()
avg1=sum1/100
sum2=data2[3].sum()
avg2=sum2/100
sum3=data3[3].sum()
avg3=sum3/100
sum4=data4[3].sum()
avg4=sum4/100
sum5=data5[3].sum()
avg5=sum5/100
max1= data1[3].max()
max2= data2[3].max()
max3= data3[3].max()
max4= data4[3].max()
max5= data5[3].max()

min1= data1[3].min()
min2= data2[3].min()
min5= data5[3].min()
min3= data3[3].min()
min4= data4[3].min()

f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[1][1])
ax.set(ylabel="SPECIFICITY")
ax.set(xlabel=" ")




data1 = pd.read_csv("LIVER_PATIENT/AverageIter10001.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data2 = pd.read_csv("LIVER_PATIENT/AverageIter10002.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data3 = pd.read_csv("LIVER_PATIENT/AverageIter10003.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data4 = pd.read_csv("LIVER_PATIENT/AverageIter10004.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
data5 = pd.read_csv("LIVER_PATIENT/AverageIter10005.csv", on_bad_lines='skip', header = None, nrows=100, usecols={0,1,2,3})
sum1=data1[0].sum()
avg1=sum1/100
sum2=data2[0].sum()
avg2=sum2/100
sum3=data3[0].sum()
avg3=sum3/100
sum4=data4[0].sum()
avg4=sum4/100
sum5=data5[0].sum()
avg5=sum5/100
max1= data1[0].max()
max2= data2[0].max()
max3= data3[0].max()
max4= data4[0].max()
max5= data5[0].max()

min1= data1[0].min()
min2= data2[0].min()
min5= data5[0].min()
min3= data3[0].min()
min4= data4[0].min()
fig, axs = plt.subplots(nrows=2,ncols=2)
f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[0][0])
ax.set(ylabel="ACCURACY")
ax.set(ylim=(60,80))
plt.suptitle("liver diseases")
ax.set(xlabel=" ")

maxi=[]
sum1=data1[1].sum()
avg1=sum1/100
sum2=data2[1].sum()
avg2=sum2/100
sum3=data3[1].sum()
avg3=sum3/100
sum4=data4[1].sum()
avg4=sum4/100
sum5=data5[1].sum()
avg5=sum5/100
max1= data1[1].max()
max2= data2[1].max()
max3= data3[1].max()
max4= data4[1].max()
max5= data5[1].max()

min1= data1[1].min()
min2= data2[1].min()
min5= data5[1].min()
min3= data3[1].min()
min4= data4[1].min()

f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[0][1])
ax.set(ylabel="ERROR")
ax.set(ylim=(20,40))
ax.set(xlabel=" ")

maxi=[]
sum1=data1[2].sum()
avg1=sum1/100
sum2=data2[2].sum()
avg2=sum2/100
sum3=data3[2].sum()
avg3=sum3/100
sum4=data4[2].sum()
avg4=sum4/100
sum5=data5[2].sum()
avg5=sum5/100
max1= data1[2].max()
max2= data2[2].max()
max3= data3[2].max()
max4= data4[2].max()
max5= data5[2].max()

min1= data1[2].min()
min2= data2[2].min()
min5= data5[2].min()
min3= data3[2].min()
min4= data4[2].min()

f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[1][0])
ax.set(ylabel="SENSITIVITY")
ax.set(ylim=(0.5,0.90))
ax.set(xlabel=" ")

maxi=[]
sum1=data1[3].sum()
avg1=sum1/100
sum2=data2[3].sum()
avg2=sum2/100
sum3=data3[3].sum()
avg3=sum3/100
sum4=data4[3].sum()
avg4=sum4/100
sum5=data5[3].sum()
avg5=sum5/100
max1= data1[3].max()
max2= data2[3].max()
max3= data3[3].max()
max4= data4[3].max()
max5= data5[3].max()

min1= data1[3].min()
min2= data2[3].min()
min5= data5[3].min()
min3= data3[3].min()
min4= data4[3].min()

f=pd.DataFrame({'algorithms':["algo1","algo2","algo3","algo4","algo5"],
                'min':[min1,min2,min3,min4,min5],
                'mean':[avg1,avg2,avg3,avg4,avg5],
                'max':[max1,max2,max3,max4,max5]})
ax=f.plot(x='algorithms',y=['min','mean','max'],kind='bar',ax=axs[1][1])
ax.set(ylabel="SPECIFICITY")
ax.set(ylim=(0.4,0.9))
ax.set(xlabel=" ")
plt.show()






