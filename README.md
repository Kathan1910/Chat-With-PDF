# Chat with PDF

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue.svg)](https://www.python.org/downloads/release)

## Table of Contents

- [About](#about)
- [Demo](#demo)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

- [Acknowledgments](#acknowledgments)

## About

"Chat with PDF" is a project that provides two Streamlit web applications for interacting with PDF documents using different AI models. The project explores the capabilities of the OpenAI API and Google's PAML (Papers with Code AutoML) API to enable natural language interactions with PDF content.




## Features

- **OpenAI Chat**: Use the OpenAI API to chat with the contents of a PDF document.
- **Google PALM Chat**: Utilize Google's PAML API to have natural conversations about a PDF document.
- **Generative AI PDF**: Examine the Jupyter Notebook `generative_ai.ipynb` to explore generative AI techniques applied to PDF content.
- **Requirements File**: A `requirements.txt` file is provided for easy environment setup.

## Getting Started

These instructions will help you set up the project on your local machine.

### Prerequisites

- Python 3.7+ installed on your system.
- [OpenAI API Key](link_to_openai_api_key) (for the OpenAI Chat application).
- [Google PALM API Key](link_to_google_paml_api_key) (for the Google PAML Chat application).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Kathan1910/Chat-With-PDF.git

2. Install the required packages:

    ```bash
    pip install -r requirements.txt

###  Usage

- streamlit run app1.py


## Generative AI PDF (Jupyter Notebook)

Explore the `generative_ai.ipynb` Jupyter Notebook to experiment with generative AI techniques applied to PDF documents.

## Project Structure

- `openai_app.py`: Streamlit app for interacting with PDF using the OpenAI API.
- `google_paml_app.py`: Streamlit app for conversational interactions with PDF using Google PAML.
- `generative_ai.ipynb`: Jupyter Notebook for experimenting with generative AI on PDFs.
- `requirements.txt`: List of project dependencies.

## Acknowledgments

- Thanks to [OpenAI](https://openai.com) for providing their powerful language models.
- Thanks to [Google PALM](https://google.com/paml) for enabling AI-powered document interactions.
