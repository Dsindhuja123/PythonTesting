
document.getElementById('add-task-button').addEventListener('click', function() {
    var newTaskInput = document.getElementById('new-task-input');
    var todoList = document.getElementById('todo-list');
    var newTask = document.createElement('li');
    newTask.textContent = newTaskInput.value;
    todoList.appendChild(newTask);
    newTaskInput.value = '';
});