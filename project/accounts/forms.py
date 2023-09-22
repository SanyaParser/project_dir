from allauth.account.forms import SignupForm
from django.core.mail import mail_managers, mail_admins


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)

        mail_managers(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )

        return user


#class AdminSignupForm(SignupForm):
#    def save(self, request):
#        user = super().save(request)
#
#        mail_admins(
#            subject='Новый пользователь!',
#            message=f'Админ, Пользователь {user.username} зарегестрировался на сайте.'
#        )
#        return user
