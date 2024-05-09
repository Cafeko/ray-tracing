from PIL import Image

# Create ppm:
width = input("Largura: ")
heigth = input("Altura: ")
image_file = open("Imagem.ppm", "w")
image_file.write("P3\n")
image_file.write(width + " " + heigth + "\n")
image_file.write("255\n")
for y in range(int(heigth)):
    for x in range(int(width)):
        r = (y * 255) // int(heigth)
        c = "255"
        image_file.write(str(r) + " " + c + " " + c)
        image_file.write("\n")
image_file.close()
# Convert ppm to jpg:
image_path = ".\Imagem"
image = Image.open(image_path + ".ppm")
image.save(image_path + ".jpg")
