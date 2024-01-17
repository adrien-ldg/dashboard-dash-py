from download.config import VERBOSE_APP
from download.chemin_dataset import DATA_DIR
import opendatasets 

def get_dataset(url):

    if VERBOSE_APP:
        print("début du téléchargement du dataset!")
    
    opendatasets.download(
        dataset_id_or_url = url,
        data_dir = DATA_DIR
    )

    if VERBOSE_APP:
        print("fin du téléchargement")

