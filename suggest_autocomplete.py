from elasticsearch import Elasticsearch

def get_suggestions(es, index_name, query):
    body = {
        "query": {
            "match": {
                "content": {
                    "query": query,
                    "fuzziness": "AUTO"
                }
            }
        }
    }

    response = es.search(index=index_name, body=body)
    suggestions = [hit["_source"]["content"] for hit in response["hits"]["hits"]]
    return suggestions


if __name__ == "__main__":
    index_name = "autocomplete_index"
    es = Elasticsearch(hosts=["http://localhost:9200"])

    while True:
        query = input("Enter text for suggestions (or type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            break

        suggestions = get_suggestions(es, index_name, query)
        if suggestions:
            print("Suggestions:", suggestions)
        else:
            print("No suggestions found.")
