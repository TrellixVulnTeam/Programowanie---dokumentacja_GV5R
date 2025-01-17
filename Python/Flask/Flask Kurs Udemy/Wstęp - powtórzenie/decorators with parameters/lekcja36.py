import functools

user = {"username": "jose", "access_level": 2}


def make_secure(access_level):
  def decorator(func):
    # kepps func first name
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
      if user["access_level"] >= access_level:
        return func(*args, **kwargs)
      else:
        return f"user {user['username']} have no {access_level} perimsons level"
    return secure_function
  return decorator

@make_secure(3)
def get_admin_password():
  return "1234"

@make_secure(2)
def get_dashboard_password():
  return "user: user_password"

print(get_admin_password(), get_dashboard_password())
user = {"username": "jose", "access_level": 3}
print(get_admin_password(), get_dashboard_password())

