const BASE = 'http://localhost:8000';
const messagesEl = document.getElementById('messages');
const inputEl = document.getElementById('input');
const sendBtn = document.getElementById('send');

function addMessage(text, who='bot', meta='') {
  const m = document.createElement('div');
  m.className = 'message ' + who;
  const b = document.createElement('div');
  b.className = 'bubble';
  b.textContent = text;
  m.appendChild(b);
  if(meta) {
    const small = document.createElement('div');
    small.className = 'small';
    small.textContent = meta;
    m.appendChild(small);
  }
  messagesEl.appendChild(m);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

sendBtn.addEventListener('click', async () => {
  const text = inputEl.value.trim();
  if (!text) return;
  addMessage(text, 'user');
  inputEl.value = '';
  try {
    const payload = { user_id: 'user_123', message: text, latitude: 28.6139, longitude: 77.2090 };
    const res = await fetch(`${BASE}/chat`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(payload)
    });
    if (!res.ok) {
      const err = await res.json();
      addMessage('Server error: ' + (err.detail || res.statusText), 'bot');
      return;
    }
    const data = await res.json();
    addMessage(data.reply, 'bot', `Sources: ${data.sources ? data.sources.map(s => s.title || s.id).join(', ') : 'none'}`);
  } catch (e) {
    addMessage('Network error: ' + e.message, 'bot');
  }
});

inputEl.addEventListener('keydown', (e) => { if (e.key === 'Enter') sendBtn.click(); });
