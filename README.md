# Gestor de Tareas CLI

Un proyecto en Python que implementa un CRUD (Crear, Leer, Actualizar, Eliminar) de tareas a través de una interfaz de línea de comandos (CLI), utilizando un archivo JSON para la persistencia de datos. El diseño sigue principios SOLID y una arquitectura limpia para garantizar modularidad, escalabilidad y mantenibilidad.

## Estructura del Proyecto

```
task_manager/
├── src/
│   ├── domain/
│   │   ├── entities/
│   │   │   └── task.py
│   │   └── interfaces/
│   │       ├── task_repository.py
│   │       └── task_service.py
│   ├── application/
│   │   └── task_service_impl.py
│   ├── infrastructure/
│   │   └── json_task_repository.py
│   ├── presentation/
│   │   └── task_cli.py
│   └── main.py
├── data/
│   └── tasks.json
├── tests/
│   ├── test_task.py
│   ├── test_task_service.py
│   └── test_json_task_repository.py
├── README.md
└── requirements.txt
```

## Requisitos

- Python 3.6 o superior
- Opcional: `pytest` para ejecutar pruebas unitarias

## Instalación

1. Clona el repositorio o copia los archivos a tu máquina.
2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - En Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - En Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
4. Instala las dependencias (si usas pruebas):
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

1. Navega al directorio raíz del proyecto:
   ```bash
   cd task_manager
   ```
2. Ejecuta el programa:
   ```bash
   python -m src.main
   ```
3. Sigue las instrucciones del menú interactivo para gestionar tareas.

## Ejecución de Pruebas

Si deseas ejecutar las pruebas unitarias:
```bash
pytest tests/
```

## Uso

El programa presenta un menú interactivo con las siguientes opciones:
1. **Agregar Tarea**: Crea una nueva tarea con título y descripción.
2. **Listar Tareas**: Muestra todas las tareas con su ID, título, estado y fecha de creación.
3. **Actualizar Tarea**: Modifica el título y descripción de una tarea existente.
4. **Eliminar Tarea**: Elimina una tarea por su ID.
5. **Completar Tarea**: Marca una tarea como completada.
6. **Salir**: Cierra la aplicación.

Las tareas se guardan automáticamente en `data/tasks.json`.

## Conceptos Practicados

Este proyecto se diseñó para practicar y aplicar los siguientes conceptos y principios:

### Principios SOLID
- **Single Responsibility Principle (SRP)**: Cada clase tiene una única responsabilidad:
  - `Task`: Representa la entidad de tarea.
  - `JsonTaskRepository`: Maneja la persistencia en JSON.
  - `TaskServiceImpl`: Gestiona la lógica de negocio.
  - `TaskCLI`: Administra la interfaz de usuario.
- **Open/Closed Principle (OCP)**: El sistema es extensible mediante interfaces (`TaskRepository`, `TaskService`) sin modificar el código existente.
- **Liskov Substitution Principle (LSP)**: Las implementaciones de interfaces pueden sustituirse sin alterar el comportamiento.
- **Interface Segregation Principle (ISP)**: Las interfaces son específicas y no obligan a implementar métodos innecesarios.
- **Dependency Inversion Principle (DIP)**: Las dependencias se basan en abstracciones, no en implementaciones concretas.

### Arquitectura Limpia
- **Separación de capas**: El proyecto está organizado en capas claras:
  - **Domain**: Entidades (`Task`) e interfaces (`TaskRepository`, `TaskService`).
  - **Application**: Lógica de negocio (`TaskServiceImpl`).
  - **Infrastructure**: Persistencia (`JsonTaskRepository`).
  - **Presentation**: Interfaz de usuario (`TaskCLI`).
- **Modularidad**: Cada componente está encapsulado, facilitando la extensibilidad (por ejemplo, cambiar JSON por una base de datos).
- **Inyección de dependencias**: Las dependencias se inyectan en el constructor (por ejemplo, `TaskService` en `TaskCLI`).

### Otros Conceptos
- **Persistencia de datos**: Uso de JSON para almacenar tareas de forma persistente.
- **Manejo de excepciones**: Gestión de errores en operaciones de entrada/salida y entrada de usuario.
- **Tipado estático**: Uso de anotaciones de tipo (`typing`) para mejorar la legibilidad y robustez.
- **Estructura modular**: Organización en carpetas con archivos `__init__.py` para importar módulos correctamente.
- **Pruebas unitarias**: Estructura preparada para pruebas con `pytest` (aunque las pruebas son opcionales).

## Notas Adicionales
- Asegúrate de que los archivos `__init__.py` estén presentes en todas las carpetas de `src` para que las importaciones funcionen correctamente.
- Si encuentras errores como `ModuleNotFoundError`, verifica que estás ejecutando el comando `python -m src.main` desde el directorio raíz (`task_manager`).