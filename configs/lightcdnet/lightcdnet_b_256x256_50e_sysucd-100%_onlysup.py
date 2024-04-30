_base_ = [
    '../_base_/models/lightcdnet.py',
    '../common/standard_256x256_50e_sysucd.py']

ann_file = 'dataset_list/sysucd-train-100%.txt'

train_dataloader = dict(dataset=dict(ann_file=ann_file))

model = dict(
    decode_head=dict(
        sampler=dict(type='mmseg.OHEMPixelSampler', thresh=0.7, min_kept=100000)),
    backbone=dict(net_type="base"),
    neck=dict(in_channels=[24, 116, 232, 464]))