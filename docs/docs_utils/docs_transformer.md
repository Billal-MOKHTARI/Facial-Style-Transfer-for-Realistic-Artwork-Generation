# Transformer Network Documentation

## Overview
This module provides implementations of Transformer Networks for image transformation tasks. It includes two main classes: `TransformerNetwork` and `TransformerNetworkTanh`, along with several helper classes for building the network architecture.

## Classes

### TransformerNetwork
- **`__init__(self)`**: Initializes the Transformer Network model. It defines the architecture of the network consisting of convolutional layers, ReLU activation functions, and deconvolutional layers.
- **`forward(self, x)`**: Defines the forward pass of the Transformer Network. It takes an input tensor `x` and passes it through the defined convolutional, residual, and deconvolutional layers to produce the output.

### TransformerNetworkTanh
- **`__init__(self, tanh_multiplier=150)`**: Initializes the Transformer Network with Tanh activation. It inherits the architecture of `TransformerNetwork` and modifies the output layer to include a Tanh activation function.
- **`forward(self, x)`**: Overrides the forward method to include the Tanh activation function. It scales the output of the parent class by the `tanh_multiplier` parameter.

### ConvLayer
- **`__init__(self, in_channels, out_channels, kernel_size, stride, norm="instance")`**: Initializes a convolutional layer with optional normalization. It includes reflection padding, convolutional layer, and normalization layer (either instance normalization or batch normalization).
- **`forward(self, x)`**: Defines the forward pass of the convolutional layer. It applies reflection padding, convolution, and normalization (if specified) to the input tensor `x`.

### ResidualLayer
- **`__init__(self, channels=128, kernel_size=3)`**: Initializes a residual layer. It consists of two convolutional layers with ReLU activation functions.
- **`forward(self, x)`**: Defines the forward pass of the residual layer. It applies two convolutional layers with ReLU activation functions and adds the input tensor `x` to the output, preserving the residual.

### DeconvLayer
- **`__init__(self, in_channels, out_channels, kernel_size, stride, output_padding, norm="instance")`**: Initializes a deconvolutional layer with optional normalization. It includes transposed convolution and normalization layer (either instance normalization or batch normalization).
- **`forward(self, x)`**: Defines the forward pass of the deconvolutional layer. It applies transposed convolution and normalization (if specified) to the input tensor `x`.

This documentation provides an overview of the methods and functionalities of each class in the Transformer Network module.
