from pydantic import BaseModel


class SzobaTipusCreate(BaseModel):
    megnevezes: str
    napi_ar: int
    fekvohelyek_szama: int
    leiras: str
