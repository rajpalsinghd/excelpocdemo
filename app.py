from flask import Flask,render_template,request
from xlrd import open_workbook, XLRDError
import os
from flask_pymongo import PyMongo,pymongo
from pymongo import MongoClient
from helper_functions.h1 import validate_excel_sheet,read_excel_file
import logging
import logs.log_initializer

app=Flask(__name__)
app.config.from_object("config.Config")
mongo = PyMongo(app)
db = mongo.db
col = mongo.db["excelinfo"]




@app.route("/api/<int:page_number>")
def pagination(page_number):
 if page_number<0:return "Invalid page number"
 offset=page_number*5
 try:
  x=col.find().skip(offset).limit(5)
  data_to_show=[]
  for i in x:
   data_to_show.append(i['1'])
  page={}
  if page_number==0:page['prev']=[False,'']
  else:page['prev']=[True,f'/api/{page_number-1}']
  page['next']=[True,f'/api/{page_number+1}']
  page['number_info']=[[page_number,"active",f'/api/{page_number}'],[page_number+1,"",f'/api/{page_number+1}'],[page_number+2,"",f'/api/{page_number+2}']]
  return render_template("pagination.html",data=data_to_show,page=page);
 except Exception as e:
  print(e)

@app.route('/api')
def main_endpoint():
 return render_template("fileuploader.html") 

@app.route('/api/datafile',methods=['POST'])
def save_file_to_db():
 if request.method == 'POST':  
   try:
    f = request.files['file']
    if f.filename=="":return render_template("error.html")
    t=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
    f.save(t)
    is_excel=validate_excel_sheet(t)
    if(is_excel):
     read_excel_file(t,col)
     return render_template("success.html",filename=f.filename)
    else:
     os.remove(t)
     return render_template("error.html")  
   except Exception as e:
     #add logs
     return render_template("error.html")




app.run()