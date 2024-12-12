import cv2

img1 = cv2.imread("pikachu.png",1)
cv2.imshow("pikachu",img1)

#lines
startpoint = (80,80)
endpoint = (280,80)
color = (0,255,0)
thickness = 10
imgL = cv2.imread("pikachu.png",1)

imgline = cv2.line(imgL,startpoint,endpoint,color,thickness)
cv2.imshow("line pikachu", imgline)


"""#circle
coordinates = (120,120)
radius = 50
color = (0,0,255)
thickness = 10
imgC = cv2.imread("pikachu.png",1)

imgcircle = cv2.circle(imgC,coordinates,radius,color,thickness)
cv2.imshow("circle pikachu", imgcircle)

#filled circle
coordinates = (240,120)
radius = 35
color = (255,0,0)
thickness =  -1 #fills circle: (-1)
imgFC = cv2.imread("pikachu.png",1)

imgcircle_filled = cv2.circle(imgFC,coordinates,radius,color,thickness)
cv2.imshow("circle fill pikachu", imgcircle_filled)

#rectangle
topleft = (100,100)
bottomright = (190,190)
color = (255,255,0)
thickness = 10
imgFRect = cv2.imread("pikachu.png",1)

imgRect_filled = cv2.rectangle(imgFRect,topleft,bottomright,color,thickness)
cv2.imshow("Fill Rectangle pikachu", imgRect_filled)

#text
coordinates = (100,100)
color = (0,0,0)
thickness = 5
text = ("OpenCV!")
font = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 2

imgT = cv2.imread("pikachu.png",1)

imgText = cv2.putText(imgT,text,coordinates,font,fontscale,color,thickness,cv2.LINE_AA)
cv2.imshow("Text Pikachu",imgText)"""

#Pentagon

startp1 = (200,20)
endp1 = (300,100)

color = (0,0,0)
thickness = 5
imgPent = cv2.imread("pikachu.png",1)

imgPentagon = cv2.line(imgPent,startp1,endp1,color,thickness)
cv2.imshow("Pentagon Pikachu", imgPentagon)

startp2 = (300,100)
endp2 = (270,200)

imgPentagon = cv2.line(imgPent,startp2,endp2,color,thickness)
cv2.imshow("Pentagon Pikachu", imgPentagon)

startp3 = (270,200)
endp3 = (130,200)

imgPentagon = cv2.line(imgPent,startp3,endp3,color,thickness)
cv2.imshow("Pentagon Pikachu", imgPentagon)

startp4 = (130,200)
endp4 = (100,100)

imgPentagon = cv2.line(imgPent,startp4,endp4,color,thickness)
cv2.imshow("Pentagon Pikachu", imgPentagon)

startp5 = (100,100)
endp5 = (200,20)

imgPentagon = cv2.line(imgPent,startp5,endp5,color,thickness)
cv2.imshow("Pentagon Pikachu", imgPentagon)

cv2.waitKey(0)
cv2.destroyAllWindows()