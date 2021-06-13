import datetime

from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


# Create your models here.
class Room(models.Model):
    RoomID = models.CharField('Ký hiệu phòng', max_length=30)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.RoomID  # hiển thị tên từng loại tờ trình theo tên phòng

    class Meta:
        verbose_name_plural = 'Phòng ban'


class LoaiTT(models.Model):
    TTId = models.CharField('Ký hiệu TT', max_length=20)

    # TTName = models.CharField('Tên đầy đủ',max_length=50)
    def __str__(self):
        return self.TTId  # hiển thị tên từng loại tờ trình theo tên tờ trình

    class Meta:
        verbose_name_plural = 'Loại tờ trình'


class Year(models.Model):
    year = models.CharField(max_length=10)
    yearQuantity = models.IntegerField(default=0)

    def __str__(self):
        return self.year


class ToTrinh(models.Model):
    TTId = models.ForeignKey(LoaiTT, on_delete=models.PROTECT, verbose_name='Loại tờ trình')
    TTtitle = models.CharField('Tên tờ trình', max_length=150)
    TTText = models.TextField('Nội dung tóm tắt', max_length=500, null=True, blank=True)
    Created_on = models.DateField('Ngày lấy số', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Người tạo')
    RoomId = models.ForeignKey(Room, on_delete=models.DO_NOTHING, null=True, verbose_name='Phòng')
    idByYear = models.IntegerField(default=0)

    def __str__(self):
        return self.TTtitle  # hiển thị tờ trình theo SoTT

    def save(self, *args, **kwargs):
        roomId = Room.objects.get(RoomID=self.RoomId)
        roomId.quantity += 1
        roomId.save()
        getTime = datetime.datetime.now()
        year = getTime.year
        yearObject, created = Year.objects.get_or_create(year=str(year))
        yearObject.yearQuantity += 1
        yearObject.save()
        self.idByYear=yearObject.yearQuantity
        return super(ToTrinh, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Tờ trình'


