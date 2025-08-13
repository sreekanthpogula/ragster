import uuid
from datetime import datetime

class ChatSession:
    def __init__(self, user_id):
        self.session_id = str(uuid.uuid4())
        self.user_id = user_id
        self.created_at = datetime.utcnow()
        self.messages = []

    def add_message(self, sender, message):
        self.messages.append({
            'timestamp': datetime.utcnow(),
            'sender': sender,
            'message': message
        })

    def get_messages(self):
        return self.messages

# Example usage:
if __name__ == "__main__":
    session = ChatSession(user_id="user123")
    session.add_message(sender="user123", message="Hello!")
    session.add_message(sender="bot", message="Hi, how can I help you?")
    for msg in session.get_messages():
        print(f"[{msg['timestamp']}] {msg['sender']}: {msg['message']}")