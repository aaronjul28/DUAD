class User:
    role: str

    def __init__(self, role):
        self.role = role


def admin_only(func):
    def wrapper(user, *args , **kwargs):
        if user.role != "Admin":
            raise ValueError(
                "You are not allowed to run this function. You are not an admin"
            )
        func(user, args, kwargs)

    return wrapper


@admin_only
def create_product(user, product_name):
    # (lógica para crear producto...)
    print(f"Product {product_name} created!")


@admin_only
def create_product_category(user, product_category_name):
    # (lógica para crear categoria...)
    print(f"Product Category {product_category_name} created!")


@admin_only
def modify_order(user, order_id):
    # (lógica para modificar pedido...)
    print(f"Order {order_id} modified!")

