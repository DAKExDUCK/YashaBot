from yandex_music import ClientAsync

from config import config


class YandexMusicClient:
    client:ClientAsync = None

    async def init():
        YandexMusicClient.client = await ClientAsync(token=config.Y_TOKEN).init()

    async def get_track(url):
        res = f"{url.split('/')[-1]}:{url.split('/')[-3]}"

        return (await YandexMusicClient.client.tracks( res ))[0]

    async def get_album(url):
        res = f"{url.split('/')[-1]}"

        return (await YandexMusicClient.client.albums_with_tracks( res ))

    async def get_tracks_ids_from_playlist(url:str) -> list[str]:
        """
        Args:
            url (str): URL of user's Playlist

        Returns:
            list[str]: List of "album_id:track_id"
        """
        uid = url.split('/')[-3]
        kind = url.split('/')[-1]

        data = (await YandexMusicClient.client.users_playlists( kind=kind, user_id=uid )).tracks

        tracks_ids = []

        for track in data:
            track = await track.fetch_track_async()
            track_id = track.track_id
            if ':' in track_id:
                tracks_ids.append( track_id )

        return tracks_ids
