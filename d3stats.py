#!/usr/bin/python
from datetime import datetime
import Tkinter, time

############
## master window creation and config
############
top = Tkinter.Tk()
top.title("GGD3Stats")

#########
## string var declarations for all the labels and fields
#########
start_time_var = Tkinter.StringVar()
stop_time_var = Tkinter.StringVar()
run_time_var = Tkinter.StringVar()

##########
## Functions
##########
def update_time():
	time_fmt='%H:%M:%S'
	ts = time.time()
	ft = datetime.fromtimestamp(ts).strftime(time_fmt)
	if start_time_var.get() == "": 
		start_time_var.set(ft)
	elif stop_time_var.get() == "":
		stop_time_var.set(ft)
		run_time_var.set(datetime.strptime(stop_time_var.get(),time_fmt)-datetime.strptime(start_time_var.get(),time_fmt))
	else:
		start_time_var.set("")
		stop_time_var.set("")
		run_time_var.set("")

###############
# Layout management
################
start_time_label = Tkinter.Label(top,text="Start Time").grid(row=0,column=1)
stop_time_label = Tkinter.Label(top,text="Stop Time").grid(row=0,column=2)
start_timestamp = Tkinter.Label(top,textvariable=start_time_var).grid(row=1,column=1)
stop_timestamp = Tkinter.Label(top,textvariable=stop_time_var).grid(row=1,column=2)
total_time_label = Tkinter.Label(top,text="Run Length").grid(row=0,column=3)
total_timestamp = Tkinter.Label(top,textvariable=run_time_var).grid(row=1,column=3)
timer_button = Tkinter.Button(top,text="Start/Stop",command=update_time).grid(row=1,column=0)

####
# Mainloop
###
top.mainloop()
