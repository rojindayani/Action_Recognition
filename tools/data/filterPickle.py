import pickle
import copy
from mmcv import dump
def mapLabel(num):

    if num == 1:
        return 0
    if num == 7:
        return 1
    if num == 8:
        return 2
    if num == 58:
        return 3
    if num == 98:
        return 4
def mapFrameDir(frame_dir):
    if int(frame_dir[-3:]) == 2:
        return frame_dir[:-3] + '001'
    if int(frame_dir[-3:]) == 8:
        return frame_dir[:-3] + '002'
    if int(frame_dir[-3:]) == 9:
        return frame_dir[:-3] + '003'
    if int(frame_dir[-3:]) == 59:
        return frame_dir[:-3] + '004'
    if int(frame_dir[-3:]) == 99:
        return frame_dir[:-3] + '005'

with open('ntu120_hrnet.pkl', 'rb') as f:
    data = pickle.load(f)

labels = [2, 8, 9, 59, 99]
annotations = data['annotations']
split = data['split']
print("editing annotations")
new_annos = [anno for anno in annotations if int(anno['frame_dir'][-3:]) in labels]

print("editing splits")
new_split = {}
for key, value in split.items():
    print(".")
    new_split[key] = [name for name in value if any(anno['frame_dir'] == name for anno in new_annos)]

final_annos = []
for anno in new_annos:
    print('..')
    new_anno = copy.deepcopy(anno)
    new_anno['frame_dir'] = mapFrameDir(anno['frame_dir'])
    new_anno['label'] = mapLabel(int(anno['label']))
    final_annos.append(new_anno)

final_split = {}
for key, value in new_split.items():
    final_split[key] = []
    print('...')
    for item in new_split[key]:
        final_split[key].append(mapFrameDir(item))

print("creating pickle...")
dump(dict(split=final_split, annotations=final_annos), 'ntu5.pkl')
