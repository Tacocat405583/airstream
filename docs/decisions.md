# Decision Log

A running record of what I've built, what I chose, and why. Newest entries at the top.

**Template**

```
## YYYY-MM-DD - Short title
**Context:** what problem or question came up
**Decision:** what I chose
**Alternatives:** what else I considered
**Why:** the reasoning
**Result / numbers:** what happened, anything measured (fill in later)
```

---

## Progress

- [x] Repo scaffold: packaging, CI, tests, README (2026-10-22)
- [ ] OpenSky: get a token
- [ ] OpenSky: bounding-box query + save raw snapshots
- [ ] OpenSky: study the response (null rates, update frequency, credit cost)
- [ ] Parse state vectors into `FlightState` + tests against a saved snapshot
- [ ] Data quality checks based on what the data actually showed
- [ ] Kafka streaming layer
- [ ] Join flights to NWS weather
- [ ] Live map + pipeline-health dashboard
- [ ] Extension: GOES wildfire smoke segmentation

## Open questions

- How many API credits does polling a SoCal box every N seconds cost per day?
- Which state-vector fields are null often enough to matter?
- Partition key for flight topics: `icao24`? Something else?
- How do I join fast-moving flight data to slower-updating hourly weather?

---

## 2026-10-22 - Build the streaming layer myself
**Context:** The initial scaffold included Kafka producer/consumer stubs and a docker-compose file.
**Decision:** Removed them. I'll design and build the streaming layer from scratch.
**Why:** It's the core of the project and the part I most want to be able to explain in depth.

## 2026-10-22 - Start with OpenSky before NWS
**Context:** Two data sources to integrate.
**Decision:** Build the OpenSky client first.
**Why:** It's the more constrained API (OAuth2 tokens that expire after 30 min, credit limits),
so its limits will shape the polling design. NWS has no auth and is easier to add later.

## 2026-10-22 - OAuth2 client credentials for OpenSky
**Context:** OpenSky dropped username/password basic auth.
**Decision:** Use the client credentials flow and write my own token handling instead of the
official Python client.
**Alternatives:** Official `opensky-api` client, which handles token refresh automatically.
**Why:** Handling token fetching, caching, and expiry myself is worth learning and explaining.

## 2026-10-22 - Limit queries to a SoCal bounding box
**Context:** `/states/all` with no box returns the whole world.
**Decision:** Query a Southern California box (lamin/lomin/lamax/lomax).
**Why:** Fewer API credits, smaller payloads, and it fits the project question about how weather
and wildfire smoke affect air traffic over SoCal.
