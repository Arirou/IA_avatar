memory = []

def add_message(role, content):
    memory.append({
        "role": role,
        "content": content[:300]
    })

def get_history():
    return memory[-10:]

def get_memory_text():
    return " | ".join([f"{m['role']}: {m['content']}" for m in memory[-5:]])

def clear_memory():
    global memory
    memory = []