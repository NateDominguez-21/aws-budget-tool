# aws-budget-tool

**BudgetWise** is a serverless budget tool built on AWS, featuring a modern web interface and a fully serverless backend.

## Features

- Add, view, update, and delete budget items (income and expenses)
- See a real-time summary of your income, expenses, and balance
- Clean, responsive web interface with navy blue and gold branding
- Powered by AWS Lambda, API Gateway, and DynamoDB

## Project Structure

aws-budget-tool/

```│
├── backend/
│ └── lambda_functions/
│ ├── add_budget_item.py
│ ├── get_budget_items.py
│ ├── get_budget_item.py
│ ├── update_budget_item.py
│ ├── delete_budget_item.py
│ └── get_budget_summary.py
│
└── frontend/
└── index.html
```

## How It Works

- **Frontend:** The app is a single-page HTML and JavaScript site (`frontend/index.html`) that interacts with the API.
- **Backend:** The backend is a set of AWS Lambda functions (in `backend/lambda_functions/`) connected to API Gateway endpoints.
- **Database:** All budget entries are stored in a DynamoDB table called `BudgetItems`.

## Getting Started

1. Clone this repository:
git clone https://github.com/NateDominguez-21/aws-budget-tool.git

2. Deploy the Lambda functions and set up API Gateway as described in the backend folder.
3. Open `frontend/index.html` in your browser, or host it on S3 for public access.

http://budgetwise-demo-nate.s3-website-us-east-1.amazonaws.com/
