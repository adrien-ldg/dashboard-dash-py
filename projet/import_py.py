import importlib
import subprocess


def pip(install_packages):
    # Vérifier si le module est déjà installé
    for i in install_packages:
        try:
            importlib.import_module(i)
            print(f"{i} est déjà installé.")
        except ImportError:
            print(f"{i} n'est pas installé. Installation en cours...")
            
            # Vous pouvez utiliser pip pour installer le module pandas
            subprocess.check_call(["python", "-m", "pip", "install", i])

            # Vérifier à nouveau si le module est installé
            try:
                importlib.import_module(i)
                print(f"{i} a été installé avec succès.")
            except ImportError:
                print(f"Impossible d'installer {i}. Veuillez l'installer manuellement.")


