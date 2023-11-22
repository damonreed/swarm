# swarm_mon
POC for decentralized, container-based network monitoring

HLD:
* Build REST API driven monitoring scripts into lightweght containers(monitors)
* Run monitors globally in free-tier cloud hosting (e.g.- GCP Cloud Run )
* Dispatch monitoring requests to monitors from controller container(TBD)
* Monitors run requests and insert results into cloud DB (influx or bigquery)
* Controller monitors DB for threshold metrics to generate alerts
* Controler serves up graphana dashboards and periodic reports via e-mail/chat/SMS
* Controler runs control UIs: chat, web GUI, REST