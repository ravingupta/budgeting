# Simple CSV Budgeting App

A lightweight budgeting application that allows you to manage your finances by uploading bank transactions via CSV files. The app automatically categorizes transactions without requiring complex tools or direct bank integrations.

## Features

- **Bank-Agnostic CSV Import**: Support for multiple bank statement formats through custom parsers
- **Automatic Categorization**: Smart transaction categorization system
- **Local Database**: All data stays on your machine - no server uploads required
- **No Bank Permissions**: Works with downloaded CSV statements - no bank API access needed
- **Smart Detection**: 
  - Automatically identifies refunds
  - Flags potential duplicate transactions
- **Simple Dashboard**: Get a clear overview of your financial status through an intuitive interface

## Requirements

- Python 3.8 or higher

## Quick Start

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/budgeting.git
   cd budgeting
   ```
2. Run the setup script:
   ```bash
    ./setup.sh
    ```
3. (Optional) Initialize default categories and settings:
   ```bash
   python migration.py
   ```

## Bank Support
The following banks are currently supported for CSV import:
- Scotia Bank

`Status: In Progress (check documentation for latest additions)`

## Security
This application:
- Runs entirely locally
- Doesn't transmit any financial data
- Doesn't require bank credentials or API access
- Processes only CSV files that you explicitly provide

## Development Status
This project is under active development. Current focus areas:
- Expanding bank CSV parser support
- Enhancing categorization accuracy
- Improving the dashboard interface

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.