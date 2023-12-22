# Şəkil axtarışı

[CLIP](https://huggingface.co/sentence-transformers/clip-ViT-B-32) və [Elasticsearch](https://www.elastic.co/elasticsearch) istifadə edərək, təbii dildə şəkil axtarışını həyata keçirən proyekt.



## İstifadə qaydası:

### 1- Elasticsearch

İlk olaraq [Elasticsearch](https://cloud.elastic.co/) servisində sizin aktiv Hosted deployment olmalıdır
<img src="https://i.postimg.cc/PqDY7rgM/1.jpg">

Deployment-in Manage bölməsinə daxil olaraq, onun Elasticsearch Endpoint linkini əldə etmək mümkündür
<img src="https://i.postimg.cc/y6hdbSkd/2.jpg">

Deployment-in login və şifrəsi, onu aktivləşdirdikdə istifadəçiyə təqdim edilir

Şəkillər haqqında məlumatların saxlanılacağı indeksi **Dev tools** bölməsi vasitəsilə də etmək mümkündür. 

Əgər indeksi optimizasiya etmək fikriniz varsa o zaman onu **Dev tools** vasitəsilə qabaqcadan hazır etmək lazımdır


### 2- Şəkillərin hazır edilməsi

Axtarışın aparılacağı şəkilləri qabaqcadan hazırlayaraq `images` qovluğunda yerləşdirmək lazımdır

### 3 - Şəkillərin vektorlaşdırılması

Qovluqda olan hər şəkili vektorlaşdırmaq üçün **vector_generate.py** faylını icra edirik

```bash
vector_generate.py
```
Fayl icra edilərkən bəzi məlumatların daxil edilməsi tələb olunacaq

**Elasticsearch cloud host** : Elasticsearch-dəki Deployment-in Endpoint ünvanı<br>
**Elasticsearch cloud username** : Elasticsearch-dəki Deployment-in istifadəçi adı<br>
**Elasticsearch cloud password** : Elasticsearch-dəki Deployment-in istifadəçi şifrəsi<br>
**Elasticsearch index name** : Şəkillər haqqında məlumatların yüklənəcəyi indeksin adı<br>
**Full images path** : Kompyüterinizdə şəkillərin saxlandığı qovluğun tam ünvanı<br>
**Model name** : Vektorlaşmanı həyata keçirəcəyimiz modelin adı. Default olaraq bu **clip-ViT-B-32**

Məlumatları daxil etdikdən sonra, şəkillər növbə ilə vektorlaşdırılaraq, Elasticsearch-dəki qeyd etdiyiniz indeksə daxil ediləcək

İndeksə daxil edilən hər sənəd faylın adından və onun vektorundan ibarət olacaq

### 4 - Şəkillərin axtarılması

Qovluqda olan hər şəkili vektorlaşdırmaq üçün **vector_generate.py** faylını icra etmıək lazımdır

Axtarışa başlamaq üçün **search.py** faylını icra etmıək lazımdır

```bash
search.py
```

Fayl icra edilərkən bəzi məlumatların daxil edilməsi tələb olunacaq

**Search query** : Axtarılan şəklin mətni təsviri<br>
**Elasticsearch cloud host** : Elasticsearch-dəki Deployment-in Endpoint ünvanı<br>
**Elasticsearch cloud username** : Elasticsearch-dəki Deployment-in istifadəçi adı<br>
**Elasticsearch cloud password** : Elasticsearch-dəki Deployment-in istifadəçi şifrəsi<br>
**Elasticsearch index name** : Şəkillər haqqında məlumatların yüklənəcəyi indeksin adı<br>
**Model name** : Vektorlaşmanı həyata keçirəcəyimiz modelin adı. Default olaraq bu **clip-ViT-B-32**

Məlumatları daxil etdikdən sonra, axtarılan şəklin mətni təsvirinə uyğun olan top 5 şəkil haqqında məlumat qaytarılacaq

Məlumatda şəklin ID-si, faylın adı və uyğunluq balı əks olunacaq

Əgər sorğuya uyğun top faylların sayını artırıb və ya azaltmaq istəsəniz, bunu **search.py** faylında k veriləninin dəyərini dəyişərək həyata keçirə bilərsiniz

```bash
k = 5  # Number of nearest neighbors
```
