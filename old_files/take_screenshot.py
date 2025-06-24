from PIL import ImageGrab

# Define the region (left, top, right, bottom)
bbox = (100, 200, 600, 600)

screenshot = ImageGrab.grab(bbox=bbox)
screenshot.save('screenshot.png')
