## ChangeAnywhere-100K Download link
[Baidu Drive](https://pan.baidu.com/s/1EBrNrDXMI2ZiMvB-ZnXrag?pwd=qhn1), Password: qhn1. 
[Hugging Face](https://huggingface.co/datasets/tangkaii/ChangeAnywhere-100K/tree/main).

## Note: This repository is no longer being maintained, and we will release an upgraded version of ChangeAnywhere soon!

## ChangeAnywhere
[ChangeAnywhere: Sample Generation for Remote Sensing Change Detection via Semantic Latent Diffusion Model](https://arxiv.org/abs/2404.08892)

## Abstract
Remote sensing change detection (CD) is a pivotal technique that pinpoints changes on a global scale based on multi-temporal images. With the recent expansion of deep learning, supervised deep learning-based CD models have shown satisfactory performance. However, CD sample labeling is very time-consuming as it is densely labeled and requires expert knowledge. To alleviate this problem, we introduce ChangeAnywhere, a novel CD sample generation method using the semantic latent diffusion model and single-temporal images. Specifically, ChangeAnywhere leverages the relative ease of acquiring large single-temporal semantic datasets to generate large-scale, diverse, and semantically annotated bi-temporal CD datasets. ChangeAnywhere captures the two essentials of CD samples, i.e., change implies semantically different, and non-change implies reasonable change under the same semantic constraints. We generated ChangeAnywhere-100K, the largest synthesis CD dataset with 100,000 pairs of CD samples based on the proposed method. The ChangeAnywhere-100K significantly improved both zero-shot and few-shot performance on two CD benchmark datasets for various deep learning-based CD models, as demonstrated by transfer experiments. This paper delineates the enormous potential of ChangeAnywhere for CD sample generation and demonstrates the subsequent enhancement of model performance. Therefore, ChangeAnywhere offers a potent tool for remote sensing CD.

## TODO
- [x] 2024-04 release the pre-trained weights of binary change detection models and configs.
- [x] Release the ChangeAnywhere-100K.
- [ ] Release the training codes of ChangeAnywhere.

## Pretrained models on the ChangeAnywhere-100K
[Google Drive](https://drive.google.com/file/d/19jI9Zi2Di0gD-hoZY-6xZ015senCsYBG/view?usp=sharing).  
[Baidu Drive](https://pan.baidu.com/s/16LEXz6hIvn6CQtlupDsvVQ?pwd=9591).

Pretrained Models with the following folder structure
```
│ChangAnywhere/
├──workdir/
│  ├── changeanywhere
│  │   ├── bit_workdir
│  │   ├── changeformer_workdir
│  │   ├── ......
│  ├── ......
```

## Usage
Binary change detection is based on the [open-cd](https://github.com/likyoo/open-cd), please install Open-cd according to its repository.

### Train
```
python tools/train.py configs/changer/changer_ex_r18_256x256_50e_sysucd-100%_finetune.py --work-dir ./workdir/sysucd-100%/changer_ex_r18_256x256_50e_sysucd-100%_finetune_workdir
```
*Note*: please replace the dataset path in configs with yours.
### Infer
```
# get .png results
python tools/test.py workdir/sysucd-100%/changer_ex_r18_256x256_50e_sysucd-100%_finetune_workdir/changer_ex_r18_256x256_50e_sysucd-100%_finetune.py workdir/sysucd-100%/changer_ex_r18_256x256_50e_sysucd-100%_finetune_workdir/last.pth --show-dir tmp_infer
# get metrics
python tools/test.py workdir/sysucd-100%/changer_ex_r18_256x256_50e_sysucd-100%_finetune_workdir/changer_ex_r18_256x256_50e_sysucd-100%_finetune.py workdir/sysucd-100%/changer_ex_r18_256x256_50e_sysucd-100%_finetune_workdir/last.pth --work-dir workdir/sysucd-100%/changer_ex_r18_256x256_50e_sysucd-100%_finetune_workdir >> workdir/sysucd-100%/changer_ex_r18_256x256_50e_sysucd-100%_finetune_workdir/test_log.log 2>&1
```
### Few-shot training
Few-shot dataset split txt with the following folder structure 
```
│ChangAnywhere/
├──SYSU-CD/
│  ├── dataset_list
│  │   ├── sysucd-train-5%
│  │   ├── sysucd-train-10%
│  │   ├── ......
│  ├── train
│  ├── val
│  ├── test
```

## Citation
Please cite the following when using our checkpoints. Also, papers citing the open-cd and related models are needed. More citation information can be found at [configs](configs). 
```bibtex
@misc{tang2024changeanywhere,
      title={ChangeAnywhere: Sample Generation for Remote Sensing Change Detection via Semantic Latent Diffusion Model}, 
      author={Kai Tang and Jin Chen},
      year={2024},
      eprint={2404.08892},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

## Related Work
[ClearSCD](https://github.com/tangkai-RS/ClearSCD) has been accepted by the *ISPRS Journal of Photogrammetry and Remote Sensing*
