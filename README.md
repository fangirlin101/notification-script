# notification-script
This is a python script to send a notification to the desktop. This was made using Python: I used Plyer specifically to implement this. 
To install plyer, ``` pip install plyer ``` is sufficient 

In order to make this an executable file, I used PyInstaller, which I installed using ``` pip install pyinstaller ``` 

The command to make the executable successfully for Windows is as follows: 

``` pyinstaller --onefile --hidden-import plyer.platforms.win.notification notifs.py ``` 


