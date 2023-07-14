import os
import zipfile
import tempfile
import shutil
import platform
import urllib.request

def download_chromedriver():
    version = '114.0.5735.90' # Substitua pela versão mais recente do chromedriver disponível
    desired_location = 'driver'

    # Verificar se o chromedriver já existe no local desejado
    if os.path.isfile(os.path.join(desired_location, 'chromedriver.exe')):
        return os.path.join(desired_location, 'chromedriver.exe')

    # Verificar a arquitetura do sistema operacional
    if platform.architecture()[0] == '64bit':
        chromedriver_url = f'https://chromedriver.storage.googleapis.com/{version}/chromedriver_win32.zip'
    else:
        chromedriver_url = f'https://chromedriver.storage.googleapis.com/{version}/chromedriver_win32.zip'

    # Baixar o chromedriver e extrair o arquivo zip
    with tempfile.TemporaryDirectory() as temp_dir:
        download_path = os.path.join(temp_dir, 'chromedriver.zip')
        urllib.request.urlretrieve(chromedriver_url, download_path)
        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # Mover o arquivo chromedriver para o local desejado
        final_path = os.path.join(temp_dir, 'chromedriver.exe')
        shutil.move(final_path, desired_location)

    return os.path.join(desired_location, 'chromedriver.exe')