function getBotResponse(input) {
    // This is a placeholder function to simulate a response. 
    // You would replace this with an API call to your backend once it's available.
    const simpleResponses = {
        "hello": "Hi there! How can I assist you today?",
        "where is the ILC?": "The ILC is located on Union and Division street."
        // Add more predefined responses here
    };

    return simpleResponses[input.toLowerCase()] || "I'm not sure how to answer that yet.";
}

document.getElementById('submit-btn').addEventListener('click', function() {
    const userInputField = document.getElementById('user-input');
    const userInput = userInputField.value.trim();

    if (userInput) {
        appendMessage(userInput, 'user-message');

        const botResponse = getBotResponse(userInput); // Simulate a bot response
        appendMessage(botResponse, 'bot-message');

        userInputField.value = ''; // Clear the input field
    }
});

document.getElementById('submit-btn').addEventListener('click', sendMessage);

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() !== '') {
        appendMessage(userInput, 'user-message');
        // Call your backend API to get a response
        // For the example, we'll just echo the user message
        appendMessage('Echo: ' + userInput, 'bot-message');
        document.getElementById('user-input').value = ''; // Clear the input field
    }
}

function appendMessage(text, className) {
    const chatBox = document.getElementById('chat-box');
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', className);
    msgDiv.textContent = text;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}