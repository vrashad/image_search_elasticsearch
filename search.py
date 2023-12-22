from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch, exceptions

def elasticsearch_connection(es_host, es_username, es_password, es_index_name):
    # Connect to the remote Elasticsearch instance
    es = Elasticsearch(
        [es_host],
        basic_auth=(es_username, es_password)
    )
    # Check if the specified index exists
    try:
        if not es.indices.exists(index=es_index_name):
            # If the index does not exist, create it
            es.indices.create(index=es_index_name)
            raise f"Index {es_index_name} does not exist."
    except exceptions.ConnectionError as e:
        print("Could not connect to Elasticsearch, check your settings:", e)
        raise e

    return es

def image_search(model_name, search_text, es, es_index_name):
    # Load the CLIP model
    model = SentenceTransformer(model_name)

    # Convert the text to a vector
    text_emb = model.encode([search_text])[0].tolist()

    # Create a kNN search query
    k = 5  # Number of nearest neighbors
    query = {
        "knn": {
            "field": "embedding",  # Specify the name of your vector field here
            "query_vector": text_emb,
            "k": k,
            "num_candidates": 10  # Adjust the number of candidates for a more precise search
        }
    }
    # Execute the query in Elasticsearch
    response = es.search(index=es_index_name, body=query)

    # Output the results
    print("Search Results:")
    for hit in response['hits']['hits']:
        print(f"ID: {hit['_id']}, Score: {hit['_score']}, Filename: {hit['_source']['filename']}")

if __name__ == '__main__':
    search_text = input("Please enter search query: ")
    es_host = input("Please enter Elasticsearch cloud host: ")
    es_username = input("Please enter Elasticsearch cloud username: ")
    es_password = input("Please enter Elasticsearch cloud password: ")
    es_index_name = input("Please enter Elasticsearch index name: ")
    use_default_model_yes_no = input("Use default model? Y/N (Default clip-ViT-B-32): ")
    if use_default_model_yes_no.lower() == 'n':
        model_name = input("Please enter model name: ")
    else:
        model_name = "clip-ViT-B-32"
    es = elasticsearch_connection(es_host, es_username, es_password, es_index_name)
    image_search(model_name, search_text, es, es_index_name)