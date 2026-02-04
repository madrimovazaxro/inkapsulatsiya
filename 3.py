import os
os.system("cls")

class User:
    def __init__(self, username):
        self.username = username
        self.friends = []
    def add_friend(self, friend):
        if friend in self.friends:
            return False
        else:
            self.friends.append(friend)
            return True
    def remove_friend(self, friend):
        if friend not in self.friends:
            return False
        else:
            self.friends.remove(friend)
            return True
    def list_friends(self):
        return self.friends
    def is_friend(self, friend):
        if friend in self.friends:
            return True
        else:
            return False
    def mutual_friends(self, other_user):
        lst = []
        for friend in self.friends:
            if friend in other_user.friends:
                lst.append(friend)
        return lst


user1 = User("Ali")
user2 = User("Vali")

print(user1.add_friend("Sami"))    # True
print(user1.add_friend("Vali"))    # True
print(user1.add_friend("Sami"))    # False (allaqachon mavjud)

print(user2.add_friend("Ali"))     # True
print(user2.add_friend("Sami"))    # True

print(user1.list_friends())   # ['Sami', 'Vali']
print(user2.list_friends())    # ['Ali', 'Sami']

print(user1.is_friend("Vali"))     # True
print(user1.is_friend("Botir"))    # False

print(user1.mutual_friends(user2)) # ['Sami']

print(user1.remove_friend("Vali")) # True
print(user1.remove_friend("Botir"))# False
print(user1.list_friends())        # ['Sami']