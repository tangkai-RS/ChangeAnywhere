_base_ = [
    '../_base_/models/fc_siam_diff.py',
    '../common/standard_256x256_50e_sysucd.py']

ann_file = 'dataset_list/sysucd-train-5%.txt'

train_dataloader = dict(dataset=dict(ann_file=ann_file))
