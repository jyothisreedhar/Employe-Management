from django import forms
class EmployeCreateForm(forms.Form):
    name=forms.CharField()
    #suppose we know the designation
    designations=(
        ("Developer", "Developer"),
        ("qa", "qa"),
        ("HR", "HR"),
        ("sales", "sales")
    )
    designation=forms.ChoiceField(choices=designations)
    salary=forms.IntegerField()
    location=forms.CharField()
    email=forms.CharField()





