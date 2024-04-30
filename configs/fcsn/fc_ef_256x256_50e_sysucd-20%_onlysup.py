_base_ = [
    '../_base_/models/fc_ef.py',
    '../common/standard_256x256_50e_sysucd.py']

ann_file = 'dataset_list/sysucd-train-20%.txt'

train_dataloader = dict(dataset=dict(ann_file=ann_file))