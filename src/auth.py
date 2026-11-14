def authenticate(
    username,
    password,
    expected_username,
    expected_password,
):
    if username is None or password is None:
        return False

    if not username.strip() or not password.strip():
        return False

    return (
        username == expected_username
        and password == expected_password
    )
