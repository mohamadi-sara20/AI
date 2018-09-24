import pandas as pd
df = pd.read_excel('AL962_HW1_Data.xlsx')
feature1, feature2, feature3, feature4 = df["feature1"], df["feature2"], df["feature3"], df["feature4"]
f1_count, f2_count, f3_count, f4_count = {}, {}, {}, {}
res = df["class"]
error_rates = []
f1, f2, f3, f4 = {}, {}, {}, {}

#Find the frequency of each feature as a total and save in in a dictionary.
for i in range(len(feature1)):
    f1_count[feature1[i]] = f1_count.get(feature1[i], 0) + 1
#Find the frequency distribution of values based on their 1 or 0 class and put it in a dictionary.
for key in f1_count.keys():
    for i in range(len(feature1)):
        if feature1[i] == key and int(res[i]) == 1:
            f1[(feature1[i], int(res[i]))] = f1.get((feature1[i], int(res[i])), 0) + 1
        elif feature1[i] == key and int(res[i]) == 0:
            f1[(feature1[i], int(res[i]))] = f1.get((feature1[i], int(res[i])), 0) + 1
#Dics are not indexed, so convert the frequency distribution to a list so that it's easier to reach the information.
f1l = (list(f1.items()))

#If some value has not been put in the dic yet (because it only occurs in one class), create an item for the other class &
#put the frequency of that class zero.

if len(f1l) % 2 == 1:
    vs1 = []
    for i in range(len(f1l)):
        vs1.append(f1l[i][0][0])
    for j in range(len(vs1)):
        if (vs1.count(vs1[j])) == 1:
            f1l.append(((vs1[j], 0), 0))

#Sort the list so that similar features are put next to each other.
f1l.sort()

error_rate = 0
#Calculate the error rate for each value.
for i in range(0, len(f1l), 2):
    if f1l[i][1] >= f1l[i + 1][1]:
        error_rate = f1l[i+1][1] / f1_count[f1l[i][0][0]]
        error_rates.append((error_rate, f1l[i][0][0], f1l[i][0][1]))

    elif f1l[i][1] < f1l[i + 1][1]:
        error_rate = f1l[i][1] / f1_count[f1l[i+1][0][0]]
        error_rates.append((error_rate, f1l[i+1][0][0], f1l[i+1][0][1]))

#Find the frequency of each feature as a total and save in in a dictionary.
for i in range(len(feature2)):
    f2_count[feature2[i]] = f2_count.get(feature2[i], 0) + 1
#Find the frequency distribution of values based on their 1 or 0 class and put it in a dictionary.
for key in f2_count.keys():
    for i in range(len(feature2)):
        if feature2[i] == key and int(res[i]) == 1:
            f2[(feature2[i], int(res[i]))] = f2.get((feature2[i], int(res[i])), 0) + 1
        elif feature2[i] == key and int(res[i]) == 0:
            f2[(feature2[i], int(res[i]))] = f2.get((feature2[i], int(res[i])), 0) + 1

#Dics are not indexed, so convert the frequency distribution to a list so that it's easier to reach the information.
f2l = (list(f2.items()))

#If some value has not been put in the dic yet (because it only occurs in one class), create an item for the other class &
#put the frequency of that class zero.

if len(f2l) % 2 == 1:
    vs2 = []
    for i in range(len(f2l)):
        vs2.append(f1l[i][0][0])
    for j in range(len(vs2)):
        if (vs2.count(vs2[j])) == 1:
            f2l.append(((vs2[j], 0), 0))

#Sort the list so that similar features are put next to each other.
f2l.sort()

error_rate = 0
#Calculate the error rate for each value.
for i in range(0, len(f2l), 2):
    if f2l[i][1] >= f2l[i + 1][1]:
        error_rate = f2l[i+1][1] / f2_count[f2l[i][0][0]]
        error_rates.append((error_rate, f2l[i][0][0], f2l[i][0][1]))

    elif f2l[i][1] < f2l[i + 1][1]:
        error_rate = f2l[i][1] / f2_count[f2l[i+1][0][0]]
        error_rates.append((error_rate, f2l[i+1][0][0], f2l[i+1][0][1]))


#Find the frequency of each feature as a total and save in in a dictionary.
for i in range(len(feature3)):
    f3_count[feature3[i]] = f3_count.get(feature3[i], 0) + 1
#Find the frequency distribution of values based on their 1 or 0 class and put it in a dictionary.
for key in f3_count.keys():
    for i in range(len(feature3)):
        if feature3[i] == key and int(res[i]) == 1:
            f3[(feature3[i], int(res[i]))] = f3.get((feature3[i], int(res[i])), 0) + 1
        elif feature3[i] == key and int(res[i]) == 0:
            f3[(feature3[i], int(res[i]))] = f3.get((feature2[i], int(res[i])), 0) + 1

#Dics are not indexed, so convert the frequency distribution to a list so that it's easier to reach the information.
f3l = (list(f3.items()))

#If some value has not been put in the dic yet (because it only occurs in one class), create an item for the other class &
#put the frequency of that class zero.

if len(f3l) % 2 == 1:
    vs3 = []
    for i in range(len(f2l)):
        vs3.append(f1l[i][0][0])
    for j in range(len(vs3)):
        if (vs3.count(vs3[j])) == 1:
            f2l.append(((vs3[j], 0), 0))

#Sort the list so that similar features are put next to each other.
f3l.sort()

error_rate = 0
#Calculate the error rate for each value.
for i in range(0, len(f3l), 2):
    if f3l[i][1] >= f3l[i + 1][1]:
        error_rate = f3l[i+1][1] / f3_count[f3l[i][0][0]]
        error_rates.append((error_rate, "f3", f3l[i][0][0], f3l[i][0][1]))

    elif f3l[i][1] < f3l[i + 1][1]:
        error_rate = f3l[i][1] / f3_count[f3l[i+1][0][0]]
        error_rates.append((error_rate, "f3", f3l[i+1][0][0], f3l[i+1][0][1]))


#Find the frequency of each feature as a total and save in in a dictionary.
for i in range(len(feature4)):
    f4_count[feature4[i]] = f4_count.get(feature4[i], 0) + 1
#Find the frequency distribution of values based on their 1 or 0 class and put it in a dictionary.
for key in f4_count.keys():
    for i in range(len(feature4)):
        if feature4[i] == key and int(res[i]) == 1:
            f4[(feature4[i], int(res[i]))] = f4.get((feature4[i], int(res[i])), 0) + 1
        elif feature4[i] == key and int(res[i]) == 0:
            f4[(feature4[i], int(res[i]))] = f4.get((feature4[i], int(res[i])), 0) + 1

#Dics are not indexed, so convert the frequency distribution to a list so that it's easier to reach the information.
f4l = (list(f4.items()))

#If some value has not been put in the dic yet (because it only occurs in one class), create an item for the other class &
#put the frequency of that class zero.

if len(f4l) % 2 == 1:
    vs4 = []
    for i in range(len(f4l)):
        vs4.append(f4l[i][0][0])
    for j in range(len(vs4)):
        if (vs4.count(vs4[j])) == 1:
            f4l.append(((vs4[j], 0), 0))

#Sort the list so that similar features are put next to each other.
f4l.sort()

error_rate = 0
#Calculate the error rate for each value.
for i in range(0, len(f4l), 2):
    if f4l[i][1] >= f4l[i + 1][1]:
        error_rate = f4l[i+1][1] / f4_count[f4l[i][0][0]]
        error_rates.append((error_rate,"f4", f4l[i][0][0], f4l[i][0][1]))

    elif f4l[i][1] < f4l[i + 1][1]:
        error_rate = f4l[i][1] / f4_count[f4l[i+1][0][0]]
        error_rates.append((error_rate, "f4", f4l[i+1][0][0], f4l[i+1][0][1]))


def oneR_test(a, b, c, d):
    if a == n:
        return min(error_rates)[2]
    return 0


















#Find the frequency of each feature as a total and save in in a dictionary.
for i in range(len(feature3)):
    f3_count[feature3[i]] = f3_count.get(feature3[i], 0) + 1
#Find the frequency distribution of values based on their 1 or 0 class and put it in a dictionary.
for key in f3_count.keys():
    for i in range(len(feature3)):
        if feature3[i] == key and int(res[i]) == 1:
            f3[(feature3[i], int(res[i]))] = f3.get((feature3[i], int(res[i])), 0) + 1
        elif feature3[i] == key and int(res[i]) == 0:
            f3[(feature3[i], int(res[i]))] = f3.get((feature2[i], int(res[i])), 0) + 1

#Dics are not indexed, so convert the frequency distribution to a list so that it's easier to reach the information.
f3l = (list(f3.items()))

#If some value has not been put in the dic yet (because it only occurs in one class), create an item for the other class &
#put the frequency of that class zero.

if len(f3l) % 2 == 1:
    vs3 = []
    for i in range(len(f2l)):
        vs3.append(f1l[i][0][0])
    for j in range(len(vs3)):
        if (vs3.count(vs3[j])) == 1:
            f2l.append(((vs3[j], 0), 0))

#Sort the list so that similar features are put next to each other.
f3l.sort()

error_rate = 0
e3 = 0
#Calculate the error rate for each value.
for i in range(0, len(f3l), 2):
    if f3l[i][1] >= f3l[i + 1][1]:
        error_rate = f3l[i+1][1] / f3_count[f3l[i][0][0]]
        e3 += f3l[i+1][1]
        error_rates.append((error_rate, "f3", f3l[i][0][0], f3l[i][0][1]))

    elif f3l[i][1] < f3l[i + 1][1]:
        error_rate = f3l[i][1] / f3_count[f3l[i+1][0][0]]
        e3 += f3l[i][1]
        error_rates.append((error_rate, "f3", f3l[i+1][0][0], f3l[i+1][0][1]))



t_e3 = e3 / len(feature3)
