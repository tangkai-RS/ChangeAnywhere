_base_ = [
    '../_base_/models/bit_r18.py', 
    '../common/standard_256x256_50e_second.py']

ann_file = 'dataset_list/second-train-20%.txt'

train_dataloader = dict(dataset=dict(ann_file=ann_file))


