from rest_framework import permissions

# from app_expenses.models import BlackListedToken


def get_income(data: dict, user) -> dict:
    return {
        'created': data.get('created'),
        'amount': data.get('amount'),
        'category': data.get('category'),
        'user': user.id
    }


def get_expenses(expenses: list, user) -> list:
    for expense in expenses:
        expense['user'] = user.id
    return expenses

#
# class IsTokenValid(permissions.BasePermission):
#     def has_permission(self, request, view):
#         user_id = request.user.id
#         is_allowed_user = True
#         token = request.auth.decode("utf-8")
#         try:
#             is_blackListed = BlackListedToken.objects.get(user=user_id, token=token)
#             if is_blackListed:
#                 is_allowed_user = False
#         except BlackListedToken.DoesNotExist:
#             is_allowed_user = True
#         return is_allowed_user