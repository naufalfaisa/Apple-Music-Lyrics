# Apple-Music-Lyrics

Fetch lyrics from Apple Music tracks and albums.

## Feature

- Download plain text lyrics (.txt)
- Download time-synced lyrics (.lrc)

## Required

- [MP4Box](https://gpac.wp.imt.fr/mp4box/) must be installed

## Usage

```bash
python main.py <options> <url>
```
## Options

| Flag | Description |
| --- | --- |
| `-h`, `--help` | Show this help message and exit |
| `-v`, `--version` | Show program version |
| `-s`, `--sync` | Save timecodes in `00:00.000` format (three ms points) |
| `--no-txt` | Don't save lyrics as a `.txt` file |
| `--no-lrc` | Don't save time-synced lyrics as a `.lrc` file |
| `url` | Apple Music URL for an album or a song |

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
