<p align="center">
  <h3 align="center">Crowley scanner</h3>
  <p align="center">
    crowley-scan is a tool to search for targets in Google search engine.
  </p>

  <p align="center">
    <a href="https://twitter.com/bsd0x1">
      <img src="https://img.shields.io/badge/twitter-@bsd0x1-blue.svg">
    </a>
    <a href="https://www.gnu.org/licenses/gpl-3.0">
      <img src="https://img.shields.io/badge/License-GPLv3-blue.svg">
    </a>
    <a href="https://github.com/bsd0x/crowley-scan/releases">
      <img src="https://img.shields.io/badge/version-3.1.1-blue.svg">
    </a>
  </p>
</p>
<hr>

## Search engines supported

```
[+] Google
```

## Install requirements

```
pip install -r requirements.txt
```

## Usage

```
Usage: crowley.py [OPTIONS]

Options:
  --dork 
  --max_results 
  --timeout
  --threads
  --help
```

<hr>

## Docker

```
docker build -t crowley-scan .

docker run -it crowley-scan --dork "news.php?id="
```

<hr>

## Examples

```
python crowley.py --dork "news.php?id="
```

## Developer

```
[+] Gabriel Dutra A.K.A bsd0x
[+] root@bsd0x.me
[+] twitter.com/bsd0x1
```
