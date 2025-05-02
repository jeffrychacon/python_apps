class User:
    #pass
    def __init__(self, user_id,username):
        print("new user is being created ...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Angela")
print(f'"{user_1.id}" Followers: {user_1.followers}')
user_2 = User("002", "Jack")
print(f'"{user_2.id}" Followers: {user_2.followers}')

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

#user_1 = User()
#user_1.id = '001'
#user_1.name = 'angela'
