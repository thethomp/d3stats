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
## Timer vars
start_time_var = Tkinter.StringVar()
stop_time_var = Tkinter.StringVar()
run_time_var = Tkinter.StringVar()

## Paragon checkbox var
paragon_lvl_var = Tkinter.IntVar()

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
#	else:
#		start_time_var.set("")
#		stop_time_var.set("")
#		run_time_var.set("")

def clear_time():
	start_time_var.set("")
	stop_time_var.set("")
	run_time_var.set("")

###############
# Layout management
################
## Time labels
start_time_label = Tkinter.Label(top,text="Start Time").grid(row=0,column=2)
stop_time_label = Tkinter.Label(top,text="Stop Time").grid(row=1,column=2)
total_time_label = Tkinter.Label(top,text="Run Length").grid(row=2,column=2)

##XP Labels
xp_before_label = Tkinter.Label(top,text="XP Before",fg='red').grid(row=4,column=0)
xp_after_label = Tkinter.Label(top,text="XP After",fg='red').grid(row=5,column=0)

## Timestamp fields
start_timestamp = Tkinter.Label(top,textvariable=start_time_var,width=10).grid(row=0,column=1)
stop_timestamp = Tkinter.Label(top,textvariable=stop_time_var,width=10).grid(row=1,column=1)
total_timestamp = Tkinter.Label(top,textvariable=run_time_var,width=10).grid(row=2,column=1)

##XP fields
xp_before_field1 = Tkinter.Entry(top,width=12).grid(row=4,column=1)#,columnspan=2)
xp_before_field2 = Tkinter.Entry(top,width=12).grid(row=4,column=2)#,columnspan=2)
xp_level_field1 = Tkinter.Entry(top,width=3).grid(row=4,column=3)

xp_after_field1 = Tkinter.Entry(top,width=12).grid(row=5,column=1)#,columnspan=2)
xp_after_field2 = Tkinter.Entry(top,width=12).grid(row=5,column=2)#,columnspan=2)
xp_level_field2 = Tkinter.Entry(top,width=3).grid(row=5,column=3)

## Paragon level check buttons
paragon_lvl_checkbox = Tkinter.Checkbutton(top,text="Paragon",variable=paragon_lvl_var).grid(row=4,column=4,rowspan=2)

## Timer Buttons
start_timer_button = Tkinter.Button(top,text="Start",command=update_time).grid(row=0,column=0)
stop_timer_button = Tkinter.Button(top,text="Stop",command=update_time).grid(row=1,column=0)
clear_timers_button = Tkinter.Button(top,text="Clear",command=clear_time).grid(row=2,column=0)

####
# Mainloop
###
top.mainloop()

