###AI Unit Testing for Angular using Private LLM (Qwen-0.5-Coder)
Overview

This project provides an AI-powered unit testing framework for Angular applications using a privately hosted Large Language Model (LLM) based on Qwen-0.5-Coder (0.5B). The model is fine-tuned on custom Angular source code and corresponding unit test datasets to automatically generate high-quality Jasmine/Karma test cases.

The system is designed for secure, offline, and enterprise environments where source code confidentiality is a priority. All inference and fine-tuning operations are performed locally or within private infrastructure, with no dependency on external cloud-based AI services.

Key Features

Automated unit test generation for Angular applications

Private LLM deployment using Qwen-0.5-Coder

Fine-tuned model trained on Angular-specific code and tests

Generates Jasmine/Karma-compatible test files

Supports components, services, pipes, and guards

Offline and secure execution

CI/CD-friendly and extensible architecture

Architecture

Angular source files are parsed and preprocessed

Relevant code context is extracted and structured

Context is passed to the fine-tuned Qwen-0.5-Coder model

Unit test files are generated following Angular testing best practices

Tests are validated and formatted for execution

Model Information

Base Model: Qwen-0.5-Coder (0.5B parameters)

Fine-Tuning Approach: Supervised fine-tuning (SFT)

Training Data: Angular code and corresponding Jasmine/Karma tests

Inference Mode: Local or private cloud deployment

Technology Stack

Angular

TypeScript

Jasmine

Karma

Python

Hugging Face Transformers

Qwen-0.5-Coder

Setup Instructions
Prerequisites

Node.js (v16 or later)

Python (v3.9 or later)

Angular CLI

Git
