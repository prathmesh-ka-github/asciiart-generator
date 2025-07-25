from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import sys
import colorama
from colorama import Fore
from colorist import ColorRGB

colorama.init(autoreset=True)

image_width=200
ascii_chars = " .,-~:;=+^*>!\#$&%@"

#ascii_chars = " .-~+=*#%$@"
#ascii_chars = " .,'-~:;=+^*>!\)]#&$%@"
#ascii_chars = " .,-~+*#$%@"

ascii_art_generator ="   _____    _________________ .___.___\n  /  _  \  /   _____\_   ___ \|   |   |\n /  /_\  \ \_____  \/    \  \/|   |   |  \n/    |    \/        \     \___|   |   |  \n\____|__  /_______  /\______  |___|___|  \n        \/        \/        \/                 \n   _____          __    ________                                   __  \n  /  _  \________/  |_ /  _____/  ____   ____   ________________ _/  |_ ___________   \n /  /_\  \_  __ \   __/   \  ____/ __ \ /    \_/ __ \_  __ \__  \\    __/  _ \_  __ \    \n/    |    |  | \/|  | \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  |(  <_> |  | \/  \n\____|__  |__|   |__|  \______  /\___  |___|  /\___  |__|  (____  |__| \____/|__|     \n        \/                    \/     \/     \/     \/           \/                  \nMade with <3 by - https://prathmesh-ka-github.github.io/pratham-c0des./ \n"

def save_ascii_image(image_path, output_path, font_path=None, font_size = 30, color = (255,255,255)):
    # variables
    # ascii_chars=" .,-~:;=+^*>!\#$&%@"
    # using global ascii_chars

    # Load and resize the image
    image = Image.open(image_path)
    # height = int(width * image.height // image.width)
    height = int(image_width * image.height // image.width *0.7)
    image = image.resize((image_width,height), Image.NEAREST)

    # load fonts
    font = ImageFont.truetype("fonts/CourierPrime-Regular.ttf", font_size)

    char_width = int(font_size * 0.605)
    char_height = int(font_size * 0.87)
    img_width = char_width * image_width
    img_height = char_height * height

    # create a blank image
    img = Image.new('RGB',(img_width,img_height),(0,0,0))
    draw = ImageDraw.Draw(img)

    for y in range(height):
        for x in range(image_width):
            if image.getpixel((x,y)) == 0:
                r = g = b = 0
            elif image.getpixel((x,y)) == 1:
                r = g = b = 256
            else:
                r, g, b = image.getpixel((x,y))
            gray = 0.299 * r + 0.587 * g + 0.114 * b
            index = int(gray / 256 * len(ascii_chars))
            # text += ascii_chars[index]
            draw.text(
                (x * char_width, y * char_height),
                ascii_chars[index],
                font=font,
                fill=(r, g, b)
            )
    # Enhancer
    enhancer = ImageEnhance.Brightness(img)
    enhancedimg = enhancer.enhance(2)
    enhancedimg.save(output_path)

def create_ascii_art(image_path, width=100):
    image = Image.open(image_path)
    height = int(width * image.height // image.width *0.5)
    image = image.resize((width,height), Image.NEAREST)
    
    for y in range(height):
        for x in range(width):
            if image.getpixel((x,y)) == 0:
                r = g = b = 0
            elif image.getpixel((x,y)) == 1:
                r = g = b = 255
            else:
                r, g, b = image.getpixel((x,y))
            gray = 0.299 * r + 0.587 * g + 0.114 * b
            index = int(gray / 256 * len(ascii_chars))
            color = ColorRGB(r,g,b)
            print(f"{color}{ascii_chars[index]}{color.OFF}", end="")
            print(f"{color}{ascii_chars[index]}{color.OFF}", end="")
        print("\n")

def create_ascii_art_txt(image_path, width=100):
    image = Image.open(image_path)
    height = int(width * image.height // image.width *0.9)
    image = image.resize((width,height), Image.NEAREST)
    ascii_image = ""

    for y in range(height):
        for x in range(width):
            if image.getpixel((x,y)) == 0:
                r = g = b = 0
            elif image.getpixel((x,y)) == 1:
                r = g = b = 256
            else:
                r, g, b = image.getpixel((x,y))
            gray = 0.299 * r + 0.587 * g + 0.114 * b
            index = int(gray / 256 * len(ascii_chars))
            ascii_image += ascii_chars[index]
            ascii_image += ascii_chars[index]
        ascii_image += "\n"
    print("ASCII art dimentions - ",height,'x',width)
    return ascii_image

def save_ascii_art(input_image, output_type):
    if output_type == "txt":
        ascii_image = create_ascii_art_txt(input_image)
        with open("ascii_text", "w") as f:
            f.write(ascii_image)
        print(Fore.GREEN + "Done! ASCII Art saved to text file!")
        print("Open the file: ")
        print("> ascii_text.txt")
    elif output_type == "-" or output_type == "stdout":
        create_ascii_art(input_image)
    elif output_type == 'img':
        save_ascii_image(sys.argv[1],"ascii_image.jpg")
        print(Fore.GREEN + "Done! ASCII Art saved to ascii_image.jpg!")
        print("Open the file: ")
        print("> ascii_image.jpg")
    else:
        print_err()

def print_err():
    usercommand = ''
    for cmd in sys.argv:
        usercommand += (cmd + " ")
    print(Fore.RED+ '> python ' + usercommand)
    print(Fore.RED + "ERROR: Invalid arguments passed. Check Usage format.\n")
    print(Fore.GREEN + f"Usage: python {sys.argv[0]} <input_image> <output_type>")
    print("<input_image> - Your input image. [.png, .jpg, .jpeg, .webp, .tiff etc]\n                Check https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html for Image file format support.\n\n<output_type> - Use '-' or 'stdout' to print the output in command line.\n                Use 'txt' to get output in text file. You will get ascii_text.txt\n                Use 'img' to get output in image file. You will get ascii_image.jpg\n\nFor example, try this:\n> python galaxy.jpg -")

if __name__ == "__main__":
    print(" ")
    print(ascii_art_generator)
    if len(sys.argv) < 3:
        print_err()
        sys.exit(1)
    
    input_image = sys.argv[1]
    output_type = sys.argv[2]

    save_ascii_art(input_image, output_type)