#----------------------------------------------------------------
# Author : Samuel Dubuis
#
# Script that pops a fullscreen window of the actual time, over all other windows so that
# it acts as a alarm, with a pre-defined text maybe
#----------------------------------------------------------------
import sys
from tkinter import * 
from tkinter.ttk import *
from time import strftime
from datetime import *

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

def test():
    root = Tk()
    root.title('Clock') 
    root.attributes('-fullscreen', True)
    root.bind('<Escape>',lambda e: root.destroy())
    root.configure(background='orange')
    
    # This function is used to  
    # display time on the label 
    def time(): 
        string = strftime('%H:%M:%S %p') 
        lbl.config(text = string) 
        lbl.after(1000, time) 
    
    # Styling the label widget so that clock 
    # will look more attractive 
    lbl = Label(root, font = ('calibri', 150, 'bold'), 
                background = 'orange', 
                foreground = 'white') 
    
    # Placing clock at the centre 
    # of the tkinter window 
    lbl.pack(anchor = 'center',expand=2, fill='both')
    time() 

    root.mainloop()
    sched.shutdown(wait=False)

today = datetime.today()
today = today.strftime("%Y-%m-%d")
exec_time = today+" "+sys.argv[1]
# print("ALARM IN : ", exec_time-datetime.now())
sched.add_job(test, 'date', run_date=exec_time)
sched.start()
sys.exit()
 
