
function displayResponseMessage(input){
    let newMessage = document.createElement("pre");
    newMessage.classList.add("response-message");
    newMessage.innerHTML = input.response;

    let messageContainer = document.createElement("div");
    messageContainer.classList.add("user-message-container")
    messageContainer.appendChild(newMessage);
    console.log('messageContainer', messageContainer)

    let output = document.getElementById("conversation-space");
    output.appendChild(messageContainer);
}

function displayUserMessage(userMessage){
   
    let newMessage = document.createElement("p");
    newMessage.classList.add("user-message");
    newMessage.innerHTML = userMessage;
    let messageContainer = document.createElement("div");
    messageContainer.classList.add("user-message-container")
    messageContainer.appendChild(newMessage);
    console.log('messageContainer', messageContainer)
    let output = document.getElementById("conversation-space");
    output.appendChild(messageContainer);

}

function send(){
    
    let prompt_content = document.getElementById("input").value
    document.getElementById("input").value = ""
    displayUserMessage(prompt_content)
    console.log('prompt content', prompt_content)
    let content = 
        {
            "prompt": prompt_content,
        }
    let config = 
        {
            type: "POST",
            url:  'prompt/',
            data: content,
            dataType: 'json',
            success: displayResponseMessage
        };
        
    $.ajax(config);
}


function handleKeyDown(event) {
    if (event.key === "Enter") {
      event.preventDefault();
      send();
    }
  }