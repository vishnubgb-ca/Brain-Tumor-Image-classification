from datavisualization import visualise_image
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
import requests
from PIL import Image
from io import BytesIO
import torch

def transform_data():
    glioma_tumor_image_urls,meningioma_tumor_image_urls,no_tumor_image_urls,pituitory_tumor_image_urls = visualise_image()
    data_transform = torchvision.transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    tumor_list = [glioma_tumor_image_urls,meningioma_tumor_image_urls,no_tumor_image_urls,pituitory_tumor_image_urls]
    images = []
    for lst in tumor_list:
        for url in lst:
            response = requests.get(url)
            image = Image.open(BytesIO(response.content))
            images.append(image)
    
    transformed_images = [data_transform(img) for img in images]
    model_dataset = torch.stack(transformed_images)
    return model_dataset

    # model_dataset = datasets.ImageFolder(path, transform=data_transform)

transform_data()
