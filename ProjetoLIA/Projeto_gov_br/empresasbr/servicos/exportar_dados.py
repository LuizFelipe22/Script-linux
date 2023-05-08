
import pandas as pd

from bd.conexao_bd import create_engine

import os


class exportar_bd:

    def __init__(self, diretorio: str = "./arquivos"):
        self.diretorio = diretorio
        self.engine = create_engine()


    def estabelecimentos(self):

        diretorio = f"{self.diretorio}/Estabelecimentos"

        atributos = ['CNPJ_BASICO', 'CNPJ_ORDEM', 'CNPJ_DV', 'ID_MATRIZ_FILIAL', 'NM_FANTASIA','SITU_CADASTRAL', 'DT_SITU_CADASTRAL', 'MT_SITU_CADASTRAL', 'CIDADE_EXTERIOR', 
                     'PAIS', 'DT_INICIO_ATIV', 'FISCAL_PRINC', 'FISCAL_SECUN', 'TP_LOGRADOURO', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO',  'BAIRRO', 'CEP', 'UF', 'MUNICIPIO', 
                     'DDD1', 'TELEFONE1', 'DDD2', 'TELEFONE2', 'DDD_FAX', 'FAX', 'CORREIO_ELETRONICO', 'SITUACAO_ESPECIAL', 'DT_SITU_ESPECIAL']

        arquivos = [arquivo for arquivo in os.listdir(diretorio) if arquivo.startswith('Estabelecimentos')]
        tipos = {atributo : type(str()) for atributo in atributos}

        for i in arquivos:
            DataFrame = pd.read_csv(f'{diretorio}/{i}', sep=';', encoding='ISO-8859-1', names=atributos, dtype=tipos)
            DataFrame.to_sql('estabelecimentos', con=self.engine, chunksize=1000, if_exists='append', index=False)


    def socios(self):

        diretorio = f"{self.diretorio}/Socios"

        atributos = ['CNPJ_BASICO', 'IDENTIFICADOR_SOCIO', 'NOME_SOCIO_OU_RAZAO_SOCIAL', 'CNPJ_CPF_SOCIO', 'QUALIFICACAO_SOCIO', 'DT_ENTRADA_SOCIEDADE', 
                     'REPRESENTANTEA_LEGAL', 'NOME_REPRESENTANTE', 'QUALIFICACAO_REPRESENTANTE_LEGAL', 'FAIXA_ETARIA']

        arquivos = [arquivo for arquivo in os.listdir(diretorio) if arquivo.startswith('Socios')]
        tipos = {atributo : type(str()) for atributo in atributos}

        for i in arquivos:
            DataFrame = pd.read_csv(f'{diretorio}/{i}', sep=';', encoding='ISO-8859-1', names=atributos, dtype=tipos)
            DataFrame.to_sql('socios', con=self.engine, chunksize=1000, if_exists='append', index=False)
