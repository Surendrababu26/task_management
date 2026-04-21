import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");

  const API = "http://127.0.0.1:8000/api/tasks/";

  //  Fetch Tasks (with error handling) 
  const fetchTasks = async () => {
    try {
      const res = await fetch(API);

      if (!res.ok) {
        throw new Error("Failed to fetch tasks");
      }

      const data = await res.json();
      setTasks(data);
    } catch (error) {
      console.error(error);
      alert("Error fetching tasks");
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  //  Add Task (with validation + error handling)
  const addTask = async () => {
    if (!title.trim()) {
      alert("Task cannot be empty!");
      return;
    }

    try {
      const res = await fetch(API, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: title,
          status: "pending",
        }),
      });

      if (!res.ok) {
        throw new Error("Failed to add task");
      }

      setTitle("");
      fetchTasks();
    } catch (error) {
      console.error(error);
      alert("Error adding task");
    }
  };

  //  Delete Task
  const deleteTask = async (id) => {
    try {
      const res = await fetch(`${API}${id}/`, {
        method: "DELETE",
      });

      if (!res.ok) {
        throw new Error("Failed to delete task");
      }

      fetchTasks();
    } catch (error) {
      console.error(error);
      alert("Error deleting task");
    }
  };

  //  Toggle Status 
  const toggleStatus = async (task) => {
    try {
      const res = await fetch(`${API}${task.id}/`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: task.title, //  required for backend
          status: task.status === "pending" ? "completed" : "pending",
        }),
      });

      if (!res.ok) {
        throw new Error("Failed to update task");
      }

      fetchTasks();
    } catch (error) {
      console.error(error);
      alert("Error updating task");
    }
  };

  return (
    <div className="container">
      <h1>Task Manager</h1>

      {/* Input Section */}
      <div className="input-box">
        <input
          type="text"
          placeholder="Enter task..."
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <button onClick={addTask}>Add</button>
      </div>

      {/* Task List */}
      <ul className="task-list">
        {tasks.length === 0 ? (
          <p>No tasks available</p>
        ) : (
          tasks.map((task) => (
            <li key={task.id} className="task-item">
              <span className={task.status === "completed" ? "done" : ""}>
                {task.title}
              </span>

              <div>
                <button onClick={() => toggleStatus(task)}>Toggle</button>
                <button onClick={() => deleteTask(task.id)}>Delete</button>
              </div>
            </li>
          ))
        )}
      </ul>
    </div>
  );
}

export default App;