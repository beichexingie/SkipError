
import ahocorasick
import pickle
from collections import defaultdict


#主体的AC机
entity_list_file = "D:\\3.0\perfect\code\kbdemo\search\data\\all_entity.txt"
entity_out_path = 'D:\\3.0\perfect\code\kbdemo\search\data\ent_ac.pkl'

#自己建立的
attr_list_file = 'D:\\3.0\perfect\code\kbdemo\search\data\\attr_ac.pkl'
attr_out_path = 'D:\\3.0\perfect\code\kbdemo\search\data\\attr_ac.pkl'

val_list_file = 'D:\\3.0\perfect\code\data\\three_val.txt'


#存入了实体的AC机
def dump_ac_entity_dict(list_file,out_path):
    A = ahocorasick.Automaton()
    f = open(list_file,encoding="utf-8")
    i = 0
    for line in f:
        word = line.strip()
        A.add_word(word, (i, word))
        i += 1
    A.make_automaton()
    pickle.dump(A,open(out_path,"wb"))

def dump_ac_attr_dict(attr_mapping_file, out_path):
    A = ahocorasick.Automaton()
    f = open(attr_mapping_file)
    i = 0
    for line in f:
        parts = line.strip().split(" ")
        for p in parts:
            if p != "":
                A.add_word(p,(i,p))
                i += 1
    A.make_automaton()
    pickle.dump(A,open(out_path,'wb'))
#存入属性的AC机


def load_ac_dict(out_path):
    A = pickle.load(open(out_path,"rb"))
    return A



def load_attr_map(attr_mapping_file):
    f = open(attr_mapping_file,encoding="utf-8")
    mapping = defaultdict(list)
    for line in f:
        parts = line.strip().split(" ")
        for p in parts:
            if p != '':
                mapping[p].append(parts[0])
    return mapping

def load_entity_dict(entity_file):
    f = open(entity_file,encoding="utf-8")
    ents = {}
    for line in f:
        ents[line.strip()] = 1
    return ents

def load_val_dict(val_file):
    f = open(val_file,encoding="utf-8")
    val_attr_map = {}
    for line in f:
        parts = line.split(" ")
        val_attr_map[parts[0]] = parts[1]
    return val_attr_map


if __name__ == '__main__':
    dump_ac_entity_dict(entity_list_file, entity_out_path)
    dump_ac_attr_dict(attr_list_file, attr_out_path)
    #load_val_dict(val_list_file)
