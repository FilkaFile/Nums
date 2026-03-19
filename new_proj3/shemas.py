from pydantic import BaseModel


class CompanyBase(BaseModel):
    name: str


class CompanyCreate(CompanyBase):
    pass


class CompanyResponse(CompanyBase):
    id: int

    class Config:
        from_attributes = True


class PersonBase(BaseModel):
    name: str
    age: int


class PersonCreate(PersonBase):
    company_id: int


class PersonResponce(PersonBase):
    id: int
    company: CompanyResponse

    class Config:
        from_attributes = True
