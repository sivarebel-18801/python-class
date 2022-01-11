#ALL MODULES
def create_list():
    List_init=[]
    number_ele_list=int(input("please enter number elements to available in list:"))
    for element in range(number_ele_list):
        element_n=int(input("please enter the element:"))
        List_init.append(element_n)
    return List_init
def append_list(List):
    element_to_be_inserted=int(input("please enter the element to be inserted:"))
    List.append(element_to_be_inserted)
    return List
def len_list(List):
    return len(List)
def pop_list(List):
    List.pop()
    return List
def sum_list(List):
    return sum(List)
def max_list(List):
    return max(List)
def min_list(List):
    return min(List)
def remove_list(List):
    element_to_be_removed=int(input("please enter the element to be removed:"))
    List.remove(element_to_be_removed)
    return List
def insert_list(List):
    element_to_be_inserted=int(input("please enter the element to be inserted:"))
    List.insert(element_to_be_inserted,index_list)
    return List
def count_list(List):
    element_to_be_count=int(input("please enter the element to be count:"))
    b=List.count(element_to_be_count)
    return b
def sort_list(List):
    List.sort()
    return List
def reverse_list(List):
    List.reverse()
    return List
def index_list(List):
    indexing_value=int(input("please enter a value"))
    List.index(indexing_value)
    return List
def clear_list(List):
    List.clear()
    return List
def copy_list(List):
    b=create_list()
    List.copy()
    return List
def extend_list(List):
    b=create_list()
    List.extend(b)
    return List

#tuple
def create_tuple():
    x=tuple(map(int,input().split(',')))
    return x
def sum_tuple(tuple):
    return sum(tuple)
def max_tuple(tuple):
    return max(tuple)
def min_tuple(tuple):
    return min(tuple)
def len_tuple(tuple):
    return len(tuple)
def count_tuple(tuple):
    element_to_be_count=int(input("please enter the element to be count:"))
    b=tuple.count(element_to_be_count)
    return b

#set 
def create_set():
    set_init=set()
    number_ele_set=int(input("please enter number elements to the avalible in set:"))
    for element in range(number_ele_set):
        element_n=int(input("please enter the element:"))
        set_init.add(element_n)
    return set_init
def sum_set(set):
    return sum(set)
def max_set(set):
    return max(set)
def min_set(set):
    return min(set)
def len_set(set):
    return len(set)
def clear_set(set):
    set.clear()
    return set
def copy_set(set):
    b=create_set()
    set.copy()
    return set
def update_set(set):
    b=create_set()
    set.update(b)
    return set
def add_set(set):
    b=create_set()
    n=int(input("enter number of elements in b:"))
    for i in range(n):
        c=int(input("enter the b element:"))
        b.add(c)
        set.update(b)
    return b
def remove_set(set):
    element_to_be_removed=int(input("please enter the element to be removed:"))
    set.remove(element_to_be_removed)
    return set
def discard_set(set):
    element_to_be_removed=int(input("please enter the element to be removed:"))
    set.discard(element_to_be_removed)
    return set
def union_set(set):
    b=create_set()
    c=set.union(b)
    return c
def intersection_set(set):
    b=create_set()
    c=set.intersection(b)
    return c
def difference_set(set):
    b=create_set()
    c=set.difference(b)
    return c
def issubset_set(set):
    b=create_set()
    c=set.issubset(b)
    return b
def issuperset_set(set):
    b=create_set()
    c=set.issuperset(b)
    return c

#dictionary
def create_dict():
    dict_init={}
    number_ele_dict=int(input("please enter number elements to the avavilble in dict:"))
    for element in range(number_ele_dict):
        a=int(input("enter the key values:"))
        b=input("enter the  values pairs:")
        dict_init[a]=b
    return dict_init
def len_dict(dict):
    return len(dict)
def pop_dict(dict):
    n=int(input("enter the key to pop:"))
    x=dict.pop(n)
    return dict
def max_dict(dict):
    return max(dict)
def min_dict(dict):
    return min(dict)
def keys_dict(dict):
    b=dict.keys()
    return b
def values_dict(dict):
    b=dict.values()
    return b
def items_dict(dict):
    b=dict.items()
    return b
def popitem_dict(dict):
    b=dict.popitem()
    return b
def clear_dict(dict):
    dict.clear()
    return dict
def copy_dict(dict):
    b=create_dict()
    dict.copy()
    return dict


print("welcome to data structure calculator")
print("please select any operation to proceed\n1.List\n2.tuple\n3.set\n4.dictionary:")
data_input=int(input("please enter a number between 1 and 4:"))
if data_input==1:
    print("welcome to list operations")
    print("create alist for proceeding list operations")
    List_main=create_list()
    print("the created list is",List_main)
    print("please select any one list operator to proceed(any number between 1 and 15:)")
    print("1.append\n2.len\n3.pop\n4.sum\n5.max\n6.min\n7.remove\n8.insert\n9.count\n10.sort\n11.reverse\n12.1ndex\n13.clear\n14.copy\n15.extend")
    list_operation_input=int(input("please enter any one number...:"))
    if list_operation_input==1:
        output_append=append_list(List_main)
        print("the output after append operations is",output_append)
    elif list_operation_input==2:
        output_len=len_list(List_main)
        print("the output after len operations is",output_len)
    elif list_operation_input==3:
        output_pop=pop_list(List_main)
        print("the output after pop operations is",output_pop)
    elif list_operation_input==4:
        output_sum=sum_list(List_main)
        print("the output after sum operations is",output_sum)
    elif list_operation_input==5:
        output_max=max_list(List_main)
        print("the output after max operations is",output_max)
    elif list_operation_input==6:
        output_min=min_list(List_main)
        print("the output after min operations is",output_min)
    elif list_operation_input==7:
        output_remove=remove_list(List_main)
        print("the output after remove operations is",output_remove)
    elif list_operation_input==8:
        output_insert=insert_list(List_main)
        print("the output after insert operations is",output_insert)
    elif list_operation_input==9:
        output_count=count_list(List_main)
        print("the output after count operations is",output_count)
    elif list_operation_input==10:
        output_sort=sort_list(List_main)
        print("the output after sort operations is",output_sort)
    elif list_operation_input==11:
        output_reverse=reverse_list(List_main)
        print("the output after reverse operations is",output_reverse)
    elif list_operation_input==12:
        output_index=index_list(List_main)
        print("the output after index operations is",output_index)
    elif list_operation_input==13:
        output_clear=clear_list(List_main)
        print("the output after clear operations is",output_clear)
    elif list_operation_input==14:
        output_copy=copy_list(List_main)
        print("the output after copy operations is",output_copy)
    elif list_operation_input==15:
        output_extend=extend_list(List_main)
        print("the output after del operations is",output_extend)
    else:
        print('invaild')
if data_input==2:
    print("welcome to tuple operations")
    print("create a tuple for proceeding tuple operations")
    tuple_main=create_tuple()
    print("the created tuple is",tuple_main)
    print("please select any one tuple operator to proceed(any number between 1 and 5:)")
    print("1.sum\n2.max\n3.min\n4.len\n5.count")
    tuple_operation_input=int(input("please enter any one number...:"))
    if tuple_operation_input==1:
        output_sum=sum_tuple(tuple_main)
        print("the output after sum operations is",output_sum)
    elif tuple_operation_input==2:
        output_max=max_tuple(tuple_main)
        print("the output after max operations is",output_max)
    elif tuple_operation_input==3:
        output_min=min_tuple(tuple_main)
        print("the output after min operations is",output_min)
    elif tuple_operation_input==4:
        output_len=len_tuple(tuple_main)
        print("the output after len operations is",output_len)
    elif tuple_operation_input==5:
        output_count=count_tuple(tuple_main)
        print("the output after count operations is",output_count)
    else:
        print('invaild')



if data_input==3:
    print("welcome to set operations")
    print("create a set for proceeding set operations")
    set_main=create_set()
    print("the created set is",set_main)
    print("please select any one set operator to proceed(any number between 1 and 15:)")
    print("1.sum\n2.max\n3.min\n4.len\n5.clear\n6.copy\n7.update\n8.add\n9.remove\n10.discard\n11.union\n12.intersection\n13.difference\n14.issubset\n15.issuperset")
    set_operation_input=int(input("please enter any one number...:"))
    if set_operation_input==1:
        output_sum=sum_set(set_main)
        print("the output after sum operations is",output_sum)
    elif set_operation_input==2:
        output_max=max_set(set_main)
        print("the output after max operations is",output_max)
    elif set_operation_input==3:
        output_min=min_set(set_main)
        print("the output after min operations is",output_min)
    elif set_operation_input==4:
        output_len=len_set(set_main)
        print("the output after len operations is",output_len)
    elif set_operation_input==5:
        output_clear=clear_set(set_main)
        print("the output after clear operations is",output_clear)
    elif set_operation_input==6:
        output_copy=copy_set(set_main)
        print("the output after copy operations is",output_copy)
    elif set_operation_input==7:
        output_update=update_set(set_main)
        print("the output after update operations is",output_update)
    elif set_operation_input==8:
        output_add=add_set(set_main)
        print("the output after add operations is",output_add)
    elif set_operation_input==9:
        output_remove=remove_set(set_main)
        print("the output after remove operations is",output_remove)
    elif set_operation_input==10:
        output_discard=discard_set(set_main)
        print("the output after discard operations is",output_discard)
    elif set_operation_input==11:
        output_union=union_set(set_main)
        print("the output after union operations is",output_union)
    elif set_operation_input==12:
        output_intersection=intersection_set(set_main)
        print("the output after intersection operations is",output_intersection)
    elif set_operation_input==13:
        output_difference=difference_set(set_main)
        print("the output after difference operations is",output_difference)
    elif set_operation_input==14:
        output_issubset=issubset_set(set_main)
        print("the output after issubset operations is",output_issubset)
    elif set_operation_input==15:
        output_issuperset=issuperset_set(set_main)
        print("the output after issuperset operations is",output_issuperset)
    else:
        print('invalid')

if data_input==4:
    print("welcome to dictionary operations")
    print("create a dictionary for proceeding dictionary operations")
    dict_main=create_dict()
    print("the created dict is",dict_main)
    print("please select any one dict operator to proceed(any number between 1 and 11:)")
    print("1.len\n2.pop\n3.max\n4.min\n5.keys\n6.values\n7.items\n8.pop_item\n9.clear\n10.copy")
    dict_operation_input=int(input("please enter any one number...:"))
    if dict_operation_input==1:
        output_len=len_dict(dict_main)
        print("the output after len operations is",output_len)
    elif dict_operation_input==2:
        output_pop=pop_dict(dict_main)
        print("the output after pop operations is",output_pop)
    elif dict_operation_input==3:
        output_max=max_dict(dict_main)
        print("the output after max operations is",output_max)
    elif dict_operation_input==4:
        output_min=min_dict(dict_main)
        print("the output after min operations is",output_min)
    elif dict_operation_input==5:
        output_keys=keys_dict(dict_main)
        print("the output after keys operations is",output_keys)
    elif dict_operation_input==6:
        output_values=values_dict(dict_main)
        print("the output after value operations is",output_values)
    elif dict_operation_input==7:
        output_items=items_dict(dict_main)
        print("the output after items operations is",output_items)
    elif dict_operation_input==8:
        output_popitem=popitem_dict(dict_main)
        print("the output after popitem operations is",output_popitem)
    elif dict_operation_input==9:
        output_clear=clear_dict(dict_main)
        print("the output after clear operations is",output_clear)
    elif dict_operation_input==10:
        output_copy=copy_dict(dict_main)
        print("the output after copy operations is",output_copy)
    else:
        print("invaild")
    


    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
               





    
