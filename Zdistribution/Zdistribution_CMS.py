from probables import (CountMinSketch)
from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#Generate Zipif's Distribution (Number = num)
###########################################
def generateZdistribution(num, a):
    x = random.zipf(a=a, size=num)
    #print(x)

    zlist = x.tolist()

    #f1 = sns.displot(x[x<15], kde=False)
    #plt.show()
    return zlist



#Count-Min Sketch (m rows, n columns)
###########################################
def storeinCMS(input_list, row, column):
    cms = CountMinSketch(width=column, depth=row)

    for i in zlist:
    	cms.add(str(i))

    n1 = cms.check("1")
#    err = cms.error_rate
#    print("Column:", column)
#    print("Estimated Error Rate:",err*100, "%")
    return cms




#CMS simulation. Change the number of column from 100 to 2000
#############################################################
num = 100000
a = 2
row = 5

xarray = []
yarray = []
zlist = generateZdistribution(num, a)

for column in range(100, 1000, 100):
    miss = 0
    cms = storeinCMS(zlist, row, column)
    dict1 = {}
    for i in zlist:
        inumber = cms.check(str(i))
        if str(i) not in dict1.keys():
            dict1[str(i)] = inumber
    totalcount = sum(dict1.values())
    error_count = totalcount - num

    xarray.append(pow((3/column),a))
    yarray.append(error_count)

    print("Column:", column)
    print("Real Error Rate:", error_count/num * 100, "%")
    print("error count", error_count)

plt.title("CMS")
plt.xlabel("X axis: (3/column)^a)")
plt.ylabel("Y axis: Error Count")
plt.plot(xarray, yarray, color ="red")
plt.show()







    



