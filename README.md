# WaifuDetector
Anime-Image-Classification Based on ResNet50

Ready for environment:
pip install -r requirements.txt

You can run child_copy.py to copy imgs to input folder:
python child_copy.py --source your_folder --target ./input

Then put resnet50 in model and run 
python classify.py --input_dir ./output --model_path ./resnet50_2detect.pthh" --output_dir ./output

In output folder,anime imgs are copyed in 0 folder.
