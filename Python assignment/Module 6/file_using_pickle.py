import pickle
'''
phonebook={'sim':'4356','defdg':'3456','reg':'3245'}
f=open('hy.txt',"wb")
pickle.dump(phonebook,f)
f.close()

'''

inp=open("hy.txt","rb")
pb=pickle.load(inp)
inp.close()
print(pb)