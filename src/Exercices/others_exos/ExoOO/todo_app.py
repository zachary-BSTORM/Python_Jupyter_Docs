import json
import os

# --- Todo App ---
# Gestionnaire de tâches persistant en JSON.
# Chaque tâche possède : id (auto-incrémenté), title, status, priority (1–5), tags (liste).
# Les données sont sauvegardées dans un fichier JSON après chaque modification.
# Le listing supporte le filtrage (status, priorité min, tag) et la pagination (10 par page).

TASKS_FILE = "tasks.json"


def load_tasks():
    # Charge les tâches depuis le fichier JSON ; retourne [] si absent ou corrompu
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_tasks(tasks):
    # Écrase le fichier avec l'état courant de la liste (indent=4 pour la lisibilité)
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def generate_id(tasks):
    # Prend le max des ids existants + 1 ; default=0 si la liste est vide → premier id = 1
    return max((t["id"] for t in tasks), default=0) + 1


def add_task(tasks, title, priority, tags):
    if not (1 <= priority <= 5):
        print("Priority must be between 1 and 5")
        return
    task = {
        "id": generate_id(tasks),
        "title": title,
        "status": "todo",   # Statut initial par défaut
        "priority": priority,
        "tags": tags
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added with id {task['id']}")


def list_tasks(tasks, params=None):
    # Applique les filtres un à un sur une copie de la liste
    if params is None:
        params = {}

    filtered = tasks[:]

    if "status" in params:
        filtered = [t for t in filtered if t["status"] == params["status"]]
    if "priority_min" in params:
        filtered = [t for t in filtered if t["priority"] >= params["priority_min"]]
    if "tag" in params:
        filtered = [t for t in filtered if params["tag"] in t["tags"]]

    if not filtered:
        print("No tasks found")
        return

    # --- Pagination ---
    # On découpe la liste filtrée en pages de 10 éléments
    page = params.get("page", 1)
    per_page = 10
    start = (page - 1) * per_page
    end = start + per_page
    page_items = filtered[start:end]

    if not page_items:
        print(f"No tasks on page {page}")
        return

    print(f"\n--- Tasks (page {page}) ---")
    for t in page_items:
        print(f"{t['id']} - {t['title']} - {t['status']} - priority:{t['priority']} - {t['tags']}")
    print(f"Showing {len(page_items)} of {len(filtered)} tasks")


def update_task(tasks, task_id, new_data):
    # next() avec default=None : recherche efficace sans lever d'exception si absent
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print(f"Task {task_id} not found")
        return

    valid_statuses = {"todo", "in_progress", "done"}

    # On ne met à jour que les champs présents dans new_data (mise à jour partielle)
    if "title" in new_data:
        task["title"] = new_data["title"]
    if "status" in new_data:
        if new_data["status"] not in valid_statuses:
            print(f"Invalid status. Choose from: {', '.join(valid_statuses)}")
            return
        task["status"] = new_data["status"]
    if "priority" in new_data:
        if not (1 <= new_data["priority"] <= 5):
            print("Priority must be between 1 and 5")
            return
        task["priority"] = new_data["priority"]
    if "tags" in new_data:
        task["tags"] = new_data["tags"]

    save_tasks(tasks)
    print(f"Task {task_id} updated")


def delete_task(tasks, task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print(f"Task {task_id} not found")
        return
    tasks.remove(task)   # list.remove() supprime la première occurrence de l'objet
    save_tasks(tasks)
    print(f"Task {task_id} deleted")


def mark_done(tasks, task_id):
    # Raccourci : délègue simplement à update_task avec le statut "done"
    update_task(tasks, task_id, {"status": "done"})


def todo_menu():
    tasks = load_tasks()

    while True:
        print("\n--- Todo App ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Mark as done")
        print("6. Back")

        choice = input("Choice: ").strip()

        match choice:
            case "1":
                title = input("Title: ").strip()
                try:
                    priority = int(input("Priority (1-5): "))
                except ValueError:
                    print("Invalid priority")
                    continue
                tags = [t.strip() for t in input("Tags : ").split(",") if t.strip()]
                add_task(tasks, title, priority, tags)

            case "2":
                params = {}
                status = input("Filter by status (leave empty to skip): ").strip()
                if status:
                    params["status"] = status
                pmin = input("Min priority (leave empty to skip): ").strip()
                if pmin:
                    try:
                        params["priority_min"] = int(pmin)
                    except ValueError:
                        pass
                tag = input("Filter by tag (leave empty to skip): ").strip()
                if tag:
                    params["tag"] = tag
                page = input("Page (default 1): ").strip()
                if page:
                    try:
                        params["page"] = int(page)
                    except ValueError:
                        pass
                list_tasks(tasks, params)

            case "3":
                try:
                    task_id = int(input("Task id: "))
                except ValueError:
                    print("Invalid id")
                    continue
                new_data = {}
                title = input("New title (leave empty to skip): ").strip()
                if title:
                    new_data["title"] = title
                status = input("New status (todo/in_progress/done, leave empty to skip): ").strip()
                if status:
                    new_data["status"] = status
                prio = input("New priority (leave empty to skip): ").strip()
                if prio:
                    try:
                        new_data["priority"] = int(prio)
                    except ValueError:
                        pass
                tags = input("New tags (comma separated, leave empty to skip): ").strip()
                if tags:
                    new_data["tags"] = [t.strip() for t in tags.split(",") if t.strip()]
                update_task(tasks, task_id, new_data)

            case "4":
                try:
                    task_id = int(input("Task id: "))
                except ValueError:
                    print("Invalid id")
                    continue
                delete_task(tasks, task_id)

            case "5":
                try:
                    task_id = int(input("Task id: "))
                except ValueError:
                    print("Invalid id")
                    continue
                mark_done(tasks, task_id)

            case "6":
                break

            case _:
                print("Invalid choice")


todo_menu()