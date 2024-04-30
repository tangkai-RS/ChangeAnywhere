_base_ = [
    '../_base_/models/bit_r18.py', 
    '../common/standard_256x256_50e_second.py']

model = dict(pretrained=None)

load_from = './workdir/changeanywhere/bit_workdir/best_mIoU_iter_500000.pth'

