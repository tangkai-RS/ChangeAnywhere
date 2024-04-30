_base_ = [
    '../_base_/models/fc_siam_diff.py',
    '../common/standard_256x256_50e_second.py']

load_from = './workdir/changeanywhere/fc_siam_diff_workdir/best_mIoU_iter_450000.pth'

ann_file = 'dataset_list/second-train-5%.txt'

train_dataloader = dict(dataset=dict(ann_file=ann_file))
