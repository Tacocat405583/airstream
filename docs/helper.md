# Helper: How to Code From Documentation

A lot of coding is reading docs and adapting their examples. What experienced developers have
is a repeatable process for doing it. This is that process, plus the docs this project needs.

---

## The process

1. **Find the official example.** Almost every API doc has a working example, often in `curl`.
   Copy it.
2. **Run it raw first, before writing any Python.** Paste the `curl` command into your terminal
   with your credentials. If it works, your credentials and URL are right. If it fails, at
   least you know the problem isn't your Python.
3. **Translate it to Python.** Every `curl` flag maps to an argument in an HTTP library (see the
   table below).
4. **Print everything and look at it.** `print(response.status_code)`, `print(response.json())`.
   Experiment in the Python REPL (type `python` in the terminal) to poke at the response
   interactively.
5. **Only once it works, organize it.** A loose script becomes a function, then a class. Design
   comes after you understand the behavior. This is the step that builds OOP skill.
6. **When it breaks, read the error slowly.** The last line usually says exactly what's wrong.
   Search for the exact error text.

**Always get something working first, then improve it.**

---

## curl to Python cheat sheet

| curl | Python (`requests` / `httpx`) |
| --- | --- |
| `-X POST` | `requests.post(...)` |
| `-X GET` (default) | `requests.get(...)` |
| `-H "Authorization: Bearer X"` | `headers={"Authorization": "Bearer X"}` |
| `-d "a=1&b=2"` (form data) | `data={"a": "1", "b": "2"}` |
| `-d '{"a": 1}'` with a JSON header | `json={"a": 1}` |
| `?lamin=32.5&lomin=...` in the URL | `params={"lamin": 32.5, ...}` |
| `-u user:pass` | `auth=("user", "pass")` |

## HTTP status codes you'll see

| Code | Meaning | Usually means |
| --- | --- | --- |
| 200 | OK | It worked |
| 400 | Bad Request | Wrong or missing parameters |
| 401 | Unauthorized | Bad or expired credentials / token |
| 403 | Forbidden | Credentials fine, but no access to this |
| 404 | Not Found | Wrong URL |
| 429 | Too Many Requests | Rate limited / out of credits. Slow down |
| 5xx | Server Error | Their problem. Retry later |

---

## Docs for this project, in the order you'll need them

### Now: the OpenSky client
- **OpenSky REST API:** https://openskynetwork.github.io/opensky-api/rest.html
  Read the authentication section and "All State Vectors." The state vector field table is
  your guide to the response.
- **OAuth2 client credentials, explained simply:**
  https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/
  Explains *why* the token step exists.
- **An HTTP library.** Pick one:
  - `requests`: https://requests.readthedocs.io/en/latest/user/quickstart/
    Simplest, with the most examples online.
  - `httpx`: https://www.python-httpx.org/quickstart/
    Works almost the same and also supports async.

### Python OOP and design (for interviews)
- **Python classes tutorial:** https://docs.python.org/3/tutorial/classes.html
- **dataclasses:** https://docs.python.org/3/library/dataclasses.html
  Useful for records like a flight.
- **Real Python OOP guide:** https://realpython.com/python3-object-oriented-programming/
  Friendlier than the official docs.

### Testing
- **pytest getting started:** https://docs.pytest.org/en/stable/getting-started.html

### Later
- **NWS API:** https://www.weather.gov/documentation/services-web-api
- **Kafka basics:** https://developer.confluent.io/what-is-apache-kafka/
- **Kafka Python client:** https://docs.confluent.io/kafka-clients/python/current/overview.html

---

## Tips for reading docs

- **Read the quickstart, not the whole thing.** Use the full reference only to look things up.
- **Skim first, then read closely.** First pass: what can this do? Second pass: the one section
  you need right now.
- **Use a scratch file** (like `scratch.py`, kept out of git) to try things before they go into
  your real code.
- **Write down what surprised you** in `docs/decisions.md`. Those notes become interview stories.

---

## Concepts quick reference

- **NWS:** National Weather Service. Free US weather API at `api.weather.gov`.
- **Observation:** actual measured weather from a station (often at an airport, e.g. KLAX), as
  opposed to a forecast.
- **Kafka:** a holding area for messages, split into named channels called **topics**.
- **Producer:** a program that *writes* messages into a Kafka topic.
- **Consumer:** a program that *reads* messages from a Kafka topic and does something with them.
- **Raw / clean / quarantine topics:** raw holds everything exactly as fetched. The validator
  sends good records to clean and bad ones to quarantine, where they're kept and counted, never
  silently dropped.

```
OpenSky API -> client -> producer -> [flights.raw] -> validator -> [flights.clean] -> storage -> map
                                                                \-> [flights.quarantine]
```

---

## Next concrete step

Once you have OpenSky credentials, get the token `curl` command from the OpenSky docs working
in your terminal. Do that before writing any Python.
