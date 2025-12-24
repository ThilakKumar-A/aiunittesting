AI Unit Testing for Angular using Private LLM (Qwen-0.5-Coder)

This repository presents an AI-driven unit testing system for Angular applications using a privately hosted Large Language Model (LLM) based on Qwen-0.5-Coder (0.5B). The model is fine-tuned on custom Angular source code and unit test datasets to automatically generate and enhance Jasmine/Karma test cases.

The solution is designed for secure, offline, and enterprise environments where source code privacy is critical. All model inference and fine-tuning are performed locally or within a private infrastructure, eliminating the need for external cloud-based LLM APIs.

Features

Private LLM-based unit test generation for Angular applications

Fine-tuned Qwen-0.5-Coder model for improved Angular test accuracy

Automatic generation of Jasmine/Karma test files

Support for Angular components, services, pipes, and guards

Secure, offline execution with no data leakage

Easily extensible architecture for CI/CD integration

Architecture Overview

The system analyzes Angular source files and extracts relevant context, which is then passed to the fine-tuned Qwen-0.5-Coder model. The model generates unit test cases, including mocks and edge cases, following Angular testing best practices. Generated tests are validated and formatted to ensure compatibility with Angular’s testing framework.

Model Details

Base Model: Qwen-0.5-Coder

Fine-Tuning Method: Supervised fine-tuning using custom datasets

Training Data: Angular code and corresponding unit test pairs

Deployment: Local machine or private cloud environment

Technology Stack

Angular

TypeScript

Jasmine / Karma

Python

Hugging Face Transformers

Qwen-0.5-Coder

Use Cases

Enterprise Angular applications

Secure development environments

Automated unit test generation and maintenance

Teams requiring private AI tooling
