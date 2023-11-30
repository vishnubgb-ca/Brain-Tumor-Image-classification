from extract_data import extract_data
from PIL import Image
import requests
from io import BytesIO

def visualise_image():
    glioma_tumor_image_urls,meningioma_tumor_image_urls,no_tumor_image_urls,pituitory_tumor_image_urls = extract_data()
    glioma_tumor_response = requests.get(glioma_tumor_image_urls[0])
    meningioma_tumor_response = requests.get(meningioma_tumor_image_urls[0])
    no_tumor_image_response = requests.get(no_tumor_image_urls[0])
    pituitory_tumor_image_response = requests.get(pituitory_tumor_image_urls[0])
    glioma_tumor_image = Image.open(BytesIO(glioma_tumor_response.content))
    meningioma_tumor_image = Image.open(BytesIO(meningioma_tumor_response.content))
    no_tumor_image = Image.open(BytesIO(no_tumor_image_response.content))
    pituitory_tumor_image = Image.open(BytesIO(pituitory_tumor_image_response.content))
    glioma_tumor_image.save('glioma_tumor.jpg')
    meningioma_tumor_image.save('meningioma_tumor.jpg')
    no_tumor_image.save('no_tumor.jpg')
    pituitory_tumor_image.save('pituitory_tumor.jpg')
    #print(glioma_tumor_image.show())
    #print(meningioma_tumor_image.show())
    #print(no_tumor_image.show())
    #print(pituitory_tumor_image.show())
    return glioma_tumor_image_urls,meningioma_tumor_image_urls,no_tumor_image_urls,pituitory_tumor_image_urls

visualise_image()