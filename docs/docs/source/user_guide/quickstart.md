---
jupytext:
  formats: md:myst
  text_representation:
    format_name: myst
    extension: .md
    format_version: '0.13'
    jupytext_version: '1.13.0'
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Quick Start Guide

Get started with {{ cookiecutter.project_name }} in minutes!

## Basic Usage

Here's a simple example:

```python
from {{ cookiecutter.project_slug }} import MyClass

# Create an instance
obj = MyClass()

# Do something cool
result = obj.process_data("example")
print(result)
```

## Using with Jupyter Notebooks

You can use {{ cookiecutter.project_name }} in Jupyter notebooks:

```{code-cell} ipython3
import {{ cookiecutter.project_slug }}

# Your code here
```

## Advanced Features

### Feature 1: Data Processing

```python
# Example of data processing
data = [1, 2, 3, 4, 5]
processed = process_data(data)
```

### Feature 2: Visualization

You can create diagrams using Mermaid:

```{mermaid}
graph TD
    A[Start] --> B{Process Data?}
    B -- Yes --> C[Process]
    B -- No --> D[Skip]
    C --> E[End]
    D --> E
```

## Configuration

Use a configuration file or environment variables:

```yaml
# config.yaml
api_key: your_api_key
max_items: 100
debug: true
```

## Next Steps

- Check out the [API Reference](../api/index) for detailed documentation