# http-tape-deck

A tiny wrapper around mitmproxy designed to help record and play a browsing session for more repeatable performance testing.

## Usage

```
# (once)
brew install mitmproxy
mitmproxy
# (configure your browser to use localhost:8080 as a proxy)
# (navigate to mitm.it and follow instructions to install certificate)

# (every time)
./record.sh your-project-name
# do some browsing, then kill record.sh
./play.sh your-project-name
# do some browsing, responses will be played back from your-project-name.tape
```