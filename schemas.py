from pydantic import BaseModel


class UserIn(BaseModel):
    name: str
    email: str

    def __repr__(self) -> str:
        return f'UserIn({self.name})'


class User(BaseModel):
    id: str
    email: str
    name: str

    def __repr__(self) -> str:
        return f'User({self.name})'

    class Config:
        orm_mode = True
