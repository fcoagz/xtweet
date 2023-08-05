import os
import requests
from cachetools import TTLCache

from xtweet.request import get_from_cache_or_api

class Media(object):
    def __init__(self, url: str, ttl=300, maxsize=1024) -> None:
        """
        Inicializa un objeto Tweet a partir de la URL de un tweet.

        Args:
            url (str): URL del tweet.
        """
        self.cache = TTLCache(maxsize, ttl)
        url = url.split('/')
        self.path = '/' + '/'.join(url[3:])
        self._tuit_info = None

    @property
    def tuit_info(self) -> dict:
            """
            Obtener la informacion del tweet.
            """
            if self._tuit_info is None:
                self._tuit_info = get_from_cache_or_api(self.cache, f"tuit_{self.path}", "https://api.vxtwitter.com" + self.path)
            return self._tuit_info
    
    @property
    def is_media(self) -> bool:
        return 'media_extended' in self.tuit_info and len(self.tuit_info['media_extended']) > 0

    def download_photo(self, fp: str = './', name_file: str = "image") -> None:
        """
        Descarga la primera imagen incluido en el tweet, si está disponible.

        Args:
            fp (str): Ruta del directorio en el que se guardará el video.
            name_file (str): Nombre del archivo en el que se guardará el video.
        """       
        if self.is_media:
            for i, media in enumerate(self.tuit_info["media_extended"]):
                if media["type"] == "image":
                    url_photo = media["url"]
                    response = requests.get(url_photo)
                    if response.status_code == 200:
                        with open(os.path.join(fp, f"{name_file}_{i}.jpg"), 'wb') as f:
                            f.write(response.content)
                    else:
                        raise requests.exceptions.HTTPError(f"No se pudo descargar la imagen {i}. Código de estado: {response.status_code}")

    def download_video(self, fp: str, name_file: str = "video") -> None:
        """
        Descarga el primer video incluido en el tweet, si está disponible.

        Args:
            fp (str): Ruta del directorio en el que se guardará el video.
            name_file (str): Nombre del archivo en el que se guardará el video.
        """
        if self.is_media:
            for i, media in enumerate(self.tuit_info["media_extended"]):
                if media["type"] == "video":
                    url_video = media["url"]
                    response = requests.get(url_video)
                    if response.status_code == 200:
                        with open(os.path.join(fp, f"{name_file}_{i}.mp4"), 'wb') as f:
                            f.write(response.content)
                    else:
                        raise requests.exceptions.HTTPError(f"No se pudo descargar el video {i}. Código de estado: {response.status_code}")