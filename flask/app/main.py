from docker_manager import DockerManager


if __name__ == "__main__":
    manager = DockerManager()

    print(manager.is_image_exist("mysql", "5.7"))