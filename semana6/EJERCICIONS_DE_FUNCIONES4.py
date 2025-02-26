def enter_phrase():
    phrase_list=[]
    normal_phrase=input('Enter the phrase you want to reverse: ')
    for i in normal_phrase:
        phrase_list.append(i)
    return phrase_list

def reverse_phrase():
    my_string = enter_phrase()
    reverse_list=[]
    reverse_string=""
    string_len = len(my_string)-1
    char_list=[]
    
    for list_value in my_string:
        char_list.append(list_value)
    for i in enumerate(char_list):
        reverse_list.append(char_list[string_len])
        string_len=string_len-1
    
    for i in reverse_list:
        reverse_string=reverse_string+i
    return reverse_string

print(reverse_phrase())