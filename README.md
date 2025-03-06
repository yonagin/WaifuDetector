# WaifuDetector  
**Anime-Image-Detection Based on ResNet50**

A tool for detecting anime-style images using a ResNet50-based model.

## Environment Setup
Ensure you have Python installed, then install the required dependencies by running:
```bash
pip install -r requirements.txt
```

## Usage Instructions
Follow these steps to use WaifuDetector:

1. **Copy Images to Input Folder**  
   Use the `child_copy.py` script to copy your images including subfolders from a source folder to the `./input` folder:
   ```bash
   python child_copy.py --source your_folder --target ./input
   ```
   - `your_folder`: Replace with the path to your image folder (e.g., `D:/my_images`).

2. **Prepare the Model**  
   Place the pre-trained ResNet50 model file (`resnet50_2detect.pth`) into the `./model` folder. If the folder doesn’t exist, create it manually.
   The model is here:https://huggingface.co/elixirx/resnet50_2detect

4. **Run Classification**  
   Execute the `classify.py` script to classify the images:
   ```bash
   python classify.py --input_dir ./input --model_path ./model/resnet50_2detect.pthh --output_dir ./output
   ```
   - `--input_dir`: Directory containing input images (default: `./input`).
   - `--model_path`: Path to the model file (default: `./model/resnet50_2detect.pthh`).
   - `--output_dir`: Directory to save the output (default: `./output`).

5. **View Results**  
   After classification, anime-style images will be copied to the `./output/0` folder.

## Notes
- If you encounter errors about missing modules, rerun `pip install -r requirements.txt`.
- For paths with spaces, enclose them in quotes (e.g., `"D:/my images"`).
- Ensure the model file `resnet50_2detect.pth` exists in the specified path, or the script will fail.
