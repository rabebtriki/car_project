CSS = """
    <style>
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        .header { 
            text-align: center; 
            margin-bottom: 2rem; 
        }
        .nav-container { 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            margin-bottom: 2rem; 
            gap: 1rem; 
        }
        .select-car { 
            padding: 0.5rem; 
            border: 1px solid #e0e0e0; 
            border-radius: 0.5rem; 
            background: white; 
            min-width: 200px; 
        }
        .chat-button { 
            padding: 0.5rem 1rem; 
            border-radius: 0.5rem; 
            border: none; 
            cursor: pointer; 
            display: flex; 
            align-items: center; 
            gap: 0.5rem; 
        }
        .expert-button { 
            background: #1a1a1a; 
            color: white; 
        }
        .car-button { 
            background: white; 
            border: 1px solid #e0e0e0; 
        }
        .car-display { 
            background: #f5f5f5; 
            border-radius: 1rem; 
            padding: 2rem; 
            margin-bottom: 2rem; 
            min-height: 400px; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
        }
        .chat-container { 
            background: white; 
            border-radius: 1rem; 
            padding: 1rem; 
            margin-top: 2rem; 
        }
        .message { 
            padding: 0.75rem 1rem; 
            border-radius: 1rem; 
            margin: 0.5rem 0; 
            display: inline-block; 
            max-width: 80%; 
        }
        .user-message { 
            background: #4285f4; 
            color: white; 
            margin-left: auto; 
        }
        .assistant-message { 
            background: #f0f0f0; 
            color: black; 
        }
        .avatar-container { 
            width: 100px; 
            height: 100px; 
            background: #f0f0f0; 
            border-radius: 50%; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            margin: 1rem auto; 
        }
    </style>
    """