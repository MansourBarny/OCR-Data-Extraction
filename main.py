import cv2
import pytesseract
import json
import os

os.system("apt-get install -y tesseract-ocr")

# Définir le chemin vers l'exécutable Tesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Pour extraire le texte et les informations associées
def extract_text_info(image):
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    text_info = []
    for i in range(len(data['text'])):
        if data['text'][i].strip():
            text_info.append({
                'text': data['text'][i],
                'left': data['left'][i],
                'top': data['top'][i],
                'width': data['width'][i],
                'height': data['height'][i],
                'confidence': data['conf'][i]
            })
    return text_info

# Chargement des images
genova_img = cv2.imread('Genova.png')
iqoa_img = cv2.imread('Extrait_IQOA_data.png')

# Extraire les informations de texte pour les deux images
genova_text_info = extract_text_info(genova_img)
iqoa_text_info = extract_text_info(iqoa_img)

# Sauvegarder les résultats dans des fichiers JSON
with open('genova_text_info.json', 'w') as genova_file:
    json.dump(genova_text_info, genova_file, indent=4)

with open('iqoa_text_info.json', 'w') as iqoa_file:
    json.dump(iqoa_text_info, iqoa_file, indent=4)

print("Les résultats ont été sauvegardés dans les fichiers genova_text_info.json et iqoa_text_info.json.")

# Extraction du tableau structuré

gray = cv2.cvtColor(iqoa_img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

table_image = iqoa_img.copy()
cv2.drawContours(table_image, contours, -1, (0, 255, 0), 3)

# Extraire le texte en utilisant Tesseract
data = pytesseract.image_to_data(iqoa_img, output_type=pytesseract.Output.DICT)

# Organiser les données extraites en structure de tableau
table_data = []
for i in range(len(data['text'])):
    if data['text'][i].strip():
        table_data.append({
            'text': data['text'][i],
            'left': data['left'][i],
            'top': data['top'][i],
            'width': data['width'][i],
            'height': data['height'][i],
            'confidence': data['conf'][i]
        })

# Sauvegarder les résultats dans un fichier JSON
with open('iqoa_table_data.json', 'w') as json_file:
    json.dump(table_data, json_file, indent=4)

print("Les résultats du tableau ont été sauvegardés dans le fichier iqoa_table_data.json.")
