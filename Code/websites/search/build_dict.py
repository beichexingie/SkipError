import ahocorasick
import pickle
from collections import defaultdict


#主体的AC机
entity_list_file = './data/all_entity.txt'
entity_out_path = './data/ent_ac.pkl'

#自己建立的
attr_list_file = './data/three_attr_mapping.txt'
attr_out_path = './data/attr_ac.pkl'

val_list_file = './data/three_val.txt'


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
    f = open(attr_mapping_file,encoding="utf-8")
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


#
#
# import ahocorasick
# import pickle
# from collections import defaultdict
#
# '''
# entity_list_file = './data/all_entity.txt'
# entity_out_path = './data/ent_ac.pkl'
# attr_list_file = './data/attr_mapping.txt'
# attr_out_path = './data/attr_ac.pkl'
# val_list_file = './data/Person_val.txt'
# '''
#
#
# dirhead='D:\perfect\code\kbdemo\search\data\\'
#
# entity_list_file =dirhead+ 'all_entity.txt'
# entity_out_path = dirhead +'ent_ac.pkl'
# attr_list_file = dirhead +'three_attr_mapping.txt'
# attr_out_path = dirhead +'attr_ac.pkl'
# val_list_file = dirhead +'three_val.txt'
#
# def dump_ac_entity_dict(list_file,out_path):
#     A = ahocorasick.Automaton()
#     f = open(list_file)
#     i = 0
#     for line in f:
#         word = line.strip()
#         A.add_word(word, (i, word))
#         i += 1
#     A.make_automaton()
#     pickle.dump(A,open(out_path,"wb"))
# # def dump_ac_entity_dict(list_file,out_path):
# #     A = ahocorasick.Automaton()
# #     f = open(list_file,encoding="utf-8")
# #     i = 0
# #     for line in f:
# #         word = line.strip()
# #         A.add_word(word, (i, word))
# #         i += 1
# #     A.make_automaton()
# #     pickle.dump(A,open(out_path,"wb"))
#
# def dump_ac_attr_dict(attr_mapping_file, out_path):
#     A = ahocorasick.Automaton()
#     f = open(attr_mapping_file)
#     i = 0
#     for line in f:
#         parts = line.strip().split(" ")
#         for p in parts:
#             if p != "":
#                 A.add_word(p,(i,p))
#                 i += 1
#     A.make_automaton()
#     pickle.dump(A,open(out_path,'wb'))
# # def dump_ac_attr_dict(attr_mapping_file, out_path):
# #     A = ahocorasick.Automaton()
# #     f = open(attr_mapping_file,encoding="utf-8")
# #     i = 0
# #     for line in f:
# #         parts = line.strip().split(" ")
# #         for p in parts:
# #             if p != "":
# #                 A.add_word(p,(i,p))
# #                 i += 1
# #     A.make_automaton()
# #     pickle.dump(A,open(out_path,'wb'))
#
#
# def load_ac_dict(out_path):
#     A = pickle.load(open(out_path,"rb"))
#     return A
#
# def load_attr_map(attr_mapping_file):
#     f = open(attr_mapping_file)
#     mapping = defaultdict(list)
#     for line in f:
#         parts = line.strip().split(" ")
#         for p in parts:
#             if p != '':
#                 mapping[p].append(parts[0])
#     return mapping
# # def load_attr_map(attr_mapping_file):
# #     f = open(attr_mapping_file,encoding="utf-8")
# #     mapping = defaultdict(list)
# #     for line in f:
# #         parts = line.strip().split(" ")
# #         for p in parts:
# #             if p != '':
# #                 mapping[p].append(parts[0])
# #     return mapping
#
#
# def load_entity_dict(entity_file):
#     f = open(entity_file)
#     ents = {}
#     for line in f:
#         ents[line.strip()] = 1
#     return ents
#
# # def load_entity_dict(entity_file):
# #     f = open(entity_file,encoding="utf-8")
# #     ents = {}
# #     for line in f:
# #         ents[line.strip()] = 1
# #     return ents
#
# def load_val_dict(val_file):
#     f = open(val_file)
#     val_attr_map = {}
#     for line in f:
#         parts = line.strip().split(" ")
#         val_attr_map[parts[0]] = parts[1]
#     return val_attr_map
# # def load_val_dict(val_file):
# #     f = open(val_file,encoding="utf-8")
# #     val_attr_map = {}
# #     for line in f:
# #         parts = line.split(" ")
# #         val_attr_map[parts[0]] = parts[1]
# #     return val_attr_map
#
# if __name__ == '__main__':
#     dump_ac_attr_dict(attr_list_file, attr_out_path)
#     # load_val_dict(val_list_file)
