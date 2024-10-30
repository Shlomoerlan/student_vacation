from graphene import ObjectType

from app.gql.mutations.student_mutations import AddStudentVacation


class Mutation(ObjectType):
    add_student_vacation = AddStudentVacation.Field()