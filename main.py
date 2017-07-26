if __name__ == "__main__":
    # Adding the model package to the python path
    import sys
    sys.path.append('model')
    # Taking user input for total of group that want to be generated and
    # the group size and the name of all of the candidates
    group_total = int(input("How many groups you want to generate? "))
    group_size  = int(input("How many members a group can hold? "))
    print("Enter the name of all the candidates, separated by comma!")
    candidates = input().split(",")
    # Creating an instance of GroupController
    from model.controller.group_controller import GroupController
    gc = GroupController(group_size, group_total)
    gc.generate(candidates)
    gc.print_groups()
