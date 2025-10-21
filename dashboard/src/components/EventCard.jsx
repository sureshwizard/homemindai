export default function EventCard({label,confidence}){
  return (
    <div className="p-4 border rounded shadow">
      <h3 className="text-lg font-semibold">{label}</h3>
      <p>Confidence: {(confidence*100).toFixed(1)}%</p>
    </div>
  );
}
