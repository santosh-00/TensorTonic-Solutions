import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    na = np.linalg.norm(a)
    nb = np.linalg.norm(b)
    c = float(np.dot(a, b))
    if na == 0 or nb == 0:
        return 0.0
    temp =  np.dot(a,b) / (na * nb)
    return float(np.clip(temp, -1.0, 1.0))
    
    
    pass