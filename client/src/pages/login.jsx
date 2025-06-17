
import { useState} from "react"
function Register() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    role: ''
  });

  const handleChange = e => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const res = await fetch('http://localhost:5000/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    });

    const data = await res.json();
    console.log(data);
    if (res.ok) {
      alert("Registered successfully!");
    } else {
      alert("Registration failed: " + data.error);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', width: '300px', gap: '10px' }}>
      <h2>Register</h2>
      <input type="text" name="name" placeholder="Name" onChange={handleChange} required />
      <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
      <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
      <select name="role" onChange={handleChange} required>
        <option value="">Select a role</option>
        <option value="Admin">Admin</option>
        <option value="Staff">Staff</option>
      </select>
      <button type="submit">Register</button>
    </form>
  );
}


function LoginForm() {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });

  const handleChange = e => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await fetch('http://localhost:5000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    });

    const data = await res.json();
    if (res.ok) {
      alert(`Welcome, ${data.user.name}`);
    } else {
      alert("Login failed: " + data.error);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', width: '300px', gap: '10px' }}>
      <h2>Login</h2>
      <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
      <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
      <button type="submit">Login</button>
    </form>
  );
}










function Login() {
  const [myForm, setForm] = useState("login");

  const changeForm = (form) => {
    setForm(form);
    console.log(`form is now: ${form}`);
  };

  return (
    <div
      className="formArea"
      style={{
        backgroundColor: "#f0f0f0",
        padding: "20px",
        borderRadius: "10px",
        width: "350px",
        margin: "50px auto",
        textAlign: "center",
        boxShadow: "0 0 10px rgba(0,0,0,0.1)",
      }}
    >
      <div style={{ marginBottom: "20px" }}>
        <button
          onClick={() => changeForm("login")}
          style={{ marginRight: "10px" }}
        >
          Login
        </button>
        <button onClick={() => changeForm("register")}>Register</button>
      </div>

      {myForm === "login" ? <LoginForm /> : <Register />}
    </div>
  );
}


export default Login