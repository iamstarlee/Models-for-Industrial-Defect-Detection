This repo includes 5 ordinary models and 5 super-resolution models for classifying super-resolution dataset after downscaling.



## 1. Datasets
**[MVTecAD](https://openaccess.thecvf.com/content_CVPR_2019/papers/Bergmann_MVTec_AD_--_A_Comprehensive_Real-World_Dataset_for_Unsupervised_Anomaly_CVPR_2019_paper.pdf)** is a dataset for benchmarking anomaly detection methods with a focus on industrial inspection. It contains over 5000 high-resolution images divided into fifteen different object and texture categories. Each category comprises a set of defect-free training images and a test set of images with various kinds of defects as well as images without defects.

## 2. Metrics
We use the common metric: AUROC (the area under the receiver operating characteristic curve).

## 3. Experiment
Quantitative results of 5 super-resolution methods on MVTecAD
| Models       | mean AUROC       |
|----------|-----------|
| PyramidFlow [[1]](https://openaccess.thecvf.com/content/CVPR2023/papers/Lei_PyramidFlow_High-Resolution_Defect_Contrastive_Localization_Using_Pyramid_Normalizing_Flow_CVPR_2023_paper.pdf)  |    |
| S-T      |    |
| SPADE    |    |
| PaDiM    |    |
| CS-Flow  |    |

Quantitative results of 5 defect classification methods on MVTecAD
| Models       | AUROC       |
|----------|-----------|
| AnoGAN   | 行6内容   |
| VAE      | 行7内容   |
| AE-SSIM  | 行8内容   |
| FNF      | 行9内容   |
| DR/EM    | 行10内容  |
