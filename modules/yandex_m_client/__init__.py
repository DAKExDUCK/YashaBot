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

    async def get_playlist(url):
        res = f"{url.split('/')[-3]}:{url.split('/')[-1]}"
        
        return (await YandexMusicClient.client.playlists_list( res ))[0]
