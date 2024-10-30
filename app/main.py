from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema

from app.api.countries_api import init_db
from app.gql.mutation_file import Mutation
from app.gql.query_file import Query

app = Flask(__name__)

schema = Schema(query=Query, mutation=Mutation)

app.add_url_rule(
   '/graphql',
   view_func=GraphQLView.as_view(
       'graphql',
       schema=schema,
       graphiql=True
   )
)

if __name__ == '__main__':
    # init_db()
    app.run(port=5003, debug=True)
