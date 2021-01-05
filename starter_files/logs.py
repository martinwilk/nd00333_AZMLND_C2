from azureml.core import Workspace
from azureml.core.webservice import Webservice
import json

# Requires the config to be downloaded first to the current working directory
ws = Workspace.from_config()

# Set with the deployment name
with open("./settings.json") as configfile:
    config = json.loads(config.read())
name = config["deployment_name"]

# load existing web service
service = Webservice(name=name, workspace=ws)
service.update(enable_app_insights=True)
logs = service.get_logs()

for line in logs.split('\n'):
    print(line)
