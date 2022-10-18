# Racetrack Plugin: Teams Notifications

This plugin sends Racetrack notifications to Teams channel.

It sends events when:
- job is submitted (fatman deployed)
- fatman is deleted

## Setup
1. Create webhook for a Teams channel - 
  https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook

2. Set `TEAMS_WEBHOOK` environment variable to your webhook URL for Lifcycle component.
  You can set different webhooks for different deployment environments.
  For instance:
  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    namespace: racetrack
    name: lifecycle
  spec:
    replicas: 1
    template:
      spec:
        containers:
          - name: lifecycle
            env:
              - name: TEAMS_WEBHOOK
                value: 'https://webhook.office.com/webhookb2/...'
  ```

3. Install `racetrack` client and generate ZIP plugin by running `make bundle`.

4. Activate the plugin in Racetrack Dashboard Admin page
  by uploading the zipped plugin file.
