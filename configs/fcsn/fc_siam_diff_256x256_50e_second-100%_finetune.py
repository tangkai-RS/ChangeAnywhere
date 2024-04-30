_base_ = [
    '../_base_/models/fc_siam_diff.py',
    '../common/standard_256x256_50e_second.py']

load_from = './workdir/changeanywhere/fc_siam_diff_workdir/best_mIoU_iter_450000.pth'
