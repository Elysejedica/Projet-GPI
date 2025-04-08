#!/usr/bin/env python
import os
import sys

def main():
    """Point d’entrée principal du script de gestion Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bibliotheque.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible d'importer Django. Es-tu sûr qu'il est installé "
            "et disponible dans ton environnement virtuel ?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
