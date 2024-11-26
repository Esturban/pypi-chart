# PyPI Download Chart Generator

This action generates a download chart for a specified PyPI package and outputs it as an SVG file.

# What's new
Please refer to the release page for the latest release notes.

## Usage

```yaml
- uses: Esturban/pypi-chart@v1
  with:
    # The name of the PyPI package.
    package_name: ''
```

## Scenarios  

- [Generate and upload PyPI download chart](#generate-and-upload-pypi-download-chart)  
- [Generate and commit PyPI download chart to repository](#generate-and-commit-pypi-download-chart-to-repository)  
- [Generate PyPI download chart on a schedule](#generate-pypi-download-chart-on-a-schedule)  

### Generate and upload PyPI download chart  

This example generates a download chart for a specified PyPI package and uploads the SVG file as an artifact.  

```yaml
name: Generate PyPI Download Chart

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Generate PyPI Download Chart
        uses: Esturban/pypi-chart@v1
        with:
          package_name: your-package-name
      - name: Upload SVG
        uses: actions/upload-artifact@v3
        with:
          name: chart
          path: chart.svg

```

### Generate and commit PyPI download chart to repository

This example generates a download chart for a specified PyPI package and commits the SVG file to the repository.

```yaml
name: Generate and Commit PyPI Download Chart

on:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:

permissions:
  contents: write 

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3
      - name: Generate PyPI Download Chart
        uses: Esturban/pypi-chart@v1
        with:
          package_name: your-package-name
      - name: Commit and Push Changes
        uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: 'Update PyPI download chart'
          file_pattern: chart.svg
```

### Generate PyPI download chart on a schedule  

This workflow generates the chart and commits it back to the repository, updating the chart daily.

```yaml
name: Generate and Commit PyPI Download Chart

on:
  schedule:
    - cron: '0 0 * * *' 
  workflow_dispatch:

permissions:
  contents: write  

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3
      - name: Generate PyPI Download Chart
        uses: Esturban/pypi-chart@v1
        with:
          package_name: your-package-name
      - name: Commit and Push Changes
        uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: 'Update PyPI download chart'
          file_pattern: chart.svg

```


## License  

The scripts and documentation in this project are released under the MIT License.