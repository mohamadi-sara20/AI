from copy import deepcopy
import re
from math import log2
import csv

class Node(object):
    def __init__(self):
        self.selected_feature = ""
        self.feature_value = ""
        self.label = ""
        self.children = []
        self.count = 0
        self.c = 0

    def print_node(self):
        print("Feature "+self.selected_feature + " Value: " +  self.feature_value + "  Path: " + self.label
              + " #Samples: " + str(self.count))


def read_data(filename):

    with open(filename) as f:
        t = f.readlines()
    del t[0]
    for i in range(len(t)):
        t[i] = re.sub(r"\n", "", t[i])

    return t


def headers(filename):

    with open(filename) as f:
        datareader = csv.reader(f, delimiter=',')
        headers = next(datareader)
    headers.pop()

    return headers


def get_features(data):
    '''Extracts and stores the features in a list.'''
    x = 0
    for i in range(len(data)):
        data[i] = data[i].split(",")
        x = len(data[i])
    # features = [[f1], [f2], [f3] ... [f10]]
    features = [[] for i in range(x)]
    for i in range(len(data)):
        for j in range(len(data[i])):
            features[j].append(data[i][j])

    return features


def num_to_nom(feature):

    average, sum = 0, 0
    NominalFeature = []
    for i in range(len(feature)):
        sum += int(feature[i])
    average = sum / len(feature)
    for i in range(len(feature)):
        if float(feature[i]) >= average:
            NominalFeature.append("High")
        else:
            NominalFeature.append("Low")

    return NominalFeature


def entropy_s(S):
    '''Returns the entropy on all samples.'''
    val = {}
    for i in range(len(S)):
        val[S[i]] = val.get(S[i], 0) + 1
    ent = 0
    for key in val:
        probability = val[key] / len(S)
        ent += -probability * log2(probability)

    return ent


def get_entropy(data, i):

    X, T = [], []
    for j in range(len(data)):
        X.append(data[j][i])
        T.append(data[j][-1])

    #dic = {sunny: (10, 20)}
    dic = {}
    for i in range(len(X)):
        dic[X[i]] = dic.get(X[i], 0) + 1
    # f1 = {sunny: (2, 1),...}
    f1 = {key: [0, 0] for key in dic}

    for i in range(len(X)):
        for j in dic:
            if X[i] == j:
                if T[i] == str(1):
                    f1[j][0] += 1
                else:
                    f1[j][1] += 1

    ent, temp_sum = 0, 0
    entropy = []
    for v in f1.values():
        e = 0
        for j in v:
            prob = j / sum(v)
            if prob == 0:
                ent = 0
            else:
                ent = -prob * log2(prob)
            temp_sum += sum(v)
        e += ent
        entropy.append((e, sum(v)/temp_sum))
    res = 0
    for i in range(len(entropy)):
        res += entropy[i][1] * entropy[i][0]

    return res


def split(subsets, feature):
    ind = features.index(feature)
    dic = {}
    for i in range(len(feature)):
        dic[feature[i]] = dic.get(feature[i], 0) + 1

    s_array = []
    for subset in subsets:
        arr = []
        for v in dic.keys():
            v_array = []
            for row in subset:
                if row[ind] == v:
                    v_array.append(row)

            arr.append(v_array)
        s_array.append(arr)
    return s_array


def get_class(rows):
    p, q = 0, 0
    for i in range(len(rows)):
        if rows[i][-1] == "1":
            p += 1
        if rows[i][-1]=="2":
            q += 1
    if p >= q:
        return 1
    return 2


def create_tree(data, remaining_features, headers, parent_label):

    node = Node()
    if headers == []:
        return node
    e = []
    for feature in remaining_features:
        ind = features.index(feature)
        ent = get_entropy(data, ind)
        e.append(ent)
    min_ent = min(e)
    ind_min_ent = e.index(min(e))
    data_list = split([data], remaining_features[ind_min_ent])
    sf = remaining_features[ind_min_ent]
    del remaining_features[ind_min_ent]
    sh = headers[ind_min_ent]
    del headers[ind_min_ent]
    counter = 0
    for row in data_list[0]:
        rem = deepcopy(remaining_features)
        head = deepcopy(headers)
        counter += 1
        if row != []:
            label = parent_label + "-" + str(counter)
            child = create_tree(row, rem, head, label)
            child.selected_feature = sh
            child.feature_value = row[0][int(sh)-1]
            child.label = str(parent_label) + "-" + str(counter)
            child.count = len(row)
            child.c = get_class(row)
            node.children.append(child)
            child.print_node()
    return node


def find_class(node, sample):
    if node.children == []:
        return node.c
    for child in node.children:
        if sample[int(child.selected_feature)-1] == child.feature_value:
            return find_class(child, sample)
    return node.c


#Main
raw_data= read_data("pregnancy_data2 - train.csv")
#rows = read_rows("pregnancy_data2 - train.csv")
features = get_features(raw_data)
feat1, feat4 = num_to_nom(features[0]), num_to_nom(features[3])
S = features[-1]
features[0], features[3] = feat1, feat4
headers = headers("pregnancy_data2 - train.csv")

#Make rows of training samples.
data = []
for row in range(0, 911):
    n = []
    for col in (features):
        n.append(col[row])
    data.append(n)


remaining_features = features[:len(features)-1]
id3 = create_tree(data, remaining_features, headers, "")



# Read test data.
test_cases = read_data("pregnancy_data2 - test.csv")
f = get_features(test_cases)
feat1, feat4 = num_to_nom(f[0]), num_to_nom(f[3])
f[0], f[3] = feat1, feat4
real_class = f[-1]

test_data = []
for row in range(0, len(test_cases)):
    n = []
    for col in (f):
        n.append(col[row])
    test_data.append(n)



#Calculate accuracy, precision and recall.
predictions = []
for test_case in test_data:
    predictions.append(find_class(id3, test_case))

c = 0
for i in range(len(predictions)):
    if str(predictions[i]) == real_class[i]:
        c += 1

acc = c / len(real_class)

TP, TN, FP, FN = 0, 0, 0, 0
for i in range(len(predictions)):
    if str(predictions[i]) == real_class[i]:
        if real_class[i] == "2":
            TP += 1
        else:
            TN += 1
    else:
        if real_class[i] == "2":
            FN += 1
        else:
            FP += 1

precision = TP / (TP + FP)
recall = TP / (TP + FN)

print("Accuracy = {}, Precision = {} and Recall = {}".format(acc, precision, recall))
