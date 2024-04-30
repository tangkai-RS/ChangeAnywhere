_base_ = [
    '../_base_/models/bit_r18.py', 
    '../common/standard_256x256_50e_second.py']

load_from = './workdir/changeanywhere/bit_workdir/best_mIoU_iter_500000.pth'

ann_file = 'dataset_list/second-train-20%.txt'

model = dict(pretrained=None)

train_dataloader = dict(dataset=dict(ann_file=ann_file))


