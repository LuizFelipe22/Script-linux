import requests

import os


class importar_zip:

    def __init__(self, diretorio: str = "./arquivos"):
        self.diretorio = diretorio


    def estabelecimentos(self) -> None:

        pasta = f"{self.diretorio}/Estabelecimentos"

        if not os.path.exists(pasta):
            os.mkdir(pasta)

        for i in range(0,10):

            url = f'https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos{i}.zip'
            arquivo_zip = requests.get(url)
            nome_arquivo = url.split('/')[4]

            with open(f'{pasta}/{nome_arquivo}', 'wb') as f:
                f.write(arquivo_zip.content)


    def empresas(self) -> None:

        pasta = f"{self.diretorio}/Empresas"

        if not os.path.exists(pasta):
            os.mkdir(pasta)

        for i in range(0,10):

            url = f'https://dadosabertos.rfb.gov.br/CNPJ/Empresas{i}.zip'
            arquivo_zip = requests.get(url)
            nome_arquivo = url.split('/')[4]

            with open(f'{pasta}/{nome_arquivo}', 'wb') as f:
                f.write(arquivo_zip.content)

    
    def socios(self) -> None:

        pasta = f"{self.diretorio}/Socios"

        if not os.path.exists(pasta):
            os.mkdir(pasta)

        for i in range(0,10):

            url = f'https://dadosabertos.rfb.gov.br/CNPJ/Socios{i}.zip'
            arquivo_zip = requests.get(url)
            nome_arquivo = url.split('/')[4]

            with open(f'{pasta}/{nome_arquivo}', 'wb') as f:
                f.write(arquivo_zip.content)
