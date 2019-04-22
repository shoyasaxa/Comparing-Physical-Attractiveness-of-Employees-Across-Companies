import cv2
import sys
import os 

#imagePath = 'C:/Users/Shoya/Aphrodite/Goldman Employees/photos_original/ali-collins-217a895a.jpeg'

root_folders = ['C:/Users/Shoya/Aphrodite/Goldman Employees/', 'C:/Users/Shoya/Aphrodite/RBC Employees/']

 
for folder in root_folders:
	image_paths = folder+'photos_original/'
	for imagePath in os.listdir(image_paths):
		try:
			image = cv2.imread(image_paths+str(imagePath))
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

			faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
			faces = faceCascade.detectMultiScale(
			    gray,
			    scaleFactor=1.3,
			    minNeighbors=3,
			    minSize=(30, 30)
			)

			height,width,channels = image.shape 

			for (x, y, w, h) in faces:

				# edit borders to get a better picture of the whole face

				if ( x >= 30):
					x -= 30 
				elif ( x >= 15):
					x -= 15 
				else:
					pass 

				if ( y >= 40):
					y -= 40
				elif ( y >= 20):
					y -= 20 
				else:
					pass 

				if ( x + 60 <= width):		
					w += 60 
				elif ( x + 30 <= width):
					w += 30 
				else:
					pass

				if ( h + 60 <= height):
					h += 60
				elif ( h + 30 <= height):
					h += 30 
				else:
					pass 

				cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
				roi_color = image[y:y + h, x:x + w]
				print("[INFO] Object found. Saving locally.")
				cv2.imwrite( folder + 'photos_cropped/' + imagePath[:-5] + '_face.jpg', roi_color)

			#status = cv2.imwrite('faces_detected.jpg', image)
			print("Image Written")

		except Exception as e: 
			print(e)