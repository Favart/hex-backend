import hashlib


def password(mdp: str):
    """
    Encodage du mot de passe de l'utilisateur
    Args:
        mdp str: mot de passe de l'utilisateur
    Return:
        return str: mot de passe encodé de l'utilisateur
    """
    mdp = hashlib.sha256(mdp.encode()).hexdigest()
    return str(mdp)
