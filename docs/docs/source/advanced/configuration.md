# Advanced Configuration

Learn about advanced configuration options in {{ cookiecutter.project_name }}.

## Environment Variables

You can configure {{ cookiecutter.project_name }} using environment variables:

```{note}
All environment variables should be prefixed with `{{ cookiecutter.project_slug.upper() }}_`
```

| Variable | Description | Default |
|----------|-------------|---------|
| `{{ cookiecutter.project_slug.upper() }}_DEBUG` | Enable debug mode | `False` |
| `{{ cookiecutter.project_slug.upper() }}_LOG_LEVEL` | Logging level | `INFO` |

## Using Type Hints

{{ cookiecutter.project_name }} uses type hints extensively:

```python
from typing import List, Optional
from dataclasses import dataclass

@dataclass
class Config:
    debug: bool = False
    log_level: str = "INFO"
    max_retries: Optional[int] = None
    allowed_types: List[str] = ["A", "B", "C"]
```

{% if cookiecutter.use_pydantic == 'y' %}
## Pydantic Models

We use Pydantic for data validation:

```python
from pydantic import BaseModel, Field

class ServerConfig(BaseModel):
    host: str = Field(
        default="localhost",
        description="Server hostname"
    )
    port: int = Field(
        default=8000,
        ge=1024,
        le=65535,
        description="Server port number"
    )
    debug: bool = Field(
        default=False,
        description="Enable debug mode"
    )
```
{% endif %}

## Custom Components

You can create custom components using our extension system:

```python
from {{ cookiecutter.project_slug }} import Component

class MyCustomComponent(Component):
    def __init__(self, name: str):
        self.name = name
    
    def process(self, data: dict) -> dict:
        # Custom processing logic
        return data
```

## Performance Tuning

Here's a table of performance settings:

| Setting | Impact | Recommended Value |
|---------|--------|------------------|
| Cache Size | Memory usage | 1000 |
| Workers | CPU usage | CPU count |
| Batch Size | Processing speed | 100 |
