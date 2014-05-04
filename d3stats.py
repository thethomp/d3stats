#!/usr/bin/python
from datetime import datetime
from Tkinter import *
import Tkinter, time, tkMessageBox

############
## master window creation and config
############
top = Tkinter.Tk()
top.title("GGD3Stats")

TIME_FRAME = Tkinter.Frame(top)
TIME_FRAME.grid(row=0,column=0)#, rowspan=3,columnspan=1)#,relief=SUNKEN)

XP_FRAME = Tkinter.Frame(top)
XP_FRAME.grid(row=0,column=1)

GOLD_FRAME = Tkinter.Frame(top)
GOLD_FRAME.grid(row=1,column=0)

MOBS_FRAME = Tkinter.Frame(top)
MOBS_FRAME.grid(row=2,column=0)

DROPDOWN_FRAME = Tkinter.Frame(top)
DROPDOWN_FRAME.grid(row=1,column=1)

#DD_FRAME = Tkinter.Frame(top)

# dropdown menu vars
DIFFICULTY = ['Normal','Hard','Expert','Master','Torment 1',
'Torment 2','Torment 3','Torment 4','Torment 5','Torment 6']
difficulty_var = StringVar(DROPDOWN_FRAME)
difficulty_var.set('Difficulty')

# Map dropdown vars
MAP = ['ACT I - New Tristram', 'ACT I - The Old Ruins']
map_var = StringVar(DROPDOWN_FRAME)
map_var.set('Map')

# Bounty drowpdown vars
BOUNTY = ["Kill the Skeleton King","Clear the Scavenger's Den"]
bounty_var = StringVar(DROPDOWN_FRAME)
bounty_var.set('Bounty')

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

def clear_time():
	start_time_var.set("")
	stop_time_var.set("")
	run_time_var.set("")

def find_xp_gain():
    if xp_before_var.get() != "" and xp_after_var.get() != "":
        xp_b = (int)(xp_before_var.get())
        xp_a = (int)(xp_after_var.get())
        change = abs(xp_a - xp_b)

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
start_time_label = Tkinter.Label(TIME_FRAME,text="Start Time").grid(row=0,column=2)
stop_time_label = Tkinter.Label(TIME_FRAME,text="Stop Time").grid(row=1,column=2)
total_time_label = Tkinter.Label(TIME_FRAME,text="Run Length").grid(row=2,column=2)

##XP Labels
xp_before_label = Tkinter.Label(XP_FRAME,text="XP Before",fg='red')
xp_before_label.grid(row=0,column=0)
xp_after_label = Tkinter.Label(XP_FRAME,text="XP After",fg='red')
xp_after_label.grid(row=1,column=0)

## MOB Labels
blue_mob_label = Tkinter.Label(MOBS_FRAME,text="Blue Mobs",bg='blue',fg='white').grid(row=0,column=0)
yellow_mob_label = Tkinter.Label(MOBS_FRAME,text="Yellow Mobs",bg='yellow').grid(row=1,column=0)
gob_mob_label = Tkinter.Label(MOBS_FRAME,text="Treasure Gobs",bg='brown').grid(row=2,column=0)
purp_mob_label = Tkinter.Label(MOBS_FRAME,text="Purple Mobs",bg='purple').grid(row=3,column=0)

##Legendary Label
lege_item_label = Tkinter.Label(MOBS_FRAME,text="Legendaries",bg="orange",fg="black").grid(row=4,column=0)

## Timestamp fields
start_timestamp = Tkinter.Label(TIME_FRAME,textvariable=start_time_var,width=10).grid(row=0,column=1)
stop_timestamp = Tkinter.Label(TIME_FRAME,textvariable=stop_time_var,width=10).grid(row=1,column=1)
total_timestamp = Tkinter.Label(TIME_FRAME,textvariable=run_time_var,width=10).grid(row=2,column=1)

##XP fields
xp_before_field1 = Tkinter.Entry(XP_FRAME,textvariable=xp_before_var,width=10)
xp_before_field1.grid(row=0,column=1)#,columnspan=2)
xp_before_field2 = Tkinter.Entry(XP_FRAME,width=10).grid(row=0,column=2)#,columnspan=2)
xp_level_field1 = Tkinter.Entry(XP_FRAME,width=3).grid(row=0,column=3)

xp_after_field1 = Tkinter.Entry(XP_FRAME,textvariable=xp_after_var,width=10)
xp_after_field1.grid(row=1,column=1)#,columnspan=2)
xp_after_field2 = Tkinter.Entry(XP_FRAME,width=10).grid(row=1,column=2)#,columnspan=2)
xp_level_field2 = Tkinter.Entry(XP_FRAME,width=3).grid(row=1,column=3)

## gold fields
start_gold_label = Tkinter.Label(GOLD_FRAME,text='Starting Gold',width=10).grid(row=6,column=0)
end_gold_label = Tkinter.Label(GOLD_FRAME,text='Ending Gold',width=10).grid(row=7,column=0)
start_gold_field = Tkinter.Entry(GOLD_FRAME,textvariable=gold_before_var,width=15).grid(row=6,column=1)
end_gold_field = Tkinter.Entry(GOLD_FRAME,textvariable=gold_after_var,width=15).grid(row=7,column=1)

## Paragon level check buttons
paragon_lvl_checkbox = Tkinter.Checkbutton(XP_FRAME,text="Paragon",variable=paragon_lvl_var).grid(row=0,column=4,rowspan=2)

## Timer Buttons
start_timer_button = Tkinter.Button(TIME_FRAME,text="Start",command=update_time).grid(row=0,column=0)
stop_timer_button = Tkinter.Button(TIME_FRAME,text="Stop",command=update_time).grid(row=1,column=0)
clear_timers_button = Tkinter.Button(TIME_FRAME,text="Clear",command=clear_time).grid(row=2,column=0)

## yellow mobs
blue_subtract_button= Tkinter.Button(MOBS_FRAME,text="-",command=blue_subtract).grid(row=0,column=1)
blue_label = Tkinter.Entry(MOBS_FRAME,textvariable=blue_mob_var,width=3).grid(row=0,column=2)
blue_add_button= Tkinter.Button(MOBS_FRAME,text="+",command=blue_add).grid(row=0,column=3)

yellow_subtract_button= Tkinter.Button(MOBS_FRAME,text="-",command=yellow_subtract).grid(row=1,column=1)
yellow_label = Tkinter.Entry(MOBS_FRAME,textvariable=yellow_mob_var,width=3).grid(row=1,column=2)
yellow_add_button= Tkinter.Button(MOBS_FRAME,text="+",command=yellow_add).grid(row=1,column=3)

gob_subtract_button= Tkinter.Button(MOBS_FRAME,text="-",command=gob_subtract).grid(row=2,column=1)
gob_label = Tkinter.Entry(MOBS_FRAME,textvariable=gob_mob_var,width=3).grid(row=2,column=2)
gob_add_button= Tkinter.Button(MOBS_FRAME,text="+",command=gob_add).grid(row=2,column=3)

purp_subtract_button= Tkinter.Button(MOBS_FRAME,text="-",command=purp_subtract).grid(row=3,column=1)
purp_label = Tkinter.Entry(MOBS_FRAME,textvariable=purp_mob_var,width=3).grid(row=3,column=2)
purp_add_button= Tkinter.Button(MOBS_FRAME,text="+",command=purp_add).grid(row=3,column=3)

lege_subtract_button= Tkinter.Button(MOBS_FRAME,text="-",command=lege_subtract).grid(row=4,column=1)
lege_label = Tkinter.Entry(MOBS_FRAME,textvariable=lege_mob_var,width=3).grid(row=4,column=2)
lege_add_button= Tkinter.Button(MOBS_FRAME,text="+",command=lege_add).grid(row=4,column=3)

## Difficulty Menu
difficulty_dropdown = Tkinter.OptionMenu(DROPDOWN_FRAME,difficulty_var,*DIFFICULTY).grid(row=0,column=0)

## Map dropdown
map_dropdown = Tkinter.OptionMenu(DROPDOWN_FRAME,map_var,*MAP).grid(row=0,column=1)

# Bounty dropdown
bounty_dropdown = Tkinter.OptionMenu(DROPDOWN_FRAME,bounty_var,*BOUNTY).grid(row=1,column=0,columnspan=2)

####
# Mainloop
###
top.mainloop()

