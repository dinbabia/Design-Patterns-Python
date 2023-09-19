from app_state import ApplicationState


def login_user():
    print("Login Dashboard")
    if ApplicationState.getAppState().isLoggedIn:
        print("User is Logged in")
    username = input("Enter password: ")
    ApplicationState.getAppState().isLoggedIn = True
