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

To be searchable, images need to be embedded with CLIP and indexed.


```bash
vector_generate.py
```



### 4 - Launch the search

After indexing, you can search for images in the frontend.

The frontend is a simple Next.js app, that send search queries to the backend.

The backend is a python app, that embed search queries with CLIP and send an approximate k-nn request to the OpenSearch service.

The sources code are in the `app` and `api` folders.

## Guide: Elasticsearch (TODO) 🚧
