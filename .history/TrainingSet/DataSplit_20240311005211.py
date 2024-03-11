import os
import shutil
import random
import tqdm

train_path_img = 'TrainingSet\\yoloset\\images\\Train'
train_path_label = 'TrainingSet\\yoloset\\labels\\Train'
val_path_img = 'TrainingSet\\yoloset\\images\\Val'
val_path_label = 'TrainingSet\\yoloset\\labels\\Val'


import os
import shutil
import random

def split_data(source_dir, dest_dir, split_ratio=0.8):
    # Create destination directories
    os.makedirs(dest_dir, exist_ok=True)
    os.makedirs(os.path.join(dest_dir, 'images', 'Train'), exist_ok=True)
    os.makedirs(os.path.join(dest_dir, 'images', 'Val'), exist_ok=True)
    os.makedirs(os.path.join(dest_dir, 'labels', 'Train'), exist_ok=True)
    os.makedirs(os.path.join(dest_dir, 'labels', 'Val'), exist_ok=True)

    # Get list of image and label files
    image_files = os.listdir(os.path.join(source_dir, 'images'))
    label_files = os.listdir(os.path.join(source_dir, 'labels'))

    # Split files
    num_train = int(len(image_files) * split_ratio)
    train_images = random.sample(image_files, num_train)
    train_labels = [f.replace('.jpg', '.txt') for f in train_images]

    # Move files to destination directories
    for img_file in train_images:
        shutil.move(os.path.join(source_dir, 'images', img_file),
                    os.path.join(dest_dir, 'images', 'Train', img_file))
    for lbl_file in train_labels:
        shutil.move(os.path.join(source_dir, 'labels', lbl_file),
                    os.path.join(dest_dir, 'labels', 'Train', lbl_file))

    for img_file in image_files:
        if img_file not in train_images:
            shutil.move(os.path.join(source_dir, 'images', img_file),
                        os.path.join(dest_dir, 'images', 'Val', img_file))
    for lbl_file in label_files:
        if lbl_file.replace('.txt', '.jpg') not in train_images:
            shutil.move(os.path.join(source_dir, 'labels', lbl_file),
                        os.path.join(dest_dir, 'labels', 'Val', lbl_file))


### for label_tag
split_data('TrainingSet\\yolo', 'yoloset') ### without negative images
