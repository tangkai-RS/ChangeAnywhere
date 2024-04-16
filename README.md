# ChangeAnywhere
[ChangeAnywhere: Sample Generation for Remote Sensing Change Detection via Semantic Latent Diffusion Model](https://arxiv.org/pdf/2404.08926.pdf)

## Abstract
Remote sensing change detection (CD) is a pivotal technique that pinpoints changes on a global scale based on multi-temporal images. With the recent expansion of deep learning, supervised deep learning-based CD models have shown satisfactory performance. However, CD sample labeling is very time-consuming as it is densely labeled and requires expert knowledge. To alleviate this problem, we introduce ChangeAnywhere, a novel CD sample generation method using the semantic latent diffusion model and single-temporal images. Specifically, ChangeAnywhere leverages the relative ease of acquiring large single-temporal semantic datasets to generate large-scale, diverse, and semantically annotated bi-temporal CD datasets. ChangeAnywhere captures the two essentials of CD samples, i.e., change implies semantically different, and non-change implies reasonable change under the same semantic constraints. We generated ChangeAnywhere-100K, the largest synthesis CD dataset with 100,000 pairs of CD samples based on the proposed method. The ChangeAnywhere-100K significantly improved both zero-shot and few-shot performance on two CD benchmark datasets for various deep learning-based CD models, as demonstrated by transfer experiments. This paper delineates the enormous potential of ChangeAnywhere for CD sample generation and demonstrates the subsequent enhancement of model performance. Therefore, ChangeAnywhere offers a potent tool for remote sensing CD.

## TODO
- [ ] 2024-04 release the pre-trained weights of binary change detection models and configs
- [ ] 2024-05 release the pre-trained weights of semantic change detection models and configs
- [ ] 2024-06 release the generation codes and model weights of the ChangeAnywhere
- [ ] release the ChangeAnywhere-100K
- [ ] release the training codes of the ChangeAnywhere

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
