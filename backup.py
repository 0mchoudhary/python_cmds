import os
import shutil

def backup(source_path,destination_path):

    backup_name=os.path.join(destination_path,"backup1")
    shutil.make_archive(backup_name,"gztar",source_path)


source = "/Users/omchoudhary/Learning/DevOps"
destination = "/Users/omchoudhary/Learning"

backup(source,destination)