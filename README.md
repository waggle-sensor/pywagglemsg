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
