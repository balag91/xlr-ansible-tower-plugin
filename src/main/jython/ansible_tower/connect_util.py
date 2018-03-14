
from tower_cli.conf import settings


def session(server, p_user, p_password):
    return settings.runtime_values(host=server['url'], verify_ssl=False, username=p_username or server['username'],
                                   password=p_password or server['password'])