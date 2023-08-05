# xtweet
**xtweet** es una biblioteca que te permite interactuar de manera eficiente con la API de Twitter. Con ella, puedes obtener información detallada sobre tweets y medios de manera rápida y sencilla.

## Uso
La clase `Tweet` representa un tweet de Twitter y proporciona propiedades para acceder a la información del tweet.

```py
from xtweet import Tweet

tweet = Tweet(url)
```

### Propiedades
La clase Tweet proporciona las siguientes propiedades para acceder a la información del tweet:

- `date`: Fecha de publicación del tweet.
- `text`: Texto del tweet.
- `thumbnail_url`: URL de la miniatura de la primera imagen incluida en el tweet, si está disponible.
- `likes`: Número de me gusta del tweet.
- `replies`: Número de respuestas al tweet.
- `retweets`: Número de retweets del tweet.
- `tweet_id`: ID del tweet.
- `user_name`: Nombre del usuario que publicó el tweet.
- `user_screen_name`: Nombre de pantalla del usuario que publicó el tweet.

La clase `Media` representa los medios incluidos en un tweet y proporciona métodos para descargar imágenes y videos.

```py
from xtweet import Media

media = Media(url)
```

### Métodos
La clase `Media` proporciona los siguientes métodos para descargar imágenes y videos:

- `download_photo(fp, name_file)`: Descarga todas las imágenes incluidas en el tweet y las guarda en el directorio especificado por el argumento `fp` con un nombre de archivo que incluye un índice para distinguir entre las diferentes imágenes. El argumento opcional `name_file` especifica el nombre base del archivo.

- `download_video(fp, name_file)`: Descarga todos los videos incluidos en el tweet y los guarda en el directorio especificado por el argumento `fp` con un nombre de archivo que incluye un índice para distinguir entre los diferentes videos. El argumento opcional `name_file` especifica el nombre base del archivo.