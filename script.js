document.getElementById("addButton").addEventListener("click", function () {
    const taskInput = document.getElementById("taskInput");
    const taskList = document.getElementById("taskList");
  
    if (taskInput.value.trim() !== "") {
      // Create a new task item
      const li = document.createElement("li");
  
      // Add text content
      li.textContent = taskInput.value;
  
      // Create delete button
      const deleteButton = document.createElement("button");
      deleteButton.textContent = "Delete";
      deleteButton.addEventListener("click", function () {
        taskList.removeChild(li);
      });
  
      // Add delete button to the task item
      li.appendChild(deleteButton);
  
      // Add task item to the list
      taskList.appendChild(li);
  
      // Clear the input field
      taskInput.value = "";
    } else {
      alert("Please enter a task!");
    }
  });