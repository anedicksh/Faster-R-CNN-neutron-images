import torch

BATCH_SIZE = 32 # increase / decrease according to GPU memeory
RESIZE_TO = 512 # resize the image for training and transforms
NUM_EPOCHS = 50 # number of epochs to train for
NUM_WORKERS = 0

DEVICE = torch.device('cpu') 
  
# Images and labels direcotry should be relative to train.py
TRAIN_DIR_IMAGES = '../input/train_images'
TRAIN_DIR_LABELS = '../input/train_xmls'
VALID_DIR_IMAGES = '../input/valid_images'
VALID_DIR_LABELS = '../input/valid_xmls'

# classes: 0 index is reserved for background
CLASSES = [
    '__background__',
    'Objects3D', 'Illegal']

NUM_CLASSES = len(CLASSES)

# whether to visualize images after creating the data loaders
VISUALIZE_TRANSFORMED_IMAGES = False

# location to save model and plots
OUT_DIR = '../outputs/5'
