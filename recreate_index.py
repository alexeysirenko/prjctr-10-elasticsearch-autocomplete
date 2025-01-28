import sys
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

def create_index(es, index_name):
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)

    settings = {
        "settings": {
            "analysis": {
                "filter": {
                    "autocomplete_filter": {
                        "type": "edge_ngram",
                        "min_gram": 2,
                        "max_gram": 7
                    }
                },
                "analyzer": {
                    "autocomplete_analyzer": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": ["lowercase", "autocomplete_filter"]
                    },
                    "autocomplete_search_analyzer": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": ["lowercase"]
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                "content": {
                    "type": "text",
                    "analyzer": "autocomplete_analyzer",
                    "search_analyzer": "autocomplete_search_analyzer"
                }
            }
        }
    }

    """
    # works too with fuzziness < 3
    settings = {
        "mappings": {
            "properties": {
                "content": {
                    'type': 'text',
                    'analyzer': 'simple',
                    'search_analyzer': 'simple'
                }
            }
        }
    }
    """

    es.indices.create(index=index_name, body=settings)
    print(f"Index '{index_name}' created successfully.")


def load_words_to_index(es, index_name, dictionary_file):
    print(f"Loading words...")
    with open(dictionary_file, 'r') as file:
        words = [line.strip() for line in file if line.strip()]

    actions = [
        {"_index": index_name, "_source": {"content": word}}
        for word in words
    ]
    bulk(es, actions)
    print(f"Indexed {len(words)} words successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python recreate_index.py <index_name> <dictionary_file>")
        sys.exit(1)

    index_name = sys.argv[1]
    dictionary_file = sys.argv[2]

    es = Elasticsearch(hosts=["http://localhost:9200"])
    create_index(es, index_name)
    load_words_to_index(es, index_name, dictionary_file)
