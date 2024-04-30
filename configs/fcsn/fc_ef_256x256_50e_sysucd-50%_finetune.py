_base_ = [
    '../_base_/models/fc_ef.py',
    '../common/standard_256x256_50e_sysucd.py']

load_from = './workdir/changeanywhere/fc_ef_workdir/best_mIoU_iter_490000.pth'

ann_file = 'dataset_list/sysucd-train-50%.txt'

train_dataloader = dict(dataset=dict(ann_file=ann_file))