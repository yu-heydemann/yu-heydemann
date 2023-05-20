from PIL import Image, ImageDraw, ImageFont
import time

def generate_heart_image(number):
   
    image_width, image_height = 200, 200
    background_color = (255, 255, 255)  

   
    image = Image.new('RGB', (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    
    heart_color = (255, 0, 0)  
    heart_size = 100
    heart_position = ((image_width - heart_size) // 2, (image_height - heart_size) // 2)
    draw.ellipse((heart_position, (heart_position[0] + heart_size, heart_position[1] + heart_size)), fill=heart_color)

   
    text_color = (0, 0, 0)  
    text_position = (image_width // 2, image_height // 2)
    font = ImageFont.truetype('arial.ttf', 30) 
    text = str(number)
    text_width, text_height = draw.textsize(text, font=font)
    text_position = (text_position[0] - text_width // 2, text_position[1] - text_height // 2)
    draw.text(text_position, text, fill=text_color, font=font)

    return image


number = 72  
image = generate_heart_image(number)
image.save('heart.png')

while True:
    
    number += 1
    image = generate_heart_image(number)
    image.save('heart.png')
    time.sleep(1)
