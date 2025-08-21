from api.lyrics import getLyrics

def album(data, syncpoints):
    info = {}
    attr = data["data"][0]["attributes"]

    name = attr["name"]

    __dir = "{0} - {1}".format(
        attr["artistName"],
        name,
        data["data"][0]["id"]
    )

    info["dir"] = __dir

    if "artwork" in attr:
        info["coverUrl"] = attr["artwork"].get("url").format(
            w=attr["artwork"].get("width"),
            h=attr["artwork"].get("height")
        )

    trackList = []
    tracks = data["data"][0]["relationships"]["tracks"]["data"]

    for track in tracks:
        __info = {}
        __info["id"] = track.get("id")
        
        attr = track["attributes"]

        if track.get("type") == "songs":
            __file = "{0}. {1}".format(
                str(attr.get("trackNumber")).zfill(2),
                attr.get("name")
            )

            __info["file"] = __file

            if "lyrics" in track["relationships"]:
                if len(track["relationships"]["lyrics"].get("data")) > 0:
                    __info["ttml"] = track["relationships"]["lyrics"]["data"][0]["attributes"].get("ttml")
                    __info.update(getLyrics(track["relationships"]["lyrics"]["data"][0]["attributes"].get("ttml"), syncpoints))

        trackList.append(__info)
        
    info["tracks"] = trackList

    return info