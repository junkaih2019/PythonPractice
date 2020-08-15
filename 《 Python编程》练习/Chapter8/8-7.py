def make_album(singer_name, ablbum_name, song_num = 0):
    if song_num == 0:
        album = {'singer': singer_name, 'ablbum_name': ablbum_name}
    else:
        album = {'singer': singer_name, 'ablbum_name': ablbum_name, 'song_num': song_num}
    return album


print(make_album('a', 'a'))
print(make_album('b', 'b', song_num= 5))
print(make_album('c', 'c'))
