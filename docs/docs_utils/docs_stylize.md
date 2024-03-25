# Style Transfer Functions Documentation

## Overview
This module provides functions for performing style transfer on images using pre-trained transformer networks. It includes functions for stylizing individual images, entire folders of images, and images in batches. Additionally, it offers utilities for preserving color during style transfer.

## Functions

### stylize(style_transform_path, content_image_path, save_image_path, net)
- **Input**: 
  - `style_transform_path` (str): Path to the pre-trained transformer network model.
  - `content_image_path` (str): Path to the content image.
  - `save_image_path` (str): Path to save the stylized image.
  - `net` (torch.nn.Module): Pre-trained transformer network model.
- **Description**: Stylizes the content image using the specified transformer network model and saves the result to the specified path.

### stylize_folder_single(style_path, content_folder, save_folder, net)
- **Input**: 
  - `style_path` (str): Path to the pre-trained transformer network model.
  - `content_folder` (str): Path to the folder containing content images.
  - `save_folder` (str): Path to save the stylized images.
  - `net` (torch.nn.Module): Pre-trained transformer network model.
- **Description**: Stylizes each image in the content folder individually and saves the stylized images to the specified save folder.

### stylize_folder(style_path, folder_containing_the_content_folder, save_folder, batch_size=1)
- **Input**: 
  - `style_path` (str): Path to the pre-trained transformer network model.
  - `folder_containing_the_content_folder` (str): Path to the folder containing the content folder.
  - `save_folder` (str): Path to save the stylized images.
  - `batch_size` (int, optional): Batch size for stylizing images. Default is 1.
- **Description**: Stylizes images in the content folder by batch and saves the stylized images to the specified save folder.

## Custom Dataset Class

### ImageFolderWithPaths(datasets.ImageFolder)
- **Description**: Custom dataset class that includes image file paths.
- **Methods**:
  - **`__getitem__(self, index)`**: Overrides the `__getitem__` method of `ImageFolder` class to return image paths along with the images.

This documentation provides an overview of the style transfer functions and the custom dataset class available in the module.
