def number_validation(func):
    def wrapper(*args):  
        args_list=list(args)
        args_list.pop(0)
        for i in args_list:
            if isinstance(i,(int,float)) is False:
                raise ValueError(f'Value {i} is not a number!')
        return func(*args)
    return wrapper     


class Sum():
    @number_validation
    def numbers_to_sum(self,value1,value2):
        result=value1+value2
        return result

sum=Sum()
result=sum.numbers_to_sum(1,2)
print(result)
#sum.numbers_to_sum(102,'1')