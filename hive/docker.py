import docker
client = docker.Client(base_url='unix://var/run/docker.sock')


class Docker():

    def node_list(self, filter=None):
        return client.nodes.list(filter)

    def node_get(self, id: str):
        return client.nodes.get(id)

    def network_list(self, *args, **kwargs):
        return client.networks.list(*args, **kwargs)

    def network_get(self, id: str):
        return client.networks.get(id, verbose=True, scope='swarm')
