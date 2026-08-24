async function saveNote() {
    const noteContent = document.getElementById('note-content').value;
    const response = await fetch('/api/note', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ note: noteContent })
    });
    const result = await response.json();
    if (result.success) {
        loadNote();
    }
}

async function loadNote() {
    const response = await fetch('/api/note');
    const result = await response.text();
    document.getElementById('note-display').innerText = result;
}

document.addEventListener('DOMContentLoaded', (event) => {
    loadNote();
    const button = document.querySelector("button")
    button.onclick = () => {
        saveNote()
    }
});
