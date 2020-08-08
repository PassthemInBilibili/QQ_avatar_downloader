# QQ_avatar_downloader

## Why writing this? 

Actually at first, this code was for my studying of Python, which was a mess and was not "pythonic". But the code seems useful. This is why I put this code onto Github. 

## How to use? 

First is to run this program. 

```
> python downloader.py
```

Then, you can see the time you open the program, and it will ask you for mode. 

If you enter nothing or enter "a", it goes to the mode A, which will read "list.txt" and download the avatars. 

In the "list.txt", you can write like: 

```
Ruixi_Xia 2781827514
Haowei_Mao 2428691146
```

Remember not to write any empty line. 

Before downloading, it will ask you the way to name the files. "NAME" means the name you wrote in "list.txt" like "Ruixi_Xia" and "Haowei_Mao". "RANDOM" means a random number from 10000000 to 99999999. "ID" means the id of the user like "2781827514" and "2428691146". 

If you enter "b", it goes to the mode B. 

It will download the avatars of the users of the ids from what you entered first to what you entered last. 

If you enter "c", it goes to the mode C. 

Then, you can enter like "514827901-514827941-10;233333333", which will download the avatars of the users of the ids of "514827901, 514827911, 514827921, 514827931, 514827941, 233333333". 

## How it works? 

If you want to download that of the id "123456789", it will GET "http://q1.qlogo.cn/g?b=qq&nk=123456789&s=640" and download it into your computer. 

**I'm sorry but my skill of writing English is really bad. Some of the sentences may be unable to understand...**
