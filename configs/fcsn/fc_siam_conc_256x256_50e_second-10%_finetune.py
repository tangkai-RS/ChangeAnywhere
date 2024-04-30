_base_ = [
    '../_base_/models/fc_siam_conc.py',
    '../common/standard_256x256_50e_second.py']

load_from = './workdir/changeanywhere/fc_siam_conc_workdir/best_mIoU_iter_330000.pth'

ann_file = 'dataset_list/second-train-10%.txt'

train_dataloader = dict(dataset=dict(ann_file=ann_file))
