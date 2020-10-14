import os
import pathlib

class Config(object):
 MONGO_URI="mongodb+srv://raj:rajpal123@cluster0.zc6zm.mongodb.net/johndeere?retryWrites=true&w=majority"
 MONGO_DBNAME= 'johndeere'
 SECRET_KEY= 'secret_key'
 root_folder=os.path.dirname(os.path.abspath('app.py'))
 upload_folder=root_folder+pathlib.os.sep+"users_excel_file"
 UPLOAD_FOLDER=upload_folder
