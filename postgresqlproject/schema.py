import graphene;
import webapp.schema;
class Query(webapp.schema.Query,graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query,mutation=webapp.schema.UpdateAuthorMutation);

