from data_transformation import transform_data
import torch

def save_artifact():
    model_dataset = transform_data()
    torch.save(model_dataset, "test.pt")
    # model_dataset = torch.load('test.pt')
    return model_dataset