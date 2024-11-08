import datetime

from copier_templates_extensions import ContextHook

class ContextUpdater(ContextHook):
    update = False

    def hook(self, context):
        context["repo_name"] = context["_copier_conf"]["dst_path"].name
        context["year"] = datetime.date.today().year
