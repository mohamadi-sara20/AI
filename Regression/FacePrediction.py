import numpy as np
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore")
import scipy.io
import matplotlib.pyplot as plt
import math

mat = scipy.io.loadmat("faces.mat")
raw = mat['faces']
data = np.transpose(raw)

images = np.empty((0,64*64), int)
for i in range(len(data)):
    b= data[i].reshape(64, 64)
    b = b.transpose()
    images =  np.concatenate((images, b.reshape(-1, 64*64)))
    plt.axis("off")
    plt.imshow(b, cmap="gray")
    if i < 300:
        plt.savefig('inputImages/train/{}.png'.format(i))
    else:
        plt.savefig('inputImages/test/{}.png'.format(i-300))
    plt.close()

train_set = images[:300]
test_set = images[300:]

half_pixels = 64*32

train_upper = train_set[:,:half_pixels]
train_lower = train_set[:, half_pixels:]
test_upper = test_set[:, :half_pixels]
test_lower = test_set[:, half_pixels:]

reg = LinearRegression()
reg.fit(train_upper, train_lower)
predic_lower = reg.predict(test_upper)

for i in range(0, len(predic_lower) // 10):
    least_error = 1000000
    least_index = 0
    for k in range(i*10, (i+1)*10):
        SquaredError = 0
        for j in range(half_pixels):
            SquaredError += (predic_lower[k][j] - test_lower[k][j]) ** 2
        RootSquaredError = math.sqrt(SquaredError / half_pixels)
        if (RootSquaredError < least_error):
            least_error = RootSquaredError
            least_index = k

    print('For person {0}, Root Mean Squared Error equals {1:.3f} in picture {2} '.format(i+1, least_error, least_index))


for i in range(0, len(predic_lower)):
    predicted_face = np.hstack((test_upper[i], predic_lower[i]))
    b = predicted_face.reshape(64, 64)
    plt.axis("off")
    plt.imshow(b, cmap="gray")
    plt.savefig('outputImages/{}.png'.format(i))
    plt.close()
