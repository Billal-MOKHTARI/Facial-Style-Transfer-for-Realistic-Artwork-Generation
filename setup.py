import sys
import imghdr
import os
from src.utils import stylize
from src.utils import experimental
import inspect


def is_image(file_path):
    return imghdr.what(file_path) is not None

if __name__ == "__main__":
    args = sys.argv

    script_name = args[0]
    general_option = args[1]


    content_image_option = "--content"
    checkpoint_option = "--checkpoint"
    save_path_option = "--save"
    folder_path_option = "--folder"
    model_option = "--model"

    assert general_option in args, f"The option [{checkpoint_option}] is not specified."
    assert checkpoint_option in args, f"The option [{checkpoint_option}] is not specified."
    assert model_option in args, f"The option [{model_option}] is not specified."


    # Get the model
    position = args.index(model_option)
    model_arg = args[position+1]

    #-------------------------------------------
    # Set of allowed model names
    allowed_models = {
        "TransformerNetworkV2",
        "TransformerResNextNetwork",
        "TransformerResNextNetwork_Pruned",
        "TransformerNetworkDenseNet",
        "TransformerNetworkUNetDenseNetResNet"
    }

    assert model_arg in allowed_models, f"The model {model_arg} is not in {allowed_models}"




    if model_arg == "TransformerResNextNetwork_Pruned":
        try:
            alpha = float(args[position+2])
        except:
            alpha = 0.3
        
        model = experimental.TransformerResNextNetwork_Pruned(alpha)
    
    else:
        model = eval("experimental."+model_arg)()   

    # Get the checkpoint
    position = args.index(checkpoint_option)
    checkpoint = args[position+1]
    assert checkpoint.endswith('.pth'), "Filename does not have a .pth extension." 

    if general_option == "single_image":
        assert content_image_option in args, f"The option [{content_image_option}] is not specified."
        assert save_path_option in args, f"The option [{save_path_option}] is not specified."

        position = args.index(content_image_option)
        content_image = args[position+1]


        position = args.index(save_path_option)
        save_image_path = args[position+1]

        stylize.stylize(checkpoint, content_image, save_image_path, model)

    if general_option == "folder":
        assert folder_path_option in args, f"The option [{folder_path_option}] is not specified."
        assert save_path_option in args, f"The option [{save_path_option}] is not specified."

        position = args.index(folder_path_option)
        folder_path = args[position+1]

        position = args.index(save_path_option)
        save_image_path = args[position+1]

        stylize.stylize_folder_single(checkpoint, folder_path, save_image_path, model)


# Example of usage
# python setup.py single_image --content "/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/data/test/test_1.jpeg" --checkpoint "/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/models/3. TransformerResNextNetwork_Pruned03/checkpoints/checkpoint_c1500.pth" --save image.png
        
# TransformerResNextNetwork_Pruned(0.3)
        
