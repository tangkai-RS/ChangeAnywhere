_base_ = [
    '../_base_/models/changeformer_mit-b0.py', 
    '../common/standard_256x256_50e_second.py']

load_from = './workdir/changeanywhere/changeformer_workdir/best_mIoU_iter_480000.pth'

ann_file = 'dataset_list/second-train-5%.txt'

train_dataloader = dict(dataset=dict(ann_file=ann_file))

# model settings
model = dict(
    pretrained=None,
    backbone=dict(
        embed_dims=64, num_heads=[1, 2, 5, 8], num_layers=[2, 2, 2, 2]),
    decode_head=dict(in_channels=[v * 2 for v in [64, 128, 320, 512]]))

# optimizer
optimizer=dict(
    type='AdamW', lr=1e-4, betas=(0.9, 0.999), weight_decay=0.01)
optim_wrapper = dict(
    _delete_=True,
    type='OptimWrapper',
    optimizer=optimizer,
    paramwise_cfg=dict(
        custom_keys={
            'pos_block': dict(decay_mult=0.),
            'norm': dict(decay_mult=0.),
            'head': dict(lr_mult=10.)
        }))