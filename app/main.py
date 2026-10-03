def copy_file(command: str) -> None:
    # Handle empty command
    if not command.strip():
        return

    parts = command.split()

    # Validate command format (must have exactly 3 parts: action, source, destination)
    if len(parts) != 3:
        return

    action, source, destination = parts

    # Validate action
    if action != "cp":
        return

    # Skip if source and destination are the same
    if source == destination:
        return

    # Handle missing source file
    try:
        with open(source, "r", encoding="utf-8") as file_in, open(
            destination, "w", encoding="utf-8"
        ) as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
