from rdflib.graph import ConjunctiveGraph
from rdflib.tools.rdf2dot import rdf2dot
from sys import stdout
olids=['OL24562640W','OL9241549A']
g=ConjunctiveGraph()
for olid in olids:
    g.parse(f"https://openlibrary.org/works/{olid}.rdf")
rdf2dot(g,stdout)

