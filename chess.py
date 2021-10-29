import cv2
import numpy as np

w = 800
h = 800
ches=np.zeros((h , w ))

for i in range(h):
    
    for j in range(w):
       
        W=(i//100)%2
       
        B=(j//100)%2
        
        if (W % 2 == 0 and B % 2 == 0 ) or (W % 2 != 0  and  B % 2 != 0 ):
           
            ches[i][j]=255
        
        else:
           
            ches[i][j]=0
           

print(ches)

cv2.imwrite("pic.jpg",ches)

cv2.imshow("chess" , ches) 

cv2.waitKey()