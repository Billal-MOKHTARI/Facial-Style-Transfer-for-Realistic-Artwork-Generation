# Transformer Network Documentation

## Overview
This module provides implementations of various versions of Transformer Networks for image transformation tasks. It includes several classes: `TransformerNetworkV2`, `TransformerResNextNetwork`, `TransformerResNextNetwork_Pruned`, `TransformerNetworkDenseNet`, `TransformerNetworkUNetDenseNetResNet`, along with helper classes for building the network architecture.

## Classes

### TransformerNetworkV2
- **`__init__(self)`**: Initializes the Transformer NetworkV2 model with fully pre-activated residual layers. It defines the architecture of the network consisting of convolutional layers, ReLU activation functions, and deconvolutional layers.
- **`forward(self, x)`**: Defines the forward pass of the Transformer NetworkV2. It takes an input tensor `x` and passes it through the defined convolutional, residual, and deconvolutional layers to produce the output.

### TransformerResNextNetwork
- **`__init__(self)`**: Initializes the Transformer ResNext Network model. It inherits the architecture of `TransformerNetworkV2` and includes ResNeXt layers in the residual block.
- **`forward(self, x)`**: Defines the forward pass of the Transformer ResNext Network. It takes an input tensor `x` and passes it through the defined convolutional, ResNeXt, and deconvolutional layers to produce the output.

### TransformerResNextNetwork_Pruned
- **`__init__(self, alpha=1.0)`**: Initializes the pruned version of the Transformer ResNext Network model. It inherits the architecture of `TransformerNetworkV2` and includes pruned ResNeXt layers in the residual block.
- **`forward(self, x)`**: Defines the forward pass of the pruned Transformer ResNext Network. It takes an input tensor `x` and passes it through the defined convolutional, pruned ResNeXt, and deconvolutional layers to produce the output.

### TransformerNetworkDenseNet
- **`__init__(self)`**: Initializes the Transformer Network using DenseNet blocks instead of residual blocks.
- **`forward(self, x)`**: Defines the forward pass of the Transformer Network using DenseNet blocks. It takes an input tensor `x` and passes it through the defined convolutional, DenseNet, and deconvolutional layers to produce the output.

### TransformerNetworkUNetDenseNetResNet
- **`__init__(self)`**: Initializes the Transformer Network using DenseNet blocks and ResNet connections.
- **`forward(self, x)`**: Defines the forward pass of the Transformer Network using DenseNet blocks and ResNet connections. It takes an input tensor `x` and passes it through the defined convolutional, DenseNet, and deconvolutional layers to produce the output.

This documentation provides an overview of the methods and functionalities of each class in the Transformer Network module.
