# Django Classification App
This application works on **Python 3+** \
Install dependencies:
```
pip install -r requirements.txt
```
Prepare database:
```
python manage.py makemigrations
python manage.py migrate
```
create superuser for database:
```
python manage.py createsuperuser
```
Run server locally:
```
python manage.py runserver
```

---
clear DB - if you want empty database. \
You also ave to delete files from data_models directory.
```
python manage.py flush
```
---

## After initial commands, You can start using this application.
In the nav bar, go to Import CSV. \
Choose name of Your dataset, and Machine Learning algorithm. \
It is very important that the csv file structure looks like this: \
class, attribute1, attribute2, attribute3, [...] attribute9. \
Minumum ammount of attributes is 2 and maximum 9. \
Then You have to upload .csv file from Your computer and click Import. \
Wait for the browser to stop loading and then click Next. \
(In the data_models should appear Your model.) \
From the drop list choose Your dataset and click Submit. 
