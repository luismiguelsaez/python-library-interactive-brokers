from python_ib import flex_query
from sys import argv

ib_token = argv[1]
ib_query_id = argv[2]

code = flex_query.getReferenceCode(ib_token,ib_query_id)
print(code)
print(flex_query.getQueryResult(ib_token,code))