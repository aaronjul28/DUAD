#5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def enter_phrase():
    phrase_list=[]
    normal_phrase=input('Enter the phrase: ')
    for i in normal_phrase:
        phrase_list.append(i)
    return phrase_list

def upper_detector():
    phrase_to_detect=enter_phrase()
    upper_count=0
    lower_count=0
    for i in phrase_to_detect:
        low = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
        upper = 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'

        if i in low:
            lower_count=lower_count+1
        if i  in upper:
            upper_count=upper_count+1
        else:
            continue
    return [lower_count, upper_count]

def main():
    final_upper_lower_count=upper_detector()
    return f'There’s {final_upper_lower_count[0]} lower cases and {final_upper_lower_count[1]} upper cases'

print(main())
