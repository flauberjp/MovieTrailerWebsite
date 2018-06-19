import fresh_tomatoes
import media

abraao_honorio = media.Movie("Abraão Honório",
                        181,
                        "An ex-hitman comes out of retirement to track down " +
                        "the gangsters that took everything from him. With " +
                        "New York City as his bullet-riddled playground, " +
                        "JOHN WICK (Keanu Reeves) is a fresh and stylized " +
                        "take on the 'assassin genre'.",
                        "./img/getToKnow/abraao_honorio.jpg",
                        "https://youtu.be/PWLVkNhBhQ8")
# print(john_wick.storyline)
flaviano_flauber = media.Movie("Flaviano Flauber",
                     221,
                     "On the lush alien world of Pandora live the Na'vi, " +
                     "beings who appear primitive but are highly evolved. " +
                     "Because the planet's environment is poisonous, " +
                     "human/Na'vi hybrids, called Avatars, must link to " +
                     "human minds to allow for free movement on Pandora. " +
                     "Jake Sully (Sam Worthington), a paralyzed former " +
                     "Marine, becomes mobile again through one such " +
                     "Avatar and falls in love with a Na'vi woman (Zoe " +
                     "Saldana). As a bond with her grows, he is drawn into " +
                     "a battle for the survival of her world.",
                     "./img/getToKnow/flaviano_flauber.jpg",
                     "https://youtu.be/2WjZu5oqgEc")
# print(avatar.storyline)
# avatar.show_trailer()
joffily_ferreira = media.Movie(
    "Joffily Ferreira",
    150,
    "300 spartans to defend their home land against the conqueror Xerxes " +
    "and his horde of millions soldiers",
    "./img/getToKnow/joffily_ferreira.jpg",
    "https://youtu.be/xCKzJWsef3M")
# the_300_spartans.show_trailer()

hugo_dantas = media.Movie(
    "Hugo Dantas",
    148,
    "Is a humam being determined by the DNA?",
    "./img/getToKnow/hugo_dantas.jpg",
    "https://youtu.be/ErSgzzVgTt0")

rafael_ferreira = media.Movie(
    "Rafael Ferreira",
    150,
    "Machines dominated the humans, transformed them in batteries, is that " +
    "true? Why we allowed it?",
    "./img/getToKnow/rafael_ferreira.jpg",
    "https://youtu.be/rDSVlGBRZaw")


anderson_lima = media.Movie(
    "Anderson Lima",
    94,
    "See how italian mafia works",
    "./img/getToKnow/anderson_lima.JPG",
    "https://youtu.be/CzRMBvbvmlE")


movies = [abraao_honorio, flaviano_flauber, joffily_ferreira, hugo_dantas, 
          rafael_ferreira, anderson_lima]


def main():
    """Funcao principal da aplicacao. """
    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    main()
