By providing, the correct IDs for elements in a LogIn web page, The script simulates a user using chromium webdriver through selenium module and tries to brute force the login using all possible passwords within the given range.
There is also a password_generator code that gives a list of all possible passwords that have the given length. The code can be easily be modified to write directly to txt file if needed, using : 
```
f = open("pwd_list.txt", "a")
f.write(pwd)
f.close()
```
