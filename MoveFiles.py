import os
import shutil

from_dir = input("Enter The Directory Path To Copy Files From >> ")
to_dir = input("Enter The Directory Path To Copy Files To >> ")

list_of_files = os.listdir(from_dir)

print(list_of_files)

for file in list_of_files:
    fileName, extension = os.path.splitext(file)

    if extension == '':
        continue
    elif extension in [".txt", ".png", ".jpeg", ".gif", ".exe", ".zip"]:
        if (os.path.exists(to_dir)):
            path1 = from_dir + "/" + file
            path2 = to_dir
            path3 = to_dir + "/" + file
            print("Moving Files... [" + file + "]")
            shutil.copy(path1, path2)
        else:
            print("Error: Destination Path Does Not Exists. Creating New Folder With Same Name...")
            os.makedirs(to_dir)
            path1 = from_dir + "/" + file
            path2 = to_dir
            path3 = to_dir + "/" + file
            print("Moving Files... [" + file + "]")
            shutil.copy(path1, path2)
print("\n Operation Completed")