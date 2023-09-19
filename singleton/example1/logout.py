from app_state import ApplicationState

def logout_user():
    print(f"\n")
    ApplicationState.getAppState().isLoggedIn = False
    print(f"User has logged out. Thank you!")
