#!/usr/bin/env python

import time
from plyer import notification
 
 
if __name__=="__main__":
 
        notification.notify(
            title = "hi",
            message="hello Vasundhara" ,
           
            # displaying time
            timeout=2
)
        # waiting time
        time.sleep(7)