import metapy
import pytoml

idx = metapy.index.make_inverted_index('config.toml')
# Examine number of documents
print(idx.num_docs())
# Number of unique terms in the dataset
print(idx.unique_terms())
# The average document length
print(idx.avg_doc_length())
# The total number of terms
print(idx.total_corpus_terms())