class UserService:
    def __init__(self):
      self._users = {
          1: {"id": 1, "name": "Ray"},
          2: {"id": 2, "name": "Louie"},
      }
    
    def get_users(self):
      print("Get All Users")
      return list(self._users.values())

    def get_user(self, user_id: int):
      print("Get User by ID:", user_id)
      print("User Data:", self._users.get(user_id))
      return self._users.get(user_id)

    def create_user(self, user_id : int, name : str):
      print("Create a new user!")
      if user_id in self._users:
          print("User already exists.")
      self._users[user_id] = {"id": user_id, "name": name}
      return self._users[user_id]
