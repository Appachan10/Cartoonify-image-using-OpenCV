#Importing required libraries
import cv2  

def cartoonify(img_rgb):    
    #STEP 1
    #{ Use bilateral filter for edge-aware smoothing. }
    numBilateralFilters = 7
    img_color = img_rgb
    
    # repeatedly apply small bilateral filter instead of
    # applying one large filter 
    for _ in range(numBilateralFilters):
      img_color = cv2.bilateralFilter(img_color, 15, 30, 15)
      
    #STEP 2
    #{ Convert to grayscale }   
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    #STEP 3 
    #{ Use median filter to reduce noise }
    img_blur = cv2.medianBlur(img_gray, 7)
    
    #STEP 4
    #{ Use adaptive thresholding to create an edge mask
    # detect and enhance edges }
    img_edge = cv2.adaptiveThreshold(img_blur, 240,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 3, 2)
    
    # Step 5
    #{ Combine color image with edge mask & display picture
    # convert back to color, bit-AND with color image }
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    return cv2.bitwise_and(img_color, img_edge)

#image input
img_rgb = cv2.imread("/content/test.jpg")
output = cartoonify(img_rgb)

#display
cv2.imshow(output)

#............Pixelating.............

# Get input size
height, width = output.shape[:2]

# Desired "pixelated" size
w, h = (100, 100)

# Resize input to "pixelated" size
temp = cv2.resize(output, (w, h), interpolation=cv2.INTER_LINEAR)

# Initialize pixelated image
pixelate = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

cv2_imshow(pixelate)

