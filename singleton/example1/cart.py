from app_state import ApplicationState


def check_cart():
    print("\n")
    if ApplicationState.getAppState().isLoggedIn:
        print("User is Logged in.")
        print(f"Viewing Cart")
    else:
        print(f"In order to view the cart, you need to login.")
