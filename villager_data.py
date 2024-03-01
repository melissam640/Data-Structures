"""Functions to parse a file containing villager data."""

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    filename = open(filename)

    species = set()

    # TODO: replace this with your code
    for line in filename:
        line = line.rstrip()
        words = line.split("|")
        
        species.add(words[1])



    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    filename = open(filename)

    villagers = []

    for line in filename:
        line = line.rstrip()
        words = line.split("|")
        
        if search_string == "All":
            villagers.append(words[0])
        else:
            if words[1] == search_string:
                villagers.append(words[0])
      

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    filename = open(filename)

    fitness_list = []
    nature_list = []
    education_list = []
    music_list = []
    fashion_list = []
    play_list = []
    final_list = [fitness_list, nature_list, education_list, music_list, fashion_list, play_list]
    
    for line in filename:
        line = line.rstrip()
        words = line.split("|")
        
        if words[3] == "Fitness":
            fitness_list.append(words[0])
        elif words[3] == "Nature":
            nature_list.append(words[0])
        elif words[3] == "Education":
            education_list.append(words[0])
        elif words[3] == "Music":
            music_list.append(words[0])
        elif words[3] == "Fashion":
            fashion_list.append(words[0])
        else:
            play_list.append(words[0])


    return final_list


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
    filename = open(filename)

    all_data = []

    for line in filename:
        line = line.rstrip()
        words = tuple(line.split("|"))
        all_data.append(words)

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    filename = open(filename)

    for line in filename:
        line = line.rstrip()
        words = line.split("|")

        if villager_name == words[0]:
            result = words[4]
        else:
            result = None

    return result


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    
    filename = open(filename)

    like_minded_animals = set()
    
    villager_personality = None
    for line in filename:
        line = line.rstrip()
        words = line.split("|")

        if villager_name == words[0]:
            villager_personality = words[2]
            break

    if villager_personality:
        for line in filename:
            line = line.rstrip()
            words = line.split("|")

            if words[2] == villager_personality: 
                like_minded_animals.add(words[0])
        
    return like_minded_animals