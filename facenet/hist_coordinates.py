import cv2
from PIL import Image
def main(): 
	try: 
		#Relative Path 
		img = Image.open("/home/harish/Pictures/dt2-hand-gesture/2handsdown.jpg") 
		
		#Getting histogram of image 
		print(img.histogram()) 
		
	except IOError: 
		pass

if __name__ == "__main__": 
	main() 

