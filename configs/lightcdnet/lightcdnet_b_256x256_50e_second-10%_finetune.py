_base_ = [
    '../_base_/models/lightcdnet.py',
    '../common/standard_256x256_50e_second.py']

load_from = './workdir/changeanywhere/lightcdnet_workdir/best_mIoU_iter_500000.pth'

ann_file = 'dataset_list/second-train-10%.txt'

train_dataloader = dict(dataset=dict(ann_file=ann_file))

model = dict(
    decode_head=dict(
        sampler=dict(type='mmseg.OHEMPixelSampler', thresh=0.7, min_kept=100000)),
    backbone=dict(net_type="base"),
    neck=dict(in_channels=[24, 116, 232, 464]))