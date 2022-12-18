import pickle

def procitajFajl(imeFajla):
    with open(imeFajla, 'rb') as fr:
        return pickle.load(fr)