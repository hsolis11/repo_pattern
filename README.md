# Repository Pattern

My attempt at implementing the repository pattern in Python that I read about on [Architecture Patterns with Python](https://www.cosmicpython.com/book/chapter_02_repository.html). The example in the book uses SQL Alchemy and for my example I want to avoid having SQL Alchemy as a dependency.  

Found an example of implementing the Repository Pattern in [StackOverflow](https://stackoverflow.com/questions/9699598/implementation-of-repository-pattern-in-python).

The end goal of this project to switch between databases easily.
Databases to be used for this project:
- Sqlite3
- MySql
- TinyDB

The app will be importing the database package and using dataclasses to handle all the data details.

```python
import database
from database import User

# Example of a dataclass
user = User(f_name="Bob", l_name="Doe", username="dragonslayer")

# Example of adding a user object to the database
repo = database.Users()
repo.add_user(user)
repo.complete()

# Example of getting a user from the database
repo = database.Users()
retrieved_user = repo.get_user(username="dragonslayer")
```

The app will run on the console and will have minimal functionality with the following options:
- Create User
- Edit User
- List Users
- Delete User

