from pydantic import BaseModel,EmailStr
from datetime import date
from typing import Optional
from datetime import datetime

class UsuarioCrear(BaseModel):
   # consecUser:str # NO va porque se genera automaticamente en la BD (trigger)
   nombre:str
   apellido:str
   userName:str
   fechaRegistro: date
   email : EmailStr
   celular : str
   imageUser : Optional[str] = None # aqui va la ruta de la imagen que se guarda en la carpeta images
   temaUser : Optional[str] = None # aqui va la ruta del tema 
   huellaUser :Optional[str] = None #ruta de una imagen de una huella del usuario

class UsuarioEditar(BaseModel):
   #Usu_consecUser  # NO va porque se genera automaticamente en la BD (trigger)
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    userName: Optional[str] = None
    celular: Optional[str] = None
    email: Optional[EmailStr] = None
    imageUser: Optional[str] = None
    temaUser : Optional[str] = None
    huellaUser :Optional[str] = None 


class ConfiUser (BaseModel):
    #consecUser:str -> es PK2  y FK de Usuario
    #nConfiUser:int -> es la PK1 
    #idPropiedad:str -> es FK de Propiedad
    estado:Optional[bool] = None
    valor:Optional[int] = None

class Propiedad (BaseModel):
    #idPropiedad -> es la PK
    #Pro_idPropiedad -> FK de propiedad
    descPropiedad: Optional[int] = None 
    valorDefecto: Optional[int] = None 
    valorPropiedad: Optional[str] = None 

class ConfiGrupo(BaseModel):
    #codGrupo -> es PK2 y FK de Grupo
    #nConfiGrupo -> es la PK
    #idPropiedad -> es FK de Propiedad
    estado:bool

class Grupo (BaseModel):
    #codGrupo:str -> es la PK
    #consecUser:str -> es FK de Usuario
    #Gru_codGrupo -> es FK de Grupo
    nomGrupo: str
    fechaRegGrupo: date
    imagGrupo: str # aqui va la ruta de la imagen que se guarda en la carpeta images

class GrupoEditar(BaseModel):
    #codGrupo:str -> es la PK
    #consecUser:str -> es FK de Usuario
    #Gru_codGrupo -> es FK de Grupo
    nomGrupo: Optional[str] = None 
    imagGrupo: Optional[str] = None  # aqui va la ruta de la imagen que se guarda en la carpeta images


class Mensaje (BaseModel):
    #consecUser:str -> PK3 FK de Usuario
    #Usu_consecUser: str ->PK2 FK de Usuario
    #consMensaje: str -> La PK1
    #Men_consecUser:str
    #Men_consMensaje:str -> FK de mensaje
    #codGrupo:str -> FK de Grupo
    fechaRegMen:date

class Contenido (BaseModel):
    #consecUser
    #Usu_consecUser
    #consMensaje
    #conseContenido
    #idTipoContenido
    #idTipoArchivo
    contenidoImag:str
    localizaContenido:str

class TipoContenido(BaseModel):
    #idTipoContenido
    descTipoContenido:str

class TipoArchivo(BaseModel):
    #idTipoArchivo
    descArchivo:str

class Ubicacion(BaseModel):
    #codUbica
    #codTipoUbica
    #Ubi_codUbica
    nomUbica:str

class TipoUbica(BaseModel):
    codTipoUbica:str
    descTipoUbica:str





