# Getting Started

Welcome to {{ cookiecutter.project_name }}! This guide will help you get started with both local documentation development and CI/CD setup.

## Local Documentation Development

### Initial Setup

1. Install the documentation dependencies:
```bash
cd docs
pip install -r requirements.txt
```

### Live Development Server

For real-time preview of your documentation as you write:

```bash
# On Unix/Linux/Mac:
make live-html

# On Windows:
make.bat live-html
```

This will:
- Start a development server at http://localhost:8000
- Open your browser automatically
- Watch for changes and rebuild instantly
- Auto-reload your browser when changes are detected

### Building Documentation Manually

If you prefer to build the documentation manually:

```bash
# On Unix/Linux/Mac:
make html

# On Windows:
make.bat html
```

The built documentation will be in `_build/html/`.

## GitLab CI/CD Setup

### 1. Create `.gitlab-ci.yml`

Create a `.gitlab-ci.yml` file in your project root:

```yaml
image: python:3.8

variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.pip-cache"

cache:
  paths:
    - .pip-cache
    - .cache/pip
    - venv/

stages:
  - docs

# Job to build and deploy documentation
pages:
  stage: docs
  script:
    - python -m venv venv
    - source venv/bin/activate
    - pip install -r docs/requirements.txt
    - cd docs
    - make html
    - cd ..
    - mv docs/_build/html/ public/
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
```

### 2. Configure GitLab Pages

1. Go to your project's **Settings > Pages**
2. Your documentation will be available at:
   - `https://<username>.gitlab.io/<project-name>` (user/group pages)
   - `https://<group>.gitlab.io/<project-name>` (project pages)

### 3. Additional CI/CD Features

#### Build Preview for Merge Requests

Add this job to preview documentation changes in merge requests:

```yaml
docs-preview:
  stage: docs
  script:
    - python -m venv venv
    - source venv/bin/activate
    - pip install -r docs/requirements.txt
    - cd docs
    - make html
    - cd ..
    - mv docs/_build/html/ preview/
  artifacts:
    paths:
      - preview
    expire_in: 1 week
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
```

#### Quality Checks

Add documentation quality checks:

```yaml
docs-lint:
  stage: docs
  script:
    - python -m venv venv
    - source venv/bin/activate
    - pip install -r docs/requirements.txt doc8
    - doc8 docs/source
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
```

## Best Practices

1. **Version Control**:
   - Keep documentation close to code
   - Include documentation changes in your PRs
   - Use meaningful commit messages

2. **Writing Style**:
   - Use clear, concise language
   - Include code examples
   - Keep documentation up-to-date with code changes

3. **Organization**:
   - Use meaningful file names
   - Group related topics together
   - Maintain a clear hierarchy

## Next Steps

- Check out the [Quick Start Guide](quickstart) for using {{ cookiecutter.project_name }}
- Read about [Advanced Configuration](../advanced/configuration)
- Browse the [API Reference](../api/index)
