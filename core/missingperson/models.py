from django.db import models


# ==============================
# Missing Person Model
# ==============================

class MissingPerson(models.Model):

    REPORT_TYPE_CHOICES = (
        ("POLICE", "Police"),
        ("INDIVIDUAL", "Individual"),
    )

    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    father_name = models.CharField(
        max_length=100
    )

    date_of_birth = models.DateField()

    address = models.TextField()

    phone_number = models.CharField(
        max_length=15
    )

    aadhar_number = models.CharField(
        max_length=20
    )

    missing_from = models.DateField()

    email = models.EmailField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    image = models.ImageField(
        upload_to="missing_persons/"
    )

    report_type = models.CharField(
        max_length=20,
        choices=REPORT_TYPE_CHOICES,
        default="INDIVIDUAL"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ==============================
# Detection Logs Model
# ==============================

class DetectionLog(models.Model):

    person = models.ForeignKey(
        MissingPerson,
        on_delete=models.CASCADE
    )

    detected_at = models.DateTimeField(
        auto_now_add=True
    )

    location = models.CharField(
        max_length=200,
        default="Surveillance Camera"
    )

    confidence = models.FloatField()

    screenshot = models.ImageField(
        upload_to="detections/",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.person.first_name} detected at {self.detected_at}"


# ==============================
# Police Login Model
# ==============================

class Police(models.Model):

    username = models.CharField(
        max_length=100,
        unique=True
    )

    password = models.CharField(
        max_length=100
    )

    station_name = models.CharField(
        max_length=200
    )

    def __str__(self):
        return self.station_name