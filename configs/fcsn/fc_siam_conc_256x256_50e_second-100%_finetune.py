_base_ = [
    '../_base_/models/fc_siam_conc.py',
    '../common/standard_256x256_50e_second.py']

load_from = './workdir/changeanywhere/fc_siam_conc_workdir/best_mIoU_iter_330000.pth'
