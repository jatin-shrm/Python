#meta string
str1="geeks"
str2="keegs"
for i in range(len(str1)):
    if str1[i]!=str2[i]:
        element_index=str1.find(str2[i])
        list_string=list(str1)
        list_string[i],list_string[element_index]=list_string[element_index],list_string[i]
        str1=''.join(list_string)
        print(str1)