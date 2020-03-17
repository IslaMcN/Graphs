
def earliest_ancestor(ancestors, starting_node):
    for i in ancestors:
        print(i)
        if starting_node == i[1]:
            goal = i
            print(goal)
        #     if temp[0] == None and temp[1] == None:
        #         return -1
        #     if i is None:
        #         return temp[0]
        #     r = earliest_ancestor(ancestors, temp[0])
        #     if r is not None:
        #         return r
        # else:
        #     return -1
    