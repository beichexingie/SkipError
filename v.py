import pickle

path = 'C:\\Users\ACER\PycharmProjects\SkipError\Code\data\\attr_ac.pkl'  # path='/root/……/aus_openface.pkl'   pkl文件所在路径

f = open(path, 'rb')
data = pickle.load(f)

print(data)
print(len(data))