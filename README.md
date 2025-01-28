# Elasticsearch Autocomplete with Fuzzy Matching

This project sets up an Elasticsearch index for autocomplete functionality with typo tolerance (up to 3 typos for words longer than 7 characters).

## Features

- Autocomplete suggestions
- Uses a dictionary file for vocabulary

## Setup Instructions

### Prerequisites

- Docker & Docker Compose
- Python 3.8 or higher

### Step 1: Clone Repository

```bash
git clone git@github.com:alexeysirenko/prjctr-10-elasticsearch-autocomplete.git
cd prjctr-10-elasticsearch-autocomplete
```

### Step 2 (Optional): Download Dictionary File

Download a dictionary file with English words:

```bash
curl -o words.txt https://raw.githubusercontent.com/dwyl/english-words/master/words.txt
```

### Step 3: Start Elasticsearch and Kibana

Use Docker Compose to start Elasticsearch and Kibana:

```bash
docker-compose up -d
```

### Step 4: Create Virtual Environment

Set up a Python virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

pip install -r requirements.txt
```

### Step 5: Create Index and Load Dictionary

Run the script to create the index and load the dictionary:

```bash
python recreate_index.py autocomplete_index words.txt
```

### Step 6: Access Kibana

Kibana is a web-based UI to manage and visualize Elasticsearch data. After starting Kibana with Docker Compose, access it in your browser:

- URL: [http://localhost:5601](http://localhost:5601)

You can use the **Dev Tools** section in Kibana to run Elasticsearch queries, explore your index, and test autocomplete functionality.

### Step 7: Test Autocomplete

Run the input prompt script:

```bash
python suggest_autocomplete.py
```

Type queries into the prompt, and the script will suggest autocompletions.

### Example Usage

```plaintext
Enter text for suggestions (or type 'exit' to quit): auto
Suggestions: ['autocomplete', 'autonomous', 'automatic']

Enter text for suggestions (or type 'exit' to quit): autocomplte
Suggestions: ['autocomplete']
```

### Step 8: Stop Elasticsearch and Kibana

To stop Elasticsearch and Kibana, run:

```bash
docker-compose down
```
