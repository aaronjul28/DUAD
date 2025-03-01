def enter_phrase():
    normal_phrase=input('Enter the phrase: ')
    phrase_split=normal_phrase.split('-')
    return phrase_split

def sort_phrase():
    list_before_sort=enter_phrase()
    list_after_sort=sorted(list_before_sort)
    return list_after_sort

def adding_dash_back():
    adding_dash_list=sort_phrase()
    adding_dash_phrase=[]
    for i in adding_dash_list:
        adding_dash_phrase.append(i)
        adding_dash_phrase.append('-')
    adding_dash_phrase.pop(len(adding_dash_phrase)-1)
    return adding_dash_phrase

def complete_string():
    list_to_make_string=adding_dash_back()
    final_string=''
    for i in list_to_make_string:
        final_string=final_string+i
    return final_string


print(complete_string())