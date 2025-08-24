const API_BASE = "http://127.0.0.1:5000";

// ------------ Activities ------------
const activityForm = document.getElementById("activity-form");
const activityList = document.getElementById("activity-list");

activityForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = document.getElementById("activity-name").value;
    const description = document.getElementById("activity-desc").value;

    await fetch(`${API_BASE}/activities`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, description })
    });

    loadActivities();
    activityForm.reset();
});

async function loadActivities() {
    const res = await fetch(`${API_BASE}/activities`);
    const data = await res.json();
    activityList.innerHTML = data.map(a => `<li>${a.name} - ${a.description || ""}</li>`).join("");
}

// ------------ Goals ------------
const goalForm = document.getElementById("goal-form");
const goalList = document.getElementById("goal-list");

goalForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const title = document.getElementById("goal-title").value;
    const target = parseInt(document.getElementById("goal-target").value);
    const period = document.getElementById("goal-period").value;

    await fetch(`${API_BASE}/goals`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, target, period })
    });

    loadGoals();
    goalForm.reset();
});

async function loadGoals() {
    const res = await fetch(`${API_BASE}/goals`);
    const data = await res.json();
    goalList.innerHTML = data.map(g => `<li>${g.title} - ${g.period} (Progress: ${g.progress}/${g.target})</li>`).join("");
}

// ------------ Reminders ------------
const reminderForm = document.getElementById("reminder-form");
const reminderList = document.getElementById("reminder-list");

reminderForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const message = document.getElementById("reminder-msg").value;
    const time = document.getElementById("reminder-time").value;

    await fetch(`${API_BASE}/reminders`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message, time })
    });

    loadReminders();
    reminderForm.reset();
});

async function loadReminders() {
    const res = await fetch(`${API_BASE}/reminders`);
    const data = await res.json();
    reminderList.innerHTML = data.map(r => `<li>${r.message} - ${r.time}</li>`).join("");
}

// ------------ Init ------------
loadActivities();
loadGoals();
loadReminders();
