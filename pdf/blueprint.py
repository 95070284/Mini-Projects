from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

styles = getSampleStyleSheet()

pdf = SimpleDocTemplate("my_assistant_mvp.pdf")

elements = []

# Title
elements.append(Paragraph("<b>🚀 My Assistant — MVP Blueprint</b>", styles['Title']))
elements.append(Spacer(1,20))

def add_heading(text):
    elements.append(Paragraph(f"<b>{text}</b>", styles['Heading2']))
    elements.append(Spacer(1,10))

def add_text(text):
    elements.append(Paragraph(text, styles['Normal']))
    elements.append(Spacer(1,8))

def create_box(title, lines):

    data = [[Paragraph(f"<b>{title}</b>", styles["Heading3"])]]

    for line in lines:
        data.append([line])

    table = Table(data, colWidths=450)

    table.setStyle(TableStyle([
        ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),
        ("BOX",(0,0),(-1,-1),1,colors.grey),
        ("LEFTPADDING",(0,0),(-1,-1),8),
        ("RIGHTPADDING",(0,0),(-1,-1),8),
        ("TOPPADDING",(0,0),(-1,-1),5),
        ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ]))

    elements.append(table)
    elements.append(Spacer(1,20))


# Section 1
add_heading("1️⃣ MVP Goal")

add_text("MVP ka main goal: User ko ek AI assistant dena jo:")
add_text("• AI se chat kar sake")
add_text("• apni chat history dekh sake")
add_text("• tasks save kar sake")
add_text("• assistant user ko thoda yaad rakhe")
add_text("Bas. Extra complex features abhi nahi.")

# Section 2
add_heading("2️⃣ MVP Core Features")

add_text("1️⃣ User Authentication")
add_text("signup kare, login kare")
add_text("Data: name, email, password")

add_text("2️⃣ AI Chat Assistant")
add_text("User: Hello / Explain JavaScript")
add_text("Flow: User → Backend → AI API → Response → User")

add_text("3️⃣ Chat History")
add_text("User apni purani chats dekh sake")

add_text("Example:")
add_text("User: What is Python")
add_text("Assistant: Python is a programming language")

add_text("4️⃣ Task Manager")
add_text("Study JavaScript")
add_text("Drink medicine")
add_text("Complete project")

add_text("5️⃣ Basic Memory System")
add_text("Example: My goal is to become a software developer")

# Pages
add_heading("3️⃣ Pages (UI Structure)")

add_text("1️⃣ Login / Signup")
add_text("2️⃣ Dashboard (today tasks, quick chat, recent chats)")
add_text("3️⃣ Chat Page")
add_text("4️⃣ Tasks Page")

# Tech stack
add_heading("4️⃣ Tech Stack")

add_text("Frontend: HTML, CSS, JavaScript (later React)")
add_text("Backend: Node.js, Express.js")
add_text("Database: MongoDB")
add_text("AI: OpenAI API")

# Database Structure Boxes
add_heading("5️⃣ Database Structure")

create_box("Users",[
"id",
"name",
"email",
"password"
])

create_box("Chats",[
"id",
"user_id",
"message",
"role",
"timestamp"
])

create_box("Tasks",[
"id",
"user_id",
"task",
"status",
"date"
])

create_box("Memories",[
"id",
"user_id",
"type",
"content"
])

# Backend API
add_heading("6️⃣ Backend API Structure")

add_text("POST /signup")
add_text("POST /login")
add_text("POST /chat")
add_text("GET /history")
add_text("POST /task")
add_text("GET /tasks")
add_text("POST /memory")

# Timeline
add_heading("7️⃣ Development Timeline")

add_text("Week 1: login/signup, database setup")
add_text("Week 2: AI chat, API integration")
add_text("Week 3: chat history, task manager")
add_text("Week 4: memory system, dashboard")

# Launch
add_heading("8️⃣ MVP Launch")

add_text("Launch after 30–40 days")
add_text("Friends ko use karne do, feedback lo, improve karo")

# Future features
add_heading("9️⃣ Future Features")

add_text("voice assistant")
add_text("smart reminders")
add_text("AI daily planning")
add_text("habit tracker")
add_text("mobile app")

# Smart memory
add_heading("⚡ Smart AI Memory")

add_text("Talib usually studies at night")
add_text("Talib is learning programming")
add_text("Talib prefers short explanations")

pdf.build(elements)

print("PDF successfully created!")