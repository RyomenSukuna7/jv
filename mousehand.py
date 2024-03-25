import cv2
import mediapipe as mp
import pyautogui as pa
import time


video=cv2.VideoCapture(0)
temphand=mp.solutions.hands
hand=temphand.Hands()
draws=mp.solutions.drawing_utils
ptime=0
indexy=0
indexx=0
thumby=0
thumbx=0

while True:
    e,frame=video.read()
    
    if e==True:
        
        frame=cv2.flip(frame,1)
        colors=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result=hand.process(colors)
        
        h,w,c=frame.shape
       
        if result.multi_hand_landmarks:
            
            cx=cy=0
            for handss in result.multi_hand_landmarks:
               
               
                for id,lm in enumerate(handss.landmark):
                    cx,cy=int(lm.x*w),int(lm.y*h)
                    if id==8:
                        frame=cv2.circle(img=frame,center=(cx,cy),radius=16,color=(255,255,0))
                        indexx=cx
                        indexy=cy
                        pa.moveTo(indexx,indexy)
                    if id==4:
                        frame=cv2.circle(img=frame,center=(cx,cy),radius=16,color=(255,0,255))
                        thumbx=cx
                        thumby=cy
                if abs(thumby-indexy)<20:
                     pa.click()
                    
                
                
                            
                    
                    
                    # if id==12:
                    #     print("click")
                    #     pa.click()
                    #     pa.sleep(1)
                        
                           
                        

                        
                draws.draw_landmarks(frame,handss,temphand.HAND_CONNECTIONS)
                
        
        ctime=time.time()
        fps= 1/(ctime-ptime)
        ptime=ctime
        
        frame=cv2.putText(img=frame,text=str(int(fps)),org=(100,50),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=5,color=(0,0,0))
        cv2.imshow("mousecontrol",frame)
        
        if cv2.waitKey(10) % 0xff==ord('q'):
            break



cv2.destroyAllWindows()