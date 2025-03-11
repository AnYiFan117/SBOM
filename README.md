# SBOM

Generating SBOM

# Setup before start

The project is based on CycloneDX SBOM format.

Support languages: **Python, Golang, Java**

Things you must do before start:

1. Install requirements based on your language.
    - **Python**: run `pip install cyclonedx-bom` in your project directory.
    - **Java**: make sure you have maven in your environment.
    - **Golang**: make sure you have go in your environment and run `go install github.com/ozonru/cyclonedx-go/cmd/cyclonedx-go@latest`
2. Install requirements of this project: `pip install -r requirements.txt`

# Run SBOM generation in CLI

go to /src and run `python main.py [project_directory] --language=[language]`

The result will be in your project directory with the name `sbom.json`.
