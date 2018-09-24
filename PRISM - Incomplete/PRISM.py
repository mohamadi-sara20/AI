import pandas as pd
def num_to_nom(feature):
    c = 0
    for i in range(len(feature)):
        if feature[i]!= "?":
            c += 1
    average = sum(feature) / c
    p = []
    for i in range(len(feature)):
        if feature[i] >= average:
            p.append("high")
        else:
            p.append("low")
    return p

df = pd.read_csv('data_heart.csv')
features = [df["age"], df["sex"], df["cp"],df["trestbps"], df["col"], df["chol"], df["fbs"], df["restecg"], df["thalach"], df["exang"], df["oldpeak"], df["slope"], df["ca"], df["thal"]]
c = df["num"]
numeric_features = [pd.to_numeric(features[0], downcast = "float"), pd.to_numeric(features[3], downcast = "float"),
                    pd.to_numeric(features[4], downcast = "float"), pd.to_numeric(features[5], downcast = "float"),
                    pd.to_numeric(features[8], downcast = "float"), pd.to_numeric(features[10], downcast = "float")]
#convert numeric features to nominal.
f = []
for i in range(len(numeric_features)):
    f.append(num_to_nom(numeric_features[i]))

# Combine all features into one variable.
fs = [f[0], features[1], features[2],f[1], f[2], f[3], features[6], features[7],
      f[4], features[9],f[5],features[11], features[12], features[13]]
#Get the frequencies.
freq = [["age",{}], ["sex",{}], ["cp",{}],["trestbps", {}], ["col", {}],
        ["chol", {}], ["fbs",{}],["restecg", {}],["thalach", {}],["exang", {}],["oldpeak", {}],
        ["slope", {}], ["ca", {}], ["thal", {}]]

for i in range(len(fs)):
    for j in range(len(fs[i])):
        freq[i][1][fs[i][j]] = freq[i][1].get(fs[i][j], 0) + 1


#Get the stats for the two classes <50 and >50_1.
k = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
p = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
for i in range(len(fs)):
    for j in range(len(fs[i])):
        for key in freq[i][1].keys():
            if fs[i][j] == key and c[j] == "<50":
                k[i][fs[i][j]] = k[i].get(fs[i][j], 0)  + 1
            elif fs[i][j] == key and c[j] == ">50_1":
                p[i][fs[i][j]] = p[i].get(fs[i][j], 0) + 1

#Get the error rate for each feature.
for i in range(len(k)):
    k[i] = list(k[i].items())

h = []
for i in range(len(k)):
    for j in range(len(k[i])):
        if(k[i][j][0])=="?" or k[i][j][0] == "st_t_wave_abnormality":
            h.append((i,j))

#delete abnormalities and missing data.
for i in range(len((h))):
    del k[h[i][0]][h[i][1]]

errors = []
vals = []
for i in range(len(k)):
    m, n = [], []
    for j in range(len(k[i])):
        m.append(k[i][j][1])
        n.append(k[i][j][0])
    error = min(m) / sum(m)
    val = n[m.index(max(m))]
    errors.append(error)
    vals.append(val)

d = min(errors)
ind = errors.index(d)
rule = []
rule.append((ind, vals[ind], "<50"))


#Find the indices of the instances covered and not covered.
r = []
n =0
for i in range(len(fs[ind])):
    if fs[ind][i] == vals[ind]:
        if c[i] != "<50":
            r.append(i)
d = []
for i in range(len(fs[ind])):
    if fs[ind][i] == vals[ind]:
        if c[i] == "<50":
            n+=1
            d.append(i)

del freq[ind]
del fs[ind]


def GetRule(fs, freq):
    for i in range(len(fs)):
        for j in range(len(fs[i])):
            freq[i][1][fs[i][j]] = freq[i][1].get(fs[i][j], 0) + 1

    # Get the stats for the two classes <50 and >50_1.
    k = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    p = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    for i in range(len(fs)):
        for j in range(len(fs[i])):
            for key in freq[i][1].keys():
                if fs[i][j] == key and c[j] == "<50":
                    k[i][fs[i][j]] = k[i].get(fs[i][j], 0) + 1
                elif fs[i][j] == key and c[j] == ">50_1":
                    p[i][fs[i][j]] = p[i].get(fs[i][j], 0) + 1

    # Get the error rate for each feature.
    for i in range(len(k)):
        k[i] = list(k[i].items())

    h = []
    for i in range(len(k)):
        for j in range(len(k[i])):
            if (k[i][j][0]) == "?" or k[i][j][0] == "st_t_wave_abnormality":
                h.append((i, j))

    # delete abnormalities and missing data.
    for i in range(len((h))):
        del k[h[i][0]][h[i][1]]

    g = []
    for i in range(len(k)):
        if k[i] == []:
            g.append(i)
    for i in range(len(g)):
        del k[g[i]]

    errors = []
    vals = []
    for i in range(len(k)):
        m, n = [], []
        for j in range(len(k[i])):
            m.append(k[i][j][1])
            n.append(k[i][j][0])
        error = min(m) / sum(m)
        val = n[m.index(max(m))]
        errors.append(error)
        vals.append(val)
    d = min(errors)
    ind = errors.index(d)
    rule.append((ind +1 , vals[ind], "<50"))
    return rule




















    stopwords = read_stopwords("stopwords.csv")
    for i in range(len(messages)):
        pat = re.compile(r"[0-9]")
        messages[i] = re.sub(pat, "", messages[i])

    import string
    ms = []
    for i in range(len(messages)):
        purified_message = ""
        for j in range(len(messages[i])):
            if messages[i][j] not in string.punctuation:
                purified_message += messages[i][j]
        ms.append(purified_message)

        for j in range(len(stopwords)):
            pat = re.compile(r" " + stopwords[j] + " ")
            ms[i] = re.sub(pat, " ", ms[i])
