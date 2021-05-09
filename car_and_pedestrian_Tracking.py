import cv2

#our image
#img_file = 'cars.png'
video=cv2.VideoCapture('tesla.mp4')

#our pre-trained car classifier
car_tracker_file = 'car.xml'
pedestrian_tracker_file = 'pedestrian.xml'

car_tracker=cv2.CascadeClassifier(car_tracker_file)
pedestrian_tracker=cv2.CascadeClassifier(pedestrian_tracker_file)


while True:

  #Read the current frame
  (read_successfull, frame) =video.read()

  if read_successfull:
       grayscaled_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  else:
      break

  cars= car_tracker.detectMultiScale(grayscaled_frame)
  pedestrians= pedestrian_tracker.detectMultiScale(grayscaled_frame)

  #print(cars)

  for (x,y,w,h) in cars:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

  for (x,y,w,h) in pedestrians:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
   #display the images with cars spotted
  cv2.imshow('vizzp car detector',frame)

  # don't autoclose ,wait for a keypress
  key=cv2.waitKey(1)

  if key==81 or key==113:
    break

video.release()

"""
  car_tracker=cv2.CascadeClassifier(classifier_file)

  grayscaled_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#detect car
  cars= car_tracker.detectMultiScale(black_n_white)

#draw rectangle around the cars
  for (x,y,w,h) in cars:
      cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

#display the images with cars spotted
cv2.imshow('vizzp car detector',img)

#don't autoclose ,wait for a keypress
cv2.waitKey()
"""
print("code completed")