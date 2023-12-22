# Şəkil axtarışı

[CLIP](https://huggingface.co/sentence-transformers/clip-ViT-B-32) və [Elasticsearch](https://www.elastic.co/elasticsearch) istifadə edərək, təbii dildə şəkil axtarışını həyata keçirən proyekt.



## İstifadə qaydası:

### 1- Elasticsearch

İlk olaraq [Elasticsearch](https://cloud.elastic.co/) servisində sizin aktiv Hosted deployment olmalıdır
<img src="https://i.postimg.cc/PqDY7rgM/1.jpg">

Deployment-in Manage bölməsinə daxil olaraq, onun Elasticsearch Endpoint linkini əldə etmək mümkündür
<img src="https://i.postimg.cc/y6hdbSkd/2.jpg">

Deployment-in login və şifrəsi, onu aktivləşdirdikdə istifadəçiyə təqdim edilir

Şəkillər haqqında məlumatların saxlanılacağı indeksi **Dev tools** bölməsi vasitəsilə də etmək mümkündür. Əgər indeksi optimizasiya etmək fikriniz varsa o zaman onu **Dev tools** vasitəsilə qabaqcadan hazır etmək lazımdır


### 2- Create the index

Next step is to create the index. The template used is defined in [/scripts/opensearch_template.py](./scripts/opensearch_template.py).

We use Approximate k-NN search because we expect a high number of images (+1M). Run the helper script:

```bash
docker-compose run --rm  scripts create-opensearch-index
```

It will create an index named `images`.

### 3 - Optional: Load unsplash dataset

To be searchable, images need to be embedded with CLIP and indexed.

If you want to try it on the [Unsplash Dataset](https://unsplash.com/data), you can compute the features [as done here](https://github.com/haltakov/natural-language-image-search#on-your-machine).
You can also use the [pre-computed features](https://drive.google.com/drive/folders/1WQmedVCDIQKA2R33dkS1f980YsJXRZ-q?usp=sharing), courtesy of [@haltakov](https://github.com/haltakov).

**In both cases, you need the permission of Unsplash.**

You should have two files:

- A csv file with photos ids, let name it `photo_ids.csv`
- A npy file with the features, let name it `features.npy`

Move them to the `/data` folder, so the docker container used to run scripts can access them.

Use the helper script to index the images. For example:

```bash
docker-compose run --rm  scripts index-unsplash-opensearch --start 0 --end 10000 /data/photo_ids.csv /data/features.npy
```

Will index the ids from 0 to 10000.

### 4 - Launch the search

After indexing, you can search for images in the frontend.

The frontend is a simple Next.js app, that send search queries to the backend.

The backend is a python app, that embed search queries with CLIP and send an approximate k-nn request to the OpenSearch service.

The sources code are in the `app` and `api` folders.

## Guide: Elasticsearch (TODO) 🚧
