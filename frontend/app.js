const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("userInput");
const chatBox = document.getElementById("messages");

const API_URL = "http://127.0.0.1:5000/chat";

function addMessage(role, text) {
    const message = document.createElement("div");
    message.classList.add("msg", role);
    message.innerText = text;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Botón enviar
document.getElementById("sendBtn").addEventListener("click", sendMessage);

// Enter para enviar
userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
});

async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    addMessage("user", message);
    userInput.value = "";

    addMessage("bot", "Pensando...");

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ mensaje: message })
        });

        const data = await response.json();

        // Eliminar "Pensando..."
        chatBox.removeChild(chatBox.lastChild);

        if (data.respuesta) {
            addMessage("bot", data.respuesta);
        } else {
            addMessage("bot", "Hubo un error.");
        }

    } catch (error) {
        console.error("Error:", error);
        addMessage("bot", "Error de conexión.");
    }
}

// ===== MODO OSCURO =====
const toggleDark = document.getElementById("toggleDark");
toggleDark.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");

    // cambiar ícono
    toggleDark.textContent = document.body.classList.contains("dark-mode") ? "☀️" : "🌙";
});
