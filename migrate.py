#!/usr/bin/env python3
"""
Migration script to run Alembic commands in Docker container
"""
import subprocess
import sys
import os

def run_command(command):
    """Run a command and return the result"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error: {e.stderr}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python migrate.py <command>")
        print("Commands:")
        print("  init          - Initialize Alembic (first time only)")
        print("  create <msg>   - Create a new migration")
        print("  upgrade       - Apply all pending migrations")
        print("  downgrade     - Rollback last migration")
        print("  history       - Show migration history")
        print("  current       - Show current migration")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "init":
        print("Initializing Alembic...")
        run_command("alembic init alembic")
        
    elif command == "create":
        if len(sys.argv) < 3:
            print("Usage: python migrate.py create <message>")
            sys.exit(1)
        message = sys.argv[2]
        print(f"Creating migration: {message}")
        run_command(f'alembic revision --autogenerate -m "{message}"')
        
    elif command == "upgrade":
        print("Applying migrations...")
        run_command("alembic upgrade head")
        
    elif command == "downgrade":
        print("Rolling back migration...")
        run_command("alembic downgrade -1")
        
    elif command == "history":
        print("Migration history:")
        run_command("alembic history")
        
    elif command == "current":
        print("Current migration:")
        run_command("alembic current")
        
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()





