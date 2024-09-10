# FastAPI Project

This is a FastAPI project with a basic structure, including a simple API and tests.

## Setup

1. Create the Conda environment:
    ```
    conda env create -f environment.yml
    ```

2. Activate the Conda environment:
    ```
    conda activate aint
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run the application:
    ```
    uvicorn app.main:app --reload
    ```

5. Run tests:
    ```
    pytest
    ```

## Jenkins

A Jenkinsfile is provided for CI/CD integration. Configure your Jenkins pipeline to use the provided `Jenkinsfile`.
