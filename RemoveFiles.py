import os
import shutil
import time

path = input("Enter the path of the files you want to delete. ")
days = 30

if os.path.exists(path):
  os.walk(path)
  os.path.join(path)
  ctime = os.stat(path).st_ctime
  list_of_files = os.listdir(path)

  for file in list_of_files:
    fileCtime = os.stat(path + '/' + file).st_ctime
    daysSinceFileOrFolderMade = (time.time() - fileCtime)//86400

    if daysSinceFileOrFolderMade <= days:
      if os.path.isdir(path + '/' + file):
        shutil.rmtree(path + '/' + file)
      
      elif os.path.isfile(path + '/' + file):
        os.remove(path + '/' + file)

    else:
      continue

else:
  print("Path not found.")