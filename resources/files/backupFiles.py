import shutil
from datetime import date
import datetime

# SOURCE: https://www.youtube.com/watch?v=uU_iuYv53-U - View the github in the description
def backupFile(src_file_name, dst_file_name=None, src_dir='', dst_dir=''):

    today = date.today()
    date_format = today.strftime("%d_%b_%Y")

    src_dir = src_dir + src_file_name

    if dst_file_name is None or not dst_file_name:
        dst_file_name = src_file_name
        dst_file_name = dst_dir+date_format+dst_file_name
    #elif block will work when user Enter an empty string with one or more spaces (' ')
    elif dst_file_name.isspace():
        dst_file_name = src_file_name
        dst_file_name = dst_dir+date_format+dst_file_name
    #else block will work when user Enter an a name for the backup copy.
    else:
        dst_file_name = dst_dir+date_format+dst_file_name

    shutil.copy(src_dir, dst_file_name)

    print("Backup Successful")

def backupAllFiles():
    fileLoc = "automatic-backups/" # Where to place the files

    pyFiles = ["StartWindow.py", "StatsWindow.py", "PerksWindow.py"]
    uiFiles = ["StartWindow.ui", "StatsWindow.ui", "PerksWindow.ui"]


    for file in pyFiles:
        backupFile(file, '', '', fileLoc)

    for file in uiFiles:
        backupFile(file, '', '', fileLoc)


