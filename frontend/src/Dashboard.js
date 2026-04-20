import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Dashboard() {
  const [data, setData] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await axios.get("http://127.0.0.1:8000/api/dashboard/", {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        });

        setData(res.data.message);
      } catch {
        navigate("/");
      }
    };

    fetchData();
  }, []);

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <div className="container mt-5">
      <div className="card p-4 shadow text-center">
        <h2>Dashboard</h2>
        <p className="mt-3">{data}</p>

        <button className="btn btn-danger mt-3" onClick={logout}>
          Logout
        </button>
      </div>
    </div>
  );
}

export default Dashboard;