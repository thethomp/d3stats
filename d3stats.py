
m datetime import datetime
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

## XP entry field var
xp_before_var = Tkinter.StringVar()
xp_after_var = Tkinter.StringVar()

## Gold vars
gold_before_var = Tkinter.StringVar()
gold_after_var = Tkinter.StringVar()

## yellow mob vars
yellow_mob_var = Tkinter.IntVar()

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

def find_xp_gain():
    if xp_before_var.get() != "" and xp_after_var.get() != "":
        xp_b = (int)(xp_before_var.get())
        xp_a = (int)(xp_after_var.get())
        change = abs(xp_a - xp_b)
    #else:
        # create pop up error message
        # tell user to put proper input

def yellow_subtract():
    yellow_mob_var.set(yellow_mob_var.get()-1)
    
def yellow_add():
    yellow_mob_var.set(yellow_mob_var.get()+1)

###############
# Layout management
################
## Time labels
start_time_label = Tkinter.Label(top,text="Start Time").grid(row=0,column=2)
stop_time_label = Tkinter.Label(top,text="Stop Time").grid(row=1,column=2)
total_time_label = Tkinter.Label(top,text="Run Length").grid(row=2,column=2)

##XP Labels
xp_before_label = Tkinter.Label(top,text="XP Before",fg='red')
xp_before_label.grid(row=4,column=0)
xp_after_label = Tkinter.Label(top,text="XP After",fg='red')
xp_after_label.grid(row=5,column=0)

## MOB Labels
blue_mob_label = Tkinter.Label(top,text="Blue Mobs",bg='blue',fg='white').grid(row=8,column=0)
yellow_mob_label = Tkinter.Label(top,text="Yellow Mobs",bg='yellow').grid(row=9,column=0)
gob_mob_label = Tkinter.Label(top,text="Treasure Gobs",bg='brown').grid(row=10,column=0)

## Timestamp fields
start_timestamp = Tkinter.Label(top,textvariable=start_time_var,width=10).grid(row=0,column=1)
stop_timestamp = Tkinter.Label(top,textvariable=stop_time_var,width=10).grid(row=1,column=1)
total_timestamp = Tkinter.Label(top,textvariable=run_time_var,width=10).grid(row=2,column=1)

##XP fields
xp_before_field1 = Tkinter.Entry(top,textvariable=xp_before_var,width=12)
xp_before_field1.grid(row=4,column=1)#,columnspan=2)
xp_before_field2 = Tkinter.Entry(top,width=12).grid(row=4,column=2)#,columnspan=2)
xp_level_field1 = Tkinter.Entry(top,width=3).grid(row=4,column=3)

xp_after_field1 = Tkinter.Entry(top,textvariable=xp_after_var,width=12)
xp_after_field1.grid(row=5,column=1)#,columnspan=2)
xp_after_field2 = Tkinter.Entry(top,width=12).grid(row=5,column=2)#,columnspan=2)
xp_level_field2 = Tkinter.Entry(top,width=3).grid(row=5,column=3)

## gold fields
start_gold_label = Tkinter.Label(top,text='Starting Gold',width=10).grid(row=6,column=0)
end_gold_label = Tkinter.Label(top,text='Ending Gold',width=10).grid(row=7,column=0)
start_gold_field = Tkinter.Entry(top,textvariable=gold_before_var,width=15).grid(row=6,column=1)
end_gold_field = Tkinter.Entry(top,textvariable=gold_after_var,width=15).grid(row=7,column=1)



## Paragon level check buttons
paragon_lvl_checkbox = Tkinter.Checkbutton(top,text="Paragon",variable=paragon_lvl_var).grid(row=4,column=4,rowspan=2)

## Timer Buttons
start_timer_button = Tkinter.Button(top,text="Start",command=update_time).grid(row=0,column=0)
stop_timer_button = Tkinter.Button(top,text="Stop",command=update_time).grid(row=1,column=0)
clear_timers_button = Tkinter.Button(top,text="Clear",command=clear_time).grid(row=2,column=0)

# XP Button
#xp_change_button = Tkinter.Button(top,text="Change",command=find_xp_gain).grid(row=6,column=0)

## yellow mobs
yellow_subtract_button= Tkinter.Button(top,text="-",command=yellow_subtract).grid(row=8,column=1)
yellow_label = Tkinter.Entry(top,textvariable=yellow_mob_var,width=3).grid(row=8,column=2)
yellow_add_button= Tkinter.Button(top,text="+",command=yellow_add).grid(row=8,column=3)


####
# Mainloop
###
top.mainloop()


