"""
Simple test file to validate the todo application functionality.
"""

from src.models.todo import Todo, TodoStatus
from src.services.todo_service import TodoService


def test_todo_creation():
    """Test creating todos."""
    service = TodoService()

    # Create a todo
    todo = service.create_todo("Test todo", "This is a test description")
    assert todo.id == 1
    assert todo.title == "Test todo"
    assert todo.description == "This is a test description"
    assert todo.status == TodoStatus.PENDING
    print("SUCCESS: Todo creation test passed")


def test_todo_status_updates():
    """Test updating todo status."""
    service = TodoService()

    # Create a todo
    todo = service.create_todo("Status test", "Testing status updates")

    # Update status to in-progress
    service.update_todo_status(todo.id, TodoStatus.IN_PROGRESS)
    updated_todo = service.get_todo_by_id(todo.id)
    assert updated_todo.status == TodoStatus.IN_PROGRESS
    print("SUCCESS: Status update test passed")


def test_todo_retrieval():
    """Test retrieving todos."""
    service = TodoService()

    # Create multiple todos
    service.create_todo("Todo 1", "First todo")
    service.create_todo("Todo 2", "Second todo")

    # Get all todos
    all_todos = service.get_all_todos()
    assert len(all_todos) == 2

    # Get todos by status
    pending_todos = service.get_pending_todos()
    assert len(pending_todos) == 2

    # Update one to completed
    service.update_todo_status(1, TodoStatus.COMPLETED)
    completed_todos = service.get_completed_todos()
    assert len(completed_todos) == 1

    print("SUCCESS: Todo retrieval test passed")


def test_todo_search():
    """Test searching todos."""
    service = TodoService()

    # Create todos
    service.create_todo("Shopping", "Buy groceries")
    service.create_todo("Work", "Finish report")

    # Search for "Shopping"
    results = service.search_todos("Shopping")
    assert len(results) == 1
    assert results[0].title == "Shopping"

    # Search for "groceries" in description
    results = service.search_todos("groceries")
    assert len(results) == 1
    assert results[0].title == "Shopping"

    print("SUCCESS: Todo search test passed")


def test_todo_deletion():
    """Test deleting todos."""
    service = TodoService()

    # Create a todo
    todo = service.create_todo("Delete me", "This will be deleted")
    assert service.get_todo_count() == 1

    # Delete the todo
    service.delete_todo(todo.id)
    assert service.get_todo_count() == 0

    print("SUCCESS: Todo deletion test passed")


if __name__ == "__main__":
    print("Running tests...")
    test_todo_creation()
    test_todo_status_updates()
    test_todo_retrieval()
    test_todo_search()
    test_todo_deletion()
    print("SUCCESS: All tests passed!")