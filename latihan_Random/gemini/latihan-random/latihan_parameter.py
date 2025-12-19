def process_system_log(message, level='INFO', *tags, **config):
    print(f"--Memproses log dengan level {level}")
    print(f"--Tags: {tags}")
    print(f"--Config: {config}")
    print(f"--Pesan: {message}")

    if tags:
        pass