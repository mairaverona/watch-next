import spacy

# Load spaCy language model
nlp = spacy.load("en_core_web_md")


def calculate_similarity(doc1, doc2):
    return doc1.similarity(doc2)


def recommend_movie_for_watched_movie(watched_description, movie_descriptions):
    watched_doc = nlp(watched_description)

    max_similarity = 0
    recommended_movie = None

    for movie, description in movie_descriptions.items():
        description_doc = nlp(description)
        similarity = calculate_similarity(watched_doc, description_doc)

        if similarity > max_similarity and movie != "Planet Hulk":
            max_similarity = similarity
            recommended_movie = movie

    return recommended_movie


# Read movie descriptions from movies.txt
movie_descriptions = {}
with open("movies.txt", "r") as file:
    for line in file:
        movie, description = line.strip().split(":", 1)
        movie_descriptions[movie.strip()] = description.strip()

# Description of "Planet Hulk" movie
watched_description = (
    "Will he save their world or destroy it? When the Hulk becomes too dangerous..."
)

# Recommend the next movie to watch
recommended_movie = recommend_movie_for_watched_movie(
    watched_description, movie_descriptions
)

print("Recommended movie:", recommended_movie)
