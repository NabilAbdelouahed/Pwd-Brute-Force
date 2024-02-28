import pyautogui
import time

characters =  ['0','1','2','3','4','5','6','7','8','9']

length = 6
pwd_img = [0 for i in range(length)]
pwd = characters[0] * length
pwd_img[-1] -= 1

while length<7 :
    print(">>>>>>> generating passwords "+str(length)+" <<<<<<<")

    pointer = length - 1
    while pwd != characters[-1] * length :

        if pwd_img[pointer] <= len(characters)-2 :
            pwd_img[pointer] += 1

        else :
            for i in range(len(pwd_img)-1,-1,-1) :
                if pwd_img[i] != len(characters)-1 :
                    pwd_img[i] += 1
                    for j in range(i+1,len(pwd_img)) :
                        pwd_img[j] = 0
                        break
        pwd = ""
        for k in range(len(pwd_img)) :
            pwd += characters[pwd_img[k]]
        pyautogui.typewrite(pwd)
        time.sleep(0.5)
        pyautogui.press("enter")
    length+=1
    pwd_img = [0 for i in range(length)]
    pwd = characters[0] * length
    pwd_img[-1] -= 1
