from django.db import models



# Create your models here.(database)

class Employee(models.Model):
    email=models.EmailField(null=True)
    uname=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)

    def __str__(self):
        return self.uname  
    
class Emp(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    salary=models.PositiveIntegerField()
    contact=models.CharField(max_length=30)







class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=30)
    publicationyear=models.PositiveIntegerField()
    genre=models.CharField(max_length=20) 

    



    


class Books(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=30)
    genre=models.CharField(max_length=20) 


    def __str__(self):
        return self.title
    
    


class Students(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    gender=models.CharField(max_length=10)



    def __str__(self,name,place):
        self.name=name
        self.place=place
        return(self.name,self.place,)
        
    
class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=30)
    publicationyear=models.PositiveIntegerField()
    genre=models.CharField(max_length=20)

      



#python manage.py runserver
#python manage.py startapp appname
#python manage.py makemigrations
#python manage.py migrate
#python manage.py shell
#s=modelname.objects.all()

 
#django default db sqlite3
#models: which is used to perform certain actions using data eg: CRUD(create,read/retrive,update,delete)




class student(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=30)
    

