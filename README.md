# pywagglemsg

Tiny Python library for (de)serializing Waggle messages. Although this is a public module, it's
mostly geared towards building internal tools and services.

## Example

```python3
import wagglemsg

msg = wagglemsg.Message(
    name='env.temperature.htu21d',
    value=10,
    timestamp=1602704769215113000,
    meta={
        "device": "bme280",
    },
)

data = wagglemsg.dump(msg)

# ... send data over the network ....
```

## Protocol Description

This version of the protocol is very different than the previous Waggle binary
protocol. The main focus is now on having a simple wire format that can be extended
to support projects like Sage.

### Overview

Conceptually, the prototol encodes "tagged timeseries" by providing fields for:

* Timestamp - Time of measurement in nanoseconds.
* Name - Name of measurement.
* Value - Value of measurement.
* Meta - Key-value "tags" used to track metadata.

### Wire Format

The current wire format implementation is a JSON payload with fields:


* `ts`. nanoseconds since epoch (int64)
* `name`: name of measurement (string)
* `val`: value of measurement (any JSON encodable type)
* `meta`: metadata tags (map[str]str)
* `enc`: optional value encoding (either ommited or "b64" when binary encoded to base64)

We show a couple reference examples here.

```json
{
    "ts": 1613485750303896000,
    "name": "env.temp.htu21d",
    "val": 23.1,
    "meta": {
        "plugin": "metsense:1.0.3"
    }
}
```

```json
{
    "ts": 1613485750303896000,
    "name": "raw.htu21d",
    "val": "AQIDBA==",
    "meta": {
        "plugin": "metsense:1.0.3"
    },
    "enc": "b64"
}
```
