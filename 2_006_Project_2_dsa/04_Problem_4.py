# In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if not isinstance(group, Group):
        print ('TypeError: second argument must be a Group instance')
        return

    group_subgroups = group.get_groups()
    group_users = group.get_users()

    if user in group_users:
        return True
    elif len(group_subgroups) == 0:
        return False
    else:
        for subgroup in group_subgroups:
            # return is_user_in_group(user, subgroup)
            if is_user_in_group(user, subgroup):
                return True

    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Normal Cases:
print('Normal Cases:')
print(is_user_in_group(user='sub_child_user', group=sub_child))
# True
print(is_user_in_group(user='child_user', group=parent))
# False
print(is_user_in_group(user='sub_child_user', group=parent), '\n')
# True



# Edge Cases:
print('Edge Cases:')
print(is_user_in_group(user='', group=child))
# False
print(is_user_in_group(user='', group=sub_child))
# False
print(is_user_in_group(user='sub_child_user', group=sub_child_user))
