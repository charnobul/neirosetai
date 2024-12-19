async function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
    });
    const data = await response.json();
    const messages = document.getElementById("messages");
    const userMessage = document.createElement("div");
    userMessage.className = "message";
    userMessage.textContent = "You: " + userInput;
    messages.appendChild(userMessage);
    const botMessage = document.createElement("div");
    botMessage.className = "message";
    botMessage.textContent = "Bot: " + data.response;
    messages.appendChild(botMessage);
    document.getElementById("userInput").value = "";
}
