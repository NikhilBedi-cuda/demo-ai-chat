#!/usr/bin/env python3
"""
Convert SETUP_GUIDE.md to Word document (.docx)
"""

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import re

# Read the markdown file
with open('/workspaces/demo-ai-chat/SETUP_GUIDE.md', 'r') as f:
    content = f.read()

# Create a new Word document
doc = Document()

# Add title
title = doc.add_heading('AI Chat Application - Complete Setup Guide', level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Add overview
doc.add_heading('Overview', level=1)
doc.add_paragraph('This guide explains how to set up and configure the demo-ai-chat application from scratch. This is a web-based chatbot that uses OpenAI\'s ChatGPT with security checks through Cisco AI Defense.')

# Add table of contents
doc.add_heading('Table of Contents', level=1)
toc_items = [
    'Project Architecture',
    'Configuration Files Explained',
    'Step-by-Step Setup',
    'How Everything Works Together',
    'Troubleshooting'
]
for item in toc_items:
    doc.add_paragraph(item, style='List Number')

# Project Architecture Section
doc.add_heading('Project Architecture', level=1)

doc.add_heading('What This App Does', level=2)
doc.add_paragraph('User (Browser) → Beautiful Chat UI (HTML/CSS/JavaScript) → Express Server (Node.js) → Cisco AI Defense (Security Check) → OpenAI ChatGPT (AI Response Generation) → Response back to User')

doc.add_heading('Project Structure', level=2)
structure_text = '''demo-ai-chat/
├── index.js                 # Main server file
├── package.json             # Project dependencies
├── .env                     # Environment variables (API keys)
├── public/
│   └── index.html          # Chat UI interface
├── node_modules/           # Installed packages
└── README.md               # Project documentation'''
doc.add_paragraph(structure_text, style='List Bullet')

# Configuration Files Section
doc.add_heading('Configuration Files Explained', level=1)

# package.json
doc.add_heading('1. package.json - Project Metadata & Dependencies', level=2)
doc.add_paragraph('Location: /workspaces/demo-ai-chat/demo-ai-chat/package.json', style='Heading 3')
doc.add_heading('What it does:', level=3)
bullets = [
    'Defines project name, version, and description',
    'Lists all required libraries (dependencies)',
    'Defines scripts to run the application'
]
for bullet in bullets:
    doc.add_paragraph(bullet, style='List Bullet')

doc.add_heading('Key dependencies explained:', level=3)
deps_text = '''express (^5.1.0) - Web server framework
axios (^1.13.2) - HTTP client for API calls
dotenv (^17.2.3) - Loads environment variables
openai (^6.9.1) - OpenAI API client'''
doc.add_paragraph(deps_text)

# .env file
doc.add_heading('2. .env - Sensitive Configuration (API Keys)', level=2)
doc.add_paragraph('Location: /workspaces/demo-ai-chat/demo-ai-chat/.env')
doc.add_heading('What it does:', level=3)
bullets = [
    'Stores sensitive information (API keys, endpoints)',
    'Never committed to Git (for security)',
    'Loaded at application startup'
]
for bullet in bullets:
    doc.add_paragraph(bullet, style='List Bullet')

doc.add_heading('Structure:', level=3)
env_text = '''OPENAI_API_KEY=sk-proj-xxxxxx...
CISCO_AI_DEFENSE_ENDPOINT=https://us-west.ciscoaidefense.com/api/v1/inspect
CISCO_API_KEY=485a4380d4af...'''
doc.add_paragraph(env_text)

# Add table for environment variables
doc.add_heading('Each variable explained:', level=3)
table = doc.add_table(rows=4, cols=3)
table.style = 'Light Grid Accent 1'
header_cells = table.rows[0].cells
header_cells[0].text = 'Variable'
header_cells[1].text = 'Purpose'
header_cells[2].text = 'Example'

rows_data = [
    ('OPENAI_API_KEY', 'Authentication token for OpenAI API', 'sk-proj-... (from platform.openai.com)'),
    ('CISCO_AI_DEFENSE_ENDPOINT', "URL to Cisco's security service", 'https://us-west.ciscoaidefense.com/api/v1/inspect'),
    ('CISCO_API_KEY', 'Authentication for Cisco service', '485a4380d4af... (from Cisco console)')
]

for i, row_data in enumerate(rows_data, 1):
    row_cells = table.rows[i].cells
    row_cells[0].text = row_data[0]
    row_cells[1].text = row_data[1]
    row_cells[2].text = row_data[2]

# Security note
doc.add_paragraph('Security note:', style='Heading 3')
security_bullets = [
    'Never share these keys',
    'Never commit .env to version control',
    '.gitignore prevents accidental commits'
]
for bullet in security_bullets:
    doc.add_paragraph(bullet, style='List Bullet')

# index.js
doc.add_heading('3. index.js - Main Application Code', level=2)
doc.add_paragraph('Location: /workspaces/demo-ai-chat/demo-ai-chat/index.js')
doc.add_heading('What it does:', level=3)
bullets = [
    'Sets up the Express web server',
    'Defines API endpoints',
    'Handles request/response flow'
]
for bullet in bullets:
    doc.add_paragraph(bullet, style='List Bullet')

# public/index.html
doc.add_heading('4. public/index.html - Chat User Interface', level=2)
doc.add_paragraph('Location: /workspaces/demo-ai-chat/demo-ai-chat/public/index.html')
doc.add_heading('What it does:', level=3)
bullets = [
    'Provides the beautiful chat interface users see',
    'Sends/receives messages via JavaScript'
]
for bullet in bullets:
    doc.add_paragraph(bullet, style='List Bullet')

doc.add_heading('Key features:', level=3)
features = [
    'Modern gradient design (purple theme)',
    'Real-time message display',
    'Typing indicator animation',
    'Error handling',
    'Responsive mobile design'
]
for feature in features:
    doc.add_paragraph(feature, style='List Bullet')

# Step-by-Step Setup
doc.add_heading('Step-by-Step Setup', level=1)

doc.add_heading('Step 0: Prerequisites', level=2)
prereq_text = 'You need: GitHub Codespaces environment, Node.js installed, OpenAI API key (free to create), Cisco AI Defense credentials (optional for testing)'
doc.add_paragraph(prereq_text)

doc.add_heading('Step 1: Get OpenAI API Key', level=2)
doc.add_paragraph('What: Authentication to access ChatGPT')
doc.add_heading('Steps:', level=3)
steps = [
    'Go to https://platform.openai.com/api-keys',
    'Sign in with your OpenAI account (create one if needed)',
    'Click "Create new secret key"',
    'Copy the key (starts with sk-proj-)',
    'Keep this safe - never share it'
]
for i, step in enumerate(steps, 1):
    doc.add_paragraph(step, style='List Number')

doc.add_heading('Step 2: Get Cisco AI Defense Credentials (Optional)', level=2)
doc.add_paragraph('What: Security layer to scan prompts for harmful content')
doc.add_heading('Steps:', level=3)
cisco_steps = [
    'Go to https://www.cisco.com/site/us/en/products/security/cloud-security/ai-defense/',
    'Sign up for a trial account',
    'Get your API endpoint and key from the console',
    'Note the regional endpoint (e.g., us-west, us-east)'
]
for i, step in enumerate(cisco_steps, 1):
    doc.add_paragraph(step, style='List Number')

doc.add_heading('Step 3: Create .env File', level=2)
doc.add_paragraph('What: File that stores your API keys securely')
doc.add_heading('Steps:', level=3)
doc.add_paragraph('Create a new file: /workspaces/demo-ai-chat/demo-ai-chat/.env', style='List Number')
doc.add_paragraph('Add the following:', style='List Number')
env_content = '''OPENAI_API_KEY=sk-proj-your_key_here
CISCO_AI_DEFENSE_ENDPOINT=https://us-west.ciscoaidefense.com/api/v1/inspect
CISCO_API_KEY=your_cisco_key_here'''
doc.add_paragraph(env_content)

doc.add_heading('Step 4: Install Dependencies', level=2)
doc.add_paragraph('What: Download all required libraries')
doc.add_heading('Command:', level=3)
doc.add_paragraph('cd /workspaces/demo-ai-chat/demo-ai-chat\nnpm install')

doc.add_heading('Step 5: Start the Server', level=2)
doc.add_heading('Command:', level=3)
doc.add_paragraph('npm start')

doc.add_heading('Step 6: Access the App', level=2)
doc.add_paragraph('In GitHub Codespaces:', style='Heading 3')
access_steps = [
    'Look for port 3000 in the "Ports" tab',
    'Click the globe icon to open the forwarded URL',
    'You\'ll see the chat interface'
]
for step in access_steps:
    doc.add_paragraph(step, style='List Bullet')

# Troubleshooting
doc.add_heading('Troubleshooting', level=1)

issues = [
    {
        'title': 'Issue: "Cannot GET /"',
        'cause': 'Server not running or wrong port',
        'solutions': [
            'Run npm start',
            'Check that it says "Server running on port 3000"',
            'Refresh browser'
        ]
    },
    {
        'title': 'Issue: "OpenAI request failed"',
        'cause': 'Invalid API key',
        'solutions': [
            'Check your OpenAI API key in .env',
            'Verify it starts with sk-proj-',
            'Get a new key from platform.openai.com'
        ]
    },
    {
        'title': 'Issue: "Cisco inspection failed"',
        'cause': 'Invalid Cisco credentials or no internet',
        'solutions': [
            'Verify Cisco endpoint and key in .env',
            'Check your Cisco account is active',
            'Comment out Cisco section for development'
        ]
    }
]

for issue in issues:
    doc.add_heading(issue['title'], level=2)
    doc.add_paragraph(f"Cause: {issue['cause']}")
    doc.add_paragraph('Solution:', style='Heading 3')
    for solution in issue['solutions']:
        doc.add_paragraph(solution, style='List Bullet')

# Key Takeaways
doc.add_heading('Key Takeaways', level=1)
takeaways = [
    'Configuration files tell the app: How to run (package.json), Where to find secrets (.env), What services to use (index.js)',
    'API keys are sensitive: Never commit to Git, Never share publicly, Use .env files',
    'The app follows a simple flow: Request → Validate → Process → Response',
    'Cisco + OpenAI = Secure AI: Cisco checks for threats, OpenAI generates responses, User gets safe, intelligent answers'
]
for takeaway in takeaways:
    doc.add_paragraph(takeaway, style='List Bullet')

# Glossary
doc.add_heading('Glossary', level=1)
glossary_table = doc.add_table(rows=11, cols=2)
glossary_table.style = 'Light Grid Accent 1'

header_cells = glossary_table.rows[0].cells
header_cells[0].text = 'Term'
header_cells[1].text = 'Meaning'

glossary_terms = [
    ('API', 'Application Programming Interface - way apps communicate'),
    ('Express', 'Web server framework for Node.js'),
    ('Endpoint', 'URL where server accepts requests (e.g., /chat)'),
    ('Authentication', 'Proving who you are with credentials'),
    ('Port', 'Virtual connection point (e.g., 3000)'),
    ('Localhost', 'Your computer (127.0.0.1)'),
    ('Dependency', 'External library your app needs'),
    ('Environment Variable', 'Configuration stored in .env file'),
    ('Response', 'Data returned by server'),
    ('Payload', 'Data sent in a request')
]

for i, (term, meaning) in enumerate(glossary_terms, 1):
    row_cells = glossary_table.rows[i].cells
    row_cells[0].text = term
    row_cells[1].text = meaning

# Support & Resources
doc.add_heading('Support & Resources', level=1)
resources = [
    'OpenAI Docs: https://platform.openai.com/docs',
    'Express.js Docs: https://expressjs.com',
    'Cisco AI Defense: https://www.cisco.com/site/us/en/products/security/cloud-security/ai-defense/',
    'Node.js Docs: https://nodejs.org/docs'
]
for resource in resources:
    doc.add_paragraph(resource, style='List Bullet')

# Save the document
output_path = '/workspaces/demo-ai-chat/SETUP_GUIDE.docx'
doc.save(output_path)
print(f"Word document created successfully: {output_path}")
