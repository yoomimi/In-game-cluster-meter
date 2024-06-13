import warnings
warnings.filterwarnings('ignore')
import os, time
import numpy as np
import pyautogui
from pynput import keyboard
from pynput import mouse
import cv2
import mss
import mss.tools


def iswindowexist(winname): # 프로세스 이름을 알아야 함
    for win in pyautogui.getAllWindows():
        if win.title == winname:
            return True
        
    return False

def mylogging(videofn, fps):
    datalist = []
    # checkprogramname = 'League of Legends (TM) Client'
    checkprogramname = 'a.txt - Windows 메모장' # 실행되는 프로그램 이름을 정확히 알아야 함
    # checkprogramname = '오버워치'
    # checkprogramname = 'VALORANT  '

    check = iswindowexist(checkprogramname)
    if check == True:
        with mouse.Listener() as mlistener, \
            keyboard.Listener() as klistener, mss.mss() as sct:
                nt = time.time_ns()
                print('logging start')
                myimg = pyautogui.screenshot()
                myimg = cv2.cvtColor(np.array(myimg), cv2.COLOR_RGB2BGR)
                height, width, channels = myimg.shape
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(videofn, fourcc, fps, (width, height))
                region = {'top': 0, 'left': 0, 'width': width, 'height': height}
                check = True

                while(check):
                    img = sct.grab(region)
                    myimage = cv2.cvtColor(np.array(img), cv2.COLOR_BGRA2BGR)
                    out.write(myimage)
                    check = iswindowexist(checkprogramname)
                out.release()
                cv2.destroyAllWindows()
                return  datalist
    return []


def makefilepath(username):
    # 파일 경로 지정, 없다면 폴더 생성
    if os.path.exists(username) == False:
        os.makedirs(username)

    filepath = f'./{username}/'
    filelist = os.listdir(filepath)
    if filelist == []:
        return f'{filepath}{username}_1'
    
    else:
        filelist = [int(x.split('_')[1].split('.')[0]) for x in filelist]
        filelist.sort()
        newfilenum = filelist[-1] + 1
        savefilepath = f'{filepath}{username}_{newfilenum}' 
        return savefilepath

nt = time.time_ns()

username = input('영상이 저장될 폴더 명을 입력해주세요(해당하는 폴더가 없다면 새로 생성됩니다): ')

while(True):
    savefilename = makefilepath(username)
    videofilename = savefilename + ".avi"
    logdatalist = mylogging(videofn = videofilename, fps= 15.0) # 저장 프레임. 메모장은 30일 때 2배속, 롤은 15일 때 2배속 30일 때 4배속 -> 게임 자체 fps 설정 때문인듯
    #if logdatalist != []:
    #    savedata(logfn= logfilename, logdatalist= logdatalist)
        # time.sleep(120)
    # else:
        # time.sleep(1)