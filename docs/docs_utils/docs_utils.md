# Image Processing Utilities Documentation

## Overview
This module provides various utility functions for image processing tasks. It includes functions for Gram matrix computation, image loading, displaying, saving, preprocessing, and color transfer, along with a custom dataset class for image folders.

## Functions

### gram(tensor)
- **Input**: `tensor` (torch.Tensor)
- **Output**: `torch.Tensor`
- **Description**: Computes the Gram matrix of the input tensor.

### load_image(path)
- **Input**: `path` (str)
- **Output**: `numpy.ndarray`
- **Description**: Loads an image from the specified path.

### show(img)
- **Input**: `img` (numpy.ndarray)
- **Description**: Displays the input image using matplotlib.

### saveimg(img, image_path)
- **Input**: `img` (numpy.ndarray), `image_path` (str)
- **Description**: Saves the input image to the specified path.

### itot(img, max_size=None)
- **Input**: `img` (numpy.ndarray), `max_size` (int, optional)
- **Output**: `torch.Tensor`
- **Description**: Converts the input image to a tensor. Optionally resizes the image to the specified maximum size.

### ttoi(tensor)
- **Input**: `tensor` (torch.Tensor)
- **Output**: `numpy.ndarray`
- **Description**: Converts the input tensor to an image.

### transfer_color(src, dest)
- **Input**: `src` (numpy.ndarray), `dest` (numpy.ndarray)
- **Output**: `numpy.ndarray`
- **Description**: Transfers the color from the source image to the destination image using the YIQ color space.

### plot_loss_hist(c_loss, s_loss, total_loss, title="Loss History")
- **Input**: `c_loss` (list), `s_loss` (list), `total_loss` (list), `title` (str, optional)
- **Description**: Plots the content loss, style loss, and total loss history.

## Custom Dataset Class

### ImageFolderWithPaths(datasets.ImageFolder)
- **Description**: Custom dataset class that includes image file paths.
- **Methods**:
  - **`__getitem__(self, index)`**: Overrides the `__getitem__` method of `ImageFolder` class to return image paths along with the images.

This documentation provides an overview of the functions and the custom dataset class available in the Image Processing Utilities module.
