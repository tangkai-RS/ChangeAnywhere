_base_ = [
    '../_base_/models/snunet_c16.py',
    '../common/standard_256x256_50e_sysucd.py']

ann_file = 'dataset_list/sysucd-train-50%.txt'

train_dataloader = dict(dataset=dict(ann_file=ann_file))

base_channels = 32
model = dict(
    backbone=dict(base_channel=base_channels),
    decode_head=dict(
        in_channels=base_channels * 4,
        channels=base_channels * 4))