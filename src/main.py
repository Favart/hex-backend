from fastapi import FastAPI
from pydantic import BaseModel


from src.utils.password import password


class User(BaseModel):
    identifiant: str
    mdp: str
    nom: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/user/create/")
async def create(user: User):
    """
    Authentification de l'utilisateur.
    Args:
    id_user int: ID de l'utilisateur
    Return:
    infos dict: informations de l'utilisateur
    """
    return user


@app.get("/user")
async def authentification(identifiant: str = None, mdp: str = None):
    """
    Authentification de l'utilisateur.
    Args:
        id_user int: ID de l'utilisateur
    Return:
        infos dict: informations de l'utilisateur
    """
    infos = {
        "identifiant": identifiant,
        "mdp": password(mdp)
    }
    return infos


@app.get("/game/{taille}")
async def new(taille: int):
    """
    Génération d'un nouveau plateau de jeu.
    Args:
        taille int: taille du plateau de jeu
    Return:
        return dict: plateau de jeu
    """
    return {i+1: True for i in range(taille**2)}
