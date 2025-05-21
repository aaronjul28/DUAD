list=[1,44,6,7,54,7,78,4,5,776]

class Bubble_sort:

    def __init__(self, list_to_order):
        self.list_to_order=list_to_order

    def order_list(self):
        for outside_index in range(len(self.list_to_order)-1):            
            for index in range(len(self.list_to_order)-1 - outside_index):
                current_index=self.list_to_order[index]
                next_index=self.list_to_order[index+1]
                #print(f'CURRENT > {current_index} NEXT {next_index}')
                if current_index > next_index:
                    #print(f'Changing index {current_index} for {next_index}')
                    self.list_to_order[index]=next_index
                    self.list_to_order[index+1]=current_index

    def order_list_backwards(self):
        for outside_index in range(len(self.list_to_order)-1):            
            for index in range(len(self.list_to_order)-1 - outside_index):
                current_index=self.list_to_order[index]
                next_index=self.list_to_order[index+1]
                #print(f'CURRENT > {current_index} NEXT {next_index}')
                if next_index > current_index:
                    #print(f'Changing index {next_index} for {current_index}')
                    self.list_to_order[index]=next_index
                    self.list_to_order[index+1]=current_index


    def print_sorted_list(self):
        print(self.list_to_order)

sort=Bubble_sort(list)
sort.order_list()
sort.print_sorted_list()
sort.order_list_backwards()
sort.print_sorted_list()
