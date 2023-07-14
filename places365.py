import torch
import torchvision
import torchvision.transforms as transforms

# Define a transform to normalize the data
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# Download and load the training data
train_data = torchvision.datasets.Places365(root='./data_256',
                                            split='train-standard',
                                            download=True,
                                            transform=transform)
train_loader = torch.utils.data.DataLoader(train_data,
                                           batch_size=4,
                                           shuffle=True,
                                           num_workers=2)

# Download and load the validation data
val_data = torchvision.datasets.Places365(root='./data_256',
                                          split='val',
                                          download=True,
                                          transform=transform)
val_loader = torch.utils.data.DataLoader(val_data,
                                         batch_size=4,
                                         shuffle=False,
                                         num_workers=2)

# Get the class names
class_names = train_data.classes
