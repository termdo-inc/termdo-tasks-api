from pydantic import BaseModel


def _to_camel_case(string: str) -> str:
    parts = string.split("_")
    return parts[0] + "".join(part.title() for part in parts[1:])


class BaseResponse(BaseModel):
    model_config = {
        "alias_generator": _to_camel_case,
    }
