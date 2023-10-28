from django.db import models
from bookProfile.models import Book
from django.contrib.auth.models import User
from datetime import timedelta

class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # otomatis diisi tanggal sekarang
    borrow_date = models.DateTimeField(auto_now_add=True)
    #nilai bisa null, field bisa kosong karena sebelum objek dibuat kita tidak tahu tanggal pengembalian
    return_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
   
    def save(self, *args, **kwargs):
        if not self.id:  # jika ini objek baru
            #durasi peminjaman maksimal diatur hanya 7 hari
            self.return_date = self.borrow_date + timedelta(days=7)
        super().save(*args, **kwargs)