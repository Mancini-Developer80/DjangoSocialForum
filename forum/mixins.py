from django.contrib.auth.mixins import UserPassesTestMixin

class StaffMixing(UserPassesTestMixin):
    """
    Consente solamente allo Staff di creare nuove Sezioni
    
    """
    def test_func(self):
        return self.request.user.is_staff
        