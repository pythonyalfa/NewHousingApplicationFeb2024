from django.contrib import admin
from .models import * #Applicant_Information, Employment_History, Household_Information, Monthly_Budget, Expenses, Credit2

#admin.site.register(Applicant_Information)
#admin.site.register(Employment_History)
#admin.site.register(Household_Information)
#admin.site.register(Monthly_Budget)
#admin.site.register(Expenses)
#admin.site.register(Credit)
#admin.site.register(Misc_Expense)
# We need all the desired models from each class into another
#

@admin.register(Applicant_Information)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'DOB', 'EDUCATION_LEVEL', 'Social_Security_Number')

#admin.register(Employment_History)
#ass EmploymentAdmin(admin.ModelAdmin):
 #   list_display = ('Job_Title',)

@admin.register(Household_Information)
class HouseholdInfoAdmin(admin.ModelAdmin):
    list_display = ('Household_Type',)

@admin.register(Monthly_Budget)
class MonthlyBudgetAdmin(admin.ModelAdmin):
    list_display = ('Total_Net_Income', 'Total_Gross_Income')

@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('Housing_Rental_Payment',)


@admin.register(Misc_Expense)
class MiscExpenseAdmin(admin.ModelAdmin):
    list_display = ('Education_Tuition_Books',)


# We have to think of how its going to look from the front
# at work the back end is jacked up and doesnt want to show

'''
from django.contrib import admin
from .models import Applicant_Information, Employment_History, Monthly_Budget, Expenses

# Inline model admin classes
class EmploymentHistoryInline(admin.TabularInline):
    model = Employment_History
    extra = 1

class MonthlyBudgetInline(admin.StackedInline):
    model = Monthly_Budget
    max_num = 1

class ExpensesInline(admin.TabularInline):
    model = Expenses
    extra = 1

# Main model admin class
class ApplicantInformationAdmin(admin.ModelAdmin):
    inlines = [
        EmploymentHistoryInline,
        MonthlyBudgetInline,
        ExpensesInline,
    ]
    # Additional configurations for Applicant_Information admin if needed

# Register the main model with its admin class
admin.site.register(Applicant_Information, ApplicantInformationAdmin)
'''