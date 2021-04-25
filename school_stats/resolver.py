from .models import School
from ariadne import QueryType, make_executable_schema, MutationType
type_defs = """

type Query{
    all_schools: [School]
}

type School {
    id: ID
    school_name: String!
    school_population: Int!

}
type Mutation{
    add_school(input: SchoolInput): SchoolResults

}
input SchoolInput {
    school_name: String
    school_population: Int
}
  type SchoolResults {
        created: Boolean!
        school: School
        err: String
}

"""
query = QueryType()
@query.field('all_schools')
def resolve_schools(*_):
    return School.objects.all()

mutation = MutationType()
@mutation.field('add_school')
def resolve_add_school(_, info, input):
    print("Invoked the mutations")
    print(input)
    school = School.objects.create(
        school_name=input['school_name'], school_population=input['school_population'])
    return {'created': True, 'school': school, 'err': None}




schema = make_executable_schema(type_defs, query, mutation)