def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    new_magicians = []
    for magician in magicians:
        new_name = magician + " the Great"
        new_magicians.append(new_name)
    return new_magicians

magician_name = ['a', 'b', 'c']
magician_name = make_great(magician_name)
show_magicians(magician_name)
