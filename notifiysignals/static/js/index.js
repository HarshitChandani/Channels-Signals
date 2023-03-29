const host = '127.0.0.1'
const port = '8000'


let notification_socket = new WebSocket(`ws://${host}:${port}/ws/connect/`)

const message_queue = []

notification_socket.addEventListener("open",(handler) => {
   console.log("Connection established and opened !")
})

notification_socket.addEventListener("message",(msg) => {
   const msg_obj = JSON.parse(msg.data)
   
   // optional
    
   const unordered_list = document.getElementById("chats")
   const new_item = document.createElement("li")
   new_item.classList.add("list-group-item")
   new_item.appendChild(document.createTextNode(msg_obj.message))
   unordered_list.appendChild(new_item)
})



