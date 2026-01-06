# Claude Code Implementation Guide: Todo Console App

## 🚀 Getting Started with Claude Code Implementation

This document provides Claude Code with the detailed instructions needed to implement the entire Todo Console Application using Spec-Kit Plus workflow.

---

## Pre-Implementation Checklist

Before starting implementation, verify:

- ✅ Constitution file reviewed and understood
- ✅ Specification requirements clear
- ✅ Technical plan and architecture documented
- ✅ Task breakdown reviewed and dependencies understood
- ✅ Project directory structure ready
- ✅ UV package manager configured
- ✅ Claude Code environment ready

**Confirmation**: I understand the project scope, architecture, and requirements. Ready to proceed with implementation.

---

## Implementation Philosophy

### Key Principles

1. **No Manual Coding**: All code generated through Claude Code interaction
2. **Specification-First**: Follow specs exactly as written
3. **Quality Over Speed**: Clean, documented, tested code
4. **Incremental Delivery**: Complete and test each phase before moving next
5. **Communication**: Explain decisions and ask for clarification when needed

### Claude Code Workflow

For each task:
1. **Understand**: Read the task requirements completely
2. **Plan**: Explain your approach before coding
3. **Implement**: Write code with full documentation
4. **Validate**: Run tests and verify functionality
5. **Report**: Show results and ask for next steps

---

## Phase 1: Project Initialization

### Steps for Claude Code

```
TASK: Initialize project structure and configuration

1. Create directory structure:
   mkdir -p src/{models,services,cli,utils} tests .specify

2. Create all __init__.py files in:
   src/__init__.py
   src/models/__init__.py
   src/services/__init__.py
   src/cli/__init__.py
   src/utils/__init__.py
   tests/__init__.py

3. Create pyproject.toml with:
   [project]
   name = "todo-app"
   version = "0.1.0"
   description = "A command-line todo application"
   requires-python = ">=3.13"

   dependencies = [
       "rich>=13.0.0",
       "questionary>=1.10.0"
   ]

   [build-system]
   requires = ["setuptools"]
   build-backend = "setuptools.build_meta"

4. Create .gitignore with Python entries

5. Create initial README.md skeleton

After completing: Show directory tree structure and confirm all files created.
```

### Validation Commands

```bash
# Check directory structure
ls -la src/
ls -la tests/
cat pyproject.toml

# Confirm all __init__.py files exist
find . -name "__init__.py"
```

**Success Criteria**: All directories and files created, pyproject.toml valid

---

## Phase 2: Data Models Implementation

### Task: Create Task Model

```
INSTRUCTIONS FOR CLAUDE CODE:

Create file: src/models/task.py

This file defines the Task data structure. Follow these requirements:

1. Imports needed:
   - from datetime import datetime
   - from typing use Optional
   - from dataclasses import dataclass (or use regular class with __init__)

2. Create Task class with:

   class Task:
       """Represents a single todo task with metadata."""

       id: int                    # Unique identifier
       title: str                 # Task title (1-100 chars)
       description: str           # Task description (1-1000 chars)
       status: str               # "Pending" or "Completed"
       created_at: str           # ISO format timestamp
       completed_at: str | None  # ISO format timestamp or None

3. Add __init__ method:
   def __init__(self, id: int, title: str, description: str)
       self.id = id
       self.title = title
       self.description = description
       self.status = "Pending"
       self.created_at = datetime.now().isoformat()
       self.completed_at = None

4. Add method: is_completed() -> bool
   """Check if task is completed."""
   return self.status == "Completed"

5. Add method: is_pending() -> bool
   """Check if task is pending."""
   return self.status == "Pending"

6. Add method: to_dict() -> dict
   """Convert task to dictionary."""
   return {
       "id": self.id,
       "title": self.title,
       "description": self.description,
       "status": self.status,
       "created_at": self.created_at,
       "completed_at": self.completed_at
   }

7. Add method: __str__() -> str
   """Human-readable task representation."""
   return f"Task {self.id}: {self.title} ({self.status})"

8. Requirements:
   - All attributes have type hints
   - All methods have type hints (parameters and return)
   - All methods have docstrings
   - ISO format for timestamps: datetime.now().isoformat()
   - No default values for created_at (always current time)

After creating: Show the complete file and confirm all methods work.
```

### Validation

```bash
# Test imports
python -c "from src.models.task import Task; print('✓ Task imported successfully')"

# Test creation
python << 'EOF'
from src.models.task import Task
t = Task(1, "Test Task", "Description")
print(f"✓ Task created: {t}")
print(f"✓ is_pending: {t.is_pending()}")
print(f"✓ to_dict: {t.to_dict()}")
EOF
```

**Success Criteria**: Task class fully functional with all methods working

---

## Phase 3: Service Layer Implementation

### Task: Create TaskManager Service

```
INSTRUCTIONS FOR CLAUDE CODE:

Create file: src/services/task_manager.py

This service handles all business logic for task operations.

1. Imports needed:
   - from src.models.task import Task
   - from typing import List
   - from datetime import datetime

2. Create TaskManager class:

   class TaskManager:
       """Manages all todo tasks and operations."""

       def __init__(self):
           """Initialize empty task list and ID counter."""
           self.tasks: List[Task] = []
           self.next_id: int = 1

3. Implement add_task method:
   def add_task(self, title: str, description: str) -> Task:
       """
       Create and add a new task to the todo list.

       Args:
           title: Task title (required, non-empty)
           description: Task description (required, non-empty)

       Returns:
           The created Task object

       Raises:
           ValueError: If title or description is empty
       """
       if not title or not title.strip():
           raise ValueError("Title cannot be empty")
       if not description or not description.strip():
           raise ValueError("Description cannot be empty")

       task = Task(self.next_id, title.strip(), description.strip())
       self.tasks.append(task)
       self.next_id += 1
       return task

4. Implement get_all_tasks method:
   def get_all_tasks(self) -> List[Task]:
       """
       Retrieve all tasks sorted by creation date (newest first).

       Returns:
           List of all Task objects
       """
       return sorted(self.tasks, key=lambda t: t.created_at, reverse=True)

5. Implement get_task_by_id method:
   def get_task_by_id(self, task_id: int) -> Task | None:
       """
       Find and return a task by its ID.

       Args:
           task_id: The task ID to search for

       Returns:
           Task object if found, None otherwise
       """
       for task in self.tasks:
           if task.id == task_id:
               return task
       return None

6. Implement update_task method:
   def update_task(self, task_id: int, title: str | None = None,
                   description: str | None = None) -> bool:
       """
       Update task title and/or description.

       Args:
           task_id: The task ID to update
           title: New title (optional, if provided must be non-empty)
           description: New description (optional, if provided must be non-empty)

       Returns:
           True if updated successfully, False if task not found
       """
       task = self.get_task_by_id(task_id)
       if not task:
           return False

       if title is not None and title.strip():
           task.title = title.strip()
       if description is not None and description.strip():
           task.description = description.strip()

       return True

7. Implement delete_task method:
   def delete_task(self, task_id: int) -> bool:
       """
       Remove a task from the todo list by ID.

       Args:
           task_id: The task ID to delete

       Returns:
           True if deleted successfully, False if task not found
       """
       for i, task in enumerate(self.tasks):
           if task.id == task_id:
               self.tasks.pop(i)
               return True
       return False

8. Implement toggle_task_status method:
   def toggle_task_status(self, task_id: int) -> bool:
       """
       Toggle task completion status between Pending and Completed.

       Args:
           task_id: The task ID to toggle

       Returns:
           True if toggled successfully, False if task not found
       """
       task = self.get_task_by_id(task_id)
       if not task:
           return False

       if task.status == "Pending":
           task.status = "Completed"
           task.completed_at = datetime.now().isoformat()
       else:
           task.status = "Pending"
           task.completed_at = None

       return True

9. Implement get_statistics method:
   def get_statistics(self) -> dict:
       """
       Get task statistics.

       Returns:
           Dictionary with keys: total, completed, pending
       """
       total = len(self.tasks)
       completed = len([t for t in self.tasks if t.is_completed()])
       pending = len([t for t in self.tasks if t.is_pending()])
       return {
           "total": total,
           "completed": completed,
           "pending": pending
       }

After creating: Show the complete file and run basic tests.
```

### Validation

```bash
python << 'EOF'
from src.services.task_manager import TaskManager

# Create manager
tm = TaskManager()
print("✓ TaskManager created")

# Add tasks
t1 = tm.add_task("Task 1", "Description 1")
t2 = tm.add_task("Task 2", "Description 2")
print(f"✓ Tasks added: ID {t1.id}, {t2.id}")

# Get all
tasks = tm.get_all_tasks()
print(f"✓ Retrieved {len(tasks)} tasks")

# Get by ID
task = tm.get_task_by_id(1)
print(f"✓ Found task: {task}")

# Toggle status
tm.toggle_task_status(1)
print(f"✓ Task 1 status: {tm.get_task_by_id(1).status}")

# Stats
stats = tm.get_statistics()
print(f"✓ Statistics: {stats}")
EOF
```

**Success Criteria**: All TaskManager methods work correctly

---

## Phase 4: Utilities & Validation

### Task: Create Input Validators

```
INSTRUCTIONS FOR CLAUDE CODE:

Create file: src/utils/validators.py

Input validation utilities for user inputs.

1. Imports needed:
   - from typing import Tuple

2. Implement validate_non_empty function:
   def validate_non_empty(value: str, field_name: str) -> Tuple[bool, str]:
       """
       Validate that a string value is not empty.

       Args:
           value: String to validate
           field_name: Name of field (for error message)

       Returns:
           Tuple of (is_valid, error_message)
       """
       if isinstance(value, str) and value.strip():
           return (True, "")
       return (False, f"{field_name} cannot be empty")

3. Implement validate_task_id function:
   def validate_task_id(task_id_str: str, max_id: int) -> Tuple[bool, int | None]:
       """
       Validate that a string is a valid task ID.

       Args:
           task_id_str: String to convert to ID
           max_id: Maximum valid ID

       Returns:
           Tuple of (is_valid, task_id_or_none)
       """
       try:
           task_id = int(task_id_str)
           if 1 <= task_id <= max_id:
               return (True, task_id)
           return (False, None)
       except (ValueError, TypeError):
           return (False, None)

4. Implement validate_title_length function:
   def validate_title_length(title: str, min_len: int = 1,
                             max_len: int = 100) -> Tuple[bool, str]:
       """
       Validate title length is within bounds.

       Args:
           title: Title string
           min_len: Minimum length
           max_len: Maximum length

       Returns:
           Tuple of (is_valid, error_message)
       """
       if min_len <= len(title) <= max_len:
           return (True, "")
       return (False, f"Title must be between {min_len} and {max_len} characters")

5. Implement validate_description_length function:
   def validate_description_length(description: str, min_len: int = 1,
                                   max_len: int = 1000) -> Tuple[bool, str]:
       """
       Validate description length is within bounds.

       Args:
           description: Description string
           min_len: Minimum length
           max_len: Maximum length

       Returns:
           Tuple of (is_valid, error_message)
       """
       if min_len <= len(description) <= max_len:
           return (True, "")
       return (False, f"Description must be between {min_len} and {max_len} characters")

After creating: Show the file and run validation tests.
```

### Validation

```bash
python << 'EOF'
from src.utils.validators import *

# Test non-empty
print(f"✓ non_empty valid: {validate_non_empty('test', 'field')}")
print(f"✓ non_empty invalid: {validate_non_empty('', 'field')}")

# Test task ID
print(f"✓ task_id valid: {validate_task_id('5', 10)}")
print(f"✓ task_id invalid: {validate_task_id('15', 10)}")

# Test title length
print(f"✓ title_valid: {validate_title_length('Test', 1, 100)}")
print(f"✓ title_invalid: {validate_title_length('a' * 101, 1, 100)}")
EOF
```

**Success Criteria**: All validators work correctly

---

## Phase 5: CLI Formatting

### Task: Create Rich Formatters

```
INSTRUCTIONS FOR CLAUDE CODE:

Create file: src/cli/formatters.py

Rich terminal formatting utilities.

1. Imports needed:
   - from rich.console import Console
   - from rich.table import Table
   - from rich.panel import Panel
   - from src.models.task import Task
   - from typing import List

2. Create module-level console:
   console = Console()

3. Implement format_status_badge function:
   def format_status_badge(status: str) -> str:
       """Return colored status badge."""
       if status == "Completed":
           return "[green]✓ Completed[/green]"
       return "[yellow]○ Pending[/yellow]"

4. Implement format_task_table function:
   def format_task_table(tasks: List[Task]) -> Table:
       """Create formatted table displaying all tasks."""
       table = Table(title="📋 Your Todo Tasks", show_header=True)
       table.add_column("ID", style="cyan")
       table.add_column("Title", style="magenta")
       table.add_column("Description")
       table.add_column("Status")
       table.add_column("Created", style="green")

       for task in tasks:
           status_badge = format_status_badge(task.status)
           table.add_row(
               str(task.id),
               task.title,
               task.description[:30] + "..." if len(task.description) > 30 else task.description,
               status_badge,
               task.created_at
           )

       return table

5. Implement format_task_details function:
   def format_task_details(task: Task) -> Panel:
       """Create detailed view panel for a single task."""
       content = f"""
ID: {task.id}
Title: {task.title}
Description: {task.description}
Status: {format_status_badge(task.status)}
Created: {task.created_at}
Completed: {task.completed_at if task.completed_at else 'Not completed'}
       """
       return Panel(content.strip(), title="📝 Task Details")

6. Implement format_success_message function:
   def format_success_message(message: str) -> None:
       """Display success message."""
       console.print(f"[green]✓[/green] {message}")

7. Implement format_error_message function:
   def format_error_message(message: str) -> None:
       """Display error message."""
       console.print(f"[red]✗[/red] {message}")

8. Implement format_info_message function:
   def format_info_message(message: str) -> None:
       """Display info message."""
       console.print(f"[blue]ℹ[/blue] {message}")

9. Implement format_statistics function:
   def format_statistics(total: int, completed: int, pending: int) -> Panel:
       """Create statistics summary panel."""
       content = f"""
Total Tasks: {total}
Completed: {completed}
Pending: {pending}
Progress: {(completed/total*100):.0f}% complete""" if total > 0 else "No tasks yet"

       return Panel(content.strip(), title="📊 Statistics")

10. Implement format_welcome_message function:
    def format_welcome_message() -> None:
        """Print welcome banner."""
        console.print("[bold cyan]═══════════════════════════════════[/bold cyan]")
        console.print("[bold yellow]   📝 Welcome to Todo Console App   [/bold yellow]")
        console.print("[bold cyan]═══════════════════════════════════[/bold cyan]")
        console.print("[green]Manage your tasks efficiently![/green]\\n")

After creating: Show the file and test formatting output.
```

### Validation

```bash
python << 'EOF'
from src.cli.formatters import *
from src.models.task import Task

format_welcome_message()
format_success_message("This is a success message")
format_error_message("This is an error message")
format_info_message("This is an info message")

t = Task(1, "Test Task", "Test Description")
print(format_task_details(t))
print(format_statistics(5, 3, 2))
EOF
```

**Success Criteria**: All formatters produce rich, colored output

---

## Phase 6: CLI Commands Implementation

```
INSTRUCTIONS FOR CLAUDE CODE:

Create file: src/cli/commands.py

Command handlers for each feature.

IMPORTANT: This is a large file with 5 command functions. Implement each carefully:

1. Imports needed:
   - import questionary
   - from src.services.task_manager import TaskManager
   - from src.utils.validators import *
   - from src.cli.formatters import *

2. Implement view_tasks_command function:
   def view_tasks_command(task_manager: TaskManager) -> None:
       """Display all tasks in formatted table with statistics."""
       tasks = task_manager.get_all_tasks()

       if not tasks:
           format_info_message("No tasks found. Add one to get started!")
           return

       console.print(format_task_table(tasks))
       stats = task_manager.get_statistics()
       console.print(format_statistics(stats["total"], stats["completed"], stats["pending"]))

3. Implement add_task_command function:
   def add_task_command(task_manager: TaskManager) -> None:
       """Create a new task with user input."""
       format_info_message("Creating new task...")

       title = questionary.text("Task Title:").ask()
       if not title:
           format_error_message("Operation cancelled")
           return

       is_valid, error = validate_title_length(title)
       if not is_valid:
           format_error_message(error)
           return

       description = questionary.text("Task Description:").ask()
       if not description:
           format_error_message("Operation cancelled")
           return

       is_valid, error = validate_description_length(description)
       if not is_valid:
           format_error_message(error)
           return

       try:
           task = task_manager.add_task(title, description)
           format_success_message(f"Task created with ID {task.id}")
           console.print(format_task_details(task))
       except ValueError as e:
           format_error_message(str(e))

4. Implement update_task_command function:
   def update_task_command(task_manager: TaskManager) -> None:
       """Update title and/or description of existing task."""
       tasks = task_manager.get_all_tasks()
       if not tasks:
           format_info_message("No tasks to update")
           return

       console.print(format_task_table(tasks))

       task_id_str = questionary.text("Enter Task ID to update:").ask()
       is_valid, task_id = validate_task_id(task_id_str, max(t.id for t in tasks))
       if not is_valid:
           format_error_message("Invalid task ID")
           return

       task = task_manager.get_task_by_id(task_id)
       if not task:
           format_error_message(f"Task {task_id} not found")
           return

       new_title = questionary.text(f"New Title (current: {task.title}):").ask()
       new_description = questionary.text(f"New Description (current: {task.description}):").ask()

       if task_manager.update_task(task_id, new_title or None, new_description or None):
           format_success_message("Task updated successfully")
           console.print(format_task_details(task_manager.get_task_by_id(task_id)))
       else:
           format_error_message("Failed to update task")

5. Implement delete_task_command function:
   def delete_task_command(task_manager: TaskManager) -> None:
       """Delete a task with confirmation."""
       tasks = task_manager.get_all_tasks()
       if not tasks:
           format_info_message("No tasks to delete")
           return

       console.print(format_task_table(tasks))

       task_id_str = questionary.text("Enter Task ID to delete:").ask()
       is_valid, task_id = validate_task_id(task_id_str, max(t.id for t in tasks))
       if not is_valid:
           format_error_message("Invalid task ID")
           return

       task = task_manager.get_task_by_id(task_id)
       if not task:
           format_error_message(f"Task {task_id} not found")
           return

       console.print(format_task_details(task))

       confirm = questionary.confirm("Are you sure you want to delete this task?").ask()
       if confirm and task_manager.delete_task(task_id):
           format_success_message("Task deleted successfully")
       elif not confirm:
           format_info_message("Deletion cancelled")
       else:
           format_error_message("Failed to delete task")

6. Implement toggle_status_command function:
   def toggle_status_command(task_manager: TaskManager) -> None:
       """Toggle task completion status with confirmation."""
       tasks = task_manager.get_all_tasks()
       if not tasks:
           format_info_message("No tasks to update")
           return

       console.print(format_task_table(tasks))

       task_id_str = questionary.text("Enter Task ID:").ask()
       is_valid, task_id = validate_task_id(task_id_str, max(t.id for t in tasks))
       if not is_valid:
           format_error_message("Invalid task ID")
           return

       task = task_manager.get_task_by_id(task_id)
       if not task:
           format_error_message(f"Task {task_id} not found")
           return

       new_status = "Completed" if task.is_pending() else "Pending"
       confirm = questionary.confirm(f"Mark as {new_status}?").ask()

       if confirm and task_manager.toggle_task_status(task_id):
           format_success_message(f"Task marked as {new_status}")
           console.print(format_task_details(task_manager.get_task_by_id(task_id)))
       elif not confirm:
           format_info_message("Operation cancelled")
       else:
           format_error_message("Failed to update task status")

After creating: Show the file and test basic command flow.
```

**Success Criteria**: All 5 commands work with proper validation and formatting

---

## Phase 7: Main CLI Application

```
INSTRUCTIONS FOR CLAUDE CODE:

Create file: src/cli/main.py

Main application menu and loop.

1. Imports needed:
   - from src.services.task_manager import TaskManager
   - from src.cli.commands import *
   - from src.cli.formatters import format_welcome_message, format_info_message
   - import questionary

2. Create main function:
   def main() -> None:
       """Main application entry point."""
       task_manager = TaskManager()

       format_welcome_message()

       while True:
           try:
               choice = questionary.select(
                   "What would you like to do?",
                   choices=[
                       "1. View All Tasks",
                       "2. Add New Task",
                       "3. Update Task",
                       "4. Delete Task",
                       "5. Mark Complete/Incomplete",
                       "6. Exit"
                   ]
               ).ask()

               if choice.startswith("1"):
                   view_tasks_command(task_manager)
               elif choice.startswith("2"):
                   add_task_command(task_manager)
               elif choice.startswith("3"):
                   update_task_command(task_manager)
               elif choice.startswith("4"):
                   delete_task_command(task_manager)
               elif choice.startswith("5"):
                   toggle_status_command(task_manager)
               elif choice.startswith("6"):
                   format_info_message("Thank you for using Todo App!")
                   break

               questionary.press_any_key_to_continue().ask()

           except KeyboardInterrupt:
               print()
               format_info_message("Application closed")
               break
           except Exception as e:
               format_error_message(f"An error occurred: {str(e)}")

3. Add main block:
   if __name__ == "__main__":
       main()

After creating: Show the file and explain the menu flow.
```

**Success Criteria**: Main menu works with all options routing correctly

---

## Phase 8: Application Initialization

```
INSTRUCTIONS FOR CLAUDE CODE:

Create file: src/app.py

Application entry point wrapper.

Create simple app initialization:

from src.cli.main import main

class TodoApp:
    """Todo Console Application."""

    def run(self) -> None:
        """Start the application."""
        main()

if __name__ == "__main__":
    app = TodoApp()
    app.run()

After creating: Confirm file created.
```

**Success Criteria**: App initializes and runs main menu

---

## Phase 9: Testing

```
INSTRUCTIONS FOR CLAUDE CODE:

Create comprehensive tests for all modules.

1. Create tests/test_models.py - Test Task class
2. Create tests/test_services.py - Test TaskManager
3. Create tests/test_integration.py - Test full workflow

Run all tests:
   pytest tests/ -v

Ensure all tests pass before proceeding.
```

**Success Criteria**: All tests pass with high coverage

---

## Phase 10: Documentation

```
INSTRUCTIONS FOR CLAUDE CODE:

Create comprehensive documentation:

1. Update README.md with:
   - Project description
   - Features list
   - Installation steps
   - Usage examples
   - Project structure
   - Development setup

2. Create CLAUDE.md with:
   - Spec-Kit Plus workflow overview
   - Constitution/Spec/Plan/Tasks explanation
   - How to use the application
   - Development guidelines
   - Future enhancements
```

**Success Criteria**: README and CLAUDE.md are complete and clear

---

## Final Validation Checklist

Before completing, verify:

- ✅ All 5 features work end-to-end
- ✅ Rich formatting displays correctly
- ✅ Questionary prompts work smoothly
- ✅ Error messages are helpful
- ✅ Input validation prevents bad data
- ✅ All code has type hints
- ✅ All functions have docstrings
- ✅ PEP 8 style followed
- ✅ All tests pass
- ✅ Documentation is complete
- ✅ Git history is clean

---

## Running the Application

Once implementation complete:

```bash
# Install dependencies
uv pip install -e .

# Run the application
python -m src.app
# or
python src/app.py

# Run tests
pytest tests/ -v

# Check code style
python -m pylint src/
```

---

## Implementation Support

**If Claude Code encounters issues:**

1. Show the error message clearly
2. Explain the attempted fix
3. Ask for guidance if solution not obvious
4. Provide alternative approaches if needed

**If requirements unclear:**

1. Ask clarifying questions
2. Reference specifications for guidance
3. Suggest reasonable interpretations
4. Wait for confirmation

---

## Success!

Upon successful completion of all phases:

✨ **Todo Console App fully implemented with:**
- ✅ All 5 core features working
- ✅ Rich CLI with colored output and formatting
- ✅ Interactive questionary prompts
- ✅ Clean code architecture
- ✅ Comprehensive documentation
- ✅ Full test coverage
- ✅ Professional GitHub repository

**Project Ready for Delivery! 🚀**