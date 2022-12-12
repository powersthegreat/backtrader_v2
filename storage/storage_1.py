# import os

# # printing current directory
# print(os.getcwd())

# # changing to new directory
# os.chdir('/Users/Owner/Desktop/backtrader_v2/preformance/results/csvs')
# print(os.getcwd())

# # gives list of all files in current directory
# print(os.listdir())

# # renaming files in a directory example
# for file in os.listdir():
#     if file == ".DS_Store":
#         continue
#     # getting file name and extension
#     name, ext = os.path.splitext(file)
#     # renaming file
#     new_name = "test"
#     os.rename(file, new_name)

# # creating a directory
# from pathlib import Path
# os.chdir('/Users/patrick/Desktop/video-files')
# if not os.path.exists("folder"):
#     os.mkdir("folder")

# # moving a file
# import shutil
# shutil.move(file, "folder")

# # copying files
# import shutil
# shutil.copy(file, "folder")
# # or
# shutil.copy2(file, "folder")

# # removing a file
# os.remove("filename")
# # os.rmdir("folder") # only if empty
# # if not empty use
# os.rmtree("folder")

# --------------------------------------------

import os
import shutil

class Storage:
    def move(self):
        os.chdir('/Users/Owner/Desktop/backtrader_v2/preformance/results/csvs')
        folder_name = None
        for file in os.listdir():
            name, ext = os.path.splitext(file)
            folder_name = name

        os.chdir('/Users/Owner/Desktop/backtrader_storage')
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        os.chdir('/Users/Owner/Desktop/backtrader_v2/preformance/results/csvs')
        for file in os.listdir():
            shutil.move(file, f'/Users/Owner/Desktop/backtrader_storage/{folder_name}')

        os.chdir('/Users/Owner/Desktop/backtrader_v2/preformance/plotting/plots')
        for file in os.listdir():
            shutil.move(file, f'/Users/Owner/Desktop/backtrader_storage/{folder_name}')

        os.chdir('/Users/Owner/Desktop/backtrader_v2/stradegies/plotting/plots')
        for file in os.listdir():
            shutil.move(file, f'/Users/Owner/Desktop/backtrader_storage/{folder_name}')





