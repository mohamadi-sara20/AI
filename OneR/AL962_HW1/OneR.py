import pandas as pd
df = pd.read_excel('AL962_HW1_Data.xlsx')
feature1, feature2, feature3, feature4 = df["feature1"], df["feature2"], df["feature3"], df["feature4"]
res = df["class"]
f1_count, f2_count, f3_count, f4_count = {}, {}, {}, {}
error_rates = []
f1, f2, f3, f4 = {}, {}, {}, {}
total_errors = []
f1_error, f2_error, f3_error, f4_error = [], [], [], []

#Find the frequency of each value in feature1.
for i in range(len(feature1)):
    f1_count[feature1[i]] = f1_count.get(feature1[i], 0) + 1

#Find the frequency distribution of values based on their 1 or 0 class and put it in a dictionary.
for key in f1_count.keys():
    for i in range(len(feature1)):
        if feature1[i] == key and int(res[i]) == 1:
            f1[(feature1[i], int(res[i]))] = f1.get((feature1[i], int(res[i])), 0) + 1
        elif feature1[i] == key and int(res[i]) == 0:
            f1[(feature1[i], int(res[i]))] = f1.get((feature1[i], int(res[i])), 0) + 1

f1l = (list(f1.items()))

#Add the left-out (if any) keys with 0 frequency.
if len(f1l) % 2 == 1:
    vs1 = []
    for i in range(len(f1l)):
        vs1.append(f1l[i][0][0])
    for j in range(len(vs1)):
        if (vs1.count(vs1[j])) == 1:
            if (vs1[j], 1) in f1:
                f1l.append(((vs1[j], 0), 0))
            elif (vs1[j], 0) in f1:
                f1l.append(((vs1[j], 1), 0))

#Sort the list so that similar features are put next to each other.
f1l.sort()


#Calculate the error rate for each value.
error_rate = 0
e1 = 0
for i in range(0, len(f1l), 2):
    if f1l[i][1] >= f1l[i + 1][1]:
        error_rate = f1l[i+1][1] / f1_count[f1l[i][0][0]]
        e1 += f1l[i+1][1]
        f1_error.append((error_rate, f1l[i][0][0], f1l[i][0][1]))

    elif f1l[i][1] < f1l[i + 1][1]:
        error_rate = f1l[i][1] / f1_count[f1l[i+1][0][0]]
        e1 += f1l[i][1]
        f1_error.append((error_rate, f1l[i+1][0][0], f1l[i+1][0][1]))

t_e1 = e1 / len(feature1)
total_errors.append(t_e1)


#Find the frequency of each value in feature2.
for i in range(len(feature2)):
    f2_count[feature2[i]] = f2_count.get(feature2[i], 0) + 1
#Find the frequency distribution of values based on their 1 or 0 class and put it in a dictionary.
for key in f2_count.keys():
    for i in range(len(feature2)):
        if feature2[i] == key and int(res[i]) == 1:
            f2[(feature2[i], int(res[i]))] = f2.get((feature2[i], int(res[i])), 0) + 1
        elif feature2[i] == key and int(res[i]) == 0:
            f2[(feature2[i], int(res[i]))] = f2.get((feature2[i], int(res[i])), 0) + 1

f2l = (list(f2.items()))

#Add the left-out keys (if any) with 0 frequency.
if len(f2l) % 2 == 1:
    vs2 = []
    for i in range(len(f2l)):
        vs2.append(f2l[i][0][0])
    for j in range(len(vs2)):
        if (vs2.count(vs2[j])) == 1:
            if (vs2[j], 1) in f2:
                f2l.append(((vs2[j], 0), 0))
            elif (vs2[j], 0) in f2:
                f2l.append(((vs2[j], 1), 0))

#Sort the list so that similar features are put next to each other.
f2l.sort()

#Calculate the error rate for each value.
error_rate = 0
e2 = 0
for i in range(0, len(f2l), 2):
    if f2l[i][1] >= f2l[i + 1][1]:
        error_rate = f2l[i+1][1] / f2_count[f2l[i][0][0]]
        e2 += f2l[i+1][1]
        f2_error.append((error_rate, f2l[i][0][0], f2l[i][0][1]))

    elif f2l[i][1] < f2l[i + 1][1]:
        error_rate = f2l[i][1] / f2_count[f2l[i+1][0][0]]
        e2 += f2l[i][1]
        f2_error.append((error_rate, f2l[i+1][0][0], f2l[i+1][0][1]))

t_e2 = e2 / len(feature2)
total_errors.append(t_e2)

#Find the frequency of each value in feature3.
for i in range(len(feature3)):
    f3_count[feature3[i]] = f3_count.get(feature3[i], 0) + 1
#Find the frequency distribution of values based on their 1 or 0 class and put it in a dictionary.
for key in f3_count.keys():
    for i in range(len(feature3)):
        if feature3[i] == key and int(res[i]) == 1:
            f3[(feature3[i], int(res[i]))] = f3.get((feature3[i], int(res[i])), 0) + 1
        elif feature3[i] == key and int(res[i]) == 0:
            f3[(feature3[i], int(res[i]))] = f3.get((feature3[i], int(res[i])), 0) + 1

f3l = (list(f3.items()))

#Add the left-out keys (if any) with 0 frequency.
if len(f3l) % 2 == 1:
    vs3 = []
    for i in range(len(f3l)):
        vs3.append(f3l[i][0][0])
    for j in range(len(vs3)):
        if (vs3.count(vs3[j])) == 1:
            if (vs3[j], 1) in f3:
                f3l.append(((vs3[j], 0), 0))
            elif (vs3[j], 0) in f3:
                f3l.append(((vs3[j], 1), 0))

#Sort the list so that similar features are put next to each other.
f3l.sort()

#Calculate the error rate for each value.
error_rate = 0
e3 = 0
for i in range(0, len(f3l), 2):
    if f3l[i][1] >= f3l[i + 1][1]:
        error_rate = f3l[i+1][1] / f3_count[f3l[i][0][0]]
        e3 += f3l[i+1][1]
        f3_error.append((error_rate, f3l[i][0][0], f3l[i][0][1]))

    elif f3l[i][1] < f3l[i + 1][1]:
        error_rate = f3l[i][1] / f3_count[f3l[i+1][0][0]]
        e3 += f3l[i][1]
        f3_error.append((error_rate, f3l[i+1][0][0], f3l[i+1][0][1]))

t_e3 = e3 / len(feature3)
total_errors.append(t_e3)

#Find the frequency of each value in feature4.
for i in range(len(feature4)):
    f4_count[feature4[i]] = f4_count.get(feature4[i], 0) + 1
#Find the frequency distribution of values based on their 1 or 0 class and put it in a dictionary.
for key in f4_count.keys():
    for i in range(len(feature4)):
        if feature4[i] == key and int(res[i]) == 1:
            f4[(feature4[i], int(res[i]))] = f4.get((feature4[i], int(res[i])), 0) + 1
        elif feature4[i] == key and int(res[i]) == 0:
            f4[(feature4[i], int(res[i]))] = f4.get((feature4[i], int(res[i])), 0) + 1

f4l = (list(f4.items()))

#Add the left-out keys (if any) with 0 frequency.
if len(f4l) % 2 == 1:
    vs4 = []
    for i in range(len(f4l)):
        vs4.append(f4l[i][0][0])
    for j in range(len(vs4)):
        if (vs4.count(vs4[j])) == 1:
            if (vs4[j], 1) in f4:
                f4l.append(((vs4[j], 0), 0))
            elif (vs4[j], 0) in f4:
                f4l.append(((vs4[j], 1), 0))

f4l.sort()

#Calculate the error rate for each value.
error_rate = 0
e4 = 0
for i in range(0, len(f4l), 2):
    if f4l[i][1] >= f4l[i + 1][1]:
        error_rate = f4l[i+1][1] / f4_count[f4l[i][0][0]]
        e4 += f4l[i+1][1]
        f4_error.append((error_rate, f4l[i][0][0], f4l[i][0][1]))

    elif f4l[i][1] < f4l[i + 1][1]:
        error_rate = f4l[i][1] / f4_count[f4l[i+1][0][0]]
        e4 += f4l[i][1]
        f4_error.append((error_rate, f4l[i+1][0][0], f4l[i+1][0][1]))

t_e4 = e4 / len(feature4)
total_errors.append(t_e4)

#Put all the error rated of each value of each feature in a list.
error_rates.extend((f1_error, f2_error, f3_error, f4_error))

#Find the index of the feature with the minimum error in "error_rates".
ind = total_errors.index(min(total_errors))

#Obtain the rules.
rules = []
for i in error_rates[ind]:
    rules.append((i[1:]))

#The indices are 0-3. The features are 1-4. So we +1 the index.
print("Feature " + str(ind + 1) + ": "+ str(rules))

def OneR(x):
    ''' Returns the class of the given instance based on the trained model. Returns -1 for test cases whose first
    value is missing.
    Input: an instance (a tuple with four str elements)
    Output: the predicted class (int)
    '''
    for i in range(len(rules)):
        if x[ind] == rules[i][0]:
            return rules[i][1]
    return -1


def xlsx_test(filename):
    '''Get the test cases from an .xlsx file and pass them to OneR function to get their predicted class.
    Input: filename (str)
    Output: the predicted class (int)
    '''
    c = []
    df = pd.read_excel(filename + ".xlsx")
    f1, f2, f3, f4 = df["f1"], df["f2"], df["f3"], df["f4"]
    test_cases = []
    for i in range(len(f1)):
        test_cases.append((f1[i], f2[i], f3[i], f4[i]))
    for i in test_cases:
        c.append(OneR(i))
    return c

def users_input_test():
    '''Get the test instance as an input. Pass the input to the OneR function.
    Output: the predicted class (int)
    '''
    i = (input("What is the instance? "))
    i = tuple(x for x in i.split(","))
    return OneR(i)

print(OneR(("A", "H", "N", "F")))
print(OneR(("B", "C", "H", "T")))
print(OneR(("A", "M", "H", "T")))
print(OneR(("C", "M", "N", "F")))
print(OneR(("?", "C", "N", "F")))
print(xlsx_test("test"))
print(users_input_test())
