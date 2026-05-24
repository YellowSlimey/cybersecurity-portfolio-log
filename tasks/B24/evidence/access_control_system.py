class AccessControlSystem:
    def __init__(self):
        self.roles = {
            "admin": {"read", "write", "delete", "manage_users"},
            "staff": {"read", "write"},
            "guest": {"read"}
        }

    def check_permission(self, user_role, action):
        if action in self.roles.get(user_role, set()):
            return f"ACCESS GRANTED: {user_role} can perform {action}"
        else:
            return f"ACCESS DENIED: {user_role} cannot perform {action}"


acs = AccessControlSystem()

print(acs.check_permission("admin", "delete"))
print(acs.check_permission("staff", "delete"))
print(acs.check_permission("guest", "read"))
print(acs.check_permission("guest", "write"))