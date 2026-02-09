import { useState, useEffect } from 'react';

function ToDoList() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    async function getTasks() {
      const res = await fetch('tasks.txt');
      const text = await res.text();
      setTasks(text.split('\n'));
    }
    getTasks();
  }, []);

  return (
    <div>
      {tasks.map((line, i) => {
        const [user, task, status] = line.split(',');
        return (
          <p key={i} style={{ textDecoration: status === 'done' ? 'line-through' : 'none' }}>
            {user}: {task} ({status})
          </p>
        ); 
      })}
    </div>
  );
}

export default ToDoList;