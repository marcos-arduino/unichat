# Unichat - Chat Multiusuario

Arquitectura completa del proyecto:

```
unichat/
│
├── backend/
│   ├── main.py                    # FastAPI app principal
│   ├── requirements.txt           # Dependencias Python
│   ├── Dockerfile                # Configuración Docker
│   ├── .env                      # Variables de entorno
│   └── app/
│       ├── __init__.py
│       ├── config.py             # Configuración general
│       ├── database.py           # Conexión a base de datos
│       ├── main.py               # FastAPI app con routers
│       ├── models/               # Modelos SQLAlchemy
│       │   ├── __init__.py
│       │   ├── user.py          # Modelo User
│       │   ├── message.py       # Modelo Message
│       │   ├── room.py          # Modelo Room y RoomMember
│       │   └── base.py          # Base declarativa
│       ├── schemas/              # Pydantic schemas
│       │   ├── __init__.py
│       │   ├── user.py          # UserCreate, UserResponse, Token
│       │   ├── message.py       # MessageCreate, MessageResponse
│       │   └── room.py          # RoomCreate, RoomResponse
│       ├── routers/              # Endpoints API
│       │   ├── __init__.py
│       │   ├── auth.py          # Login, register, token refresh
│       │   ├── users.py         # CRUD usuarios
│       │   ├── messages.py      # CRUD mensajes
│       │   └── rooms.py         # CRUD salas
│       ├── services/             # Lógica de negocio
│       │   ├── __init__.py
│       │   ├── auth_service.py  # JWT, password hashing
│       │   ├── message_service.py # Lógica mensajes
│       │   └── room_service.py  # Lógica salas
│       ├── websockets/           # Conexiones en tiempo real
│       │   ├── __init__.py
│       │   ├── connection_manager.py # Gestor de conexiones
│       │   └── handlers.py      # Eventos WebSocket
│       └── utils/                # Utilidades
│           ├── __init__.py
│           ├── security.py      # Funciones seguridad
│           └── dependencies.py  # Dependencias FastAPI
│
├── frontend/
│   ├── package.json              # Dependencias Node
│   ├── vite.config.js           # Configuración Vite
│   ├── index.html               # HTML base
│   ├── public/                  # Assets estáticos
│   └── src/
│       ├── main.jsx             # Punto entrada React
│       ├── App.jsx              # App principal
│       ├── components/          # Componentes UI
│       │   ├── Chat/
│       │   │   ├── ChatRoom.jsx
│       │   │   ├── MessageList.jsx
│       │   │   ├── MessageInput.jsx
│       │   │   └── UserList.jsx
│       │   ├── Auth/
│       │   │   ├── Login.jsx
│       │   │   └── Register.jsx
│       │   └── Layout/
│       │       ├── Header.jsx
│       │       └── Sidebar.jsx
│       ├── hooks/               # Hooks personalizados
│       │   ├── useAuth.js
│       │   ├── useWebSocket.js
│       │   └── useChat.js
│       ├── services/            # API calls
│       │   ├── api.js          # Configuración axios
│       │   ├── authService.js
│       │   ├── messageService.js
│       │   └── roomService.js
│       ├── store/               # Estado global
│       │   ├── authStore.js
│       │   ├── chatStore.js
│       │   └── index.js
│       └── styles/              # CSS/estilos
│           ├── globals.css
│           └── components/
│
├── docker-compose.yml           # Orquestación Docker
└── .gitignore                  # Ignorar archivos
```

## Tecnologías

### Backend
- **FastAPI**: Framework web Python
- **SQLAlchemy**: ORM base de datos
- **PostgreSQL**: Base de datos principal con soporte JSONB
- **Redis**: Cache y sesiones
- **WebSocket**: Comunicación en tiempo real
- **JWT**: Autenticación
- **Pydantic**: Validación datos
- **WhatsApp Business API**: Integración mensajería

### Frontend
- **React**: Framework UI
- **Vite**: Build tool
- **TailwindCSS**: Estilos
- **Zustand**: Estado global
- **Axios**: HTTP client
- **WebSocket API**: Conexión real-time

## Flujo de datos con WhatsApp Integration

```
CLIENTE (ALUMNO) → WhatsApp Business API → Webhook FastAPI → PostgreSQL → WebSocket → Profesores (React)
                      ↑
              Respuesta Profesor → FastAPI → WhatsApp API → CLIENTE
```

1. **Entrada WhatsApp**: Webhook recibe mensaje → Guarda en DB → Broadcast WebSocket
2. **Asignación**: Sistema asigna conversación a profesor disponible
3. **Respuesta**: Profesor responde desde web → Backend envía a WhatsApp
4. **Estados**: Sincronización de delivered/read desde webhooks WhatsApp

## Características principales

- ✅ Chat en tiempo real con WebSocket
- ✅ Integración WhatsApp Business API
- ✅ Sistema de atención centralizada
- ✅ Asignación automática de conversaciones
- ✅ Múltiples profesores/administradores
- ✅ Historial completo de mensajes
- ✅ Estados de entrega WhatsApp (sent/delivered/read)
- ✅ Soporte multimedia (imágenes, audio, video)
- ✅ Autenticación de usuarios con roles
- ✅ Estados de usuario (online/offline)
- ✅ Sistema de notificaciones en tiempo real
- ✅ Respuestas a mensajes
- ✅ Reacciones emoji
