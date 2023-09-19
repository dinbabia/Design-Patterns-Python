from app_state import ApplicationState


def check_account():
    print("\n")
    if ApplicationState.getAppState().isLoggedIn:
        print("User is Logged in.")
        print("Viewing Account Dashboard")
    else:
        print("User cannot view Account.")
        print("Please log in first.")
