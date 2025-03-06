import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import os
import shutil
from concurrent.futures import ThreadPoolExecutor
import argparse

# 设备配置
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 图像预处理
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])


def load_model(model_path):
    """ResNet50二次元图像识别模型"""
    model = models.resnet50(weights=None)

    # 修改最后一层全连接层为2个输出（二分类）
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 2)

    # 加载模型权重
    model.load_state_dict(torch.load(model_path, map_location=device))
    model = model.to(device)
    model.eval()
    return model


def process_image(img_path, model, output_dir):
    """处理单张图片并分类"""
    try:
        # 加载图像
        img = Image.open(img_path).convert('RGB')
        img_tensor = preprocess(img).unsqueeze(0).to(device)

        # 模型推理
        with torch.no_grad():
            outputs = model(img_tensor)
            _, predicted = torch.max(outputs, 1)
            class_id = predicted.item()

        # 复制图片到相应文件夹
        class_folder = os.path.join(output_dir, str(class_id))
        os.makedirs(class_folder, exist_ok=True)
        shutil.copy(img_path, os.path.join(class_folder, os.path.basename(img_path)))
        print(f"Processed {img_path} -> Class {class_id}")
    except Exception as e:
        print(f"Error processing {img_path}: {e}")


def main(input_dir, model_path, output_dir, num_workers=4):
    """主函数：加载模型，处理文件夹中的图片"""

    model = load_model(model_path)

    # 获取所有图片路径
    img_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    img_paths = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.lower().endswith(img_extensions)]

    # 使用线程池并行处理
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        for img_path in img_paths:
            executor.submit(process_image, img_path, model, output_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ResNet50 二次元图像识别")
    parser.add_argument("--input_dir", type=str, required=True, help="输入图片文件夹路径")
    parser.add_argument("--model_path", type=str, required=True, help="模型文件路径")
    parser.add_argument("--output_dir", type=str, required=True, help="输出文件夹路径")
    parser.add_argument("--num_workers", type=int, default=4, help="并行处理的工作线程数")
    args = parser.parse_args()

    main(args.input_dir, args.model_path, args.output_dir, args.num_workers)