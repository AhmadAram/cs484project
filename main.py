import pickle
import pylast
import pandas
import numpy
# import pyechonest


def preprocess_users(x=None):
    """
    This method accepts optional parameter x to specify an amount of user data to pre-process.
    This builds a basic list of the user IDs and saves them using the pickle library.

    :param x: Int - default None
    """
    with open("assets/train_triplets.txt", "r") as infile:
        if x is None:
            users = [x.split()[1] for x in infile]
        else:
            n = 0
            users = []
            for line in infile:
                if n == x:
                    break
                users.append(line.split()[0])
                n += 1
    with open('assets/pickle_dumps/users.dat', 'wb+') as outfile:
        pickle.dump(users, outfile)


def load_data(file):
    """
    Loads the pickle data that was pre-processed.

    :param file: String - pre-processed file name
    :return:
    """
    with open('assets/pickle_dumps/' + file, 'rb') as infile:
        return pickle.load(infile)


def main():
    preprocess_users(100)
    print(load_data('users.dat'))
    # API_KEY = "55b31ae7d1992d0523876c1a27b86d80"
    # API_SECRET = "4746d5e29db93c379645934051aef021"
    #
    # username = "deathfire260"
    # password_hash = pylast.md5("kopzub-cihrux-0hoKji")
    #
    # network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
    #                                username=username, password_hash=password_hash)
    #
    # artist = network.get_artist("Mastodon")
    # # print(artist.get_top_albums())
    # # print(artist.get_top_tags())
    # # print(artist.get_top_tracks())
    # # print(artist.get_similar())
    # [print("{}\n".format(x)) for x in artist.get_top_albums()[0]]
    # [print("{}\n".format(x)) for x in artist.get_top_tags()[0]]
    # [print("{}\n".format(x)) for x in artist.get_top_tracks()[0]]
    # [print("{}\n".format(x)) for x in artist.get_similar()[0]]
    #
    # artist = network.get_artist("Paganini")
    # # print(artist.get_top_albums())
    # # print(artist.get_top_tags())
    # # print(artist.get_top_tracks())
    # # print(artist.get_similar())
    # [print("{}\n".format(x)) for x in artist.get_top_albums()[0]]
    # [print("{}\n".format(x)) for x in artist.get_top_tags()[0]]
    # [print("{}\n".format(x)) for x in artist.get_top_tracks()[0]]
    # [print("{}\n".format(x)) for x in artist.get_similar()[0]]


if __name__ == "__main__":
    main()
