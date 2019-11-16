import docker
client = docker.DockerClient(base_url='unix://var/run/docker.sock')


def node_list(filter=None):
    return client.nodes.list(filter)


def node_get(id: str):
    return client.nodes.get(id)


def network_list(*args, **kwargs):
    return client.network.list(*args, **kwargs)


def network_get(id: str):
    return client.network.get(id, verbose=True, scope='swarm')
