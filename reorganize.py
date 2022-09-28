import os
import shutil
import time
#base directory and machine forler for my trials
# base_dir="C:\\Users\\coman\\Documents\\GitHub\\Python_script_projects\\Folderprojec"
# machinedir ="machine make 2"
base_dir=input("Please paste the working directory with double slash format: ")
machinedir=input("Please paste the machine directory you want to extract: ")
 
print(base_dir)
print(machinedir)

time.sleep(15)
slash='\\'
parent=[]
for folder , sub_folders , files in os.walk(machinedir):
    print("Currently looking at folder: "+ folder)
    time.sleep(15)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    time.sleep(15)
    if slash in folder:
        for sub_fold in sub_folders:
            print("\t Subfolder: "+sub_fold )
            #print("Two levels down in:"+str(sub_fold)+"-")
            for parents in parent:
                # creating directories in parent in new format
                directories=folder.split(slash)
                #checking if we are in the right folder to create
                if directories[0] in parents and directories[1] in parents:                
                    os.chdir(base_dir+slash+parents)
                    #print('changed inside directory')
                    #os.getcwd()
                    os.mkdir("T-"+sub_fold)
                    lastcreateddir=os.getcwd()+slash+"T-"+sub_fold
                    #print (lastcreateddir)
                    #print('created new inside directory t-')
                    os.chdir(base_dir)
                    #print('changed outside directory')
                    #os.getcwd()
                    #print('\n')
                else:
                    pass
    else:
        for sub_fold in sub_folders:
            print("\t Subfolder: "+sub_fold )
            # creating parent in new format
            #print("One level down in : "+str(sub_fold)+"-"+str(folder))
            os.mkdir("TO-"+sub_fold+"-"+str(folder))
            parent.append("TO-"+sub_fold+"-"+str(folder))
        print('\n')
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
        shutil.move(folder+slash+f,lastcreateddir)
        #shutil.move(f,lastcreateddir)
    print('\n')
print("Files moved!")
time.sleep(15)