This repo includes 5 ordinary models and 5 super-resolution models for classifying super-resolution dataset after downscaling.



## 1. Datasets
**[MVTecAD](https://openaccess.thecvf.com/content_CVPR_2019/papers/Bergmann_MVTec_AD_--_A_Comprehensive_Real-World_Dataset_for_Unsupervised_Anomaly_CVPR_2019_paper.pdf)** is a dataset for benchmarking anomaly detection methods with a focus on industrial inspection. It contains over 5000 high-resolution images divided into fifteen different object and texture categories. Each category comprises a set of defect-free training images and a test set of images with various kinds of defects as well as images without defects.

## 2. Metrics
We use the common metric: AUROC (the area under the receiver operating characteristic curve).

## 3. Experiment
Quantitative results of 5 super-resolution methods on MVTecAD
|| Models       | mean AUROC       |Year|
|--|----------|-----------|--|
|1| PyramidFlow [[论文]](https://openaccess.thecvf.com/content/CVPR2023/papers/Lei_PyramidFlow_High-Resolution_Defect_Contrastive_Localization_Using_Pyramid_Normalizing_Flow_CVPR_2023_paper.pdf) [[代码]](https://github.com/gasharper/PyramidFlow) |    |2023|
|2| GLASS     [[论文]](https://arxiv.org/pdf/2407.09359v1) [[代码]](https://github.com/cqylunlun/glass?tab=readme-ov-file#) | 76.1% |2024|
|3| UniNet  [[论文]](https://pangdatangtt.github.io/static/pdfs/UniNet__arXix_.pdf) [[代码]](https://github.com/pangdatangtt/UniNet)  |  78.9%  |2025|
|4| HETMM   [[论文]](https://arxiv.org/pdf/2303.16191v5) [[代码]](https://github.com/NarcissusEx/HETMM) |  82.1%  |2023|
|5| INP-Fomer ViT-L [[论文]](https://arxiv.org/pdf/2503.02424v1) [[代码]](https://github.com/luow23/inp-former) |  68.5%  |2025|

Quantitative results of 5 defect classification methods on MVTecAD
|| Models       | mean AUROC       |Year|
|--|----------|-----------|--|
|1| DDAD [[论文]](https://arxiv.org/pdf/2305.15956v2) [[代码]](https://github.com/arimousa/DDAD)  |    | 2023|
|2| EfficientAD [[论文]](https://arxiv.org/pdf/2303.14535v3) [[代码]](https://github.com/nelson1425/EfficientAD)  | 62.1%   | 2023|
|3| Dinomaly ViT-L [[论文]](https://arxiv.org/pdf/2405.14325v4) [[代码]](https://github.com/guojiajeremy/dinomaly)   | 70.2%   | 2024|
|4| ReConPatch Ensemble  [[论文]](https://arxiv.org/pdf/2305.16713v3) [[代码]](https://github.com/travishsu/ReConPatch-TF)    | 54.9%   | 2023|
|5| ReConPatch WRN-50  [[论文]](https://arxiv.org/pdf/2305.16713v3) [[代码]](https://github.com/travishsu/ReConPatch-TF)  | 57.6% | 2023|

Expected results of PyramidFlow in half resolution of MVTec AD:
| Category | Carpet | Grid |  Leather | Tile | Wood | Bottle |  Cable | Capsule | Hazel nut | Metalnut | Pill | Screw | Toothbrush | Transistor | Zipper |Average
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Detection | 99.3% | 100% | 100% | 100% | 100% | 100% | 99.4% | 99.4% | 100% | 100% | 100% | 99.0% | 100% | 100% | 100% | 99.8% 

Expected results of DDAD in half resolution of MVTec AD:
| Category | Carpet | Grid |  Leather | Tile | Wood | Bottle |  Cable | Capsule | Hazel nut | Metalnut | Pill | Screw | Toothbrush | Transistor | Zipper |Average
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Detection | 99.3% | 100% | 100% | 100% | 100% | 100% | 99.4% | 99.4% | 100% | 100% | 100% | 99.0% | 100% | 100% | 100% | 99.8% 
