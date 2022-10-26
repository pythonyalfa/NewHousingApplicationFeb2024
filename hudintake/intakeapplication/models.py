from django.db import models


class Applicant_Information(models.Model):

    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Social_Security_Number = models.PositiveIntegerField(default='0')
    EDUCATION_LEVEL = (
        ('1', ' No High School Diploma'),
        ('2', 'High School Diploma'),
        ('3', 'GED'),
        ('4', 'Vocational Certificate'),
        ('5', 'Some College, did not graduate'),
        ('6', 'Associate\'s Degree'),
        ('7', 'Bachelor\'s Degree'),
        ('8', 'Master\'s Degree'),
        ('9', 'Doctorate'),
    )
    Education_Level = models.CharField(max_length=1, choices=EDUCATION_LEVEL, default='Doctorate')
    DOB = models.DateTimeField(max_length=11)
    Cell_Phone = models.PositiveIntegerField()
    Alternate_Phone = models.PositiveIntegerField()
    Current_Address = models.CharField(max_length=30, default='Current Address')  # (Since)
    MARITAL_STATUS = (
        ('1', 'Married'),
        ('2', 'Single'),
        ('3', 'Widow'),
        ('4', 'Domestic Partnership'),
        ('5', 'Separated'),
        ('6', 'Divorced'),
    )
    Marital_Status = models.CharField(max_length=20, choices=MARITAL_STATUS, default='')

    User_ID = models.CharField(max_length=20, default='')
    #todaysdate = models.DateTimeField() Removed due to redundancy

# Copied and paste this so i can update the model with out declaring it a class
# again this we will see soon what the best method is



    Citizenship = (
        ('1', 'US Born'),
        ('2', 'Other'),
        ('3', 'Permanent resident'),
    )
    citizen = models.CharField(max_length=2, choices=Citizenship, default='')


#class FarmWorker(models.Model):
    farmw = (
        ('1', 'Yes'),
        ('2', 'No'),
    )
    #Farm_Work2 = 'Farm_Work\(y\/n\)'
    Farm_Work = models.CharField(max_length=1, choices=farmw, default='')



#class RaceEthnicity(models.Model):
    race = (
        ('1', 'American Indian'),
        ('2', 'Alaskan Native'),
        ('3', 'Asian'),
        ('4', 'Black or African Amrican'),
        ('5', 'Native Hawaiian'),
        ('6', 'White'),
        ('7', 'Other'),
        ('8', 'Hispanic/Latino'),
    )
    Race = models.CharField(max_length=1, choices=race, default='')


#class Employed(models.Model):
    isworking = (
        ('1', 'Yes'),
        ('2', 'No'),
    )
    Employment_Status = models.CharField(max_length=1, choices=isworking, default='Yes')


#class PreferredLanguage(models.Model):
    languages = (
        ('1', 'English'),
        ('2', 'Spanish'),
        ('3', 'Other'),
    )
    language = models.CharField(max_length=1, choices=languages, default='-')


#within = 'Within_50_miles_of_Mexico_Border?'
 #   within = models.PositiveIntegerField()

created = models.DateTimeField(auto_now_add=True)


class Employment_History(models.Model):
    Employer_Name = models.CharField(max_length=200)
    Employer_Address = models.CharField(max_length=200)
    Job_Title = models.CharField(max_length=200)
    Employment_Start = models.DateTimeField(auto_now=False, default='')
    Employment_End =  models.DateTimeField(auto_now=False, default='')


Number_in_household = models.IntegerField(max_length=2, default='')


class Household_Information(models.Model):
    choice = (
        ('1', 'Single Adult'),
        ('2', 'Female-headed single parent household'),
        ('3', 'Male-headed single parent household'),
        ('4', 'Married without dependents'),
        ('5', 'Two or more unrelated adults'),
        ('6', 'Two or more unrelated adults'),
        ('7', 'Other'),
    )

    Household_Type = models.CharField(max_length=20, choices=choice)

class Monthly_Budget(models.Model):
    Total_Gross_Income = models.PositiveIntegerField(blank=True, default='1')#may need to add editable
    Total_Net_Income = models.PositiveIntegerField(blank=True, default='1')#may need to add editable
    Total_Expense = models.PositiveIntegerField(blank=True, default='1')#may need to add editable

class Expenses(models.Model):
    Housing_Rental_Payment = models.SmallIntegerField(default='')
    Housing_1st_Mortgage_Payment = models.SmallIntegerField(default='')
    Housing_Utility_Electric_Gas_Payment = models.SmallIntegerField(default='')
    Housing_Utility_Water = models.SmallIntegerField(default='')
    Housing_Utility_Garbage = models.SmallIntegerField(default='')
    Telephone_Internet_Phone = models.SmallIntegerField(default='')
    Telephone_Cell_Phone = models.SmallIntegerField(default='')
    Food_Groceries = models.SmallIntegerField(default='')


class Misc_Expense(models.Model):
    Food_Eating_Out_Delivery = models.SmallIntegerField(default='')
    Auto_Loan_Lease_Payments = models.SmallIntegerField(default='')
    Auto_Gas_Maintenance = models.BigIntegerField(default='')
    Health_Care_Medical_Dental = models.SmallIntegerField(default='')
    Entertainment = models.SmallIntegerField(default='')
    Credit_Cards_Minimum_Payments = models.SmallIntegerField(default='')
    State_Federal_Taxes = models.SmallIntegerField(default='')
    Dependents_Day_Care_Clothing = models.SmallIntegerField(default='')
    Donations = models.SmallIntegerField(default='')
    Education_Tuition_Books = models.SmallIntegerField(default='')
    Pets = models.SmallIntegerField(default='')
    Other_Expenses = models.SmallIntegerField(default='')
    #add loop to add all these expensees up and list_display them



class Credit(models.Model):
    choice = (
    ('1', 'yes'),
    ('2', 'no'),
)
    Credit2 = models.CharField(max_length=3, choices=choice)

anythingelse = models.TextField()




