class user:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.follower=0
        self.following=0
        # print("user is being created")
        print( id +" " + name)

    def follow(self,user):
        user.follower +=1
        self.following +=1

user1= user("100","Aditya")
# user1.id=""
# user1.username="Aditya"

# print(user1.id)
# print(user1.name)

user2=user("101","john")
user1.follow(user2)
print(user1.follower)
print(user1.following)
print(user2.follower)
print(user2.following)