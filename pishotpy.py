import easygui as eg
import os
from subprocess import Popen
import webbrowser
import sys

while(1):
    flag=1
    picker = eg.buttonbox(msg="Please select an option",title='PiShotPy', choices = ['Quick Screen Shot', 'Screen Shot with delay', 'About this App','Exit'] )
    cwd = os.getcwd()
    if((picker==None) or (picker=='Exit')):
        quit()
        sys.exit()
        
    fn=eg.enterbox(msg="Enter file name with extension .jpg or .png: ",title='PiShotPy')
    if((('.jpg') or ('.png')) in fn ):
        flag=0
    if(flag==1):
        fn=fn+'.jpg'
#scrot -cd 10 example.jpg
    if(picker=='Quick Screen Shot'):
        os.system("scrot {}".format(fn))
        eg.msgbox (msg="Your Quick Screen Shot has been saved in {}/".format(cwd),title='PiShotPy')
    
    elif(picker=='Screen Shot with delay'):
        req=eg.buttonbox(msg="Select your requirement",title='PiShotPy', choices = ['Custom delay times','Built-in delay times'] )
        if(req=='Custom delay times'):
            sec=eg.enterbox(msg="Enter delay time (in seconds): ",title='PiShotPy')
        #use sec to inject
            eg.msgbox (msg="Screen Shot will be taken in {} seconds".format(sec),title='PiShotPy')
            os.system("scrot -cd {} {}".format(sec,fn))
            eg.msgbox (msg="Your Quick Screen Shot has been saved in {}/".format(cwd),title='PiShotPy')
        
        if(req=='Built-in delay times'):
            bsec=eg.buttonbox(msg="Select your requirement",title='PiShotPy', choices = ['5 sec','10 sec','20 sec'] )
            if(bsec=='5 sec'):
            #ss in 5 sec
            
            #scrot -cd 10
                eg.msgbox (msg="Screen Shot will be taken in 5 seconds",title='PiShotPy')
                os.system("scrot -cd 5 {}".format(fn))
                eg.msgbox (msg="Your Quick Screen Shot has been saved in {}/".format(cwd),title='PiShotPy')
            
            elif(bsec=='10 sec'):
            
            #ss in 10 sec
                eg.msgbox (msg="Screen Shot will be taken in 10 seconds",title='PiShotPy')
                os.system("scrot -cd 10 {}".format(fn))
                eg.msgbox (msg="Your Quick Screen Shot has been saved in {}/".format(cwd),title='PiShotPy')
            
            elif(bsec=='20 sec'):
            #ss in 20 sec
            
                eg.msgbox (msg="Screen Shot will be taken in 20 seconds",title='PiShotPy')
                os.system("scrot -cd 20 {}".format(fn))
                eg.msgbox (msg="Your Quick Screen Shot has been saved in {}/".format(cwd),title='PiShotPy')
            
    elif(picker=='About this App'):
        webbrowser.open("About_PiShotPy.txt")
    elif(picker=='Exit'):
        quit()
        sys.exit()
        
    elif(picker==None):
        quit()
        sys.exit()
        
#scrot '%Y-%m-%d_$wx$h_scrot.png' -e 'mv $f ~/home/pi/images/'


