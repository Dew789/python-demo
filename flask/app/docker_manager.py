import docker
from docker.errors import ImageNotFound


class DockerManager:

    client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')

    @staticmethod
    def build_name(repository, tag):
        return "%s:%s" % (repository, tag)

    def is_image_exist(self, repository, tag):
        try:
            return self.client.images.get(self.build_name(repository, tag))
        except ImageNotFound as e:
            return False

    def pull_image(self, repository, tag):
        self.client.images.pull(self.build_name(repository, tag))
