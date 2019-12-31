import pathlib
import dropbox
import re
import datetime
import os
def upload_to_dropbox(file_name,file_contents):
    # the source file

    filename = file_name+".txt".strip()  # file name

    f = open(filename,"w+")
    f.write(file_contents)
    f.close()

    # target location in Dropbox
    target = "/Apps/CY Teleprompter/"  # the target folder
    targetfile = target + filename  # the target path and file name

    # Create a dropbox object using an API v2 key
    API_KEY = "cG2kM3HuQMAAAAAAAAAANK93dG11lbL4Oh4IYgIQNMBzWjG6KrKoFoRNQskABtws"
    d = dropbox.Dropbox(API_KEY)

    # upload gives you metadata about the file
    # we want to overwite any previous version of the file
    f = open(filename,"rb")
    meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
    f.close()
    os.remove(filename) #remove the file
    print(meta)
    return filename
