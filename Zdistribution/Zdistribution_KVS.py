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

    #n1 = cms.check("1")
    #err = cms.error_rate
    #print("Collision Rate:",err*100, "%")
    return cms



#Put CMS's hot key and value into KVS (k most popular keys)
###########################################
def storeinKVS(k, cms):
    dict1 = {}
    for i in zlist:
        inumber = cms.check(str(i))
        if str(i) not in dict1.keys():
            if inumber not in dict1.values():
                dict1[str(i)] = inumber

    #sort keys by number of occurance
    sorted_temp = sorted(dict1.items(), key = lambda kv: kv[1], reverse = True)
    sorted_dictionary = dict(sorted_temp)
    #print(" ")
    #print("###############      Keys and Numbers     ################")
    #print(sorted_dictionary)

    #print(" ")
    #print("###############      First K Keys     ################")
    key_list = sorted_dictionary.keys()

    first_k_key_list = list(sorted_dictionary.keys())[0:k]
    #print(first_k_key_list)
    #print(len(first_k_key_list))
    return first_k_key_list



#Simulate the miss rate (for )
############################################
num = 100000
a = 2
m = 4
n = 1000


zlist = generateZdistribution(num, a)
cms = storeinCMS(zlist, m, n)

xarray = []
x0array = []
yarray = []
#inverse_k = 1/k
for k in range(1, 5000):
    if (k<50 or (1/k) in np.arange(0.0001, 1, 0.0001)):
        first_k_key_list = storeinKVS(k, cms)
        miss = 0
        for i in zlist:
            if str(i) not in first_k_key_list:
                miss += 1
        print("k:", k)

        k_sum = 0
        for i in range(1,k+1):
            k_sum += pow((1/i), a)
        xarray.append(k_sum)
        x0array.append(k)

        hit_rate = (num - miss)/num
        print("hit:", hit_rate)
        yarray.append(hit_rate)

#print(xarray)
plt.figure(1)
plt.title("KVS")
plt.xlabel("X axis: K")
plt.ylabel("Y axis: Hit Rate")
plt.plot(x0array, yarray, color ="red")
#plt.show()

plt.figure(2)
plt.title("KVS")
plt.xlabel("X axis: sum((1/ki)^a)")
plt.ylabel("Y axis: Hit Rate")
plt.plot(xarray, yarray, color ="red")
plt.show()




    



