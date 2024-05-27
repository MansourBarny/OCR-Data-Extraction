# Extraction de Texte OCR

## Description

Ce projet démontre l'utilisation de l'OCR pour extraire du texte à partir d'images en utilisant Python. Les données extraites comprennent le contenu textuel, sa localisation sur l'image et le niveau de confiance du processus OCR. De plus, un tableau structuré est extrait d'une des images.

## Fichiers

- `main.py`: Le script principal pour l'extraction OCR.
- `requirements.txt`: Les dépendances Python.
- `genova_text_info.json`.
- `iqoa_text_info.json`.

## Comment Exécuter

1. Installez les dépendances requises :
    ```
    pip install -r requirements.txt
    ```
2. Placez les images `Genova.png` et `Extrait_IQOA_data.png` dans le même répertoire que `main.py`.
3. Exécutez le script :
    ```
    python main.py
    ```
4. Les résultats seront sauvegardés dans `genova_text_info.json`, `iqoa_text_info.json`, et `iqoa_table_data.json`.

## Exemple de Résultat

Exemple de sortie JSON pour l'image de Gênes :
```json
[
    {
        "text": "Gênes",
        "left": 100,
        "top": 50,
        "width": 100,
        "height": 30,
        "confidence": 95
    },
    ...
]
