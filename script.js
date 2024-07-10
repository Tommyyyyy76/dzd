document.getElementById("button").addEventListener('click',function(){
    const task = document.getElementById("task");
    const taskText= task.value;
  
    if (taskText !== " "){
      const li = document.createElement("li");
      
      
      li.textContent = taskText;
      
      li.addEventListener('click', function(){
        li.remove();
      
      })
      document.getElementById("list").appendChild(li);
      taskInput.value = " ";
    }
  })

  const username = prompt('Quel est votre nom?');

  const date = new Date();
  date.setMonth(date.getMonth()+1);

  document.cookie = `username=${username} ; expires=${date.toUTCString()}`;

  console.log(document.cookie);

  var element = document.getElementById('h');
  element.innerHTML = "Bienvenue "+ username;

  const btn = document.getElementById('btn').addEventListener('click',function(){
    window.open('./index2.html');
  })