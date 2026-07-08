import json

from pydantic import ValidationError

from benchmark.schema import Explanation


def validate_output(text: str):

    try:

        text = text.strip()

        text = text.removeprefix("```json")
        text = text.removeprefix("```")
        text = text.removesuffix("```")

        text = text.strip()

        data = json.loads(text)

        parsed = Explanation.model_validate(data)

        return True, parsed, None

    except (json.JSONDecodeError, ValidationError) as error:

        return False, None, str(error)