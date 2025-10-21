import React, {useState, useEffect} from "react";
import axios from "axios";
import EventCard from "../components/EventCard";

export default function Dashboard(){
  const [events, setEvents] = useState([]);

  useEffect(()=>{ axios.get("/api/status").then(r=>setEvents([{label:"System Ready",confidence:1.0}])) },[]);

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-4">HomeMindAI Dashboard</h1>
      <div className="grid grid-cols-3 gap-4">
        {events.map((e,i)=><EventCard key={i} label={e.label} confidence={e.confidence}/>)}
      </div>
    </div>
  )
}
