def sort (my_list):
    for current_pos in range(len(my_list))
        max_pos = current_pos
        for comp_pos in range (current_pos +1, len(my_list)):
            if my_list[comp_pos]> my_list[current_pos]:
                max_pos = comp_pos
        temp = my_list[max_pos]
        my_list[max_pos] = my_list[comp_pos]
        my_list[current_pos] = temp
        print my_list
    return my_list
sort([20,32,23,67,2,5])                