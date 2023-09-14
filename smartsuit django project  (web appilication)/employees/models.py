from django.db import models

gender_options = (('M', 'Male'), ('F', 'Female'), ('T', 'Transgender'), ('N', 'None'))


class Employee(models.Model):
    emp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    dob = models.DateField()
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=11, choices=gender_options, null=True, blank=True, default='N')
    address = models.TextField()
    is_suited = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Available_Suit(models.Model):
    suit_id = models.CharField(max_length=10)
    allocate_to = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    div = models.CharField(max_length=10)

    def __str__(self):
        return self.div + "-" + self.suit_id


class Suit(models.Model):
    suit_id = models.ForeignKey(Available_Suit, on_delete=models.CASCADE)
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    temperature = models.IntegerField(null=True, blank=True)
    pressure = models.IntegerField(null=True, blank=True)
    Methane = models.IntegerField(null=True, blank=True)
    co = models.IntegerField(null=True, blank=True)
    heart_rate = models.IntegerField(null=True, blank=True)
    oxygen = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name.name

    def full_name(self):
        return self.name.name
