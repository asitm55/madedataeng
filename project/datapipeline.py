import os
os.environ['KAGGLE_USERNAME'] = 'asitm77' 
os.environ['KAGGLE_KEY'] = '3cfe9b1053b958b8b2a933b96d992f93' 

import kaggle
import time

dataset_links = ["https://www.kaggle.com/datasets/shrutibhargava94/india-air-quality-data",
                 "https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india",
                 "https://www.kaggle.com/datasets/abhisheksjha/time-series-air-quality-data-of-india-2010-2023",
                 "https://www.kaggle.com/datasets/fedesoriano/air-quality-data-in-india",
                 "https://www.kaggle.com/datasets/neomatrix369/air-quality-data-in-india-extended"]

for dataset in dataset_links:
    folder_name = f"../data/{'-'.join(dataset.split('/')[-2:])}"
    dataset = '/'.join(dataset.split('/')[-2:])

    print(f'Creating folder at {folder_name}')
    os.mkdir(folder_name)

    print(f'Downloading the {dataset} dataset')

    kaggle.api.dataset_download_files(dataset, path=folder_name, unzip=True)
    time.sleep(1)

print('Done')
