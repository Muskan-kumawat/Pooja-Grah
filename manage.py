#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'panditMitra.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
# #!/usr/bin/env python
# """Flask's command-line utility for administrative tasks."""
# import os
# import sys

# from flask.cli import FlaskGroup

# # Import your Flask application
# from main import create_app

# def main():
#     """Run administrative tasks."""
#     # Set the Flask application instance
#     app = create_app()

#     # Create a FlaskGroup instance to handle command-line tasks
#     cli = FlaskGroup(app)

#     # Add your command-line commands here if needed

#     # Run the FlaskGroup instance with the provided arguments
#     cli()

# if __name__ == '__main__':
#     main()
