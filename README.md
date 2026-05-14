````md
# YouTube Downloader

Downloader simples para vídeos e playlists do YouTube usando yt-dlp.

## Features

- Vídeos
- Playlists
- Áudio
- Resume automático
- Pausa com CTRL+C
- Continua downloads interrompidos
- Não precisa de ffmpeg

---

## Instalação

Instala o yt-dlp:

```bash
pip install yt-dlp
````

---

## Uso

### Vídeo

```bash
python yt_playlist_downloader.py "URL"
```

### Playlist

```bash
python yt_playlist_downloader.py "URL_DA_PLAYLIST"
```

### Apenas áudio

```bash
python yt_playlist_downloader.py "URL" --audio
```

### Pasta personalizada

```bash
python yt_playlist_downloader.py "URL" --output videos
```

---

## Pausar

Durante o download:

```text
CTRL + C
```

O progresso fica salvo automaticamente.

---

## Continuar

Executa novamente o mesmo comando:

```bash
python yt_playlist_downloader.py "URL"
```

---

## Estrutura

```text
.
├── yt_playlist_downloader.py
└── downloads/
```

---

## Windows

Se `python` não funcionar:

```bash
py yt_playlist_downloader.py "URL"
```

---

## Linux

Pode ser necessário usar:

```bash
python3 yt_playlist_downloader.py "URL"
```

---

## Dependência

* yt-dlp

---

## Licença

MIT

```
```
