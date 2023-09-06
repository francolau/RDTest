from fastapi import FastAPI, status, HTTPException, Depends
from typing import Annotated
from config.auth import authenticate_user
from config.database import database
from config.database import Engine
from models.entity import entity, EntityIn, metadata

metadata.create_all(Engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def index():
    return {"msg": "Ir a /docs para utilizar el swagger"}

@app.get("/get_data/{id}", summary="Get entity by id", status_code=status.HTTP_200_OK, response_model=EntityIn)
async def get_entitie(id: int, credentials: Annotated[str, Depends(authenticate_user)]):
    """
    Obtiene una entidad por su ID.

    Args:
        id (int): El ID de la entidad que se desea obtener.
        user (str): El nombre de usuario autenticado.

    Returns:
        dict: Los datos de la entidad encontrada.

    Raises:
        HTTPException: Si no se encuentra ninguna entidad con el ID especificado, se genera un error con código de estado 404.
    """
    query = entity.select().where(entity.c.ID == id)
    RESPONSE = await database.fetch_one(query)

    if RESPONSE == None:
        raise HTTPException(status_code=404, detail="Entity not found")

    return RESPONSE

@app.post("/input/{my_target_field}", summary="Create entity with target field on uppercase", status_code=status.HTTP_201_CREATED)
async def create_entitie(my_target_field: str, entitie: EntityIn, credentials: Annotated[str, Depends(authenticate_user)]):
    """
    Crea una entidad con un campo de destino especificado. Si el campo de destino coincide con una propiedad de la entidad,
    convierte el valor de esa propiedad a mayúsculas. Luego, inserta la entidad en la base de datos y devuelve el ID del 
    registro creado.

    Args:
        my_target_field (str): El campo de destino especificado.
        entitie (EntityIn): Los datos de la entidad a crear.
        user (str): El nombre de usuario autenticado.

    Returns:
        id: Un diccionario que contiene el ID del registro creado.
    
    Raises:
        HTTPException: Si el campo de destino es 'my_numeric_field', se genera un error con código de estado 400.
                      Si el campo de destino no coincide con ninguna propiedad de la entidad, se genera un error con 
                      código de estado 404.
    """
    lowerField = my_target_field.lower()

    if lowerField in entitie.__dict__.keys():
        for prop in entitie.__dict__.keys():
            if lowerField == 'my_numeric_field':
                raise HTTPException(status_code=400, detail=f"{my_target_field} no es un campo válido para convertir a mayúscula")
    
            if lowerField == prop:
                setattr(entitie, prop, getattr(entitie, prop).upper()) # Setea el mayus en el objeto entitie cuando coincidan las keys
    else:
        raise HTTPException(status_code=404, detail=f"{my_target_field} no es un campo válido para convertir a mayúscula")
        
    query = entity.insert().values(field_1=entitie.field_1, author=entitie.author, description=entitie.description, my_numeric_field=entitie.my_numeric_field)
    last_record_id = await database.execute(query)
    result = await database.fetch_one("SELECT * FROM entity WHERE id = :id", values={"id": last_record_id})
    return result