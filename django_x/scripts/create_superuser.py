from django.contrib.auth.models import User

username = "admin1234"
password = "admin1234"
email = "admin1234@twitter.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created.")
else:
    print("Superuser creation skipped.")