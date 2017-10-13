import docker
import unittest

client = docker.from_env()

# Set variables for tests
container_name = 'minion'

def set_container_id():
    container_id = ''
    for container in client.containers.list():
        if container.name == container_name:
            container_id = container.id
    assert container_id != ''
    return container_id

# Check for container name
def test_minion_container_exists():
    found_master_container = False
    for container in client.containers.list():
        if container.name == container_name:
            found_master_container = True

    assert found_master_container == True

# Check container is running
def test_minion_container_is_running():
    cid = set_container_id()
    container = client.containers.get(cid)
    assert container.status == 'running'

