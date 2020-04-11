"""
Creates a mosaic picture (Warhol Style)

Attributes:
    colors (list): a list of the selected colors

"""
import cv2
import numpy as np 
import argparse


COLORS = [['1', (37, 70, 219), (122, 202, 165)], ['2', (181, 134, 106), (188, 157, 242)], ['3', (143, 154, 58), (183, 149, 236)], 
			  ['4', (102, 185, 140), (199, 177, 242)], ['5', (76, 134, 237), (33, 84, 218)], ['6', (188, 222, 198), (191, 226, 200)]]


def generate_frame(img: str, color: tuple, filename: str):
	"""Generates a frame with selected color.
	
	Args:
	    img (str): filename of the original image
	    color (tuple): selected color (bgr)
	    filename (str): filename to save the edited image
	"""
	img = cv2.imread(img, cv2.IMREAD_COLOR)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	rows, cols, _ = img.shape

	roi = img[0:rows, 0:cols]
	roi[::] = color

	_, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
	canvas = cv2.bitwise_and(roi, roi, mask=threshold)

	cv2.imwrite(filename, canvas)


def generate_mosaic(filename: str):
	"""Created a mosaic of six different images
	
	Args:
	    filename (str): filename to save the edited image
	"""
	one = cv2.imread('1.jpg', cv2.IMREAD_COLOR)
	two = cv2.imread('2.jpg', cv2.IMREAD_COLOR)
	three = cv2.imread('3.jpg', cv2.IMREAD_COLOR)
	four = cv2.imread('4.jpg', cv2.IMREAD_COLOR)
	five = cv2.imread('5.jpg', cv2.IMREAD_COLOR)
	six = cv2.imread('6.jpg', cv2.IMREAD_COLOR)

	rows, columns, _ = one.shape

	canvas = np.zeros((2*rows + 1, 3*columns + 2, 3), np.uint8)

	canvas[0:rows, 0:columns] = one
	canvas[0:rows, (columns + 1):(2 * columns + 1)] = two
	canvas[0:rows, (2 * columns + 2):(3 * columns + 2)] = three
	canvas[(rows + 1):(2 * rows + 1), 0:columns] = four
	canvas[(rows + 1):(2 * rows + 1), (columns + 1):(2 * columns + 1)] = five
	canvas[(rows + 1):(2 * rows + 1), (2 * columns + 2):(3 * columns + 2)] = six
	
	cv2.imwrite(filename, canvas)


def main():
	parser = argparse.ArgumentParser(description='Process an input image to a mosaic in the Andy Warhol style.')

	parser.add_argument('input', type=str, help='Filename of the input image')
	parser.add_argument('--out', type=str, default='Mosaic.jpg',  help='Filename of the output image')

	args = parser.parse_args()

	try:
		for color in COLORS:
			generate_frame(args.input, color[1], '%s.jpg' % color[0])

	except cv2.error:
		print('Invalid input file.')

	except Exception as e:
		print(e)

	try:
		generate_mosaic(args.out)

	except Exception as e:
		print(e)

if __name__ == '__main__':

	main()