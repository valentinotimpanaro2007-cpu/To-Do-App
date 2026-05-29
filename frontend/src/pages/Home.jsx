import { useState, useEffect } from "react"
import api from "../api"
import Note from "../components/Note"
import "../styles/Home.css"

function Home() {
    const [notes, setNotes] = useState([]);
    const [content, setContent] = useState("")
    const [title, setTitle] = useState("")

    useEffect(() => {
        getNotes();
    }, [])

    const getNotes = () => {
        api
            .get("/api/notes/")
            .then((res) => res.data)
            .then((data) => setNotes(data))
            .catch((err) => alert(err))
    }

    const deleteNote = (id) => {
        api
            .delete(`/api/notes/${id}/`)
            .then((res) => {        
                getNotes();
            })
            .catch((error) => alert(error))
    }

    const toggleTodo = (id) => {
        const note = notes.find((n) => n.id === id)
        api
            .patch(`/api/notes/${id}/`, { completed: !note.completed })
            .then((res) => getNotes())
            .catch((err) => alert(err))
    }

    const createNote = (e) => {
        e.preventDefault()
        api
            .post("/api/notes/", { content, title })
            .then((res) => {
                getNotes();
            })
            .catch((err) => alert(err))
    }

    return <div>
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
