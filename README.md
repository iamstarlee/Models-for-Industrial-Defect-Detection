This repo includes 5 ordinary models and 5 super-resolution models for classifying super-resolution dataset after downscaling.



## 1. Datasets
**[MVTecAD](https://openaccess.thecvf.com/content_CVPR_2019/papers/Bergmann_MVTec_AD_--_A_Comprehensive_Real-World_Dataset_for_Unsupervised_Anomaly_CVPR_2019_paper.pdf)** is a dataset for benchmarking anomaly detection methods with a focus on industrial inspection. It contains over 5000 high-resolution images divided into fifteen different object and texture categories. Each category comprises a set of defect-free training images and a test set of images with various kinds of defects as well as images without defects.

## 2. Metrics
We use the common metric: AUROC (the area under the receiver operating characteristic curve).

## 3. Experiment
Quantitative results of 5 super-resolution methods on MVTecAD, scale = 0.5
|| Models       | mean AUROC       |Year|
|--|----------|-----------|--|
|1| PyramidFlow [[论文]](https://openaccess.thecvf.com/content/CVPR2023/papers/Lei_PyramidFlow_High-Resolution_Defect_Contrastive_Localization_Using_Pyramid_Normalizing_Flow_CVPR_2023_paper.pdf) [[代码]](https://github.com/gasharper/PyramidFlow) |  97.89%  |2023|
|2| GLASS     [[论文]](https://arxiv.org/pdf/2407.09359v1) [[代码]](https://github.com/cqylunlun/glass?tab=readme-ov-file#) | **99.80%** |2024|
|3| UniNet  [[论文]](https://pangdatangtt.github.io/static/pdfs/UniNet__arXix_.pdf) [[代码]](https://github.com/pangdatangtt/UniNet)  |  98.9%  |2025|
|4| HETMM   [[论文]](https://arxiv.org/pdf/2303.16191v5) [[代码]](https://github.com/NarcissusEx/HETMM) |  92.1%  |2023|
|5| INP-Fomer ViT-L [[论文]](https://arxiv.org/pdf/2503.02424v1) [[代码]](https://github.com/luow23/inp-former) |  95.5%  |2025|

Quantitative results of 5 defect classification methods on MVTecAD, scale = 0.5
|| Models       | mean AUROC       |Year|
|--|----------|-----------|--|
|1| DDAD [[论文]](https://arxiv.org/pdf/2305.15956v2) [[代码]](https://github.com/arimousa/DDAD)  |  91.12  | 2023|
|2| EfficientAD [[论文]](https://arxiv.org/pdf/2303.14535v3) [[代码]](https://github.com/nelson1425/EfficientAD)  | **99.9%**   | 2023|
|3| Dinomaly ViT-L [[论文]](https://arxiv.org/pdf/2405.14325v4) [[代码]](https://github.com/guojiajeremy/dinomaly)   | 90.2%   | 2024|
|4| ReConPatch Ensemble  [[论文]](https://arxiv.org/pdf/2305.16713v3) [[代码]](https://github.com/travishsu/ReConPatch-TF)    | 94.9%   | 2023|
|5| ReConPatch WRN-50  [[论文]](https://arxiv.org/pdf/2305.16713v3) [[代码]](https://github.com/travishsu/ReConPatch-TF)  | 97.6% | 2023|

Expected results of GLASS in MVTec AD, scale = 0.5:
| Category | Carpet | Grid |  Leather | Tile | Wood | Bottle |  Cable | Capsule | Hazel nut | Metalnut | Pill | Screw | Toothbrush | Transistor | Zipper |Average
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Detection | 99.76% | 99.88% | 98.99% | 99.65% | 100% | 100% | 99.43% | 99.49% | 98.78% | 100% | 100% | 99.98% | 100% | 99.88% | 99.95% | 99.80% 

Expected results of GLASS in MVTec AD, scale = 0.25:
| Category | Carpet | Grid |  Leather | Tile | Wood | Bottle |  Cable | Capsule | Hazel nut | Metalnut | Pill | Screw | Toothbrush | Transistor | Zipper |Average
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Detection | 99.76% | 100% | 100% | 99.96% | 99.91% | 99.92% | 99.59% | 99.12% | 99.96% | 99.46% | 93.81% | 92.11% | 100% | 99.50% | 99.97% | 98.87% 

Expected results of EfficientAD in MVTec AD, scale = 0.25:
| Category | Carpet | Grid |  Leather | Tile | Wood | Bottle |  Cable | Capsule | Hazel nut | Metalnut | Pill | Screw | Toothbrush | Transistor | Zipper |Average
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Detection | 98.39% | 97.12% | 99.78% | 97.89% | 99.34% | 98.01% | 97.19% | 99.40% | 99.19% | 98.12% | 100% | 99.00% | 97.45% | 98.98% | 100% | 98.66% 

## 4. Downsample
![image](https://github.com/iamstarlee/Models-for-Industrial-Defect-Detection/blob/main/images/0000x.png)![image](https://github.com/iamstarlee/Models-for-Industrial-Defect-Detection/blob/main/images/0001x.png)![image](https://github.com/iamstarlee/Models-for-Industrial-Defect-Detection/blob/main/images/0002x.png)
## 5. Usage
### a. Generating data
- run `conda env create -f anomaly.yaml`, to config env.
- run `python down_sample.py`, to downsample data.

### b. Reproducing models
- For training EfficientAD, run `python efficientad.py --dataset mvtec_ad --subdataset bottle --mvtec_ad_path '../anomalib/down_dataset25'` to train sub-class bottle, the same is true for other classes.
- For evaluating EfficientAD
  - run `python mvtec_ad_evaluation/pro_curve_util.py` first, then
  - run `python mvtec_ad_evaluation/evaluate_experiment.py --dataset_base_dir './mvtec_anomaly_detection/' --anomaly_maps_dir './output/1/anomaly_maps/mvtec_ad/' --output_dir './output/1/metrics/mvtec_ad/' --evaluated_objects bottle`.
- For GLASS, cd shell, and modify `run-mvtec.sh`, then run `bash run-mvtec.sh` to train/test.
  
