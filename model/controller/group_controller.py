from group import Group
import random
class GroupController():
    # Default constructor for the generator
    def __init__(self, group_size=2, group_count=2):
        self._groups = [Group(group_size) for i in range(group_count)]
        self._group_size = group_size
    # Inflating every group with given list of names
    def generate(self, names):
        total_candidates = len(names)
        # Save the position of every candidate's name that already a member
        already_member = list()
        for member in range(self._group_size):
            for group in self._groups:
                # Generate a new position that has not have a group
                new_member = self.get_new_member(total_candidates, already_member)
                # Exitting the generating the proc
                if new_member == -1:
                    return True
                # Add the names with the generated position to certain group
                group.add(names[new_member - 1])
                # Update already member list
                already_member.append(new_member)
    # Generating a random position of the names to add to the current group
    def get_new_member(self, total_candidates, already_member):
        # Stop the generating proc if all the candidates already has a group
        if total_candidates == len(already_member) :
            return -1
        new_member = self.get_random_pos(total_candidates)
        # Check if the new member position generated is already a member of
        # certain group if so, generate a new random int
        while new_member in already_member:
            new_member = self.get_random_pos(total_candidates)
        return new_member
    # Generating a random int from 0 to group_size
    def get_random_pos(self, total_candidates):
        return random.randint(0, total_candidates)
    # Print every group to the screen
    def print_groups(self):
        for _id, group in enumerate(self._groups):
            print("Group {}:".format(_id + 1))
            for _idm, member in enumerate(group.get_member()):
                print("{}. {}".format(_idm + 1, member))
