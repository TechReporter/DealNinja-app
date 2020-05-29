from django.db import models


# Create your models here.


class Contact(models.Model):
    f_name = models.CharField(max_length=50, default="")
    l_name = models.CharField(max_length=50, default="")
    MR = 'Mr.'
    MRS = 'Mrs.'
    STATUS = [
        (MR, 'Mr.'),
        (MRS, 'Mrs.')]
    status = models.CharField(
        max_length=5,
        choices=STATUS,
        default=MR, )
    title = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=10)
    office_number = models.CharField(max_length=10)
    company = models.CharField(max_length=100)
    corporate_ph = models.CharField(max_length=10)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=10)
    website = models.CharField(max_length=10)
    emp_count = models.IntegerField()
    yearly_revenue = models.CharField(max_length=10)


class Notes(models.Model):
    notes_date = models.DateField()
    activity = models.CharField(max_length=100)
    notes_text = models.CharField(max_length=500)
    contact = models.ForeignKey(Contact, related_name='notes', on_delete=models.CASCADE)

    def __str__(self):
        # return '%d: %s' % (self.order, self.title)
        return f"{self.activity} - added on {self.notes_date}"
