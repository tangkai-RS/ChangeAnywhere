_base_ = [
    '../_base_/models/fc_siam_conc.py',
    '../common/standard_256x256_50e_sysucd.py']

load_from = './workdir/changeanywhere/fc_siam_conc_workdir/best_mIoU_iter_330000.pth'

ann_file = 'dataset_list/sysucd-train-5%.txt'

train_dataloader = dict(dataset=dict(ann_file=ann_file))
