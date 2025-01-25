async function fetchNotes() {
    const response = await fetch('/notes');
    const notes = await response.json();
    const notesList = document.getElementById('notes-list');
    notesList.innerHTML = '';
    notes.forEach((note, index) => {
        const li = document.createElement('li');
        li.innerHTML = `${note} <button class="delete-btn" onclick="deleteNoteById(${index})">Delete</button>`;
        notesList.appendChild(li);
    });
}

async function addNote() {
    const noteInput = document.getElementById('note-input');
    const note = noteInput.value;
    if (note) {
        await fetch('/notes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ note })
        });
        noteInput.value = '';
        fetchNotes();
    }
}

async function getNote() {
    const noteIdInput = document.getElementById('note-id-input');
    const noteId = noteIdInput.value;
    if (noteId) {
        const response = await fetch(`/notes/${noteId}`);
        const note = await response.json();
        const noteDetail = document.getElementById('note-detail');
        if (response.status === 200) {
            noteDetail.innerHTML = `Note ID ${noteId}: ${note}`;
        } else {
            noteDetail.innerHTML = `Error: ${note.message}`;
        }
    }
}

async function deleteNote() {
    const noteIdInput = document.getElementById('note-id-input');
    const noteId = noteIdInput.value;
    if (noteId) {
        const response = await fetch(`/notes/${noteId}`, {
            method: 'DELETE'
        });
        const result = await response.json();
        const noteDetail = document.getElementById('note-detail');
        noteDetail.innerHTML = `Message: ${result.message}`;
        fetchNotes();
    }
}

window.onload = fetchNotes;

