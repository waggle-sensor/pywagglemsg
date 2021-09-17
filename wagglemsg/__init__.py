import base64
import json
from typing import NamedTuple, Any, Dict


class Message(NamedTuple):
    """Message contains message data."""
    name: str
    value: Any
    timestamp: int
    meta: Dict[str, str]


def dump(msg: Message) -> bytes:
    """dump serializes a Message object."""
    payload = {
        "name": msg.name,
        "ts": msg.timestamp,
        "meta": msg.meta,
    }

    # binary data is encoded to base64 by default. all other
    # data is shipped as-is for now.
    if isinstance(msg.value, (bytes, bytearray)):
        payload["enc"] = "b64"
        payload["val"] = base64.b64encode(msg.value).decode()
    else:
        payload["val"] = msg.value

    return json.dumps(payload, separators=(",", ":"))


def load(body: bytes) -> Message:
    """dump deserializes a Message object."""
    data = json.loads(body)

    if data.get("enc") == "b64":
        data["val"] = base64.b64decode(data["val"])

    return Message(
        name=data["name"],
        value=data["val"],
        timestamp=data["ts"],
        meta=data["meta"])
