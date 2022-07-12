Her gün koyduğunuz öğelerin sayısını iki
katına çıkaran sihirli bir kutunuz var.
Verilen program, ilk madde sayısını ve
gün sayısını girdi olarak alır.

 Görev
 Son gündeki öğelerin sayısını
 hesaplayan ve çıktısını veren
 bir program yazın.

 Örnek Giriş
 3
 2

 Örnek Çıktı
 12

 Açıklama
 1. Gün: 6 (3*2)
 2. Gün: 12 (6*2)

 Kodlama :


items = int(input())
days = int(input())
while days>0 :
 items*=2
 days-=1
 
 print(items)
