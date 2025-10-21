import React, {useState} from "react";
import axios from "axios";

export default function Upload(){
  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");

  const handleUpload = async ()=>{
    const formData = new FormData();
    formData.append("file", file);
    const res = await axios.post("/api/upload", formData);
    setResult(JSON.stringify(res.data));
  }

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-3">Test Event Detection</h1>
      <input type="file" onChange={e=>setFile(e.target.files[0])}/>
      <button onClick={handleUpload} className="bg-blue-600 text-white px-4 py-2 rounded ml-2">Upload</button>
      <pre className="mt-4">{result}</pre>
    </div>
  )
}
