from probables import (CountMinSketch)
from numpy import random
import numpy as np
import math
import matplotlib.pyplot as plt



#Generate Zipif's Distribution (Number = num)
###########################################
def generateZdistribution(num, a):
    x = random.zipf(a=a, size=num)
    #print(x)

    zlist = x.tolist()
    #print(zlist)

    return zlist



#Count-Min Sketch (rows, columns)
###########################################
def storeinCMS(input_list, row, column):
    cms = CountMinSketch(width=column, depth=row)

    for i in zlist:
    	cms.add(str(i))

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



#Simulate the miss rate (for CMS and KVS)
#Assume Cache size =  row * column + K = cache
############################################
cache = 1000
num = 100000
a = 2
row = 4



zlist = generateZdistribution(num, a)
zlist2 = generateZdistribution(num, a)

xarray = []
yarray = []
y0array = []

for k in range(1, cache):
    
    
    if (k<50 or (k>cache-100 and k<cache-4) or (1/k) in np.arange(0.0001, 1, 0.0001)):
        column = math.floor((cache - k)/4)
        cms = storeinCMS(zlist, row, column)
        first_k_key_list = storeinKVS(k, cms)
        miss = 0
        for i in zlist2:
            if str(i) not in first_k_key_list:
                miss += 1
        print("k:", k)
        print("column:", column)

        k_sum = 0
        #for i in range(1,k+1):
        #    k_sum += pow((1/i), a)
        #xarray.append(k_sum)
        xarray.append(k)

        hit_rate = (num - miss)/num
        print("hit:", hit_rate)
        yarray.append(hit_rate)

#Objective Function
        kvs_obj = 0
        for i in range(1,k+1):
            kvs_obj = kvs_obj + pow((1/i), a)
        cms_obj = pow((3/column), a)
        obj = 0.8*kvs_obj - 0.2*cms_obj
        y0array.append(obj)


#print(xarray)
plt.figure(1)
plt.title("CMS + KVS")
plt.xlabel("X axis: k")
plt.ylabel("Y axis: Hit Rate")
plt.plot(xarray, yarray, color ="red")
plt.plot(xarray, y0array, color ="blue")

plt.figure(2)
plt.title("CMS + KVS")
plt.xlabel("simulation hit rate")
plt.ylabel("objective function")
plt.plot(yarray, y0array, color ="green")
plt.show()


