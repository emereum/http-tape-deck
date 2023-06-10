# http-tape-deck

A tiny wrapper around mitmproxy designed to help record and play a browsing session for more repeatable performance testing.

## Install

```
brew install emereum/tap/http-tape-deck

# configure your browser to use localhost:8080 as a proxy
# navigate to mitm.it and follow instructions to install certificate
```

## Usage

```
http-tape-deck record project-name
# do some browsing, then kill http-tape-deck

http-tape-deck play project-name
# do some browsing, responses will be played back from project-name.tape
```

## Notes

* `http-tape-deck` freezes time (by clobbering `new Date()`) and makes random APIs predictable by clobbering `Math.random()` and `crypto.getRandomValues()`.

* Browser extensions like [FoxyProxy](https://chrome.google.com/webstore/detail/foxyproxy-standard/gcknhkkoolaabfmlnjonogaaifnjlfnp) make switching between normal browsing and tape recording / playing easier.