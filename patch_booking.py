with open('templates/book-consultation.html', 'r') as f:
    content = f.read()

content = content.replace("Confirm &amp; Request Consultation &rarr;", "Request Appointment Call &rarr;")

injection = """</form>
                    <p style="font-size: 0.85rem; color: #d97706; margin-top: 12px; font-weight: 500; text-align: center;">Our reception team will call you back within 1 hour (during clinic hours) to confirm your exact appointment slot.</p>"""

content = content.replace("</form>", injection)

with open('templates/book-consultation.html', 'w') as f:
    f.write(content)
