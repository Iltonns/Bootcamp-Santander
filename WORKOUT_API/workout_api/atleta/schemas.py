from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat
from WORKOUT_API.workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", examples='Eleilton', max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", examples='123.456.789-00', max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", examples=32)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", examples=75)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", examples=1.71)]
    sexo: Annotated[str, Field(description="Sexo do atleta", examples='M', max_length=1)]
