class Group():
    # Default constructor for the Group class
    def __init__(self, member_size = 2):
        self._member = list()
        self._member_size = member_size
    # Get the names of all the member of this group
    def get_member(self):
        return self._member
    # Add the new given name to the group as member
    def add(self, name):
        self._member.append(name)
