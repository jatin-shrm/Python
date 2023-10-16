#Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
thisdict={}
for item in keys:
    thisdict.update({item:sample_dict[item]})
print(thisdict)