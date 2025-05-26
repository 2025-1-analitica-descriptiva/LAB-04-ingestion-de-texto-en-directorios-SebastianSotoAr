# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import zipfile
import pandas as pd
import os

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```

    
    """

    with zipfile.ZipFile("files/input.zip", "r") as zip:
        zip.extractall("files")
    
    files = []
    for root, dirs, files_in_dir in os.walk("files/input"):
        for file_name in files_in_dir:
            if file_name.endswith(".txt"):
                files.append(os.path.join(root, file_name))

    test = {"phrase":[], "target":[]}
    train = {"phrase":[], "target":[]}

    for file_path  in files:
        with open(file_path , "r") as file:
            phrase = file.read()
        target = file_path.split(os.sep)[-2]

        if "test" in file_path:
            test["phrase"].append(phrase)
            test["target"].append(target)

        if "train" in file_path:
            train["phrase"].append(phrase)
            train["target"].append(target)
    
    test_df = pd.DataFrame(test)
    train_df = pd.DataFrame(train)

    dir = "files/output"
    if not os.path.exists(dir):
        os.makedirs(dir)
    
    test_df.to_csv(os.path.join(dir, "test_dataset.csv"), index=False)
    train_df.to_csv(os.path.join(dir, "train_dataset.csv"), index=False)