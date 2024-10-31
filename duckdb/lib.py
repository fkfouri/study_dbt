import glob
import os
from pathlib import Path
from typing import List


def listar_arquivos_filtrados(diretorio, filter="*.*") -> List[Path]:
    padrao = os.path.join(diretorio, filter)
    arquivos_filtrados = []

    for caminho_completo in glob.glob(padrao):
        arquivos_filtrados.append(Path(caminho_completo))

    return arquivos_filtrados