Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... secret = random.randint(1, 100)
... guess = 0
... tries = 0
... 
... while guess != secret:
...     guess = int(input("یک عدد بین ۱ تا ۱۰۰ حدس بزن: "))
...     tries = tries + 1
... 
...     if guess < secret:
...         print("برو بالاتر")
...     elif guess > secret:
...         print("بیا پایین‌تر")
...     else:
