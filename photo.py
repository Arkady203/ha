from PIL import Image, ImageDraw #Подключим необходимые библиотеки. 

########################################
########################################


image = Image.open("input2.jpg") #Открываем изображение. 
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
width = image.size[0] #Определяем ширину. 
height = image.size[1] #Определяем высоту. 	
print('size:',width*height);
pix = image.load() #Выгружаем значения пикселей.

bl_p = 0
wh_p = 0

########################################
########################################

factor = int(input('factor:'))
for i in range(width):
	for j in range(height):
		a = pix[i, j][0]
		b = pix[i, j][1]
		c = pix[i, j][2]
		S = a + b + c
		if (S > (((255 + factor) // 2) * 3)):
			a, b, c = 255, 255, 255; wh_p +=1;
		else:
			a, b, c = 0, 0, 0; bl_p +=1;
		draw.point((i, j), (a, b, c))

########################################
########################################

print('black pixels: ',bl_p,'white pixels: ',wh_p);
print('%:',wh_p/(width*height));

image.save("output2.jpg", "JPEG")
print('save')
del draw