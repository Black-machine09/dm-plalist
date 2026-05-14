import argparse
import os
import sys
import time

try:
    import yt_dlp 
except ImportError:
    print("Instala o yt-dlp:")
    print("pip install yt-dlp")
    sys.exit(1)


def progress(d):
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "").strip()
        speed = d.get("_speed_str", "")
        eta = d.get("_eta_str", "")

        print(
            f"\r{percent} | {speed} | ETA {eta}",
            end="",
            flush=True
        )

    elif d["status"] == "finished":
        print(f"\nOK -> {os.path.basename(d['filename'])}")


def get_opts(args):
    os.makedirs(args.output, exist_ok=True)

    opts = {
        "outtmpl": os.path.join(
            args.output,
            "%(playlist_index)s - %(title)s.%(ext)s"
        ),

        "ignoreerrors": True,
        "continuedl": True,
        "nopart": False,

        "retries": 10,
        "fragment_retries": 10,

        "socket_timeout": 30,

        "progress_hooks": [progress],
    }

    if args.audio:
        opts["format"] = (
            "bestaudio[ext=m4a]/"
            "bestaudio[ext=webm]/"
            "bestaudio"
        )
    else:
        opts["format"] = "best[ext=mp4]/best"

    return opts


def show_info(url):
    try:
        with yt_dlp.YoutubeDL({
            "quiet": True,
            "extract_flat": True
        }) as ydl:

            info = ydl.extract_info(url, download=False)

            if not info:
                return

            title = info.get("title", "Playlist")
            entries = info.get("entries", [])

            print(f"\n{title}")
            print(f"{len(entries)} vídeos\n")

    except:
        pass


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("url")
    parser.add_argument("--audio", action="store_true")
    parser.add_argument(
        "--output",
        default="downloads"
    )

    args = parser.parse_args()

    print("\nYouTube Downloader\n")

    print("URL:", args.url)
    print("Modo:", "audio" if args.audio else "video")
    print("Destino:", os.path.abspath(args.output))

    print("\nCTRL+C para pausar\n")

    show_info(args.url)

    start = time.time()

    try:
        with yt_dlp.YoutubeDL(get_opts(args)) as ydl:
            ydl.download([args.url])

    except KeyboardInterrupt:
        print("\nPausado")
        sys.exit(0)

    except yt_dlp.utils.DownloadError as e:
        print("\nErro:", e)
        sys.exit(1)

    print(f"\nConcluído em {time.time() - start:.1f}s")


if __name__ == "__main__":
    main()