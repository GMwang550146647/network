import pickle
d = dict(name='Bob', age=20, score=88)
with open("3.files/test.txt",'wb') as f:
    pickle.dump(d,f,0)
with open("3.files/test.txt",'rb') as f:
    di=pickle.load(f)
print(di)
