from cv2 import *

IMG_SRC = 'sample/src.png'

if __name__ == '__main__':
    src = imread(IMG_SRC)

    # Kernel definition
    kernel = getStructuringElement(MORPH_ELLIPSE, (5, 5))

    # Contrast enhancement
    dilated = dilate(src, kernel)
    topHat = morphologyEx(src, MORPH_TOPHAT, kernel)
    blackHat = morphologyEx(src, MORPH_BLACKHAT, kernel)
    accentuated = add(src, topHat)
    highContrast = subtract(accentuated, blackHat)

    # Background subtraction
    backgroundSubtraction = subtract(highContrast, dilated)

    # Threshold to extract microcalcifications
    th, thresholding = threshold(backgroundSubtraction, 25, 255, THRESH_BINARY)

    imshow('Microcalcifications', thresholding)
    waitKey(0)
