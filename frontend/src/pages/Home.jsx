import { useState, useEffect } from "react"
import { useNavigate } from "react-router-dom"
import api from "../api"
import Note from "../components/Note"
import "../styles/Home.css"

function Home() {
    const navigate = useNavigate()
    const [notes, setNotes] = useState([]);
    const [content, setContent] = useState("")
    const [title, setTitle] = useState("")

    // Beim ersten Rendern: Todos aus der API laden
    useEffect(() => {
        getNotes();
    }, [])

    // Holt alle Todos vom Backend (GET /api/notes/)
    const getNotes = () => {
        api
            .get("/api/notes/")
            .then((res) => res.data)
            .then((data) => setNotes(data))
            .catch((err) => alert(err))
    }

    // Löscht ein Todo (DELETE /api/notes/<id>/)
    const deleteNote = (id) => {
        api
            .delete(`/api/notes/${id}/`)
            .then((res) => {        
                getNotes();  // Liste nach dem Löschen neu laden
            })
            .catch((error) => alert(error))
    }

    // Schaltet den Erledigt-Status um (PATCH /api/notes/<id>/)
    const toggleTodo = (id) => {
        const note = notes.find((n) => n.id === id)
        api
            .patch(`/api/notes/${id}/`, { completed: !note.completed })
            .then((res) => getNotes())
            .catch((err) => alert(err))
    }

    // Erstellt ein neues Todo (POST /api/notes/)
    const createNote = (e) => {
        e.preventDefault()  // Verhindert Neuladen der Seite
        api
            .post("/api/notes/", { content, title })
            .then((res) => {
                getNotes();           // Liste aktualisieren
                setTitle("");         // Eingabefelder leeren
                setContent("");
            })
            .catch((err) => alert(err))
    }

    return <div>
    <div className="home-header">
        <h2>Todo App</h2>
        <button className="logout-button" onClick={() => navigate("/logout")}>Logout</button>
    </div>
    <h2>Create a Todo</h2>
    <form onSubmit={createNote}>
        <label htmlFor="title">Title:</label>
        <br></br>
        <input
            type="text"
            id="title"
            name="title"
            required
            onChange={(e) => setTitle(e.target.value)}
            value={title}
        />
        <label htmlFor="content">Content:</label>
        <br></br>
        <textarea
            id="content"
            name="content"
            required value={content}
            onChange={(e) => setContent(e.target.value)}
        />
        <br></br>
        <input type="submit" value="Submit"></input>
    </form>
    <div className="todo-list">
        <h2>Todos</h2>
        {notes.map((note) => (
            <Note note={note} onDelete={deleteNote} onToggle={toggleTodo} key={note.id}></Note>
        ))}
    </div>
</div>
}

export default Home
