If a user wants to store a excel file for analytical purpose in database this application can be used. Here using a web interface user has to upload
the excel file. After successful upload the file will be stored in mongodb, file will be readed in chunks and to remove network overhead batch operation
is applied so for every transaction we don't have to fire a query.
