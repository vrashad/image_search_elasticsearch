from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch, exceptions
from PIL import Image
from pathlib import Path
import os

def elasticsearch_connection(es_host, es_username, es_password, es_index_name):
    # Connecting to the remote Elasticsearch
    es = Elasticsearch(
        [es_host],
        basic_auth=(es_username, es_password)
    )
    # Check if the specified index exists
    try:
        if not es.indices.exists(index=es_index_name):
            # If not, create it
            es.indices.create(index=es_index_name)
            print(f"Created index: {es_index_name}")
        else:
            print(f"Index {es_index_name} exists.")
    except exceptions.ConnectionError as e:
        print("Could not connect to Elasticsearch, check your settings:", e)
        raise e

    return es

def image_encoding(model_name, images_path, es, es_index_name):
    # Loading the CLIP model
    model = SentenceTransformer(model_name)

    # Path to the image folder
    images_folder_path = str(Path(images_path))

    # Iterating through all files in the folder
    for filename in os.listdir(images_folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp')):  # Checking the image format
            image_path = os.path.join(images_folder_path, filename)

            # Loading and encoding the image
            image = Image.open(image_path)
            img_emb = model.encode([image])[0]  # Obtaining the vector

            # Creating a document for Elasticsearch
            doc = {
                'filename': filename,
                'embedding': img_emb.tolist()  # Converting to list for Elasticsearch compatibility
            }

            # Indexing the document
            es.index(index=es_index_name, document=doc)

    print("All images have been processed and indexed.")


if __name__ == '__main__':
    es_host = input("Please enter Elasticsearch cloud host: ")
    es_username = input("Please enter Elasticsearch cloud username: ")
    es_password = input("Please enter Elasticsearch cloud password: ")
    es_index_name = input("Please enter Elasticsearch index name: ")
    images_path = input("Please enter full images path: ")
    use_default_model_yes_no = input("Use default model ? Y/N (Default clip-ViT-B-32: ")
    if use_default_model_yes_no.lower() == 'n':
        model_name = input("Please enter model name: ")
    else:
        model_name = "clip-ViT-B-32"
    es = elasticsearch_connection(es_host, es_username, es_password, es_index_name)
    image_encoding(model_name, images_path, es, es_index_name)
