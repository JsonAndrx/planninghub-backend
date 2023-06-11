from django.contrib.auth import get_user_model


class get_object_user():

    def user_init(self):
        User = get_user_model()
        return User

    def get_users(self):
        return self.user_init().objects.all()