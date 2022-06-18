import fileinput
from django.db import models
from django.forms import FilePathField
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Person(models.Model):
     SUBJECT_CHOICES = (
        (1, 'Mr'),
        (2, 'Mrs'),
        (3, 'Miss'),
        (4, 'Other'),
    )
   
     title = models.IntegerField('Title', choices=SUBJECT_CHOICES,null=True)
     first_name = models.CharField('First Name', max_length=50,null=True )
     surname = models.CharField('Surname', max_length=70,null=True )
     date_of_birth = models.DateField('Date of Birth',null=True )
     nationality = models.CharField('Nationality', max_length=50,null=True )
     national_id_number = models.CharField('National ID Number', max_length=40, null=True )
     country_of_birth = models.CharField('Country Of Birth', max_length=80, null=True )
     CHOICES = [('M','Male'),('F','Female')]
     Gender=models.CharField('Gender', max_length=20, choices=CHOICES,null=True)
     passport_photo = models.ImageField('Passport Photo', default="profile1.png",blank=True ,null=True )
     

     def __str__(self):
        return self.first_name + '' + self.surname

class Contact(models.Model):
   ZIMBABWE_RESIDENT = [('no','No'),('Y','Yes')]
   person = models.OneToOneField(Person, null=True, blank=True, on_delete=models.CASCADE)
   phone = models.CharField(max_length=200, null=True)
   email = models.CharField(max_length=200, null=True)
   house_number = models.CharField('House Number', max_length=70,null=True)
   mobile_number = models.CharField('Mobile Number', max_length=70,null=True )
   city = models.CharField('Town/City Of Birth', max_length=70 ,null=True)
   date_created = models.DateTimeField(auto_now_add=True, null=True)
   
   def __str__(self):
      return self.name


class Work_contact(models.Model):
   organisation = models.CharField('Organisation', max_length=70,null=True )
   department = models.CharField('Department', max_length=70,null=True )
   address = models.CharField('Address', max_length=70,null=True )
   city = models.CharField('City', max_length=70,null=True )
   country = models.CharField('Country', max_length=70,null=True )
   mobile_number = models.CharField('Mobile Number', max_length=70,null=True )
   email_address = models.EmailField('Email Address', max_length=70,null=True )

   def __str__(self):
       return self.organisation

class education_and_training(models.Model):
   title_of_your_training = models.CharField('Title Of Your Training', max_length=70,null=True )
   start_date = models.DateField('Start Date',null=True )
   end_date = models.DateField('End Date',null=True )
   name_of_provider = models.CharField('Name Of Provider', max_length=70,null=True )
   certificates = models.FileField('Certificates', blank=False,null=True )
   city = models.CharField('City/Town',null=True ,max_length=70)
   # address = models.CharField('City/Town',null=True ,max_length=200)
   country = models.CharField('Country',null=True ,max_length=70)
   name = models.CharField('Name',null=True ,max_length=70)
   job_title = models.CharField('Job Title',null=True ,max_length=70)
   telephone_number = models.CharField('Telephone Number',null=True ,max_length=70)
   email = models.EmailField('Email',null=True ,max_length=70)
   title_of_your_training1 = models.CharField('Title Of Your Training',null=True ,max_length=70)
   start_date1 = models.DateField('Start Date',null=True ,max_length=70)
   end_date1 = models.DateField('End Date',null=True ,max_length=70)
   name_of_pro = models.CharField('Name Of Provider',null=True ,max_length=70)
   address = models.CharField('Address',null=True ,max_length=700)
   town = models.CharField('City/Town',null=True ,max_length=70)
   country1 = models.CharField('Country',null=True ,max_length=70)

   def __str__(self):
       return self.title_of_your_training

class pst_five_work(models.Model):
   organisation = models.CharField('Organisation', max_length=70,null=True,blank=True)
   start_date = models.DateField('Start Date',null=True,blank=True)
   end_date = models.DateField('End Date',null=True,blank=True )
   post = models.CharField('Post', max_length=70,null=True,blank=True)
   address = models.CharField('Address',null=True ,max_length=70, blank=True)
   town = models.CharField('City/Town',null=True ,max_length=70, blank=True)
   country1 = models.CharField('Country',null=True ,max_length=70, blank=True)
   name_of_manager = models.CharField('Name Of Manager', max_length=70,null=True,blank=True)
   mobile_number = models.CharField('Mobile Number', max_length=70,null=True,blank=True)
   email_address = models.EmailField('Email Address', max_length=70,null=True ,blank=True)

   def __str__(self):
       return self.organisation

class character_ref(models.Model):
   name = models.CharField('Name',null=True ,max_length=70)
   address = models.CharField('Address',null=True ,max_length=70)
   name1 = models.CharField('Name',null=True ,max_length=70)
   occupation= models.CharField('Occupation',null=True ,max_length=70)
   business_address = models.CharField('Business Address',null=True ,max_length=70)
   email = models.EmailField('Email',null=True ,max_length=70)
   capacity = models.CharField('Capacity In Which You Know The Applicant',null=True ,max_length=70)

   def __str__(self):
       return self.name

class practise_outside(models.Model):
   country_of_practise = models.CharField('Name Of Country Practice',null=True ,max_length=70, blank=True)
   regulatory_body = models.CharField('Regulatory Body',null=True ,max_length=70, blank=True)
   regulatory_number = models.CharField('Regulatory Number',null=True ,max_length=70, blank=True)
   organisation= models.CharField('Organisation',null=True ,max_length=70, blank=True)
   start_date = models.DateField('Start Date',null=True, blank=True )
   end_date = models.DateField('End Date',null=True, blank=True )
   post = models.CharField('Post', max_length=70,null=True, blank=True )
   address = models.CharField('Address',null=True ,max_length=70, blank=True)
   city = models.CharField('City/Town',null=True ,max_length=70, blank=True)
   country = models.CharField('Country',null=True ,max_length=70)
   name_of_manager = models.CharField('Name Of Manager', max_length=70,null=True ,blank=True)
   mobile_number = models.CharField('Mobile Number', max_length=70,null=True ,blank=True)
   email = models.EmailField('Email',null=True ,max_length=70,blank=True)
   CHOICES = [('N','NO'),('Y','Yes'),('I','If Yes Give Reason')]
   any_discipinary =models.CharField('Faced Any Disciplinary Action', max_length=20, choices=CHOICES,null=True, blank=True)

   def __str__(self):
       return self.country_of_practise

class rivate_practice(models.Model):
   CHOICES = [('N','NO'),('Y','Yes'),('I','If Yes Give Reason')]
   any_discipinary =models.CharField('Have you ever practiced as a Registered Social Worker', max_length=20, choices=CHOICES,null=True)
   jurisdiction = models.CharField('Jurisdiction',null=True ,max_length=70)
   area_of_practice = models.CharField('Area of Practice eg Counselling',null=True ,max_length=70)
   name_of_practise = models.CharField('Name Of Practise', max_length=70,null=True )
   address = models.CharField('Address',null=True ,max_length=70)
   mobile_number = models.CharField('Mobile Number', max_length=70,null=True )
   email = models.EmailField('Email',null=True ,max_length=70)
   CHOICES = [('N','NO'),('Y','Yes'),('I','If Yes Give Reason')]
   any_discipinary =models.CharField('Have you ever practiced as a Registered Social Worker', max_length=20, choices=CHOICES,null=True)

   def __str__(self):
       return self.jurisdiction


# class Person(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField(blank=True)
#     location = models.CharField(max_length=100, blank=True)
#     phone = models.CharField(max_length=200, null=True)
   

   
   


        
