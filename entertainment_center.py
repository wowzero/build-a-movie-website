import media
import fresh_tomatoes

fate_zero = media.Moive("Fate Zero",
                        "assassin caster lancer rider berserker saber archer",
                        "https://myanimelist.cdn-dena.com/images/anime/2/73249.jpg",
                        "https://www.youtube.com/watch?v=hKoXqe2w6z0")
#print fate_zero.storyline
#fate_zero.show_trailer()

code_geass = media.Moive("Code Geass",
                        "After the war in the ruins of a Japanese city Lelouch vi Britannia then vows to his Japanese friend Suzaku Kururugi that he will one day obliterate Britannia.",
                        "https://myanimelist.cdn-dena.com/images/anime/5/50331.jpg",
                        "https://youtu.be/lvF19D7WemQ")

steins_gate = media.Moive("Steins;Gate",
                        "The story follows a group of students as they discover and develop technology that gives them the means to change the past.",
                        "https://upload.wikimedia.org/wikipedia/en/b/bb/Steins_gate_xbox360.jpg",
                        "https://youtu.be/SBQprWeOx8g")

movies = [fate_zero, code_geass, steins_gate]
fresh_tomatoes.open_movies_page(movies)
