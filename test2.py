import metapy
import pytoml


idx = metapy.index.make_inverted_index('config.toml')


# Build the query object and initialize a ranker
query = metapy.index.Document()
ranker = metapy.index.OkapiBM25(k1=1.2,b=0.75,k3=500)
# To do an IR evaluation, we need to use the queries file and relevance judgements.
ev = metapy.index.IREval('config.toml')
# Load the query_start from config.toml or default to zero if not found
with open('config.toml', 'r') as fin:
        cfg_d = pytoml.load(fin)
query_cfg = cfg_d['query-runner']
query_start = query_cfg.get('query-id-start', 0)
# We will loop over the queries file and add each result to the IREval object ev.
num_results = 10
with open('cranfield-queries.txt') as query_file:
    for query_num, line in enumerate(query_file):
        query.content(line.strip())
        results = ranker.score(idx, query, num_results)                            
        avg_p = ev.avg_p(results, query_start + query_num, num_results)
        print("Query {} average precision: {}".format(query_num + 1, avg_p))
ev.map()