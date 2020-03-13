from graphene_django.types import DjangoObjectType;
import graphene
from webapp.models import author, cookbook, airlines;
class AirlineType(DjangoObjectType):
    class Meta:
        model = airlines;
class AuthorType (DjangoObjectType):
    class Meta:
        model = author;
class CookbookType (DjangoObjectType):
    class Meta:
        model = cookbook;
class CeateAuthor(graphene.Mutation):
    class Arguments:
        name = graphene.String(required= True);
        address = graphene.String();
        id = graphene.String(required=True);
    authorDetails = graphene.Field(AuthorType);
    def mutate(self,info,name,address,id):
        print('@@@@@@@@@@@@@@@@@@@@@@@', info,name,address,id);
        authorDetails = author.objects.get(id=id);
        if authorDetails is not None:
            authorDetails.name = name;
            authorDetails.address = address;
            authorDetails.save();
            return CeateAuthor(authorDetails=authorDetails);
class UpdateAuthorMutation(graphene.ObjectType):
    updateAuthor = CeateAuthor.Field();
class CreateAirline(graphene.Mutation):
    class Arguments:
        name = graphene.String(required= True);
        type = graphene.String(required= True);
        id = graphene.String(required=True);
    airlineDetails = graphene.Field(AirlineType);
    def mutate(self,info,name,type,id):
        airlineDetails = airlines.objects.get(id=id);
        if airlineDetails is not None:
            airlineDetails.name = name;
            airlineDetails.type = type;
            return CreateAirline(airlineDetails= airlineDetails);
class UpdateAirlineMutation():
    updateAirline = CreateAirline.Field();


class Query(object):
    single_airline = graphene.Field(AirlineType, id=graphene.Int());
    single_author = graphene.Field(AuthorType, id=graphene.Int());
    single_cookbook = graphene.Field(CookbookType, id=graphene.Int());
    all_airlines = graphene.List(AirlineType);
    all_authors = graphene.List(AuthorType);
    all_cookbooks = graphene.List(CookbookType);
    def resolve_all_airlines(self,info,**kwargs):
        return airlines.objects.all();
    def resolve_all_authors(self,info,**kwargs):
        return author.objects.all();
    def resolve_all_cookbooks(self,info,**kwargs):
        return cookbook.objects.all();
    def resolve_single_author (self,info,**kwargs):
        id = kwargs.get('id');
        if id is not None:
            return author.objects.get(id=id);
        else:
            return 'no data found';
    def resolve_single_cookbook(self,info,**kwargs):
        id = kwargs.get('id');
        if id is not None:
            return cookbook.objects.get(id=id);
        else:
            return 'no data found';
    def resolve_single_airline(self,info,**kwargs):
        id = kwargs.get('id');
        if id is not None:
            return airlines.objects.get(id=id);
        else:
            return 'no data found';