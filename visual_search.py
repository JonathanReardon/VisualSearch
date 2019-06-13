from psychopy import visual, core, gui, event, sound
from psychopy.data import getDateStr
import os
import glob
import csv

# Set window and mouse

win = visual.Window([1000,800],color=(1,1,1), colorSpace='rgb', allowGUI=True, monitor='testMonitor', units='deg', fullscr=False)

myMouse = event.Mouse(visible=True,win=win)

# Practice Circles

circles_on = 1

practice_circle = visual.Circle(win, units='deg', radius=1, pos=(8.5,-5.1),lineColor="red", opacity=circles_on)

# vis search correct detection areas (to display ticks)

circle1 = visual.Circle(win, units='deg', radius=1, pos=(4.5,-6), lineColor="red")
circle2 = visual.Circle(win, units='deg', radius=1, pos=(9,-.8), lineColor="red")
circle3 = visual.Circle(win, units='deg', radius=1, pos=(-11.1,0), lineColor="red")
circle4 = visual.Circle(win, units='deg', radius=1, pos=(9.2,-8.2), lineColor="red")

# Set clock and other variables

clock = core.Clock()
rt_clock = core.Clock()
default_time=.5
blank_time=.5
shape_rad = 1
refresh_rate = 60.0
fix = 3
blank = 2

fix_time = fix * refresh_rate
fix_time = int(fix_time)

blank_screen = blank * refresh_rate
blank_screen = int(blank_screen)

stim_size = (2560/2.7,1556/2.7)
prac_stim_size = (2560/100,1556/100)

rt = []
correct = 0

practice_gate = 0

gate1 = 0
gate2 = 0
gate3 = 0
gate4 = 0
gate5 = 0

# -------------------------- Import stim directories ---------------------------- 

Practice                 = glob.glob(os.path.join('/home/jon/matt/practice','*.jpg'))

vis_search               = glob.glob(os.path.join('/home/jon/matt/vis_search','*.jpg')) 

# ------------------------ Make image objects --------------------------------------

visual_search          = [visual.ImageStim(win, img, name='detection_image' + img, units='pix', size=(stim_size)) for img in vis_search[:]]

practice      = [visual.ImageStim(win, img, name='prac_1' + img, units='deg', size=(prac_stim_size))     for img in Practice[:]] 
 
prac1         = practice[0]

# Set stim order (because they were not appearing in the order that they appear in the directory

youtube_one = visual_search[2]
all_four_one = visual_search[1]
youtube_two = visual_search[3]
all_four_two = visual_search[0]

visual_search_set = [all_four_two, all_four_one, youtube_one, youtube_two] # list of learning images

#instructions = visual.TextStim(win, text="This task is all about speed!\n The aim of the game is to find the blue X embedded within each image as quickly as possible. Once you've found it, click on the X to stop the clock. There wlil be a series of 4 images; two will be from All4 and two will be from YouTube.\n\n            PRESS SPACEBAR TO START ", color="black", units="deg", antialias=True,alignHoriz='center',alignVert='center',height = 0.6)
instructions = visual.TextStim(win, text="PRESS SPACEBAR TO START ", color="black", units="deg", antialias=True,alignHoriz='center', alignVert='center', height = 2)
#practice_instruction = visual.TextStim(win, text="Here's a practice run of the visual task. Remember, you need to find the embedded blue X as quickly as you can. Don't forget to click on the X once you have found it, as this wlil end the trial.\n\n            PRESS SPACEBAR TO CONTINUE", color="black", units="deg", antialias=True,alignHoriz='center',alignVert='center',height = 0.6)
practice_instruction = visual.TextStim(win, text="PRESS SPACEBAR TO CONTINUE", color="black", units="deg", antialias=True, alignHoriz='center', alignVert='center', height = 2)
ready = visual.TextStim(win, text="Ready to begin?\n\nPRESS SPACEBAR TO START", color="black", units="deg", antialias=True,alignHoriz='center',alignVert='center',height = 0.6)
ITI_message = visual.TextStim(win, text="PRESS SPACEBAR FOR THE NEXT TRIAL", color="black", units="deg", antialias=True,alignHoriz='center',alignVert='center',height = 0.6)

def intro_screen():
    instructions.draw()
    win.flip()
    event.waitKeys()
    
def ready_screen():
    ready.draw()
    win.flip()
    event.waitKeys()
    
def practice_screen():
    practice_instruction.draw()
    win.flip()
    event.waitKeys()
    
def inter_trial_interval():
    ITI_message.draw()
    print("in interval")
    win.flip()
    event.waitKeys()
        
user_circle = visual.Circle(win, units = 'deg', pos=(0,0), radius=shape_rad, lineColor="red")

rt_list = []
rt_list1 = []
rt_list2 = []
rt_list3 = []
rt_list4 = []

counter_practice = 0

# -------------------- PRACTICE TRIAL --------------------

end_practice = 1
displaycircle1 = 0

#intro_screen()

while end_practice==1:
        
    detection=1
    while detection==1:
                
        prac1.draw()
        practice_circle.draw()
                
        user_circle.setPos(myMouse.getPos())
        user_circle.draw()
                
        mouse_loc = myMouse.getPos()
        buttons = myMouse.getPressed(getTime=True)
        
        if  practice_circle.contains(myMouse.getPos()):
            if any(myMouse.getPressed()):
                if practice_gate == 0:
                    counter_practice += 1
                    practice_gate1 = 1
                    detection = 0
                    end_practice = 0
        else:
            pass
                
        allKeys = event.getKeys(keyList = ('escape','space'))
        for thisKey in allKeys:
            if thisKey == 'space':
                end_practice= 0
                detection=0
                
            if thisKey == 'escape':
                win.close()
                core.quit()
            

        win.flip()
    
#ready_screen()
        
#-----------------------------------------------------------#
#-----------------------------------------------------------#
# -------------------- BEGIN EXPERIMENT --------------------#
#_----------------------------------------------------------#
#-----------------------------------------------------------#

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0

running = 0
detection = 0
while running==0:
    
    rt_clock.reset()
    while detection==0:
        
        visual_search_set[0].draw()
        circle1.draw()
                    
        user_circle.setPos(myMouse.getPos())
        user_circle.draw()
                    
        mouse_loc = myMouse.getPos()
        buttons = myMouse.getPressed(getTime=True)
            
        if  circle1.contains(myMouse.getPos()):
            if any(myMouse.getPressed()):
                if gate1 == 0:
                    counter1 += 1
                    gate1 = 1
                    detection = 0
                    running = 0
        else:
            pass
                    
        allKeys = event.getKeys(keyList = ('escape','space'))
        for thisKey in allKeys:
            if thisKey == 'space':
                rt_list1.append(rt_clock.getTime())
                detection = 1
                running = 0
            if thisKey == 'escape':
                win.close()
                core.quit()
                
        if counter1 ==1:
            rt_list1.append(rt_clock.getTime())
            detection = 1
                

    win.flip()
    #inter_trial_interval()
        
    visual_search_set.pop(0)
    
    # ------------------------------------ image 2 ------------------------------------
    
    detection = 0
    rt_clock.reset()
    while detection ==0:
        
        visual_search_set[0].draw()
        circle2.draw()
                    
        user_circle.setPos(myMouse.getPos())
        user_circle.draw()
                    
        mouse_loc = myMouse.getPos()
        buttons = myMouse.getPressed(getTime=True)
            
        if  circle2.contains(myMouse.getPos()):
            if any(myMouse.getPressed()):
                if gate2 == 0:
                    counter2 += 1
                    gate2 = 1
                    detection = 0
                    running = 0
        else:
            pass
                    
        allKeys = event.getKeys(keyList = ('escape','space'))
        for thisKey in allKeys:
            if thisKey == 'space':
                rt_list2.append(rt_clock.getTime())
                detection = 1
                running = 0
            if thisKey == 'escape':
                win.close()
                core.quit()
                
        if counter2 ==1:
            rt_list2.append(rt_clock.getTime())
            detection = 1
                

        win.flip()
        
    #inter_trial_interval()
        
    visual_search_set.pop(0)
    # ------------------------------------ image 3 ------------------------------------
    
    detection = 0
    rt_clock.reset()
    while detection ==0:
        
        visual_search_set[0].draw()
        circle3.draw()
                    
        user_circle.setPos(myMouse.getPos())
        user_circle.draw()
                    
        mouse_loc = myMouse.getPos()
        buttons = myMouse.getPressed(getTime=True)
            
        if  circle3.contains(myMouse.getPos()):
            if any(myMouse.getPressed()):
                if gate3 == 0:
                    counter3 += 1
                    gate3 = 1
                    detection = 0
                    running = 0
        else:
            pass
                    
        allKeys = event.getKeys(keyList = ('escape','space'))
        for thisKey in allKeys:
            if thisKey == 'space':
                rt_list3.append(rt_clock.getTime())
                detection = 1
                running = 0
            if thisKey == 'escape':
                win.close()
                core.quit()
                
        if counter3 ==1:
            rt_list3.append(rt_clock.getTime())
            detection = 1

        win.flip()
        
    clock.reset()
    #inter_trial_interval()
        
    visual_search_set.pop(0)
    # ------------------------------------ image 4 ------------------------------------
    
    detection = 0
    rt_clock.reset()
    while detection ==0:
        
        visual_search_set[0].draw()
        circle4.draw()
                    
        user_circle.setPos(myMouse.getPos())
        user_circle.draw()
                    
        mouse_loc = myMouse.getPos()
        buttons= myMouse.getPressed(getTime=True)
            
        if  circle4.contains(myMouse.getPos()):
            if any(myMouse.getPressed()):
                if gate4 == 0:
                    counter4 += 1
                    gate4 = 1
                    detection = 0
                    running = 0
        else:
            pass
                    
        allKeys = event.getKeys(keyList = ('escape','space'))
        for thisKey in allKeys:
            if thisKey == 'space':
                rt_list4.append(rt_clock.getTime())
                detection = 1
                running = 0
            if thisKey == 'escape':
                win.close()
                core.quit()
                
        if counter4 ==1:
            rt_list4.append(rt_clock.getTime())
            detection = 1

        win.flip()
    
        
    running = 1
    
myText = "Image  TIME"
    
print(rt_list1)
print(rt_list2)
print(rt_list3)
print(rt_list4)

avg_youtube = []
avg_youtube.append(rt_list4[0])
avg_youtube.append(rt_list3[0])
avg_youtube = sum(avg_youtube) / len(avg_youtube)
avg_youtube = str(round(avg_youtube, 2))
print(avg_youtube)

avg_allfour = []
avg_allfour.append(rt_list2[0])
avg_allfour.append(rt_list1[0])
avg_allfour = sum(avg_allfour) / len(avg_allfour)
avg_allfour = str(round(avg_allfour, 2))
print(avg_allfour)

rt_list1 = str(round(rt_list1[0], 2))
rt_list2 = str(round(rt_list2[0], 2))
rt_list3 = str(round(rt_list3[0], 2))
rt_list4 = str(round(rt_list4[0], 2))

Results_title = visual.TextStim(win, text=myText, color="red", pos=(0,6.5),antialias=True,wrapWidth=None)
rt_list1         = visual.TextStim(win,   text="3:       " + rt_list1, color="black",   pos=(0,.5),    antialias=True)
rt_list4      = visual.TextStim(win, text="2:       " + rt_list4, color="black", pos=(0,3.5),    antialias=True)
average_youtube = visual.TextStim(win, text="Avg YouTube: " + avg_youtube, color="green", pos=(0,2),antialias=True,wrapWidth=None)

rt_list2 = visual.TextStim(win,   text="4:       " + rt_list2, color="black",   pos=(0,-1),  antialias=True)
rt_list3 = visual.TextStim(win,  text="1:       " + rt_list3, color="black",  pos=(0,5),  antialias=True)
average_allfour = visual.TextStim(win, text="Avg AllFour: " + avg_allfour, color="green", pos=(0,-2.5),antialias=True,wrapWidth=None)

results_screen = 1

while results_screen:
    
    Results_title.draw()
    win.flip()
    core.wait(1)
    
    Results_title.draw()
    rt_list1.draw()
    win.flip()
    core.wait(1)
    
    Results_title.draw()
    rt_list1.draw()
    rt_list4.draw()
    win.flip()
    core.wait(1)
    
    Results_title.draw()
    rt_list1.draw()
    rt_list4.draw()
    average_youtube.draw()
    win.flip()
    core.wait(1)
    
    Results_title.draw()
    rt_list1.draw()
    rt_list4.draw()
    average_youtube.draw()
    rt_list2.draw()
    win.flip()
    core.wait(1)
    
    Results_title.draw()
    rt_list1.draw()
    rt_list4.draw()
    average_youtube.draw()
    rt_list2.draw()
    rt_list3.draw()
    win.flip()
    core.wait(1)
    
    Results_title.draw()
    rt_list1.draw()
    rt_list4.draw()
    average_youtube.draw()
    rt_list2.draw()
    rt_list3.draw()
    average_allfour.draw()
    win.flip()
    core.wait(1)
    
    wait_results = 1
    while wait_results == 1:
        Results_title.draw()
        average_youtube.draw()
        average_allfour.draw()
        rt_list1.draw()
        rt_list2.draw()
        rt_list3.draw()
        rt_list4.draw()
    
        allKeys = event.getKeys(keyList = ('escape','space'))
        for thisKey in allKeys:
            if thisKey == 'escape' or thisKey == 'space':
                wait_results = 0
                win.close()
                core.quit()
                
        win.flip()
        
win.close()
core.quit()