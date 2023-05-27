import os
import shutil

root_dir = "Garbage classification"
split_ratio = 0.8

for type in os.listdir(root_dir):
    class_path = os.path.join(root_dir, type)

    # Calculate ratio of train images and mve to new path
    train_samples = int(len(os.listdir(class_path)) * split_ratio)
    path = os.path.join("img", "train", type)
    os.mkdir(path)

    count = 0
    for img in os.listdir(class_path):
        if count <= train_samples:
            src = os.path.join(class_path, img)
            dst = os.path.join(path, img)
                
            shutil.move(src, dst)
            count += 1

    # Move the rest of the images to test
    path = os.path.join("img", "test", type)
    os.mkdir(path)
    for img in os.listdir(class_path):
        src = os.path.join(class_path, img)
        dst = os.path.join(path, img)

        shutil.move(src, dst)

        

        