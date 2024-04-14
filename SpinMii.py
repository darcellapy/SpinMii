# nova is real

import time
import urllib.request

def main():
  print("NOTE: the process of downloading the rendered mii frames is complete when the program says \"done! the program will now close automatically\". if it closes randomly, that means the downloading of the renders failed. anyways, have fun!\nmade by nova\n")
  time.sleep(10)
  
  leFunniURLpart1 = "https://studio.mii.nintendo.com/miis/image.png?data="

  leFunniURLpart2 = "&type=face&expression=surprise_open_mouth&width=512&bgColor=FFFFFF00&clothesColor=default&cameraXRotate="
  
  leFunniURLpart3 = "&cameraYRotate="
  
  leFunniURLpart4 = "&cameraZRotate=0&characterXRotate=0&characterYRotate=0&characterZRotate=0&lightDirectionMode=none&instanceCount=1&instanceRotationMode=model"

  cameraY = 0
  
  cameraX = 0

  miiID = input("enter your mii code (if you don't know how to get one, read the README.txt provided or contact @glitchyteam): ")
  
  num = 0
  
  horiORvert = input("welcome to SpinMii. how do you want your mii to spin? (h = horizontal, v = vertical): ")
  
  if horiORvert.lower() == "h":
    try:
      urllib.request.urlretrieve(f"https://studio.mii.nintendo.com/miis/image.png?data={miiID}&type=face&expression=surprise_open_mouth&width=512&bgColor=FFFFFF00&clothesColor=default&cameraXRotate=0&cameraYRotate=0&cameraZRotate=0&characterXRotate=0&characterYRotate=0&characterZRotate=0&lightDirectionMode=none&instanceCount=1&instanceRotationMode=model", "./spin/" + str(0) + ".png")
    except Exception as e:
        print(f"an error occured, here's the details:\n{e} ")
    while True:
      cameraY = cameraY + 10
      imgURL = leFunniURLpart1 + miiID + leFunniURLpart2 + str(0) + leFunniURLpart3 + str(cameraY) + leFunniURLpart4
      num = num + 1
      urllib.request.urlretrieve(imgURL, "./spin/" + str(num) + ".png")
      print(f"{cameraY} of 360 [GET {imgURL}]")
      if cameraY == 360:
          break
    print("done! the program will now close automatically")
    time.sleep(5)
    exit()
  elif horiORvert.lower() == "v":
    try:
      urllib.request.urlretrieve(f"https://studio.mii.nintendo.com/miis/image.png?data={miiID}&type=face&expression=surprise_open_mouth&width=512&bgColor=FFFFFF00&clothesColor=default&cameraXRotate=0&cameraYRotate=0&cameraZRotate=0&characterXRotate=0&characterYRotate=0&characterZRotate=0&lightDirectionMode=none&instanceCount=1&instanceRotationMode=model", "./spin/" + str(0) + ".png")
    except Exception as e:
        print(f"an error occured, here's the details:\n {e} ")
    while True:
      cameraX = cameraX + 10
      imgURL = leFunniURLpart1 + miiID + leFunniURLpart2 + str(cameraX) + leFunniURLpart3 + str(0) + leFunniURLpart4
      num = num + 1
      urllib.request.urlretrieve(imgURL, "./spin/" + str(num) + ".png")
      print(f"{cameraX} of 360 [GET {imgURL}]")
      if cameraX == 360:
          break
    print("done! the program will now close automatically")
    time.sleep(5)
    exit()
  else:
    print("did not get a valid response.\nexiting. . .")
    exit()
 
main()