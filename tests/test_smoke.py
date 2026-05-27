from src.infrastructure.llm.utils import model_schema_as_json
from src.infrastructure.llm.contracts.reading import ReadingGeneration


print(model_schema_as_json(ReadingGeneration))
print(ReadingGeneration.model_json_schema)

