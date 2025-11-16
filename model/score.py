from sentence_transformers import SentenceTransformer, util
from .club import Club


class Embedding:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.cache = dict()

    def vectorize(self, phrase: str):
        index = phrase
        if index in self.cache:
            return self.cache[index]
        vector = self.model.encode(phrase)
        self.cache[index] = vector
        return vector


embedding = Embedding()


def cos_sim(p1: str, p2: str) -> float:
    v1 = embedding.vectorize(p1)
    v2 = embedding.vectorize(p2)
    return util.cos_sim(v1, v2)


def score(club: Club, user_input: list[str]) -> float:
    final_score = 0
    for label in club.labels:
        for phrase in user_input:
            final_score += cos_sim(label, phrase)

    return final_score / len(user_input) / len(club.labels)
