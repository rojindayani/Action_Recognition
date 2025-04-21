import pickle
import copy


def mapp(num):

    if num == 1:
        return 0
    if num == 7:
        return 1
    if num == 8:
        return 2
    if num == 58:
        return 3

with open('ntu4.pkl', 'rb') as f:
    data = pickle.load(f)

print(data['annotations'][:10])
print('\n')
print(data['split']['xsub_val'][:10])
print('\n')

# final_annos = []
#
# for anno in data['annotations']:
#     print('..')
#     new_anno = copy.deepcopy(anno)
#     new_anno['label'] = mapp(int(anno['label']))
#     final_annos.append(new_anno)
#
# from mmcv import dump
#
# print("creating pickle...")
# dump(dict(split=data['split'], annotations=final_annos), 'ntu4.pkl')

