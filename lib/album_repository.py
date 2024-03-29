from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM albums')
        albums = []
        for row in rows:
            album = Album(row['id'], row['title'], row['release_year'], row['artist_id'])
            albums.append(album)
        return albums

    def add_album(self, album):
        self.connection.execute(
            'INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)',
            [album.title, album.release_year, album.artist_id]
            )
    
    def find(self, album_id):
        rows = self.connection.execute(
            'SELECT * FROM albums WHERE albums.id = %s',
            [album_id]
            )
        row = rows[0]
        return Album(row['id'], row['title'], row['release_year'], row['artist_id'])
    
    def get_artist_name(self, album_id):
        rows = self.connection.execute(
            '''SELECT artists.name 
            FROM albums JOIN artists 
            ON artists.id = albums.artist_id 
            WHERE albums.id = %s''',
            [album_id]
            )
        row = rows[0]
        return row['name']
