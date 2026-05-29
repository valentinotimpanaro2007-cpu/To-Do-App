import {useState} from "react"
import { Link } from "react-router-dom"
import api from "../api"
import { useNavigate } from "react-router-dom"
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants"
import "../styles/Form.css"
import LoadingIndicator from "./LoadingIndicator"

function Form ({route, method})
{
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [address, setAddress] = useState("")
    const [phoneNumber, setPhoneNumber] = useState("")
    const [secondaryEmail, setSecondaryEmail] = useState("")
    const [loading, setLoading] = useState(false)
    const navigate = useNavigate()

    const name = method == "login" ? "Login" : "Register"

    const handelSubmit = async (e) =>{
        setLoading(true);
        e.preventDefault();

        const body = method == "login"
            ? {email, password}
            : {email, password, address, phone_number: phoneNumber, secondary_email: secondaryEmail}

        try
        {
            const res = await api.post(route, body)
            if (method == "login")
            {
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
                navigate("/")
            }
            else{
                navigate("/login")
            }
        }
        catch(error)
        {
            alert(error)
        }
        finally
        {
            setLoading(false)
        }
    }
    return <form onSubmit={handelSubmit} className="form-container">
        <h1>{name}</h1>
        <input
            className="form-input"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value) }
            placeholder="Email"
        />
        <input
            className="form-input"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value) }
            placeholder="Password"
        />
        {method == "register" && (
            <>
                <input
                    className="form-input"
                    type="text"
                    value={address}
                    onChange={(e) => setAddress(e.target.value) }
                    placeholder="Address"
                />
                <input
                    className="form-input"
                    type="tel"
                    value={phoneNumber}
                    onChange={(e) => setPhoneNumber(e.target.value) }
                    placeholder="Phone Number"
                />
                <input
                    className="form-input"
                    type="email"
                    value={secondaryEmail}
                    onChange={(e) => setSecondaryEmail(e.target.value) }
                    placeholder="Secondary Email"
                />
            </>
        )}
        {loading && <LoadingIndicator />}
        <button className="form-button" type="submit">{name}</button>
        {method == "login" ? (
            <p className="form-switch">
                Don't have an account? <Link to="/register">Register</Link>
            </p>
        ) : (
            <p className="form-switch">
                Already have an account? <Link to="/login">Login</Link>
            </p>
        )}
    </form>
}

export default Form
