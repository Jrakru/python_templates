# API Reference

This section provides detailed API documentation for {{ cookiecutter.project_name }}.

## Core API

```{eval-rst}
.. automodule:: {{ cookiecutter.project_slug }}.core
   :members:
   :undoc-members:
   :show-inheritance:
```

## Utilities

```{eval-rst}
.. automodule:: {{ cookiecutter.project_slug }}.utils
   :members:
   :undoc-members:
   :show-inheritance:
```

## Type Definitions

```{eval-rst}
.. automodule:: {{ cookiecutter.project_slug }}.types
   :members:
   :undoc-members:
   :show-inheritance:
```

## Examples

Here's a quick example of using the core API:

```python
from {{ cookiecutter.project_slug }} import Client

# Initialize the client
client = Client()

# Use the API
result = client.process_data({"key": "value"})
```

## API Versioning

We follow semantic versioning (MAJOR.MINOR.PATCH):

- MAJOR version for incompatible API changes
- MINOR version for new functionality in a backwards compatible manner
- PATCH version for backwards compatible bug fixes
