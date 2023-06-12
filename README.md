![http-tape-deck](tape_deck.png)

<p align="center">
    <img src="https://raw.githubusercontent.com/emereum/http-tape-deck/main/tape_deck.png"/><br />
    <kbd>brew install emereum/tap/http-tape-deck</kbd>
</p>

# http-tape-deck
![brew-test-bot](https://github.com/emereum/homebrew-tap/actions/workflows/tests.yml/badge.svg)

A little tool that intercepts and records a browsing session, then plays it back to you on demand.

`http-tape-deck` allows you to capture a production-like browsing session, serve it back locally to remove the variance introduced by network delays, then reintroduce repeatable network delays through your profiling tools (such as the throttling option in `devtools`).

This gives you the best of both worlds: It allows you to produce repeatable profiling data (i.e. low variance) as if testing locally, while also ensuring the page is behaving as if running in production.

## Install

```
brew install emereum/tap/http-tape-deck
```

On your first recording, you'll need to visit http://mitm.it and follow the instructions to install `mitmproxy's` HTTPS certificate.

## Usage

```
http-tape-deck record project-name
# configure your browser to use https://localhost:8080 as a proxy
# do some browsing, then kill http-tape-deck

http-tape-deck play project-name
# do some browsing, responses will be played back from project-name.tape
```

The key to making a reusable recording is to start recording and playback with an identical initial state. Depending on the page, this may include:

* Clearing your browser cache (or suspending it via `devtools > Network > Disable cache`)
* Using a new incognito tab (or otherwise deleting all local data via `devtools > Application > Storage > Clear site data`)
* Ensuring the page is always opened in the same window dimensions (or if you intend to play back in both desktop and mobile layouts, make sure you recorded in both those layouts, too.)
* Ensuring that if devtools was open during recording, that it's also open during playback.

### Recording `localhost`

Chrome has a built in blacklist that prevents `localhost` and `127.0.0.1` from being proxied. This can be bypassed but it's awkward to do. An easier solution is to `sudo -- sh -c "echo 127.0.0.1 local >> /etc/hosts"` and navigate to `http://local/`.

### Proxy Setup

When `http-tape-deck` is recording, it will start an https proxy on `https://localhost:8080`. Your browser will need to use this proxy and it can be configured with these settings:

* Proxy Host: `localhost`
* Proxy Port: `8080`
* Proxy Type: `HTTPS` (_not_ `SOCKS`)

### Security Considerations

`http-tape-deck` creates a repeatable browsing session by clobbering `new Date()`, `Math.random()`, and `crypto.getRandomValues()`. This means any client-side cryptographic algorithms will be even less secure than usual.

`http-tape-deck` records all server responses that pass through its proxy. This includes the response content, cookies, etc. Sharing `*.tape` files is not much different than sharing a saved Wireshark session. Guard these files carefully and delete them when no longer useful. To minimise the risk of recording personal data, close all other Chrome windows and tabs before recording.

A proxy-switching extension like [Proxy Switcher](https://chrome.google.com/webstore/detail/proxy-switcher-and-manage/onnfghpihccifgojkpnnncpagjcdbjod) makes switching between record/playback and normal browsing easier.

