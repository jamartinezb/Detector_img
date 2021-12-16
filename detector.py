  
import cv2

#utilizar camara del pc
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#leemos el clasificador
majinBooClassif = cv2.CascadeClassifier('cascade.xml')

while True:
	
	ret,frame = cap.read() #leer fotogramas
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #comvertir a escala de gris

	toy = majinBooClassif.detectMultiScale(gray,
#piramide de imagenes
 	scaleFactor = 1.5, #que tanto se reducirá la imagen en %
	minNeighbors = 1350, #numero mínimo de cuadros vecinos para identificar objeto si alto menos % de eficiencia valores bajos falsos positivos
	minSize=(100,100), # valores inferiores no son reconocidos
	maxSize=(200,200)) # tamaño máximo del objeto

	for (x,y,w,h) in toy:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2) #dibujar rectángulo de objeto detectado
		cv2.putText(frame,'CLUB NAVI',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA) # nombre del objeto

	cv2.imshow('frame',frame)
	
	if cv2.waitKey(1) == 27:
		break
cap.release()
cv2.destroyAllWindows()