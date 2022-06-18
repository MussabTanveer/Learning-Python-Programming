import functools

user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."
    return secure_function


@make_secure
def get_admin_password():
    return "1234"


print(get_admin_password())
print(get_admin_password.__name__)  # secure_function wrong
