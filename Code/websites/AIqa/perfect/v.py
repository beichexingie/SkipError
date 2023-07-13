import pickle

path = 'D:\perfect\code\kbdemo\search\data\\attr_ac.pkl'  # path='/root/……/aus_openface.pkl'   pkl文件所在路径

f = open(path, 'rb')
data = pickle.load(f)

print(data)
print(len(data))