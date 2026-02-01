from pages.login_page import LoginPage

BASE_URL = "https://localhost.com"

USERS = {
    "admin": {
        "username": "admin_user",
        "password": "pass",
        "role": "Admin"
    }
}

def test_login_with_valid_admin_user(get_browser_driver_handle):
    driver = get_browser_driver_handle
    login_page = LoginPage(driver)

    login_page.open(f"{BASE_URL}/login")

    user = USERS["admin"]
    login_page.login(user["username"], user["password"])

    assert login_page.is_login_successful(), \
        "Login failed: Dashboard not visible"
