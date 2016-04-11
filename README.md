# pastebin

[![Build Status](https://travis-ci.org/11mariom/pastebin.png)](https://travis-ci.org/11mariom/pastebin)

## Example

```bash
~ $ python pastebin/pastebin.py &
~ $ curl 127.0.0.1:5000/paste/ --data "Pierwsza wklejona pierdoła"
pasted to id: 1
~ $ curl 127.0.0.1:5000/paste/1
Pierwsza wklejona pierdoła
```
