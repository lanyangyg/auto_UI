#   测试数据

LOGIN_TEST_DATA = [
    (
        "standard_user",
        "wrong_password",
        {"error": "Epic sadface: Username and password do not match any user in this service"}
    ),
    (
        "locked_out_user",
        "secret_sauce",
        {"error": "Epic sadface: Sorry, this user has been locked out."}
    ),
    (
        "standard_user",
        "secret_sauce",
        {"success": "Swag Labs"}
    )
]