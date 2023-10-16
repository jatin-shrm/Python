#Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
thisdict=dict.fromkeys(employees,defaults)
print(thisdict)