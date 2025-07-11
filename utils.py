from fpdf import FPDF

class ChatPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.set_font("Arial", size=12)

    def add_message(self, sender, message):
        # Apply distinct color styles
        if sender == "user":
            self.set_text_color(60, 60, 60)  # dark gray
        else:
            self.set_text_color(0, 102, 204)  # assistant: deep blue
        
        # Sender label
        self.set_font("Arial", 'B', 12)
        self.cell(0, 10, f"{sender.capitalize()}:", ln=True)
        
        # Message body
        self.set_font("Arial", '', 12)
        self.multi_cell(0, 10, message, border=0)
        self.ln(2)

def export_chat_to_pdf(chat_history, filename="chat_log.pdf"):
    pdf = ChatPDF()
    for msg in chat_history:
        role = "user" if msg.role == "user" else "assistant"
        pdf.add_message(role, msg.parts[0].text)
    pdf.output(filename)
    return filename
