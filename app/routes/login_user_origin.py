from flask_login import login_user


# TODO: The `login_user` function of Flask probably has to be a token with the api endpoint
def login_user_origin(users_name, users_email, origin):
    # Not sure why it has to be like this, but it will be different with endpoints
    from app import db
    from app.models.user import User

    print("logging in user from origin that is not regular")
    # Check if the user has logged in before using this origin.
    # If that's the case it has a Row in the User database, and we log in
    # (we don't use the username, because the user can change it from the Google name)
    origin_user = User.query.filter_by(email=users_email, origin=origin).first()
    if origin_user is None:
        print("new user")
        # If not than we create a new entry in the User table and then log in.
        # The last verification is to check if username is not taken
        new_user = User.query.filter_by(username=users_name).first()
        if new_user is None:
            print("really new user!")
            user = User(
                username=users_name,
                email=users_email,
                password_hash="",
                origin=origin
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
        else:
            print("username is taken....")
            # If the username is taken than we change it because we have to create the user here.
            # The user can change it later if he really hates it.
            # We just assume that it eventually always manages to create a user.
            index = 2
            while index < 100:
                new_user_name = users_name + "_%s" % index
                print("attempting user creation with username: %s" % new_user_name)
                new_user = User.query.filter_by(username=new_user_name).first()
                if new_user is None:
                    print("we finally have a correct username!")
                    user = User(
                        username=new_user_name,
                        email=users_email,
                        password_hash="",
                        origin=origin
                    )
                    db.session.add(user)
                    db.session.commit()
                    login_user(user)
                    break
                else:
                    print("still taken...")
                    index += 1
    else:
        print("logging in existing user")
        login_user(origin_user)


