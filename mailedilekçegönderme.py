import smtplib

tarih = input ("Tarihi giriniz: ")
okul = input ("Okudugunuz universitenin adini giriniz: ")
bolum = input ("Universite Bolumunuzu giriniz: ")

adı = input ("Adinizi giriniz: ")
soyadi = input ("Soyadinizi Giriniz: ")

gonderilecekmail = """
                                                                                                Tarih : {}

                TURKİYE CUMHURİYETİ MİLLİ SAVUNMA  BAKANLİGİ

                            ASKER ALMA SUBE BASKANLIGINA


    {} OKULUNDA {} BOLUMUNDE ogrenci oldugum icin derslerimden geri
    kalmamak ve sinavlarimda basari saglayabilmek amaci ile en erken celp 
    doneminde silah altına alinarak, Bedelli Askerlik yukumlulugumu yerine
    getirmek istiyorum



Bilgi ve geregi arz olunur.                                    Ad : {}
                                                                            Soyad: {}





---------------------------------------------------------------------------------------------------------------


""".format (tarih, okul.upper (), bolum, adı.upper (), soyadi.upper ())

content = ((gonderilecekmail.encode ("utf-8")))

mail = smtplib.SMTP ("smtp.gmail.com", 587)

mail.ehlo ()

mail.starttls ()

mail.login ("baglanılacakmail@gmail.com")

mail.sendmail ("gönderenmail.gmail.com", "alıcı@gmail.com", content)
