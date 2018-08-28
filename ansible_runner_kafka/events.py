from confluent_kafka import Producer
import json
import os
import logging


logger = logging.getLogger('ansible-runner')


def get_configuration(runner_config):
    bootstrap_servers = runner_config.settings.get("bootstrap_servers", None)
    bootstrap_servers = os.getenv("BOOTSTRAP_SERVERS", bootstrap_servers)
    event_topic = runner_config.settings.get("event_topic", "ansible.runner.event")
    event_topic = os.getenv("EVENT_TOPIC", event_topic)
    status_topic = runner_config.settings.get("status_topic", "ansible.runner.state")
    status_topic = os.getenv("STATUS_TOPIC", status_topic)
    return dict(bootstrap_servers=bootstrap_servers,
                event_topic=event_topic,
                status_topic=status_topic)


def event_handler(runner_config, data):
    cfg = get_configuration(runner_config)

    if cfg['bootstrap_servers'] is not None:
        p = Producer({'bootstrap.servers': cfg['bootstrap_servers']})
        p.produce(cfg['event_topic'], json.dumps(data))
        p.flush(5)
    else:
        logger.info("Kafka Plugin Skipped")


def status_handler(runner_config, data):
    cfg = get_configuration(runner_config)

    if cfg['bootstrap_servers'] is not None:
        p = Producer({'bootstrap.servers': cfg['bootstrap_servers']})
        p.produce(cfg['status_topic'], json.dumps(data))
        p.flush(5)
    else:
        logger.info("Kafka Plugin Skipped")
