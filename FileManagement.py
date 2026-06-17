# Importing libraries
import os # Importing os is mandatory so that we can get access of file paths directly
import shutil # Importing is necessary to move file from source path to destination path 




# Creating variables for folders to perform actions on it 
source_folder='Source'
destination_folder='Destination'




# Iterating over each file to check .jpg files exist in folder or not 
for file in os.listdir(source_folder):
    # If .jpg present , move it to destination folder
    if file.endswith(".jpg"):
        source_path=os.path.join(source_folder,file)
        destination_path=os.path.join(destination_folder,file)
        shutil.move(source_path,destination_path)
        print("✅ Work Done . 👍")
    else:
        print("No .jpg file found .")



# # Functions of os used -->
# 1.listdir -->List out directories
# 2.path.join -->Provides path of file

# # Functions of shutil ised 
# 1.move--> Moves one path file to another path