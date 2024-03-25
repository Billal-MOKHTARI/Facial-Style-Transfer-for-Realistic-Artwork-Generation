# Facial-Style-Transfer-for-Realistic-Artwork-Generation

## Stylize Script
This script allows you to stylize images using a pre-trained model. It takes command-line arguments to specify the input image, the checkpoint file containing the pre-trained model, and the path to save the stylized image.

### Requirements

- Python 3.x
- torch
- opencv-python
- torchvision

### Usage

1. Clone the repository:
   ```shell
   $ git clone https://github.com/mahdid-lilia/Facial-Style-Transfer-for-Realistic-Artwork-Generation.git
   $ cd Facial-Style-Transfer-for-Realistic-Artwork-Generation
   ```

2. Run the script with the following command:

   ```shell
   python setup.py <option> <arguments>
   ```

   Replace `<option>` and `<arguments>` with the appropriate values:

   - `<option>`: Specify the option for stylizing the image. Currently, options supported are `single_image` and `folder`.
   - `<arguments>`:
     - `--content`: Path to the content image (for single image stylization) or folder path containing images (for batch stylization).
     - `--checkpoint`: Path to the checkpoint file containing the pre-trained model.
     - `--save`: Path to save the stylized image or folder path to save stylized images.
     - `--model`: Specify the model name for stylization.
     - Additional arguments specific to the chosen model (e.g., `alpha` for `TransformerResNextNetwork_Pruned` model).

### Example
Stylize a single image:
   ```shell
   content_path="/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/data/test/test_1.jpeg"
   checkpoint_path="/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/models/3. TransformerResNextNetwork_Pruned03/checkpoints/checkpoint_d1500.pth"
   output_path="image.png"
   model_name="TransformerResNextNetwork_Pruned"
   alpha=0.3

   python setup.py single_image --content "$content_path" --checkpoint "$checkpoint_path" --save "$output_path" --model "$model_name" "$alpha"
   ```

Stylize images in a folder:
   ```shell
   folder_path="/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/data/test/"
   checkpoint_path="models/3. TransformerResNextNetwork_Pruned03/checkpoints/checkpoint_d1500.pth"
   output_path="data/output/3. TransformerResNextNetwork_Pruned03/"
   model_name="TransformerResNextNetwork_Pruned"
   alpha=0.3

   python setup.py folder --folder "$folder_path" --checkpoint "$checkpoint_path" --save "$output_path" --model "$model_name" "$alpha"
   ```


## Test Results

### Stylized Images

#### TransformerResNextNetwork-Pruned (alpha=0.3)

<table>
  <tr>
    <td><img src="https://github.com/mahdid-lilia/Facial-Style-Transfer-for-Realistic-Artwork-Generation/assets/100322125/cb690036-c1ba-498c-93b7-0d0d02319848" alt="test_5"></td>
    <td><img src="https://github.com/mahdid-lilia/Facial-Style-Transfer-for-Realistic-Artwork-Generation/assets/100322125/b41d80f3-ad8c-4b70-b8dd-a6eae887225b" alt="test_7"></td>
    <td><img src="https://github.com/mahdid-lilia/Facial-Style-Transfer-for-Realistic-Artwork-Generation/assets/100322125/8624cf79-825e-42cc-8021-10588be163af" alt="test_8"></td>
    <td><img src="https://github.com/mahdid-lilia/Facial-Style-Transfer-for-Realistic-Artwork-Generation/assets/100322125/cde9ccb2-08c2-4d94-b415-5f421e8801ac" alt="test_9"></td>
  </tr>
</table>

#### TransformerResNextNetwork-Pruned (alpha=1.0)

<table>
  <tr>
    <td><img src="https://github.com/mahdid-lilia/Facial-Style-Transfer-for-Realistic-Artwork-Generation/assets/100322125/1cefc057-0674-4c0f-8a72-f2784b2feec6" alt="test_5"></td>
    <td><img src="https://github.com/mahdid-lilia/Facial-Style-Transfer-for-Realistic-Artwork-Generation/assets/100322125/1fd89e7a-ebe8-4273-99b1-b5f43f478666" alt="test_7"></td>
    <td><img src="https://github.com/mahdid-lilia/Facial-Style-Transfer-for-Realistic-Artwork-Generation/assets/100322125/54fce425-446b-4bed-b5fa-c54aad991a5d" alt="test_8"></td>
    <td><img src="https://github.com/mahdid-lilia/Facial-Style-Transfer-for-Realistic-Artwork-Generation/assets/100322125/5b37b513-f6a0-4c03-b00f-2d389f70ad48" alt="test_9"></td>
  </tr>
</table>

#### TransformerNetworkV2

<table>
  <tr>
    <td><img src="https://github.com/mahdid-lilia/Facial-Style-Transfer-for-Realistic-Artwork-Generation/assets/100322125/928bc8f0-6fe1-4763-9dd8-778316f3a853" alt="test_5"></td>
    <td><img src="https://github.com/mahdid-lilia/Facial-Style-Transfer-for-Realistic-Artwork-Generation/assets/100322125/565c3bc8-0fb9-4780-bf82-a102dd52bc52" alt="test_7"></td>
    <td><img src="https://github.com/mahdid-lilia/Facial-Style-Transfer-for-Realistic-Artwork-Generation/assets/100322125/ff576a51-59c6-40a8-845e-9a335d8aa16a" alt="test_8"></td>
    <td><img src="https://github.com/mahdid-lilia/Facial-Style-Transfer-for-Realistic-Artwork-Generation/assets/100322125/61d1eebd-86e5-403a-acea-7e04bf032dba" alt="test_9"></td>
  </tr>
</table>













