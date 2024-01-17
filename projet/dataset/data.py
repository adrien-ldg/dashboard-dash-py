from dataset.nettoyage_dataset import nettoyage
from download.download import check_dataset

check_dataset()
df = nettoyage()