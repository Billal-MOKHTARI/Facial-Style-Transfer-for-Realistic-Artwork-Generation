#!/bin/bash

content_path="/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/data/test/test_1.jpeg"
checkpoint_path="/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/models/3. TransformerResNextNetwork_Pruned03/checkpoints/checkpoint_d1500.pth"
output_path="image.png"
model_name="TransformerResNextNetwork_Pruned"
alpha=0.3

python setup.py single_image --content "$content_path" --checkpoint "$checkpoint_path" --save "$output_path" --model "$model_name" "$alpha"

# content_path="/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/data/test/test_9.jpg"
# checkpoint_path="models/5. mosaic_TransformerNetworkV2/checkpoints/checkpoint_e2000.pth"
# output_path="data/output/5. TransformerNetworkV2/test_9.jpg"
# model_name="TransformerNetworkV2"

# python setup.py single_image --content "$content_path" --checkpoint "$checkpoint_path" --save "$output_path" --model "$model_name"
