import time

characters =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','W','X','Y','Z',
     'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
     '1','2','3','4','5','6','7','8','9',
     '*','-',' ']


length = 4
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


def generate_iter(characters, length):
     niveau_length = 1

     pwd_list = characters.copy()
     if length == 1:
          return (pwd_list)
     while niveau_length < length :
          pwd = []
          for i in range(len(pwd_list)):
               for j in range(len(characters)):
                    pwd.append(pwd_list[i]+characters[j])
          pwd_list = pwd.copy()
          niveau_length += 1
     return(pwd)

start = time.time()
print(generate_iter(characters,length))
end = time.time()
print(f"time : {end-start}")