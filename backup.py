import shutil
import datetime
import os

def backup_files(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination,f"backup_{today}") # formated string
    shutil.make_archive(backup_file_name,'gztar', source)

source = "D:/Git Demo/Python_for_deveops" # source path 
destination = "D:/Git Demo/Python_for_deveops/backup"  # destination path
backup_files(source,destination)

 