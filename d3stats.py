#!/usr/bin/python
from datetime import datetime
from Tkinter import *
import Tkinter, time, tkMessageBox

############
## master window creation and config
############
top = Tkinter.Tk()
top.title("GGD3Stats")

####
# dropdown menu vars
###
DIFFICULTY = ['Normal','Hard','Expert','Master','Torment 1',
'Torment 2','Torment 3','Torment 4','Torment 5','Torment 6']
difficulty_var = StringVar(top)
difficulty_var.set('Difficulty')

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
blue_mob_var = Tkinter.IntVar()
gob_mob_var = Tkinter.IntVar()
purp_mob_var = Tkinter.IntVar()
lege_mob_var = Tkinter.IntVar()

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

def blue_subtract():
    blue_mob_var.set(blue_mob_var.get()-1)
    
def blue_add():
    blue_mob_var.set(blue_mob_var.get()+1)

def gob_subtract():
    gob_mob_var.set(gob_mob_var.get()-1)
    
def gob_add():
    gob_mob_var.set(gob_mob_var.get()+1)

def purp_subtract():
    purp_mob_var.set(purp_mob_var.get()-1)

def purp_add():
    purp_mob_var.set(purp_mob_var.get()+1)

def lege_subtract():
    lege_mob_var.set(lege_mob_var.get()-1)

def lege_add():
    lege_mob_var.set(lege_mob_var.get()+1)
    
###############
# Layout management
################
## Time labels
start_time_label = Tkinter.Label(top,text="Start Time").grid(row=0,column=2)
stop_time_label = Tkinter.Label(top,text="Stop Time").grid(row=1,column=2)
total_time_label = Tkinter.Label(top,text="Run Length").grid(row=2,column=2)

##XP Labels
xp_before_label = Tkinter.Label(top,text="XP Before",fg='red',width=18)
xp_before_label.grid(row=4,column=0)
xp_after_label = Tkinter.Label(top,text="XP After",fg='red')
xp_after_label.grid(row=5,column=0)

## MOB Labels
blue_mob_label = Tkinter.Label(top,text="Blue Mobs",bg='blue',fg='white').grid(row=8,column=0)
yellow_mob_label = Tkinter.Label(top,text="Yellow Mobs",bg='yellow').grid(row=9,column=0)
gob_mob_label = Tkinter.Label(top,text="Treasure Gobs",bg='brown').grid(row=10,column=0)
purp_mob_label = Tkinter.Label(top,text="Purple Mobs",bg='purple').grid(row=11,column=0)

##Legendary Label
lege_item_label = Tkinter.Label(top,text="Legendaries",bg="orange",fg="black").grid(row=12,column=0)

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
blue_subtract_button= Tkinter.Button(top,text="-",command=blue_subtract).grid(row=8,column=1)
blue_label = Tkinter.Entry(top,textvariable=blue_mob_var,width=3).grid(row=8,column=2)
blue_add_button= Tkinter.Button(top,text="+",command=blue_add).grid(row=8,column=3)

yellow_subtract_button= Tkinter.Button(top,text="-",command=yellow_subtract).grid(row=9,column=1)
yellow_label = Tkinter.Entry(top,textvariable=yellow_mob_var,width=3).grid(row=9,column=2)
yellow_add_button= Tkinter.Button(top,text="+",command=yellow_add).grid(row=9,column=3)

gob_subtract_button= Tkinter.Button(top,text="-",command=gob_subtract).grid(row=10,column=1)
gob_label = Tkinter.Entry(top,textvariable=gob_mob_var,width=3).grid(row=10,column=2)
gob_add_button= Tkinter.Button(top,text="+",command=gob_add).grid(row=10,column=3)

purp_subtract_button= Tkinter.Button(top,text="-",command=purp_subtract).grid(row=11,column=1)
purp_label = Tkinter.Entry(top,textvariable=purp_mob_var,width=3).grid(row=11,column=2)
purp_add_button= Tkinter.Button(top,text="+",command=purp_add).grid(row=11,column=3)

lege_subtract_button= Tkinter.Button(top,text="-",command=lege_subtract).grid(row=12,column=1)
lege_label = Tkinter.Entry(top,textvariable=lege_mob_var,width=3).grid(row=12,column=2)
lege_add_button= Tkinter.Button(top,text="+",command=lege_add).grid(row=12,column=3)

## Difficulty Menu
#difficulty_dropdown = Tkinter.OptionMenu(top,difficulty_var,DIFFICULTY).grid(row=13,column=0)
difficulty_dropdown = apply(Tkinter.OptionMenu,(top,difficulty_var) + tuple(DIFFICULTY)).grid(row=13,column=0)

#difficulty_mb = Menubutton(top,text="Difficulty",relief=RAISED)
#difficulty_mb.grid(row=13,column=0)
#difficulty_mb.grid()
#difficulty_mb.menu = Menu(difficulty_mb,tearoff=0)
#difficulty_mb["menu"] = difficulty_mb.menu
#diff_var_t1 = IntVar()
#difficulty_mb.menu.add_checkbutton(label="Torment 1",variable=diff_var_t1)
#difficulty_mb.pack()

# the constructor syntax is:
# OptionMenu(master, variable, *values)

#variable = StringVar(top)
#variable.set(OPTIONS[0]) # default value
#difficulty = apply(Tkinter.OptionMenu, (top, variable) + tuple(OPTIONS)).grid(row=14,column=2)
#w.pack()


####
# Mainloop
###
top.mainloop()

