def make_album(singer_name, ablbum_name, song_num = 0):
    if song_num == 0:
        album = {'singer': singer_name, 'ablbum_name': ablbum_name}
    else:
        album = {'singer': singer_name, 'ablbum_name': ablbum_name, 'song_num': song_num}
    return album

while True:
    print("Enter q to quit at any place.")
    s_name = input("Enter a singer's name:\n")
    if s_name.lower() == 'q':
        break
    a_name = input("Enter a album name:\n")
    if a_name.lower() == 'q':
        break
    album = make_album(s_name, a_name)
    print(album)
