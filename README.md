# FinSight

Ask questions about any Indian company's annual report and get answers with page references.

## Problem
Investors who want to research a company before investing usually turn to its annual report,
which is often 200–400 pages long. Reading it fully takes hours. Ctrl+F only works if you
guess the exact wording used in the report. General AI chatbots may miss details in a document
this long, can make up numbers, and rarely show where their answer came from, so it can't be verified.

## Who it's for
Retail investors and analysts who want specific answers from a company's financial report
without reading the whole thing.

## Features (planned)
- Upload a company's annual report as a PDF
- Ask questions in plain English (e.g. "What are the key risks this year?")
- Get answers grounded in the report, with page numbers to verify each answer
- Sign up and log in to keep your documents private
- View your past questions and answers

## Out of scope
- No investment advice or buy/sell recommendations
- No stock price predictions
- Reports must be uploaded by the user (no automatic fetching in v1)

## Tech Stack (planned)
Python, FastAPI, PostgreSQL, React, an LLM API, Docker, GitHub Actions