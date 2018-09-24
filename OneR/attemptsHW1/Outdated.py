import pandas as pd
df = pd.read_excel('AL962_HW1_Data.xlsx')
feature1, feature2, feature3, feature4 = df["feature1"], df["feature2"], df["feature3"], df["feature4"]
f1_count, f2_count, f3_count, f4_count = {}, {}, {}, {}
res = df["class"]
error_rates = []

a_pos, a_neg, b_pos, b_neg, c_pos, c_neg = 0, 0, 0, 0, 0, 0
f1_error_rate = 0
f1_outcome = 0

for i in range(len(feature1)):
    # Calculate frequency distribution for each value.
    f1_count[feature1[i]] = f1_count.get(feature1[i], 0) + 1

    #Calculate the frequency distribution for "A".
    if feature1[i] == "A" and int(res[i]) == 1:
        a_pos += 1
    elif feature1[i] == "A" and int(res[i]) == 0:
        a_neg += 1
    freq = [((0, 0)) * len(f1_count)]

    #Calculate the frequency distribution for "B".
    if feature1[i] == "B" and int(res[i]) == 1:
        b_pos += 1

    elif feature1[i] == "B" and int(res[i]) == 0:
        b_neg += 1

    #Calculate the frequency distribution for "C".
    if feature1[i] == "C" and int(res[i]) == 1:
        c_pos += 1
    elif feature1[i] == "C" and int(res[i]) == 0:
        c_neg += 1


#Calcualte the error rate for feature1.
if a_pos >= a_neg:
    error_rate = a_neg / f1_count["A"]
    f1_outcome = 1
    f1_value = "A"

else:
    error_rate = a_pos / f1_count["A"]
    f1_outcome = 0
    f1_value = "A"
    c = 0

if b_pos >= b_neg:
    #Check if the current error rate is more than that we want to calculate.
    if error_rate > b_neg / f1_count["B"]:
        error_rate = b_neg / f1_count["B"]
        f1_outcome = 1
        f1_value = "B"
else:
    if error_rate > b_pos / f1_count["B"]:
        # Check if the current error rate is more than that we want to calculate.
        error_rate = b_pos / f1_count["B"]
        f1_outcome = 0
        f1_value = "B"
if c_pos >= c_neg:
    #Check if the current error rate is more than that we want to calculate.
    if error_rate > c_neg /f1_count["C"]:
        error_rate = c_neg / f1_count["C"]
        f1_outcome = 1
        f1_value = "C"
else:
    #Check if the current error rate is more than that we want to calculate.
    if error_rate > c_pos / f1_count["C"]:
        error_rate = c_pos / f1_count["C"]
        f1_outcome = 0
        f1_value = "C"

#Add f1 error rate to the list.
error_rates.append((f1_error_rate, f1_outcome, f1_value))

h_pos, h_neg, m_pos, m_neg, c2_pos, c2_neg = 0, 0, 0, 0, 0, 0
f2_outcome = 0.0
f2_error_rate = 0

for i in range(len(feature2)):
    f2_count[feature2[i]] = f2_count.get(feature2[i], 0) + 1

    #Calcualate error rate for H.
    if feature2[i] == "H" and int(res[i]) == 1:
        h_pos += 1
    elif feature2[i] == "H" and int(res[i]) == 0:
        h_neg += 1

    #Calculate error rate for M.
    if feature2[i]  == "M" and int(res[i]) == 1:
        m_pos += 1
    elif feature2[i] == "M" and int(res[i]) == 0:
        m_neg += 1

    #Calculate error rate for C.
    if feature2[i] == "C" and int(res[i]) == 1:
        c2_pos += 1
    elif feature2[i] == "C" and int(res[i]) == 0:
        c2_neg += 1

#Calcualte the error rate.
if h_pos >= h_neg:
    f2_outcome = 1
    f2_error_rate = h_neg / f2_count["H"]
    f2_value = "H"

elif h_neg > h_pos:
    f2_outcome = 0
    f2_error_rate = h_pos / f2_count["H"]
    f2_value = "H"

if m_pos >= m_neg:
    if f2_error_rate > m_neg / f2_count["M"]:
        f2_outcome = 1
        f2_error_rate = m_neg / f2_count["M"]
        f2_value = "M"
else:
    if f2_error_rate> m_pos / f2_count["M"]:
        f2_outcome = 0
        f2_error_rate = m_pos / f2_count["M"]
        f2_value = "M"

if c2_pos >= c2_neg:
    if f2_error_rate > c2_neg / f2_count["C"]:
        f2_outcome = 1
        f2_error_rate = c2_neg / f2_count["C"]
        f2_value = "C"
else:
    if f2_outcome > c2_pos/f2_count["C"]:
        f2_outcome = 0
        f2_error_rate = c2_neg / f2_count["C"]
        f2_value = "C"
#Add f2 error rate to the list.
error_rates.append((f2_error_rate, f2_outcome, f2_value))

h2_pos, h2_neg, n_pos, n_neg = 0, 0, 0, 0
f3_outcome = 0
f3_error_rate = 0

print(f1_count)

for i in range(len(feature3)):
    f3_count[feature3[i]] = f3_count.get(feature3[i], 0) + 1

    #Calculate error rate for H.
    if feature3[i] == "H" and int(res[i]) == 1:
        h2_pos += 1
    elif feature3[i] == "H" and int(res[i]) == 0:
        h2_neg += 1

    #Calculate error rate for N.
    if feature3[i] == "N" and int(res[i]) == 1:
        n_pos += 1
    elif feature3[i] == "N" and int(res[i]) == 0:
        n_neg += 1

#Calcualte error rate for feature3.
if h2_pos >= h2_neg:
    f3_error_rate = h2_neg / f3_count["H"]
    f3_outcome = 1
    f3_value = "H"
else:
    f3_error_rate = h2_pos / f3_count["H"]
    f3_outcome = 0
    f3_value = "H"

if n_pos >= n_neg:
    if f3_error_rate > n_neg/f3_count["N"]:
        f3_error_rate = n_neg / f3_count["N"]
        f3_outcome = 1
        f3_value = "N"
else:
    if f3_error_rate > n_pos / f3_count["N"]:
        f3_error_rate = n_pos / f3_count["N"]
        f3_outcome = 0
        f3_value = "N"
#Add the f3 error rate to the list.
error_rates.append((f3_error_rate, f3_outcome, f3_value))

t_pos, t_neg, f_pos, f_neg = 0, 0, 0, 0
f4_error_rate = 0
f4_outcome = 0

for i in range(len(feature4)):
    f4_count[feature4[i]] = f4_count.get(feature4[i], 0) + 1
    #Calcualte error rate for T.
    if feature4[i] == "T" and int(res[i]) == 1:
        t_pos += 1
    elif feature4[i] == "T" and int(res[i]) == 0:
        t_neg += 1

    #Calcualte error rate for F.
    if feature4[i] == "F" and int(res[i]) == 1:
        f_pos += 1
    elif feature4[i] == "F" and int(res[i]) == 0:
        f_neg += 1


#Calculate f4 error rate.
if t_pos >= t_neg:
    f4_error_rate = t_neg / f4_count["T"]
    f4_outcome = 1
    f4_value = "T"
else:
    f4_error_rate = t_pos / f4_count["T"]
    f4_outcome = 0
    f4_value = "T"

if f_pos >= f_neg:
    if f4_error_rate >= f_neg / f4_count["F"]:
        f4_error_rate = f_neg / f4_count["F"]
        f4_outcome = 1
        f4_value = "F"
    else:
        if f4_error_rate > f_pos / f4_count["F"]:
            f4_error_rate = f_pos / f4_count["F"]
            f4_outcome = 0
            f4_value = "F"

error_rates.append((f4_error_rate, f4_outcome, f4_value))
x = min(error_rates)
ind = error_rates.index(x)
print(ind)
oner_rule = "If feature" + str(ind + 1) + " = " + str((x[2])) + " then class = " + str(x[1]) + "."
final_error = "The error rate is " + str(x[0]) + ". "
print(oner_rule)
print(final_error)
