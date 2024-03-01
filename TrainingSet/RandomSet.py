import os
import random
import shutil

def copy_random_images(source_folder, destination_folder, num_images_to_copy):
    # Get a list of all files in the source folder
    all_images = os.listdir(source_folder)

    # Ensure the destination folder exists, create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Choose a random subset of images
    selected_images = random.sample(all_images, min(num_images_to_copy, len(all_images)))

    # Copy selected images to the destination folder
    for image in selected_images:
        source_path = os.path.join(source_folder, image)
        destination_path = os.path.join(destination_folder, image)
        shutil.copyfile(source_path, destination_path)

# Example usage:
source_directory = "Images/"
destination_directory = "TrainingSetRandom/"
number_of_images_to_copy = 100  # Set the desired number of images

copy_random_images(source_directory, destination_directory, number_of_images_to_copy)
