# Retrieval-Augmented Generation (RAG) System

This project implements a Retrieval-Augmented Generation (RAG) system using Python. It processes text data from various sources, including CSV files and PDFs, to create embeddings and store them in a vector store for efficient retrieval. The system leverages the `langchain` library for text splitting and embedding, and `Chroma` for vector storage.

## Key Features

- **Text Splitting**: Divides text into manageable chunks for embedding.
- **Embeddings**: Generates text embeddings using the nomic-embed-text model.
- **Vector Store**: Stores and retrieves embeddings using Chroma.
- **Interactive Q&A**: Allows users to ask questions and get responses based on the stored embeddings.

## Video Tutorials

- **Running LLMs on Laptop | Open Web UI for local ChatGPT like UI | Tools & Techniques - Edition 4**: [Watch on YouTube](https://youtu.be/qXHlnYXGaXI)
- **How I created Retrieval-Augmented Generation (RAG) using locally run LLM | Tools & Techniques - 5**: [Watch on YouTube](https://youtu.be/hylovClsMoo)

## Overview

The project is designed to facilitate efficient information retrieval and question answering from large text datasets. In this case it is about quering whether a video on a particular topic exists on YouTube channel. The pre-procedding of the data has already been done kept. That logic to prepare the data is not part of this codebase.

### PDF Parsing

Extracts text from PDF documents using the PyMuPDF library.

### Text Splitting

Divides large text data into manageable chunks to create effective embeddings.

### Embeddings

Generates text embeddings using the `nomic-embed-text` model for accurate and meaningful representations of the text data.

### Vector Store

Utilizes Chroma to store and retrieve embeddings, enabling efficient and fast searches within the text data.

### Interactive Q&A

Provides an interface for users to ask questions and receive responses based on the stored embeddings, enhancing the retrieval of relevant information from large text datasets.

## Pre-Conditions

1. **Ensure that Ollama is installed on your laptop.**
2. **Ensure `llama3` model is installed using Ollama.**
3. **Ensure that you install `nomic-embed-text` using Ollama.** Run the command:
   ```bash
   ollama run nomic-embed-text
   ```

## Installation

Install `pipenv` to add all the project dependencies.

To install packages using `pipenv`, follow these steps:

1. **Install `pipenv` if you haven't already:**
   ```bash
   pip install pipenv
   ```

2. **Create a `Pipfile` if you don't have one yet:**
   ```bash
   pipenv install
   ```

3. **Install the necessary packages using `pipenv`:**
   ```bash
   pipenv install <package-name>
   ```

This will add the packages to your `Pipfile` and create a `Pipfile.lock` to ensure reproducible builds.

## Example Commands

After running these commands, your `Pipfile` should include the installed packages, and you can use `pipenv shell` to activate the virtual environment.

## Development Environment

The project has been created in PyCharm. If you have PyCharm, you should be able to directly run this code much more easily.
