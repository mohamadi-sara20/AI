import re
import random
import string

def read_stopwords(Filename):
    '''Reads the stopwords file in the same directory given the name.
    Input: Filename (str)
    Output: t (str)
    '''
    with open(Filename) as f:
        t = f.read()
        t = t.split(",")
    for i in range(len(t)):
        t[i] = re.sub(r"\s", "",t[i])
    return t

def normalize(message):
    '''Gets a message and normalizes it; removing stopwords, numbers and punctuation marks.
    Input: message (str)
    Output: message (str)
    '''

    message = message.lower()
    stopwords = read_stopwords("stopwords.csv")

    #remove punctuation marks.
    message = message.lower()
    punc = string.punctuation
    pat = re.compile(r"[" + punc + "]")
    message = re.sub(pat, r" ", message)

    #remove numbers.
    pat = re.compile(r"[0-9]")
    message = re.sub(pat, "", message)
    message = " " + message + " "

    #remove stopwords.
    for j in range(len(stopwords)):
        pat = re.compile(r" " + stopwords[j] + " ")
        message = re.sub(pat, " ", message)


    #pat = re.compile(r"[^a-z\s]")
    message = re.sub(pat, " ", message)

    pat = re.compile(r"\s{2,}")
    message = re.sub(pat, r" ", message)

    return message

def read_data(Filename):
    '''Reads the data file.
    Input: Filename(str)
    Output: ms(str), c(str)
    '''

    with open(Filename) as f:
        t = f.readlines()
    del t[0]

    #Shuffle the list.
    random.shuffle(t)
    messages = []
    c = []

    #Store the messages and the classes in two variables.
    for i in range(len(t)):
        t[i] = t[i].split('"')
        c.append(t[i][1])
        messages.append(t[i][3])

    ms =[]
    for i in range(len(messages)):
        text = normalize(messages[i])
        ms.append(text)
        text = ""

    return ms, c


def lemmatize(text):
    ''' Lemmatizes the text.
    Input: text(list)
    Output: messages (list)
    '''
    import nltk
    from nltk.stem.wordnet import WordNetLemmatizer
    lemmatize = WordNetLemmatizer()
    messages = []
    for i in range(len(text)):
        messages.append(text[i].split())

    for i in range(len(messages)):
        for j in range(len(messages[i])):
            messages[i][j] = lemmatize.lemmatize(messages[i][j])

    return messages


#Don't
def del_dup(message):
    '''Removes duplicate words from a message.
    Input: message(list)
    Output: res (list)
    '''
    res = []
    for i in range(len(message)):
        if message[i] not in res:
            res.append(message[i])
    return res

def separate_messages(x, start, end):
    '''Separates spam messages from non-spam messages.
    Input: x (list), start (int), end (int)
    Output: spam(list), ham(list)
    '''
    l = [[], []]
    for i in range(start, end):
        if x[1][i] == "spam":
            l[0].append(i)
        else:
            l[1].append(i)

    spam = []
    ham = []
    for i in l[0]:
        spam.append(x[0][i])
    for i in l[1]:
        ham.append(x[0][i])

    return spam, ham


def vectorize(text):
    '''Returns the feature vector.
    Input: text (list)
    Output: dic (dict), c (int)
    '''

    dic = {}
    for i in range(len(text)):
        unique = del_dup(text[i])
        for j in range(len(unique)):
            if unique[j] not in dic:
                dic[unique[j]] = 1
            else:
                dic[unique[j]] += 1

    return dic


data, c = read_data("sms_spam.csv")

r = int((len(c) * 80) / 100)
spam = separate_messages([data, c], 0, r + 1)[0]
n = lemmatize(spam)
len_spam = len(n)
dic_spam = vectorize(n)
ham = separate_messages([data, c], 0, r + 1)[1]
n = lemmatize(ham)
len_ham = len(n)
dic_ham = vectorize(n)
n += lemmatize(spam)
len_dic = len(n)
dic_corpus = vectorize(n)
p_ham = len(ham) / (len(spam) + len(ham))
p_spam = len(spam) / (len(spam) + len(ham))


def classify(message):
    '''Classifies a new message as <spam> or <ham>.
    Input: message (str)
    Output: (str)
    '''

    message = del_dup(message.split())
    x, g = 1, 1

    for word in message:
        if word in dic_ham:
            x *= dic_ham[word] / len_ham

        if word in dic_spam:
            g *= dic_spam[word] / len_spam

    p1 = (x * len_ham/(len_ham + len_spam))
    p2 = (x * len_spam/(len_spam + len_ham))
    if p1 >= p2:
        return "ham"
    return "spam"


def test(message, c):
    TP, FP, TN, FN = 0, 0, 0, 0
    counter = 0
    for i in range(r + 1, len(message) - 1):
        real = c[i]
        pred = classify(message[i])
        if pred == real:
            counter += 1
            if pred == "ham":
                TN += 1
            else:# pred == "spam":
                TP += 1
        if pred != real:
            if pred == "ham":
                FN += 1
            else:# pred == "spam":
                FP += 1
    return counter / (len(message) - 1 - (r + 1)), (TP, FP, TN, FN)

acc = test(data, c)[0]
for i in range(9):
    acc += test(data, c)[0]

buf = "TP = %d , FP = %d , TN = %d , FN = %d" % test(data, c)[1]
print(buf)
print("Accuracy = {0:.2f}".format(acc/10))

