import os
from typing import Optional
from pathlib import Path

import pymsteams

from racetrack_client.manifest import Manifest
from racetrack_commons.entities.dto import FatmanDto


class Plugin:

    def __init__(self) -> None:
        self.webhook_url = os.environ.get('TEAMS_WEBHOOK')
        assert self.webhook_url, 'TEAMS_WEBHOOK env var was not set'

    def post_fatman_deploy(self, manifest: Manifest, fatman: FatmanDto, image_name: str, deployer_username: str = None):
        """Supplementary actions invoked after fatman is deployed"""
        cluster = os.environ.get('CLUSTER_FQDN')
        self._send_notification(f'Fatman {fatman} has been deployed to {cluster} cluster by {deployer_username}')

    def post_fatman_delete(self, fatman: FatmanDto, username_executor: str = None):
        """Supplementary actions invoked after fatman is deleted"""
        cluster = os.environ.get('CLUSTER_FQDN')
        self._send_notification(f'Fatman {fatman} has been deleted from {cluster} cluster by {username_executor}')

    def markdown_docs(self) -> Optional[str]:
        """
        Return documentation for this plugin in markdown format
        """
        readme_file: Path = self.plugin_dir.parent / 'README.md'
        readme_markdown = readme_file.read_text()
        info_markdown = f"""
# Plugin configuration
- **Plugin version**: {self.plugin_manifest.version}
        """
        return readme_markdown + info_markdown

    def _send_notification(self, message: str):
        notification = pymsteams.connectorcard(self.webhook_url)
        notification.text(message)
        notification.send()
