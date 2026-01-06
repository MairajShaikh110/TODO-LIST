# Todo Console App

A rich, interactive command-line todo application built with Python.

## Features

- **Add Tasks**: Create new todo tasks with titles and descriptions
- **View Tasks**: Display all tasks in a formatted table with statistics
- **Update Tasks**: Modify existing task titles and descriptions
- **Delete Tasks**: Remove tasks with confirmation
- **Toggle Status**: Mark tasks as complete/incomplete with confirmation
- **Rich Terminal Interface**: Colored output using the rich library
- **Interactive Prompts**: User-friendly interface using questionary
- **Input Validation**: Comprehensive validation for all user inputs
- **Statistics Tracking**: View task completion statistics

## Installation

1. Clone the repository
2. Install dependencies using uv:
   ```bash
   uv pip install -e .
   ```

## Usage

Run the application:
```bash
python -m src.app
# or
python src/app.py
```

The application will present an interactive menu with the following options:
1. View All Tasks - Display all tasks in a formatted table
2. Add New Task - Create a new task with title and description
3. Update Task - Modify existing task details
4. Delete Task - Remove a task after confirmation
5. Mark Complete/Incomplete - Toggle task completion status
6. Exit - Close the application

## Project Structure

```
todo-list/
├── src/
│   ├── models/
│   │   └── task.py          # Task data model
│   ├── services/
│   │   └── task_manager.py  # Business logic layer
│   ├── cli/
│   │   ├── formatters.py    # Rich formatting utilities
│   │   ├── commands.py      # CLI command handlers
│   │   └── main.py          # Main CLI application
│   ├── utils/
│   │   └── validators.py    # Input validation utilities
│   └── app.py              # Application entry point
├── tests/
│   ├── test_task_model.py   # Unit tests for Task model
│   ├── test_task_manager.py # Unit tests for TaskManager
│   ├── test_validators.py   # Unit tests for validators
│   └── test_integration.py  # Integration tests
├── pyproject.toml          # Project dependencies and metadata
├── README.md              # Project documentation
└── CLAUDE.md              # Claude Code implementation guide
```

## Development Setup

1. Install Python 3.13 or higher
2. Install uv package manager
3. Install dependencies: `uv pip install -e .`
4. Run tests: `pytest tests/ -v`
5. Run the application: `python src/app.py`

## Code Quality

- Type hints included for all functions and classes
- Comprehensive docstrings following Google style
- Input validation for all user inputs
- Error handling with appropriate messages
- Unit tests covering all functionality
- Integration tests for complete workflows

## Future Enhancements

- Add data persistence with file storage
- Add search and filter functionality
- Add due dates and priority levels
- Add export/import capabilities
- Add recurring tasks feature