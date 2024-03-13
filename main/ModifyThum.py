from PIL import Image, ImageFont, ImageDraw
import FetchViews


#Generating the thumnail
def genThumnail():
    views = FetchViews.getViews()
    img = Image.open('components/img0.jpg')
    font = ImageFont.truetype("arial.ttf", 100)

    draw = ImageDraw.Draw(img)

    text = f'Views => {views}'

    font_color = (255, 255, 255)  # White color
    draw.text((10, 450), text, font_color, font=font)
    img.save('components/img1.jpg')
genThumnail()