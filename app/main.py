def copy_file(command: str) -> None:
    _, source, destination = command.split()

    if source == destination:
        return

    with open(source, "r", encoding="utf-8") as file_in, open(
        destination, "w", encoding="utf-8"
    ) as file_out:
        file_out.write(file_in.read())
