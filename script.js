const API_BASE_URL = 'http://localhost:5000/api';

let terminalOutput = [];

document.addEventListener('DOMContentLoaded', function () {
  initializeTerminal();
  setupEventListeners();
});

function initializeTerminal() {
  terminalOutput = []; 
  updateTerminalOutput();
}

function updateTerminalOutput() {
  const outputElement = document.getElementById('terminal-output');
  outputElement.innerHTML = terminalOutput.map(line => `<div>${line}</div>`).join('');
  outputElement.scrollTop = outputElement.scrollHeight;
}

async function handleTerminalCommand(command) {

  terminalOutput.push(`userName@secureSystem:~$ ${command}`);

  if (command.toLowerCase() === 'clear') {
    terminalOutput = [];
    updateTerminalOutput();
    document.getElementById('terminal-input').value = '';
    return;
  }

  try {
    const response = await fetch(`${API_BASE_URL}/command`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ command }),
    });
    const data = await response.json();
    terminalOutput.push(data.output);
  } catch (error) {
    terminalOutput.push(`Error: ${error.message}`);
  }

  updateTerminalOutput();
  document.getElementById('terminal-input').value = '';
}

function setupEventListeners() {
  const terminalInput = document.getElementById('terminal-input');
  terminalInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter' && this.value.trim()) {
      handleTerminalCommand(this.value.trim());
    }
  });
}