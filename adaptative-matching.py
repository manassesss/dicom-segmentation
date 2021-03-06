import cv2
import numpy as np
import os
import pydicom
from random import choice
#ADAPTIVE TEMPLATE MATCHING

def show(pixel_array):
    """
    Exibe a imagem a partir de um array de pixels.

    :param pixel_array: numpy array com os pixels da imagem.
    :return:
    """
    cv2.imshow('image',pixel_array)
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()

def load_files(path):
    """
    Carrega todos os arquivos DICOM de um diretório.

    :param path: str indicando o diretório de origem dos
                 dos arquivos que se deseja carregar
    :return volume: numpy array com os arquivos dicom
    """
    volumes = list()
    for root, dirs, files in os.walk(path):
        for file in files:
            volumes.append(pydicom.dcmread(root + '/'+ file))
    return volumes
###########Suponha que o volume tenha sido selecionado aleatoriamente
volume = load_files("C:/Users/luisc/Documents/dicom-database/LCTSC/LCTSC-Train-S1-001")

test = pydicom.dcmread("C:/Users/luisc/Documents/dicom-database/LCTSC/LCTSC-Train-S1-001/11-16-2003-RTRCCTTHORAX8FLow Adult-39664/1-.simplified-62948/000000.dcm")
print(test)
#Gerando o template padrão
#- Seleciona aleatoriamente um volume dentre todos os outros do banco de dados. 1.2.840.10008.5.1.4.1.1.481.3
slice = choice(volume)
#- Encontrar a marcação do especialista, encontrar o centro da massa dessa marcação;
print(slice)
show(slice.pixel_array)
#- Recortar duas vezes o tamanho da região correspondente de todos os lados.

#Gerando o template inicial
#- O algoritmo Template Matching é executado em cada slice do volume, onde o template é o
#template padrão definido anteriormente;
#- Calcular a similaridade em cada slice;
#- O template inicial selecionado é aquele que tem maior similaridade com o template padrão,
#o número do slice do melhor template inicial é salvo.
#Adaptando o template para cada slice
#- Executa o Template Matching no primeiro slice onde a combinação ocorre, como resultado temos:
#o Novo Template e uma imagem.
#- O Novo Template é executado no próximo slice e, novamente, o resultado será um Novo Template e uma image.
#- No final, teremos um conjunto de imagens onde á apenas a região da medula segmentada.