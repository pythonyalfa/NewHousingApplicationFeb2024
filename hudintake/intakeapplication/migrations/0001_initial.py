# Generated by Django 4.1.2 on 2024-02-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('Social_Security_Number', models.PositiveIntegerField(default='0')),
                ('Education_Level', models.CharField(choices=[('1', ' No High School Diploma'), ('2', 'High School Diploma'), ('3', 'GED'), ('4', 'Vocational Certificate'), ('5', 'Some College, did not graduate'), ('6', "Associate's Degree"), ('7', "Bachelor's Degree"), ('8', "Master's Degree"), ('9', 'Doctorate')], default='Doctorate', max_length=1)),
                ('DOB', models.DateTimeField(max_length=11)),
                ('Cell_Phone', models.PositiveIntegerField()),
                ('Alternate_Phone', models.PositiveIntegerField()),
                ('Current_Address', models.CharField(default='Current Address', max_length=30)),
                ('Marital_Status', models.CharField(choices=[('1', 'Married'), ('2', 'Single'), ('3', 'Widow'), ('4', 'Domestic Partnership'), ('5', 'Separated'), ('6', 'Divorced')], default='', max_length=20)),
                ('User_ID', models.CharField(default='', max_length=20)),
                ('citizen', models.CharField(choices=[('1', 'US Born'), ('2', 'Other'), ('3', 'Permanent resident')], default='', max_length=2)),
                ('Farm_Work', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], default='', max_length=1)),
                ('Race', models.CharField(choices=[('1', 'American Indian'), ('2', 'Alaskan Native'), ('3', 'Asian'), ('4', 'Black or African Amrican'), ('5', 'Native Hawaiian'), ('6', 'White'), ('7', 'Other'), ('8', 'Hispanic/Latino')], default='', max_length=1)),
                ('Employment_Status', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], default='Yes', max_length=1)),
                ('language', models.CharField(choices=[('1', 'English'), ('2', 'Spanish'), ('3', 'Other')], default='-', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Credit2', models.CharField(choices=[('1', 'yes'), ('2', 'no')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Employment_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employer_Name', models.CharField(max_length=200)),
                ('Employer_Address', models.CharField(max_length=200)),
                ('Job_Title', models.CharField(max_length=200)),
                ('Employment_Start', models.DateTimeField(default='')),
                ('Employment_End', models.DateTimeField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Housing_Rental_Payment', models.SmallIntegerField(default='')),
                ('Housing_1st_Mortgage_Payment', models.SmallIntegerField(default='')),
                ('Housing_Utility_Electric_Gas_Payment', models.SmallIntegerField(default='')),
                ('Housing_Utility_Water', models.SmallIntegerField(default='')),
                ('Housing_Utility_Garbage', models.SmallIntegerField(default='')),
                ('Telephone_Internet_Phone', models.SmallIntegerField(default='')),
                ('Telephone_Cell_Phone', models.SmallIntegerField(default='')),
                ('Food_Groceries', models.SmallIntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Household_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Household_Type', models.CharField(choices=[('1', 'Single Adult'), ('2', 'Female-headed single parent household'), ('3', 'Male-headed single parent household'), ('4', 'Married without dependents'), ('5', 'Two or more unrelated adults'), ('6', 'Two or more unrelated adults'), ('7', 'Other')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Misc_Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Food_Eating_Out_Delivery', models.SmallIntegerField(default='')),
                ('Auto_Loan_Lease_Payments', models.SmallIntegerField(default='')),
                ('Auto_Gas_Maintenance', models.BigIntegerField(default='')),
                ('Health_Care_Medical_Dental', models.SmallIntegerField(default='')),
                ('Entertainment', models.SmallIntegerField(default='')),
                ('Credit_Cards_Minimum_Payments', models.SmallIntegerField(default='')),
                ('State_Federal_Taxes', models.SmallIntegerField(default='')),
                ('Dependents_Day_Care_Clothing', models.SmallIntegerField(default='')),
                ('Donations', models.SmallIntegerField(default='')),
                ('Education_Tuition_Books', models.SmallIntegerField(default='')),
                ('Pets', models.SmallIntegerField(default='')),
                ('Other_Expenses', models.SmallIntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Monthly_Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_Gross_Income', models.PositiveIntegerField(blank=True, default='1')),
                ('Total_Net_Income', models.PositiveIntegerField(blank=True, default='1')),
                ('Total_Expense', models.PositiveIntegerField(blank=True, default='1')),
            ],
        ),
    ]
