import docker
from flask import Blueprint
from flask_login import login_required

client = docker.Client(base_url='unix://var/run/docker.sock')
route = Blueprint("hive", __name__)


@route.route("/nodes/list")
@route.route("/nodes/list/<filter_args>")
@login_required
def docker_nodes_list(filter_args):
    return client.nodes.list(filter_args)


@route.route("/nodes/<node_id>")
@login_required
def docker_nodes_get(node_id):
    return client.nodes.get(node_id)


@route.route("/networks/list")
@route.route("/networks/list/<filter_args>")
def docker_networks_list(filter_args):
    return client.networks.list(filter_args)


@route.route("/networks/<net_id>")
def docker_networks_get(net_id):
    return client.networks.get(net_id, verbose=True, scope='swarm')

