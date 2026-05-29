import "../styles/Note.css"
function Note({note, onDelete, onToggle}) {
    const formattedDate = new Date(note.created_at).toLocaleDateString("en-US")
    return <div className={`note-container ${note.completed ? "completed" : ""}`}>
        <input
            type="checkbox"
            checked={note.completed}
            onChange={() => onToggle(note.id)}
            className="note-checkbox"
        />
        <div className="note-content-wrapper">
            <p className="note-title">{note.title}</p>
            <p className="note-content">{note.content}</p>
            <p className="note-date">{formattedDate}</p>
        </div>
        <button className="delete-button" onClick={() => onDelete(note.id)}>
            Delete
        </button>
    </div>
}
export default Note