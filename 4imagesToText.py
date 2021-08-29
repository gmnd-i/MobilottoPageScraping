import os
from PIL import Image
import pytesseract

print("start");

texts = []

for file_name in os.listdir("Images"):
    img = Image.open("Images/" + file_name);
    #print(pytesseract.image_to_string(img))
    texts.append(pytesseract.image_to_string(img));
    print("-");
    
f = open("allText.txt", "w");

for t in texts:
    f.write(t);
    f.write("\n");
    print("*");

f.close();


