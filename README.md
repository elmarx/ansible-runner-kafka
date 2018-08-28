Ansible Runner Kafka Event Emitter
=================================

This project is a plugin for [Ansible Runner](https://github.com/ansible/ansible-runner) that allows emitting Ansible status and events to Kafka topics.

For more details and the latest documentation see: https://ansible-runner.readthedocs.io/en/latest

This plugin is very *very* basic. Especially error-handling is missing, since the produce-call is asymmetric, and I don't know how to return errors back to ansible runner.
Also the repeated initialization of the producer and call to flush is not very efficient.

Available settings
------------------

These [runner-settings](https://ansible-runner.readthedocs.io/en/latest/intro.html#env-settings-settings-for-runner-itself) are available:

- `bootstrap_servers` input for confluent-kafka's producer's *bootstrap_servers*. **default**: None. **Sample**: localhost:9092. If not set, this plugin will be skipped
- `event_topic` topic to produce events to. **default**: ansible.runner.event. **Sample**: event
- `status_topic` topic to produces status messages to. **default**: ansible.runner.status. **Sample**: status
