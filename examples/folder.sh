#!/bin/bash

folder_path="/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/data/test/"

# TransformerResNextNetwork_Pruned03 model
checkpoint_path="models/3. TransformerResNextNetwork_Pruned03/checkpoints/checkpoint_d1500.pth"
output_path="data/output/3. TransformerResNextNetwork_Pruned03/"
model_name="TransformerResNextNetwork_Pruned"
alpha=0.3

python setup.py folder --folder "$folder_path" --checkpoint "$checkpoint_path" --save "$output_path" --model "$model_name" "$alpha"

# # TransformerResNextNetwork_Pruned1.0 model
# checkpoint_path="models/7. mosaic_TransformerResNextNetwork_Pruned10/checkpoints/transformer_weight.pth"
# output_path="data/output/7. TransformerResNextNetwork_Pruned10"
# model_name="TransformerResNextNetwork_Pruned"
# alpha=1.0

# python setup.py folder --folder "$folder_path" --checkpoint "$checkpoint_path" --save "$output_path" --model "$model_name" "$alpha"


# # TransformerNetworkV2 model
# checkpoint_path="models/5. mosaic_TransformerNetworkV2/checkpoints/checkpoint_e2000.pth"
# output_path="data/output/5. TransformerNetworkV2"
# model_name="TransformerNetworkV2"

# python setup.py folder --folder "$folder_path" --checkpoint "$checkpoint_path" --save "$output_path" --model "$model_name"
