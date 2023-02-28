#pip install speedtest-cli

import speedtest
import time

s=speedtest.Speedtest()

print("Hız Testiniz Yapılıyor. Daha Doğru Sonuçlar İçin Bilgisayarınızı Modeme Kablo İle Bağlayınız ve Cihazlarınızın Wifi Bağlantılarını Kapatınız.\n")
time.sleep(5)
print("Lütfen Bekleyiniz...\n")

downloadspeed=s.download()
uploadspeed=s.upload()
ping=round(s.results.ping)

print("İndirme Hızınız {} Mbps".format(downloadspeed))
print("Yükleme Hızınız {} Mbps".format(uploadspeed))
print("Ping {} ms".format(ping))




