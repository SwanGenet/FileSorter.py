import os
import shutil

cwd = os.getcwd() #Current Working Directory
ls = os.listdir(cwd) #List of files in cwd
    
directory = ['img','video','txt','pdf','audio'] #Different dir to create
parent_dir = os.getcwd() 
mode = 0o666   

i = 0
while i < len(directory):
    if directory[i] not in ls:
        path = os.path.join(parent_dir, directory[i]) 
        os.makedirs(path, mode) #Creation of the dir
    i += 1

img_ext = ('png','jpg','svg','jpeg','gif','tiff','psd','eps','ai','indd','raw')
txt_ext = ('txt','docx','doc','odt')
video_ext = ('avi','mkv','mp4','mov','flv','wvm','webm')
audio_ext = ('mp3','flac','wav','aac','m4v','wma')

i = 0
while i < len(ls):
    if ls[i].lower().endswith(img_ext):
        shutil.move(ls[i], os.getcwd()+'/img') #Move files to /img

    elif ls[i].endswith(txt_ext):
        shutil.move(ls[i], os.getcwd()+'/txt') #Move files to /txt

    elif ls[i].endswith('.pdf'):
        shutil.move(ls[i], os.getcwd()+'/pdf') #Move files to /pdf

    elif ls[i].endswith(audio_ext):
        shutil.move(ls[i], os.getcwd()+'/audio') #Move files to /audio

    elif ls[i].endswith(video_ext):
        shutil.move(ls[i], os.getcwd()+'/video') #Move files to /vid
    i += 1
 
