const API_URL = "http://localhost:8000";

document.addEventListener("DOMContentLoaded", loadTasks);

async function loadTasks() {
    try {
        const response = await fetch(`${API_URL}/tasks`);
        const tasks = await response.json();
        displayTasks(tasks);
    } catch (error) {
        console.error("Error loading tasks:", error);
        document.getElementById("tasks").innerHTML = `
            <div class="empty">❌ Unable to connect to backend.</div>
        `;
    }
}

function displayTasks(tasks) {
    const container = document.getElementById("tasks");

    if (tasks.length === 0) {
        container.innerHTML = `
            <div class="empty">📝 No tasks yet.</div>
        `;
        return;
    }

    container.innerHTML = tasks.map(task => `
        <div class="task ${task.completed ? "completed" : ""}">
            <h3>${escapeHTML(task.title)}</h3>
            <p>${escapeHTML(task.description || "No description")}</p>
            <div class="actions">
                <button class="complete-btn"
                    onclick="toggleTask('${task.id}', ${task.completed})">
                    ${task.completed ? "↩️ Undo" : "✅ Complete"}
                </button>
                <button class="delete-btn"
                    onclick="deleteTask('${task.id}')">
                    🗑️ Delete
                </button>
            </div>
        </div>
    `).join("");
}

async function addTask() {
    const titleInput = document.getElementById("title");
    const descriptionInput = document.getElementById("description");

    const title = titleInput.value.trim();
    const description = descriptionInput.value.trim();

    if (!title) {
        alert("Please enter a task title.");
        return;
    }

    try {
        const response = await fetch(`${API_URL}/tasks`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({title, description})
        });

        if (!response.ok) throw new Error("Failed to create task");

        titleInput.value = "";
        descriptionInput.value = "";
        await loadTasks();
    } catch (error) {
        console.error(error);
        alert("Unable to add task.");
    }
}

async function toggleTask(id, completed) {
    try {
        await fetch(`${API_URL}/tasks/${id}`, {
            method: "PUT",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({completed: !completed})
        });

        await loadTasks();
    } catch (error) {
        console.error(error);
        alert("Unable to update task.");
    }
}

async function deleteTask(id) {
    if (!confirm("Are you sure you want to delete this task?")) return;

    try {
        await fetch(`${API_URL}/tasks/${id}`, {method: "DELETE"});
        await loadTasks();
    } catch (error) {
        console.error(error);
        alert("Unable to delete task.");
    }
}

function escapeHTML(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}
