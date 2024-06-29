from PIL import Image
import os
import glob

# Directory contenenti le immagini per i canali di colore
red_folder = 'RedFolder'
green_folder = 'GreenFolder'
blue_folder = 'BlueFolder'

# Percorso della cartella in cui salvare le immagini sovrapposte
output_folder = 'MergeFolder'

# Assicurarsi che le cartelle esistano
os.makedirs(output_folder, exist_ok=True)

# Trova tutte le immagini nelle cartelle (formato PNG anziché JPG)
red_images = sorted(glob.glob(os.path.join(red_folder, '*.png')))
green_images = sorted(glob.glob(os.path.join(green_folder, '*.png')))
blue_images = sorted(glob.glob(os.path.join(blue_folder, '*.png')))

# Assicurarsi che le cartelle contengano lo stesso numero di immagini
assert len(red_images) == len(green_images) == len(blue_images), "Numero diverso di immagini nelle cartelle"

# Itera su tutte le immagini
for i in range(len(red_images)):
    print(i)
    # Carica le immagini per i canali di colore
    image_red = Image.open(red_images[i]).convert('RGB')
    image_green = Image.open(green_images[i]).convert('RGB')
    image_blue = Image.open(blue_images[i]).convert('RGB')
    
    # Assicurarsi che le immagini abbiano le stesse dimensioni
    width, height = image_red.size
    image_green = image_green.resize((width, height))
    image_blue = image_blue.resize((width, height))
    
    # Creare nuove immagini per ogni canale di colore
    red_channel = image_red.split()[0]
    green_channel = image_green.split()[1]
    blue_channel = image_blue.split()[2]
    
    # Combinare i canali per creare l'immagine finale
    final_image = Image.merge("RGB", (red_channel, green_channel, blue_channel))
    
    # Salvare l'immagine finale sovrapposta nella cartella di output
    output_filename = os.path.join(output_folder, f'composite_image_{i}.png')
    final_image.save(output_filename)

print("Immagini composite create con successo!")
