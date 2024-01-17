import os.path
from download.open_dataset import get_dataset
from download.config import KAGGLE_DATASET_URL, VERBOSE_APP
from download.chemin_dataset import DATA_DIR

def check_dataset():

    if os.path.isfile(DATA_DIR + "/global-data-on-sustainable-energy/global-data-on-sustainable-energy.csv"):
        if VERBOSE_APP:
            print("Dataset déjà récupéré")
    else:
        if VERBOSE_APP:
            print("Début du téléchargement")
        get_dataset(KAGGLE_DATASET_URL) 