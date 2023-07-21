def findEncodings(images):
encodeList = []
for img in images:
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
encode = face_recognition.face_encodings(img)[0]
encodeList.append(encode)
return encodeList

def markAttendance(name):
with open('Attendance.csv', 'r+') as f:
myDataList = f.readlines()
nameList = []

for line in myDataList:
entry = line.split(',')
nameList.append(entry[0])

if name not in nameList:
now = datetime.now()
timeString=now.strftime('%H:%M:%S')
dateString=now.strftime('%d/%m/%Y')
f.writelines(f'\n{name},{timeString},{dateString}')
"""if dateString != now.strftime('%d/%m/%Y'):
f.writelines(f'\n{name},{timeString},{dateString}')"""
#ds = now.strftime('%d/%m')
'''if ds in nameList:
f.writelines(f'\n{name},{timeString},{dateString}')'''
#ms = now.strftime('%d/%m')

encodeListKnown = findEncodings(images)
print('Encoding Complete')

videoCap = cv2.VideoCapture(0)
while True:
success, img = videoCap.read()
imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)
imgSmall = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

faceCurrentFrame=face_recognition.face_locations(imgSm
all)
encodeCurrentFrame=face_recognition.face_encodings(im
gSmall,faceCurrentFrame)

for encodeFace, faceLoc in zip(encodeCurrentFrame,
faceCurrentFrame):
matches=face_recognition.compare_faces(encodeListKn
own,encodeFace)
faceDis=face_recognition.face_distance(encodeListKnown,
encodeFace)
print(faceDis)

matchIndex = np.argmin(faceDis)

if matches[matchIndex]:
name = classNames[matchIndex].upper()
print(name)
y1, x2, y2, x1 = faceLoc
# y1,x2,y2,x1 = y1*3,x2*3,y2*3,x1*3
cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0),
cv2.FILLED)
cv2.putText(img, name, (x1 + 6, y2 - 6),
cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

markAttendance(name)

cv2.imshow('Webcam', img)
#cv2.waitKey(1)
if cv2.waitKey(10)==13:
break
cap.release()
cv2.destroyAllWindows()