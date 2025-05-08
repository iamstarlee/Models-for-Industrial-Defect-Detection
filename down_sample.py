import os
from PIL import Image
from tqdm import tqdm


if hasattr(Image, 'Resampling'):
    RESAMPLE = Image.Resampling.LANCZOS
else:
    RESAMPLE = Image.ANTIALIAS

def resize_image(image_path, scale=0.5, save_path=None):
    img = Image.open(image_path)
    w, h = img.size
    img_resized = img.resize((int(w * scale), int(h * scale)), resample=RESAMPLE)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    img_resized.save(save_path)

def process_mvtec_dataset(source_root, dest_root, scale=0.5, image_exts={'.png', '.jpg', '.jpeg'}):
    for cls_name in os.listdir(source_root):
        cls_path = os.path.join(source_root, cls_name)
        if not os.path.isdir(cls_path):
            continue

        for split in ['train', 'test']:
            split_path = os.path.join(cls_path, split)
            if not os.path.exists(split_path):
                continue

            for subfolder, _, files in os.walk(split_path):
                for file in tqdm(files, desc=f"Processing {cls_name}/{split}"):
                    ext = os.path.splitext(file)[-1].lower()
                    if ext in image_exts:
                        src_img_path = os.path.join(subfolder, file)
                        

                        relative_path = os.path.relpath(src_img_path, source_root)
                        dst_img_path = os.path.join(dest_root, relative_path)

                        resize_image(src_img_path, scale=scale, save_path=dst_img_path)


source_root = 'datasets/MVTecAD'          # 这里是 MVTec AD 数据集路径
dest_root   = 'down_dataset'              # 这里是存放降分辨率数据集的路径

process_mvtec_dataset(source_root, dest_root, scale=0.5) #scale控制压缩率
