# logicmonitor_sdk.LMApi

All URIs are relative to *https://localhost/santaba/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ack_alert_by_id**](LMApi.md#ack_alert_by_id) | **POST** /alert/alerts/{id}/ack | ack alert by id
[**ack_collector_down_alert_by_id**](LMApi.md#ack_collector_down_alert_by_id) | **POST** /setting/collector/collectors/{id}/ackdown | ack collector down alert
[**add_admin**](LMApi.md#add_admin) | **POST** /setting/admins | add user
[**add_alert_note_by_id**](LMApi.md#add_alert_note_by_id) | **POST** /alert/alerts/{id}/note | add alert note
[**add_alert_rule**](LMApi.md#add_alert_rule) | **POST** /setting/alert/rules | add alert rule
[**add_api_token_by_admin_id**](LMApi.md#add_api_token_by_admin_id) | **POST** /setting/admins/{adminId}/apitokens | add api tokens for a user
[**add_collector**](LMApi.md#add_collector) | **POST** /setting/collector/collectors | add collector
[**add_collector_group**](LMApi.md#add_collector_group) | **POST** /setting/collector/groups | add collector group
[**add_dashboard**](LMApi.md#add_dashboard) | **POST** /dashboard/dashboards | add dashboard
[**add_dashboard_group**](LMApi.md#add_dashboard_group) | **POST** /dashboard/groups | add dashboard group
[**add_device**](LMApi.md#add_device) | **POST** /device/devices | add a new device
[**add_device_datasource_instance**](LMApi.md#add_device_datasource_instance) | **POST** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances | add device instance 
[**add_device_datasource_instance_group**](LMApi.md#add_device_datasource_instance_group) | **POST** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups | add device datasource instance group 
[**add_device_group**](LMApi.md#add_device_group) | **POST** /device/groups | add device group
[**add_device_group_cluster_alert_conf**](LMApi.md#add_device_group_cluster_alert_conf) | **POST** /device/groups/{deviceGroupId}/clusterAlertConf | Add cluster alert configuration
[**add_device_group_property**](LMApi.md#add_device_group_property) | **POST** /device/groups/{gid}/properties | add device group property
[**add_device_property**](LMApi.md#add_device_property) | **POST** /device/devices/{deviceId}/properties | add device property
[**add_escalation_chain**](LMApi.md#add_escalation_chain) | **POST** /setting/alert/chains | add escalation chain
[**add_netscan**](LMApi.md#add_netscan) | **POST** /setting/netscans | add a new netscan
[**add_ops_note**](LMApi.md#add_ops_note) | **POST** /setting/opsnotes | add opsnote
[**add_recipient_group**](LMApi.md#add_recipient_group) | **POST** /setting/recipientgroups | add recipient group
[**add_report**](LMApi.md#add_report) | **POST** /report/reports | add report
[**add_report_group**](LMApi.md#add_report_group) | **POST** /report/groups | add report group
[**add_role**](LMApi.md#add_role) | **POST** /setting/roles | add role
[**add_sdt**](LMApi.md#add_sdt) | **POST** /sdt/sdts | add SDT
[**add_website**](LMApi.md#add_website) | **POST** /website/websites | add website
[**add_website_group**](LMApi.md#add_website_group) | **POST** /website/groups | add website group
[**add_widget**](LMApi.md#add_widget) | **POST** /dashboard/widgets | add widget
[**collect_device_config_source_config**](LMApi.md#collect_device_config_source_config) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/config/collectNow | collect a config for a device
[**delete_admin_by_id**](LMApi.md#delete_admin_by_id) | **DELETE** /setting/admins/{id} | delete user
[**delete_alert_rule_by_id**](LMApi.md#delete_alert_rule_by_id) | **DELETE** /setting/alert/rules/{id} | delete alert rule
[**delete_api_token_by_id**](LMApi.md#delete_api_token_by_id) | **DELETE** /setting/admins/{adminId}/apitokens/{apitokenId} | delete apiToken
[**delete_collector_by_id**](LMApi.md#delete_collector_by_id) | **DELETE** /setting/collector/collectors/{id} | delete collector
[**delete_collector_group_by_id**](LMApi.md#delete_collector_group_by_id) | **DELETE** /setting/collector/groups/{id} | delete collector group
[**delete_dashboard_by_id**](LMApi.md#delete_dashboard_by_id) | **DELETE** /dashboard/dashboards/{id} | delete dashboard
[**delete_dashboard_group_by_id**](LMApi.md#delete_dashboard_group_by_id) | **DELETE** /dashboard/groups/{id} | delete dashboard group
[**delete_datasource_by_id**](LMApi.md#delete_datasource_by_id) | **DELETE** /setting/datasources/{id} | delete datasource
[**delete_device_by_id**](LMApi.md#delete_device_by_id) | **DELETE** /device/devices/{id} | delete a device
[**delete_device_datasource_instance_by_id**](LMApi.md#delete_device_datasource_instance_by_id) | **DELETE** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | delete a device instance
[**delete_device_group_by_id**](LMApi.md#delete_device_group_by_id) | **DELETE** /device/groups/{id} | delete device group
[**delete_device_group_cluster_alert_conf_by_id**](LMApi.md#delete_device_group_cluster_alert_conf_by_id) | **DELETE** /device/groups/{deviceGroupId}/clusterAlertConf/{id} | Delete cluster alert configuration
[**delete_device_group_property_by_name**](LMApi.md#delete_device_group_property_by_name) | **DELETE** /device/groups/{gid}/properties/{name} | delete device group property
[**delete_device_property_by_name**](LMApi.md#delete_device_property_by_name) | **DELETE** /device/devices/{deviceId}/properties/{name} | delete device property
[**delete_escalation_chain_by_id**](LMApi.md#delete_escalation_chain_by_id) | **DELETE** /setting/alert/chains/{id} | delete escalation chain
[**delete_netscan_by_id**](LMApi.md#delete_netscan_by_id) | **DELETE** /setting/netscans/{id} | delete a netscan
[**delete_ops_note_by_id**](LMApi.md#delete_ops_note_by_id) | **DELETE** /setting/opsnotes/{id} | delete opsnote
[**delete_recipient_group_by_id**](LMApi.md#delete_recipient_group_by_id) | **DELETE** /setting/recipientgroups/{id} | delete recipient group
[**delete_report_by_id**](LMApi.md#delete_report_by_id) | **DELETE** /report/reports/{id} | delete report
[**delete_report_group_by_id**](LMApi.md#delete_report_group_by_id) | **DELETE** /report/groups/{id} | delete report group
[**delete_role_by_id**](LMApi.md#delete_role_by_id) | **DELETE** /setting/roles/{id} | delete role
[**delete_sdt_by_id**](LMApi.md#delete_sdt_by_id) | **DELETE** /sdt/sdts/{id} | delete SDT
[**delete_website_by_id**](LMApi.md#delete_website_by_id) | **DELETE** /website/websites/{id} | delete website
[**delete_website_group_by_id**](LMApi.md#delete_website_group_by_id) | **DELETE** /website/groups/{id} | delete website group
[**delete_widget_by_id**](LMApi.md#delete_widget_by_id) | **DELETE** /dashboard/widgets/{id} | delete widget
[**execute_debug_command**](LMApi.md#execute_debug_command) | **POST** /debug | Execute a Collector debug command
[**generate_report_by_id**](LMApi.md#generate_report_by_id) | **POST** /report/reports/{id}/executions | run a report
[**get_admin_by_id**](LMApi.md#get_admin_by_id) | **GET** /setting/admins/{id} | get user
[**get_admin_list**](LMApi.md#get_admin_list) | **GET** /setting/admins | get user list
[**get_alert_by_id**](LMApi.md#get_alert_by_id) | **GET** /alert/alerts/{id} | get alert
[**get_alert_list**](LMApi.md#get_alert_list) | **GET** /alert/alerts | get alert list
[**get_alert_list_by_device_group_id**](LMApi.md#get_alert_list_by_device_group_id) | **GET** /device/groups/{id}/alerts | get device group alerts
[**get_alert_list_by_device_id**](LMApi.md#get_alert_list_by_device_id) | **GET** /device/devices/{id}/alerts | get alerts
[**get_alert_rule_by_id**](LMApi.md#get_alert_rule_by_id) | **GET** /setting/alert/rules/{id} | get alert rule by id
[**get_alert_rule_list**](LMApi.md#get_alert_rule_list) | **GET** /setting/alert/rules | get alert rule list
[**get_all_sdt_list_by_device_id**](LMApi.md#get_all_sdt_list_by_device_id) | **GET** /device/devices/{id}/sdts | get SDTs for a device
[**get_all_sdt_list_by_website_group_id**](LMApi.md#get_all_sdt_list_by_website_group_id) | **GET** /website/groups/{id}/sdts | get a list of SDTs for a website group
[**get_api_token_list**](LMApi.md#get_api_token_list) | **GET** /setting/admins/apitokens | get a list of api tokens across users
[**get_api_token_list_by_admin_id**](LMApi.md#get_api_token_list_by_admin_id) | **GET** /setting/admins/{adminId}/apitokens | get api tokens for a user
[**get_associated_device_list_by_data_source_id**](LMApi.md#get_associated_device_list_by_data_source_id) | **GET** /setting/datasources/{id}/devices | get devices associated with a datasource
[**get_audit_log_by_id**](LMApi.md#get_audit_log_by_id) | **GET** /setting/accesslogs/{id} | Get audit log by id
[**get_audit_log_list**](LMApi.md#get_audit_log_list) | **GET** /setting/accesslogs | Get audit logs
[**get_aws_external_id**](LMApi.md#get_aws_external_id) | **GET** /aws/externalId | Get AWS external id
[**get_collector_by_id**](LMApi.md#get_collector_by_id) | **GET** /setting/collector/collectors/{id} | get collector
[**get_collector_group_by_id**](LMApi.md#get_collector_group_by_id) | **GET** /setting/collector/groups/{id} | get collector group
[**get_collector_group_list**](LMApi.md#get_collector_group_list) | **GET** /setting/collector/groups | get collector group list
[**get_collector_installer**](LMApi.md#get_collector_installer) | **GET** /setting/collector/collectors/{collectorId}/installers/{osAndArch} | get collector installer
[**get_collector_list**](LMApi.md#get_collector_list) | **GET** /setting/collector/collectors | get collector list
[**get_dashboard_by_id**](LMApi.md#get_dashboard_by_id) | **GET** /dashboard/dashboards/{id} | get dashboard
[**get_dashboard_group_by_id**](LMApi.md#get_dashboard_group_by_id) | **GET** /dashboard/groups/{id} | get dashboard group
[**get_dashboard_group_list**](LMApi.md#get_dashboard_group_list) | **GET** /dashboard/groups | get dashboard group list
[**get_dashboard_list**](LMApi.md#get_dashboard_list) | **GET** /dashboard/dashboards | get dashboard list
[**get_data_source_overview_graph_by_id**](LMApi.md#get_data_source_overview_graph_by_id) | **GET** /setting/datasources/{dsId}/ographs/{id} | get datasource overview graph by id
[**get_data_source_overview_graph_list**](LMApi.md#get_data_source_overview_graph_list) | **GET** /setting/datasources/{dsId}/ographs | get datasource overview graph list
[**get_datasource_by_id**](LMApi.md#get_datasource_by_id) | **GET** /setting/datasources/{id} | get datasource by id
[**get_datasource_list**](LMApi.md#get_datasource_list) | **GET** /setting/datasources | get datasource list
[**get_debug_command_result**](LMApi.md#get_debug_command_result) | **GET** /debug/{id} | Get the result of a Collector debug command
[**get_device_by_id**](LMApi.md#get_device_by_id) | **GET** /device/devices/{id} | get device by id
[**get_device_config_source_config_by_id**](LMApi.md#get_device_config_source_config_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/config/{id} | get a config for a device
[**get_device_config_source_config_list**](LMApi.md#get_device_config_source_config_list) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/config | get config instances for a configsource
[**get_device_datasource_by_id**](LMApi.md#get_device_datasource_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{id} | get device datasource 
[**get_device_datasource_data_by_id**](LMApi.md#get_device_datasource_data_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{id}/data | get device datasource data 
[**get_device_datasource_instance_alert_setting_by_id**](LMApi.md#get_device_datasource_instance_alert_setting_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings/{id} | get device instance alert setting
[**get_device_datasource_instance_alert_setting_list**](LMApi.md#get_device_datasource_instance_alert_setting_list) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings | get a list of alert settings for a device
[**get_device_datasource_instance_by_id**](LMApi.md#get_device_datasource_instance_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | get device instance 
[**get_device_datasource_instance_data**](LMApi.md#get_device_datasource_instance_data) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id}/data | get device instance data
[**get_device_datasource_instance_graph_data**](LMApi.md#get_device_datasource_instance_graph_data) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id}/graphs/{graphId}/data | get device instance graph data 
[**get_device_datasource_instance_group_by_id**](LMApi.md#get_device_datasource_instance_group_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{id} | get device datasource instance group 
[**get_device_datasource_instance_group_list**](LMApi.md#get_device_datasource_instance_group_list) | **GET** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups | get device datasource instance group list 
[**get_device_datasource_instance_group_overview_graph_data**](LMApi.md#get_device_datasource_instance_group_overview_graph_data) | **GET** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{dsigId}/graphs/{ographId}/data | get device instance group overview graph data 
[**get_device_datasource_instance_list**](LMApi.md#get_device_datasource_instance_list) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances | get device instance list
[**get_device_datasource_instance_sdt_history**](LMApi.md#get_device_datasource_instance_sdt_history) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id}/historysdts | get device instance SDT history
[**get_device_datasource_list**](LMApi.md#get_device_datasource_list) | **GET** /device/devices/{deviceId}/devicedatasources | get device datasource list 
[**get_device_group_by_id**](LMApi.md#get_device_group_by_id) | **GET** /device/groups/{id} | get device group
[**get_device_group_cluster_alert_conf_by_id**](LMApi.md#get_device_group_cluster_alert_conf_by_id) | **GET** /device/groups/{deviceGroupId}/clusterAlertConf/{id} | Get cluster alert configuration by id
[**get_device_group_cluster_alert_conf_list**](LMApi.md#get_device_group_cluster_alert_conf_list) | **GET** /device/groups/{deviceGroupId}/clusterAlertConf | get a list of cluster alert configurations for a device group
[**get_device_group_datasource_alert_setting**](LMApi.md#get_device_group_datasource_alert_setting) | **GET** /device/groups/{deviceGroupId}/datasources/{dsId}/alertsettings | get device group datasource alert setting 
[**get_device_group_datasource_by_id**](LMApi.md#get_device_group_datasource_by_id) | **GET** /device/groups/{deviceGroupId}/datasources/{id} | get device group datasource
[**get_device_group_datasource_list**](LMApi.md#get_device_group_datasource_list) | **GET** /device/groups/{deviceGroupId}/datasources | get device group datasource list
[**get_device_group_list**](LMApi.md#get_device_group_list) | **GET** /device/groups | get device group list
[**get_device_group_property_by_name**](LMApi.md#get_device_group_property_by_name) | **GET** /device/groups/{gid}/properties/{name} | get device group property by name
[**get_device_group_property_list**](LMApi.md#get_device_group_property_list) | **GET** /device/groups/{gid}/properties | get device group properties
[**get_device_group_sdt_list**](LMApi.md#get_device_group_sdt_list) | **GET** /device/groups/{id}/sdts | get device group SDTs
[**get_device_instance_graph_data_only_by_instance_id**](LMApi.md#get_device_instance_graph_data_only_by_instance_id) | **GET** /device/devicedatasourceinstances/{instanceId}/graphs/{graphId}/data | get device instance data
[**get_device_list**](LMApi.md#get_device_list) | **GET** /device/devices | get device list
[**get_device_property_by_name**](LMApi.md#get_device_property_by_name) | **GET** /device/devices/{deviceId}/properties/{name} | get device property by name
[**get_device_property_list**](LMApi.md#get_device_property_list) | **GET** /device/devices/{deviceId}/properties | get device properties
[**get_escalation_chain_by_id**](LMApi.md#get_escalation_chain_by_id) | **GET** /setting/alert/chains/{id} | get escalation chain by id
[**get_escalation_chain_list**](LMApi.md#get_escalation_chain_list) | **GET** /setting/alert/chains | get escalation chain list
[**get_immediate_device_list_by_device_group_id**](LMApi.md#get_immediate_device_list_by_device_group_id) | **GET** /device/groups/{id}/devices | get immediate devices under group
[**get_immediate_website_list_by_website_group_id**](LMApi.md#get_immediate_website_list_by_website_group_id) | **GET** /website/groups/{id}/websites | get a list of websites for a group
[**get_netflow_endpoint_list**](LMApi.md#get_netflow_endpoint_list) | **GET** /device/devices/{id}/endpoints | get netflow endpoint list
[**get_netflow_flow_list**](LMApi.md#get_netflow_flow_list) | **GET** /device/devices/{id}/flows | get netflow flow list
[**get_netflow_port_list**](LMApi.md#get_netflow_port_list) | **GET** /device/devices/{id}/ports | get netflow port list
[**get_netscan_by_id**](LMApi.md#get_netscan_by_id) | **GET** /setting/netscans/{id} | get netscan by id
[**get_netscan_list**](LMApi.md#get_netscan_list) | **GET** /setting/netscans | get netscan list
[**get_ops_note_by_id**](LMApi.md#get_ops_note_by_id) | **GET** /setting/opsnotes/{id} | get opsnote by id
[**get_ops_note_list**](LMApi.md#get_ops_note_list) | **GET** /setting/opsnotes | get opsnote list
[**get_recipient_group_by_id**](LMApi.md#get_recipient_group_by_id) | **GET** /setting/recipientgroups/{id} | get recipient group by id
[**get_recipient_group_list**](LMApi.md#get_recipient_group_list) | **GET** /setting/recipientgroups | get recipient group List
[**get_report_by_id**](LMApi.md#get_report_by_id) | **GET** /report/reports/{id} | get report by id
[**get_report_group_by_id**](LMApi.md#get_report_group_by_id) | **GET** /report/groups/{id} | get report group by id
[**get_report_group_list**](LMApi.md#get_report_group_list) | **GET** /report/groups | get report group list
[**get_report_list**](LMApi.md#get_report_list) | **GET** /report/reports | get report list
[**get_role_by_id**](LMApi.md#get_role_by_id) | **GET** /setting/roles/{id} | get role by id
[**get_role_list**](LMApi.md#get_role_list) | **GET** /setting/roles | get role list
[**get_sdt_by_id**](LMApi.md#get_sdt_by_id) | **GET** /sdt/sdts/{id} | get SDT by id
[**get_sdt_history_by_device_data_source_id**](LMApi.md#get_sdt_history_by_device_data_source_id) | **GET** /device/devices/{deviceId}/devicedatasources/{id}/historysdts | get SDT history for the device dataSource
[**get_sdt_history_by_device_group_id**](LMApi.md#get_sdt_history_by_device_group_id) | **GET** /device/groups/{id}/historysdts | get SDT history for the group
[**get_sdt_history_by_device_id**](LMApi.md#get_sdt_history_by_device_id) | **GET** /device/devices/{id}/historysdts | get SDT history for the device
[**get_sdt_list**](LMApi.md#get_sdt_list) | **GET** /sdt/sdts | get SDT list
[**get_site_monitor_check_point_list**](LMApi.md#get_site_monitor_check_point_list) | **GET** /website/smcheckpoints | get website checkpoint list
[**get_top_talkers_graph**](LMApi.md#get_top_talkers_graph) | **GET** /device/devices/{id}/topTalkersGraph | get top talkers graph
[**get_unmonitored_device_list**](LMApi.md#get_unmonitored_device_list) | **GET** /device/unmonitoreddevices | get unmonitored device list
[**get_update_reason_list_by_data_source_id**](LMApi.md#get_update_reason_list_by_data_source_id) | **GET** /setting/datasources/{id}/updatereasons | get update history for a datasource
[**get_website_alert_list_by_website_id**](LMApi.md#get_website_alert_list_by_website_id) | **GET** /website/websites/{id}/alerts | get alerts for a website
[**get_website_by_id**](LMApi.md#get_website_by_id) | **GET** /website/websites/{id} | get website by id
[**get_website_checkpoint_data_by_id**](LMApi.md#get_website_checkpoint_data_by_id) | **GET** /website/websites/{srvId}/checkpoints/{checkId}/data | get data for a website checkpoint
[**get_website_data_by_graph_name**](LMApi.md#get_website_data_by_graph_name) | **GET** /website/websites/{id}/graphs/{graphName}/data | get website data by graph name
[**get_website_graph_data**](LMApi.md#get_website_graph_data) | **GET** /website/websites/{websiteId}/checkpoints/{checkpointId}/graphs/{graphName}/data | get website graph data
[**get_website_group_by_id**](LMApi.md#get_website_group_by_id) | **GET** /website/groups/{id} | get website group
[**get_website_group_list**](LMApi.md#get_website_group_list) | **GET** /website/groups | get website group list
[**get_website_list**](LMApi.md#get_website_list) | **GET** /website/websites | get website list
[**get_website_property_list_by_website_id**](LMApi.md#get_website_property_list_by_website_id) | **GET** /website/websites/{id}/properties | get a list of properties for a website
[**get_website_sdt_list_by_website_id**](LMApi.md#get_website_sdt_list_by_website_id) | **GET** /website/websites/{id}/sdts | get a list of SDTs for a website
[**get_widget_by_id**](LMApi.md#get_widget_by_id) | **GET** /dashboard/widgets/{id} | get widget by id
[**get_widget_data_by_id**](LMApi.md#get_widget_data_by_id) | **GET** /dashboard/widgets/{id}/data | get widget data
[**get_widget_list**](LMApi.md#get_widget_list) | **GET** /dashboard/widgets | get widget list
[**get_widget_list_by_dashboard_id**](LMApi.md#get_widget_list_by_dashboard_id) | **GET** /dashboard/dashboards/{id}/widgets | get widget list by DashboardId
[**import_batch_job**](LMApi.md#import_batch_job) | **POST** /setting/batchjobs/importxml | import batch job via xml
[**import_config_source**](LMApi.md#import_config_source) | **POST** /setting/configsources/importxml | import config source via xml
[**import_data_source**](LMApi.md#import_data_source) | **POST** /setting/datasources/importxml | import datasource via xml
[**import_event_source**](LMApi.md#import_event_source) | **POST** /setting/eventsources/importxml | import eventsource via xml
[**patch_admin_by_id**](LMApi.md#patch_admin_by_id) | **PATCH** /setting/admins/{id} | update user
[**patch_alert_rule_by_id**](LMApi.md#patch_alert_rule_by_id) | **PATCH** /setting/alert/rules/{id} | update alert rule
[**patch_api_token_by_admin_id**](LMApi.md#patch_api_token_by_admin_id) | **PATCH** /setting/admins/{adminId}/apitokens/{apitokenId} | update api tokens for a user
[**patch_collector_by_id**](LMApi.md#patch_collector_by_id) | **PATCH** /setting/collector/collectors/{id} | update collector
[**patch_collector_group_by_id**](LMApi.md#patch_collector_group_by_id) | **PATCH** /setting/collector/groups/{id} | update collector group
[**patch_dashboard_by_id**](LMApi.md#patch_dashboard_by_id) | **PATCH** /dashboard/dashboards/{id} | update dashboard
[**patch_dashboard_group_by_id**](LMApi.md#patch_dashboard_group_by_id) | **PATCH** /dashboard/groups/{id} | update dashboard group
[**patch_device**](LMApi.md#patch_device) | **PATCH** /device/devices/{id} | update a device
[**patch_device_datasource_instance_alert_setting_by_id**](LMApi.md#patch_device_datasource_instance_alert_setting_by_id) | **PATCH** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings/{id} | update device instance alert setting
[**patch_device_datasource_instance_by_id**](LMApi.md#patch_device_datasource_instance_by_id) | **PATCH** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | update device instance
[**patch_device_datasource_instance_group_by_id**](LMApi.md#patch_device_datasource_instance_group_by_id) | **PATCH** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{id} | update device datasource instance group 
[**patch_device_group_by_id**](LMApi.md#patch_device_group_by_id) | **PATCH** /device/groups/{id} | update device group
[**patch_device_group_cluster_alert_conf_by_id**](LMApi.md#patch_device_group_cluster_alert_conf_by_id) | **PATCH** /device/groups/{deviceGroupId}/clusterAlertConf/{id} | Update cluster alert configuration
[**patch_device_group_datasource_alert_setting**](LMApi.md#patch_device_group_datasource_alert_setting) | **PATCH** /device/groups/{deviceGroupId}/datasources/{dsId}/alertsettings | update device group datasource alert setting
[**patch_device_group_property_by_name**](LMApi.md#patch_device_group_property_by_name) | **PATCH** /device/groups/{gid}/properties/{name} | update device group property
[**patch_device_property_by_name**](LMApi.md#patch_device_property_by_name) | **PATCH** /device/devices/{deviceId}/properties/{name} | update device property
[**patch_escalation_chain_by_id**](LMApi.md#patch_escalation_chain_by_id) | **PATCH** /setting/alert/chains/{id} | update escalation chain
[**patch_netscan**](LMApi.md#patch_netscan) | **PATCH** /setting/netscans/{id} | update a netscan
[**patch_ops_note_by_id**](LMApi.md#patch_ops_note_by_id) | **PATCH** /setting/opsnotes/{id} | update opsnote
[**patch_recipient_group_by_id**](LMApi.md#patch_recipient_group_by_id) | **PATCH** /setting/recipientgroups/{id} | update recipient group
[**patch_report_by_id**](LMApi.md#patch_report_by_id) | **PATCH** /report/reports/{id} | update report
[**patch_report_group_by_id**](LMApi.md#patch_report_group_by_id) | **PATCH** /report/groups/{id} | update report group
[**patch_role_by_id**](LMApi.md#patch_role_by_id) | **PATCH** /setting/roles/{id} | update role
[**patch_sdt_by_id**](LMApi.md#patch_sdt_by_id) | **PATCH** /sdt/sdts/{id} | update SDT
[**patch_website_by_id**](LMApi.md#patch_website_by_id) | **PATCH** /website/websites/{id} | update website
[**patch_website_group_by_id**](LMApi.md#patch_website_group_by_id) | **PATCH** /website/groups/{id} | update website group
[**patch_widget_by_id**](LMApi.md#patch_widget_by_id) | **PATCH** /dashboard/widgets/{id} | update widget
[**schedule_auto_discovery_by_device_id**](LMApi.md#schedule_auto_discovery_by_device_id) | **POST** /device/devices/{id}/scheduleAutoDiscovery | schedule active discovery for a device
[**update_admin_by_id**](LMApi.md#update_admin_by_id) | **PUT** /setting/admins/{id} | update user
[**update_alert_rule_by_id**](LMApi.md#update_alert_rule_by_id) | **PUT** /setting/alert/rules/{id} | update alert rule
[**update_api_token_by_admin_id**](LMApi.md#update_api_token_by_admin_id) | **PUT** /setting/admins/{adminId}/apitokens/{apitokenId} | update api tokens for a user
[**update_collector_by_id**](LMApi.md#update_collector_by_id) | **PUT** /setting/collector/collectors/{id} | update collector
[**update_collector_group_by_id**](LMApi.md#update_collector_group_by_id) | **PUT** /setting/collector/groups/{id} | update collector group
[**update_dashboard_by_id**](LMApi.md#update_dashboard_by_id) | **PUT** /dashboard/dashboards/{id} | update dashboard
[**update_dashboard_group_by_id**](LMApi.md#update_dashboard_group_by_id) | **PUT** /dashboard/groups/{id} | update dashboard group
[**update_device**](LMApi.md#update_device) | **PUT** /device/devices/{id} | update a device
[**update_device_datasource_instance_alert_setting_by_id**](LMApi.md#update_device_datasource_instance_alert_setting_by_id) | **PUT** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings/{id} | update device instance alert setting
[**update_device_datasource_instance_by_id**](LMApi.md#update_device_datasource_instance_by_id) | **PUT** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | update device instance
[**update_device_datasource_instance_group_by_id**](LMApi.md#update_device_datasource_instance_group_by_id) | **PUT** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{id} | update device datasource instance group 
[**update_device_group_by_id**](LMApi.md#update_device_group_by_id) | **PUT** /device/groups/{id} | update device group
[**update_device_group_cluster_alert_conf_by_id**](LMApi.md#update_device_group_cluster_alert_conf_by_id) | **PUT** /device/groups/{deviceGroupId}/clusterAlertConf/{id} | Update cluster alert configuration
[**update_device_group_datasource_alert_setting**](LMApi.md#update_device_group_datasource_alert_setting) | **PUT** /device/groups/{deviceGroupId}/datasources/{dsId}/alertsettings | update device group datasource alert setting
[**update_device_group_property_by_name**](LMApi.md#update_device_group_property_by_name) | **PUT** /device/groups/{gid}/properties/{name} | update device group property
[**update_device_property_by_name**](LMApi.md#update_device_property_by_name) | **PUT** /device/devices/{deviceId}/properties/{name} | update device property
[**update_escalation_chain_by_id**](LMApi.md#update_escalation_chain_by_id) | **PUT** /setting/alert/chains/{id} | update escalation chain
[**update_netscan**](LMApi.md#update_netscan) | **PUT** /setting/netscans/{id} | update a netscan
[**update_ops_note_by_id**](LMApi.md#update_ops_note_by_id) | **PUT** /setting/opsnotes/{id} | update opsnote
[**update_recipient_group_by_id**](LMApi.md#update_recipient_group_by_id) | **PUT** /setting/recipientgroups/{id} | update recipient group
[**update_report_by_id**](LMApi.md#update_report_by_id) | **PUT** /report/reports/{id} | update report
[**update_report_group_by_id**](LMApi.md#update_report_group_by_id) | **PUT** /report/groups/{id} | update report group
[**update_role_by_id**](LMApi.md#update_role_by_id) | **PUT** /setting/roles/{id} | update role
[**update_sdt_by_id**](LMApi.md#update_sdt_by_id) | **PUT** /sdt/sdts/{id} | update SDT
[**update_website_by_id**](LMApi.md#update_website_by_id) | **PUT** /website/websites/{id} | update website
[**update_website_group_by_id**](LMApi.md#update_website_group_by_id) | **PUT** /website/groups/{id} | update website group
[**update_widget_by_id**](LMApi.md#update_widget_by_id) | **PUT** /dashboard/widgets/{id} | update widget


# **ack_alert_by_id**
> object ack_alert_by_id(body, id)

ack alert by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.AlertAck() # AlertAck | 
id = 'id_example' # str | 

try:
    # ack alert by id
    api_response = api_instance.ack_alert_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->ack_alert_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertAck**](AlertAck.md)|  | 
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ack_collector_down_alert_by_id**
> object ack_collector_down_alert_by_id(id, body)

ack collector down alert



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.AckCollectorDown() # AckCollectorDown | 

try:
    # ack collector down alert
    api_response = api_instance.ack_collector_down_alert_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->ack_collector_down_alert_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**AckCollectorDown**](AckCollectorDown.md)|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_admin**
> Admin add_admin(body)

add user



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Admin() # Admin | 

try:
    # add user
    api_response = api_instance.add_admin(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Admin**](Admin.md)|  | 

### Return type

[**Admin**](Admin.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_alert_note_by_id**
> object add_alert_note_by_id(body, id)

add alert note



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.AlertAck() # AlertAck | 
id = 'id_example' # str | 

try:
    # add alert note
    api_response = api_instance.add_alert_note_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_alert_note_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertAck**](AlertAck.md)|  | 
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_alert_rule**
> AlertRule add_alert_rule(body)

add alert rule



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.AlertRule() # AlertRule | 

try:
    # add alert rule
    api_response = api_instance.add_alert_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_alert_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertRule**](AlertRule.md)|  | 

### Return type

[**AlertRule**](AlertRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_api_token_by_admin_id**
> APIToken add_api_token_by_admin_id(admin_id, body)

add api tokens for a user



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
admin_id = 56 # int | 
body = logicmonitor_sdk.APIToken() # APIToken | 

try:
    # add api tokens for a user
    api_response = api_instance.add_api_token_by_admin_id(admin_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_api_token_by_admin_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**|  | 
 **body** | [**APIToken**](APIToken.md)|  | 

### Return type

[**APIToken**](APIToken.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_collector**
> Collector add_collector(body)

add collector



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Collector() # Collector | 

try:
    # add collector
    api_response = api_instance.add_collector(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_collector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Collector**](Collector.md)|  | 

### Return type

[**Collector**](Collector.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_collector_group**
> CollectorGroup add_collector_group(body)

add collector group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.CollectorGroup() # CollectorGroup | 

try:
    # add collector group
    api_response = api_instance.add_collector_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_collector_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectorGroup**](CollectorGroup.md)|  | 

### Return type

[**CollectorGroup**](CollectorGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dashboard**
> Dashboard add_dashboard(body)

add dashboard



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Dashboard() # Dashboard | 

try:
    # add dashboard
    api_response = api_instance.add_dashboard(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dashboard**](Dashboard.md)|  | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dashboard_group**
> DashboardGroup add_dashboard_group(body)

add dashboard group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.DashboardGroup() # DashboardGroup | 

try:
    # add dashboard group
    api_response = api_instance.add_dashboard_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_dashboard_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DashboardGroup**](DashboardGroup.md)|  | 

### Return type

[**DashboardGroup**](DashboardGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device**
> Device add_device(body, start=start, end=end, netflow_filter=netflow_filter, add_from_wizard=add_from_wizard)

add a new device



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Device() # Device | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
add_from_wizard = false # bool |  (optional) (default to false)

try:
    # add a new device
    api_response = api_instance.add_device(body, start=start, end=end, netflow_filter=netflow_filter, add_from_wizard=add_from_wizard)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Device**](Device.md)|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **add_from_wizard** | **bool**|  | [optional] [default to false]

### Return type

[**Device**](Device.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_datasource_instance**
> DeviceDataSourceInstance add_device_datasource_instance(device_id, hds_id, body)

add device instance 



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
body = logicmonitor_sdk.DeviceDataSourceInstance() # DeviceDataSourceInstance | 

try:
    # add device instance 
    api_response = api_instance.add_device_datasource_instance(device_id, hds_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device_datasource_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **body** | [**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)|  | 

### Return type

[**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_datasource_instance_group**
> DeviceDataSourceInstanceGroup add_device_datasource_instance_group(device_id, device_ds_id, body)

add device datasource instance group 



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
body = logicmonitor_sdk.DeviceDataSourceInstanceGroup() # DeviceDataSourceInstanceGroup | 

try:
    # add device datasource instance group 
    api_response = api_instance.add_device_datasource_instance_group(device_id, device_ds_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device_datasource_instance_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**| The device-datasource ID you&#39;d like to add an instance group for | 
 **body** | [**DeviceDataSourceInstanceGroup**](DeviceDataSourceInstanceGroup.md)|  | 

### Return type

[**DeviceDataSourceInstanceGroup**](DeviceDataSourceInstanceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_group**
> DeviceGroup add_device_group(body)

add device group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.DeviceGroup() # DeviceGroup | 

try:
    # add device group
    api_response = api_instance.add_device_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceGroup**](DeviceGroup.md)|  | 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_group_cluster_alert_conf**
> DeviceClusterAlertConfig add_device_group_cluster_alert_conf(device_group_id, body)

Add cluster alert configuration



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
body = logicmonitor_sdk.DeviceClusterAlertConfig() # DeviceClusterAlertConfig | 

try:
    # Add cluster alert configuration
    api_response = api_instance.add_device_group_cluster_alert_conf(device_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device_group_cluster_alert_conf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **body** | [**DeviceClusterAlertConfig**](DeviceClusterAlertConfig.md)|  | 

### Return type

[**DeviceClusterAlertConfig**](DeviceClusterAlertConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_group_property**
> EntityProperty add_device_group_property(gid, body)

add device group property



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
gid = 56 # int | group ID
body = logicmonitor_sdk.EntityProperty() # EntityProperty | 

try:
    # add device group property
    api_response = api_instance.add_device_group_property(gid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device_group_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**| group ID | 
 **body** | [**EntityProperty**](EntityProperty.md)|  | 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_property**
> EntityProperty add_device_property(device_id, body)

add device property



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
body = logicmonitor_sdk.EntityProperty() # EntityProperty | 

try:
    # add device property
    api_response = api_instance.add_device_property(device_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **body** | [**EntityProperty**](EntityProperty.md)|  | 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_escalation_chain**
> EscalatingChain add_escalation_chain(body)

add escalation chain



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.EscalatingChain() # EscalatingChain | 

try:
    # add escalation chain
    api_response = api_instance.add_escalation_chain(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_escalation_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EscalatingChain**](EscalatingChain.md)|  | 

### Return type

[**EscalatingChain**](EscalatingChain.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_netscan**
> Netscan add_netscan(body=body)

add a new netscan



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Netscan() # Netscan |  (optional)

try:
    # add a new netscan
    api_response = api_instance.add_netscan(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_netscan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Netscan**](Netscan.md)|  | [optional] 

### Return type

[**Netscan**](Netscan.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_ops_note**
> OpsNote add_ops_note(body)

add opsnote



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.OpsNote() # OpsNote | 

try:
    # add opsnote
    api_response = api_instance.add_ops_note(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_ops_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpsNote**](OpsNote.md)|  | 

### Return type

[**OpsNote**](OpsNote.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_recipient_group**
> RecipientGroup add_recipient_group(body)

add recipient group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RecipientGroup() # RecipientGroup | 

try:
    # add recipient group
    api_response = api_instance.add_recipient_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_recipient_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecipientGroup**](RecipientGroup.md)|  | 

### Return type

[**RecipientGroup**](RecipientGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_report**
> ReportBase add_report(body)

add report



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.ReportBase() # ReportBase | 

try:
    # add report
    api_response = api_instance.add_report(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportBase**](ReportBase.md)|  | 

### Return type

[**ReportBase**](ReportBase.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_report_group**
> ReportGroup add_report_group(body)

add report group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.ReportGroup() # ReportGroup | 

try:
    # add report group
    api_response = api_instance.add_report_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_report_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportGroup**](ReportGroup.md)|  | 

### Return type

[**ReportGroup**](ReportGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role**
> Role add_role(body)

add role



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Role() # Role | 

try:
    # add role
    api_response = api_instance.add_role(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_sdt**
> SDT add_sdt(body)

add SDT



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.SDT() # SDT | 

try:
    # add SDT
    api_response = api_instance.add_sdt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_sdt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SDT**](SDT.md)|  | 

### Return type

[**SDT**](SDT.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_website**
> Website add_website(body)

add website



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Website() # Website | 

try:
    # add website
    api_response = api_instance.add_website(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_website: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Website**](Website.md)|  | 

### Return type

[**Website**](Website.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_website_group**
> WebsiteGroup add_website_group(body)

add website group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.WebsiteGroup() # WebsiteGroup | 

try:
    # add website group
    api_response = api_instance.add_website_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_website_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebsiteGroup**](WebsiteGroup.md)|  | 

### Return type

[**WebsiteGroup**](WebsiteGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_widget**
> Widget add_widget(body)

add widget



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Widget() # Widget | 

try:
    # add widget
    api_response = api_instance.add_widget(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Widget**](Widget.md)|  | 

### Return type

[**Widget**](Widget.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collect_device_config_source_config**
> object collect_device_config_source_config(device_id, hds_id, instance_id)

collect a config for a device



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | 
instance_id = 56 # int | 

try:
    # collect a config for a device
    api_response = api_instance.collect_device_config_source_config(device_id, hds_id, instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->collect_device_config_source_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **instance_id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_admin_by_id**
> object delete_admin_by_id(id)

delete user



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete user
    api_response = api_instance.delete_admin_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_admin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_rule_by_id**
> object delete_alert_rule_by_id(id)

delete alert rule



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete alert rule
    api_response = api_instance.delete_alert_rule_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_alert_rule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_token_by_id**
> object delete_api_token_by_id(admin_id, apitoken_id)

delete apiToken



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
admin_id = 56 # int | 
apitoken_id = 56 # int | 

try:
    # delete apiToken
    api_response = api_instance.delete_api_token_by_id(admin_id, apitoken_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_api_token_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**|  | 
 **apitoken_id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collector_by_id**
> object delete_collector_by_id(id)

delete collector



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete collector
    api_response = api_instance.delete_collector_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_collector_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collector_group_by_id**
> object delete_collector_group_by_id(id)

delete collector group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete collector group
    api_response = api_instance.delete_collector_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_collector_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_by_id**
> object delete_dashboard_by_id(id)

delete dashboard



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete dashboard
    api_response = api_instance.delete_dashboard_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_dashboard_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_group_by_id**
> object delete_dashboard_group_by_id(id, allow_non_empty_group=allow_non_empty_group)

delete dashboard group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
allow_non_empty_group = false # bool |  (optional) (default to false)

try:
    # delete dashboard group
    api_response = api_instance.delete_dashboard_group_by_id(id, allow_non_empty_group=allow_non_empty_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_dashboard_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **allow_non_empty_group** | **bool**|  | [optional] [default to false]

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datasource_by_id**
> object delete_datasource_by_id(id)

delete datasource



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete datasource
    api_response = api_instance.delete_datasource_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_by_id**
> object delete_device_by_id(id, start=start, end=end, netflow_filter=netflow_filter, delete_hard=delete_hard)

delete a device



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
delete_hard = true # bool |  (optional) (default to true)

try:
    # delete a device
    api_response = api_instance.delete_device_by_id(id, start=start, end=end, netflow_filter=netflow_filter, delete_hard=delete_hard)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **delete_hard** | **bool**|  | [optional] [default to true]

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_datasource_instance_by_id**
> object delete_device_datasource_instance_by_id(device_id, hds_id, id)

delete a device instance



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
id = 56 # int | 

try:
    # delete a device instance
    api_response = api_instance.delete_device_datasource_instance_by_id(device_id, hds_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_device_datasource_instance_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_group_by_id**
> object delete_device_group_by_id(id, delete_children=delete_children, delete_hard=delete_hard)

delete device group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
delete_children = false # bool |  (optional) (default to false)
delete_hard = true # bool |  (optional) (default to true)

try:
    # delete device group
    api_response = api_instance.delete_device_group_by_id(id, delete_children=delete_children, delete_hard=delete_hard)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **delete_children** | **bool**|  | [optional] [default to false]
 **delete_hard** | **bool**|  | [optional] [default to true]

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_group_cluster_alert_conf_by_id**
> object delete_device_group_cluster_alert_conf_by_id(device_group_id, id)

Delete cluster alert configuration



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
id = 56 # int | 

try:
    # Delete cluster alert configuration
    api_response = api_instance.delete_device_group_cluster_alert_conf_by_id(device_group_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_device_group_cluster_alert_conf_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_group_property_by_name**
> object delete_device_group_property_by_name(gid, name)

delete device group property



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
gid = 56 # int | group ID
name = 'name_example' # str | 

try:
    # delete device group property
    api_response = api_instance.delete_device_group_property_by_name(gid, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_device_group_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**| group ID | 
 **name** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_property_by_name**
> object delete_device_property_by_name(device_id, name)

delete device property



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
name = 'name_example' # str | 

try:
    # delete device property
    api_response = api_instance.delete_device_property_by_name(device_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_device_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **name** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_escalation_chain_by_id**
> object delete_escalation_chain_by_id(id)

delete escalation chain



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete escalation chain
    api_response = api_instance.delete_escalation_chain_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_escalation_chain_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_netscan_by_id**
> object delete_netscan_by_id(id)

delete a netscan



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete a netscan
    api_response = api_instance.delete_netscan_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_netscan_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ops_note_by_id**
> object delete_ops_note_by_id(id)

delete opsnote



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # delete opsnote
    api_response = api_instance.delete_ops_note_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_ops_note_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recipient_group_by_id**
> object delete_recipient_group_by_id(id)

delete recipient group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete recipient group
    api_response = api_instance.delete_recipient_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_recipient_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_by_id**
> object delete_report_by_id(id)

delete report



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete report
    api_response = api_instance.delete_report_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_group_by_id**
> object delete_report_group_by_id(id)

delete report group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete report group
    api_response = api_instance.delete_report_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_report_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_by_id**
> object delete_role_by_id(id)

delete role



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete role
    api_response = api_instance.delete_role_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_role_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sdt_by_id**
> object delete_sdt_by_id(id)

delete SDT



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # delete SDT
    api_response = api_instance.delete_sdt_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_sdt_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_website_by_id**
> object delete_website_by_id(id)

delete website



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete website
    api_response = api_instance.delete_website_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_website_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_website_group_by_id**
> object delete_website_group_by_id(id, delete_children=delete_children)

delete website group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
delete_children = 0 # int |  (optional) (default to 0)

try:
    # delete website group
    api_response = api_instance.delete_website_group_by_id(id, delete_children=delete_children)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_website_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **delete_children** | **int**|  | [optional] [default to 0]

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_widget_by_id**
> object delete_widget_by_id(id)

delete widget



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete widget
    api_response = api_instance.delete_widget_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_widget_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_debug_command**
> Debug execute_debug_command(body=body, collector_id=collector_id)

Execute a Collector debug command



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Debug() # Debug |  (optional)
collector_id = -1 # int |  (optional) (default to -1)

try:
    # Execute a Collector debug command
    api_response = api_instance.execute_debug_command(body=body, collector_id=collector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->execute_debug_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Debug**](Debug.md)|  | [optional] 
 **collector_id** | **int**|  | [optional] [default to -1]

### Return type

[**Debug**](Debug.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_report_by_id**
> GenerateReportResult generate_report_by_id(id, body=body)

run a report



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.GenerateReportRequest() # GenerateReportRequest |  (optional)

try:
    # run a report
    api_response = api_instance.generate_report_by_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->generate_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**GenerateReportRequest**](GenerateReportRequest.md)|  | [optional] 

### Return type

[**GenerateReportResult**](GenerateReportResult.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_by_id**
> Admin get_admin_by_id(id, fields=fields)

get user



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get user
    api_response = api_instance.get_admin_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_admin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Admin**](Admin.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_list**
> AdminPaginationResponse get_admin_list(fields=fields, size=size, offset=offset, filter=filter)

get user list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get user list
    api_response = api_instance.get_admin_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_admin_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**AdminPaginationResponse**](AdminPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_by_id**
> Alert get_alert_by_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields)

get alert



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
need_message = false # bool |  (optional) (default to false)
custom_columns = 'custom_columns_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    # get alert
    api_response = api_instance.get_alert_by_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_alert_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Alert**](Alert.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_list**
> AlertPaginationResponse get_alert_list(custom_columns=custom_columns, fields=fields, size=size, offset=offset, filter=filter)

get alert list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
custom_columns = 'custom_columns_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get alert list
    api_response = api_instance.get_alert_list(custom_columns=custom_columns, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_alert_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_columns** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**AlertPaginationResponse**](AlertPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_list_by_device_group_id**
> AlertPaginationResponse get_alert_list_by_device_group_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, filter=filter)

get device group alerts



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
need_message = false # bool |  (optional) (default to false)
custom_columns = 'custom_columns_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device group alerts
    api_response = api_instance.get_alert_list_by_device_group_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_alert_list_by_device_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**AlertPaginationResponse**](AlertPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_list_by_device_id**
> AlertPaginationResponse get_alert_list_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter, need_message=need_message, custom_columns=custom_columns, bound=bound, fields=fields, size=size, offset=offset, filter=filter)

get alerts



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
need_message = false # bool |  (optional) (default to false)
custom_columns = 'custom_columns_example' # str |  (optional)
bound = 'instances' # str |  (optional) (default to instances)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get alerts
    api_response = api_instance.get_alert_list_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter, need_message=need_message, custom_columns=custom_columns, bound=bound, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_alert_list_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **bound** | **str**|  | [optional] [default to instances]
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**AlertPaginationResponse**](AlertPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_rule_by_id**
> AlertRule get_alert_rule_by_id(id, fields=fields)

get alert rule by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get alert rule by id
    api_response = api_instance.get_alert_rule_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_alert_rule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**AlertRule**](AlertRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_rule_list**
> AlertRulePaginationResponse get_alert_rule_list(fields=fields, size=size, offset=offset, filter=filter)

get alert rule list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get alert rule list
    api_response = api_instance.get_alert_rule_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_alert_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**AlertRulePaginationResponse**](AlertRulePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_sdt_list_by_device_id**
> SDTPaginationResponse get_all_sdt_list_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)

get SDTs for a device



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get SDTs for a device
    api_response = api_instance.get_all_sdt_list_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_all_sdt_list_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**SDTPaginationResponse**](SDTPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_sdt_list_by_website_group_id**
> SDTPaginationResponse get_all_sdt_list_by_website_group_id(id, fields=fields, size=size, offset=offset, filter=filter)

get a list of SDTs for a website group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get a list of SDTs for a website group
    api_response = api_instance.get_all_sdt_list_by_website_group_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_all_sdt_list_by_website_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**SDTPaginationResponse**](SDTPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_token_list**
> ApiTokenPaginationResponse get_api_token_list()

get a list of api tokens across users



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))

try:
    # get a list of api tokens across users
    api_response = api_instance.get_api_token_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_api_token_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiTokenPaginationResponse**](ApiTokenPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_token_list_by_admin_id**
> ApiTokenPaginationResponse get_api_token_list_by_admin_id(admin_id, fields=fields, size=size, offset=offset, filter=filter)

get api tokens for a user



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
admin_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get api tokens for a user
    api_response = api_instance.get_api_token_list_by_admin_id(admin_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_api_token_list_by_admin_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**ApiTokenPaginationResponse**](ApiTokenPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_associated_device_list_by_data_source_id**
> DeviceDataSourceAssociatedPaginationResponse get_associated_device_list_by_data_source_id(id, fields=fields, size=size, offset=offset, filter=filter)

get devices associated with a datasource



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get devices associated with a datasource
    api_response = api_instance.get_associated_device_list_by_data_source_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_associated_device_list_by_data_source_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceDataSourceAssociatedPaginationResponse**](DeviceDataSourceAssociatedPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_log_by_id**
> AuditLog get_audit_log_by_id(id)

Get audit log by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get audit log by id
    api_response = api_instance.get_audit_log_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_audit_log_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AuditLog**](AuditLog.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_log_list**
> AccessLogPaginationResponse get_audit_log_list(format=format, fields=fields, size=size, offset=offset, filter=filter)

Get audit logs



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
format = 'format_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # Get audit logs
    api_response = api_instance.get_audit_log_list(format=format, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_audit_log_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**AccessLogPaginationResponse**](AccessLogPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_external_id**
> AwsExternalId get_aws_external_id()

Get AWS external id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))

try:
    # Get AWS external id
    api_response = api_instance.get_aws_external_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_aws_external_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AwsExternalId**](AwsExternalId.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_by_id**
> Collector get_collector_by_id(id, fields=fields)

get collector



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get collector
    api_response = api_instance.get_collector_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Collector**](Collector.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_group_by_id**
> CollectorGroup get_collector_group_by_id(id, fields=fields)

get collector group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get collector group
    api_response = api_instance.get_collector_group_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**CollectorGroup**](CollectorGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_group_list**
> CollectorGroupPaginationResponse get_collector_group_list(fields=fields, size=size, offset=offset, filter=filter)

get collector group list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get collector group list
    api_response = api_instance.get_collector_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**CollectorGroupPaginationResponse**](CollectorGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_installer**
> file get_collector_installer(collector_id, os_and_arch, collector_version=collector_version, token=token, monitor_others=monitor_others, collector_size=collector_size, use_ea=use_ea)

get collector installer



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
collector_id = 56 # int | 
os_and_arch = 'os_and_arch_example' # str | 
collector_version = 56 # int | The version of the installer you'd like to download. This defaults to the latest GD Collector, unless useEA is true (optional)
token = 'token_example' # str |  (optional)
monitor_others = true # bool |  (optional) (default to true)
collector_size = 'medium' # str | The size of the Collector you'd like to install. Options are nano, small (requires 2GB memory), medium (requires 4GB memory), large (requires 8GB memory). Requires collector version 22.180 or higher. Defaults to small (optional) (default to medium)
use_ea = false # bool | If true, the latest EA Collector version will be used. Defaults to false (optional) (default to false)

try:
    # get collector installer
    api_response = api_instance.get_collector_installer(collector_id, os_and_arch, collector_version=collector_version, token=token, monitor_others=monitor_others, collector_size=collector_size, use_ea=use_ea)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_installer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_id** | **int**|  | 
 **os_and_arch** | **str**|  | 
 **collector_version** | **int**| The version of the installer you&#39;d like to download. This defaults to the latest GD Collector, unless useEA is true | [optional] 
 **token** | **str**|  | [optional] 
 **monitor_others** | **bool**|  | [optional] [default to true]
 **collector_size** | **str**| The size of the Collector you&#39;d like to install. Options are nano, small (requires 2GB memory), medium (requires 4GB memory), large (requires 8GB memory). Requires collector version 22.180 or higher. Defaults to small | [optional] [default to medium]
 **use_ea** | **bool**| If true, the latest EA Collector version will be used. Defaults to false | [optional] [default to false]

### Return type

[**file**](file.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_list**
> CollectorPaginationResponse get_collector_list(fields=fields, size=size, offset=offset, filter=filter)

get collector list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get collector list
    api_response = api_instance.get_collector_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**CollectorPaginationResponse**](CollectorPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_by_id**
> Dashboard get_dashboard_by_id(id, template=template, format=format, fields=fields)

get dashboard



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
template = false # bool |  (optional) (default to false)
format = 'json' # str |  (optional) (default to json)
fields = 'fields_example' # str |  (optional)

try:
    # get dashboard
    api_response = api_instance.get_dashboard_by_id(id, template=template, format=format, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_dashboard_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **template** | **bool**|  | [optional] [default to false]
 **format** | **str**|  | [optional] [default to json]
 **fields** | **str**|  | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_group_by_id**
> DashboardGroup get_dashboard_group_by_id(id, template=template, fields=fields)

get dashboard group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
template = false # bool |  (optional) (default to false)
fields = 'fields_example' # str |  (optional)

try:
    # get dashboard group
    api_response = api_instance.get_dashboard_group_by_id(id, template=template, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_dashboard_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **template** | **bool**|  | [optional] [default to false]
 **fields** | **str**|  | [optional] 

### Return type

[**DashboardGroup**](DashboardGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_group_list**
> DashboardGroupPaginationResponse get_dashboard_group_list(fields=fields, size=size, offset=offset, filter=filter)

get dashboard group list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get dashboard group list
    api_response = api_instance.get_dashboard_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_dashboard_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DashboardGroupPaginationResponse**](DashboardGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_list**
> DashboardPaginationResponse get_dashboard_list(fields=fields, size=size, offset=offset, filter=filter)

get dashboard list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get dashboard list
    api_response = api_instance.get_dashboard_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_dashboard_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DashboardPaginationResponse**](DashboardPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_source_overview_graph_by_id**
> DataSourceOverviewGraph get_data_source_overview_graph_by_id(ds_id, id)

get datasource overview graph by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
ds_id = 56 # int | 
id = 56 # int | 

try:
    # get datasource overview graph by id
    api_response = api_instance.get_data_source_overview_graph_by_id(ds_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_data_source_overview_graph_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ds_id** | **int**|  | 
 **id** | **int**|  | 

### Return type

[**DataSourceOverviewGraph**](DataSourceOverviewGraph.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_source_overview_graph_list**
> DatasourceOverviewGraphPaginationResponse get_data_source_overview_graph_list(ds_id, fields=fields, size=size, offset=offset, filter=filter)

get datasource overview graph list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
ds_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get datasource overview graph list
    api_response = api_instance.get_data_source_overview_graph_list(ds_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_data_source_overview_graph_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ds_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DatasourceOverviewGraphPaginationResponse**](DatasourceOverviewGraphPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasource_by_id**
> DataSource get_datasource_by_id(id, format=format, fields=fields)

get datasource by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
format = 'json' # str |  (optional) (default to json)
fields = 'fields_example' # str |  (optional)

try:
    # get datasource by id
    api_response = api_instance.get_datasource_by_id(id, format=format, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] [default to json]
 **fields** | **str**|  | [optional] 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasource_list**
> DatasourcePaginationResponse get_datasource_list(format=format, fields=fields, size=size, offset=offset, filter=filter)

get datasource list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
format = 'json' # str |  (optional) (default to json)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get datasource list
    api_response = api_instance.get_datasource_list(format=format, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_datasource_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] [default to json]
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DatasourcePaginationResponse**](DatasourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_command_result**
> Debug get_debug_command_result(id, collector_id=collector_id)

Get the result of a Collector debug command



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
collector_id = -1 # int |  (optional) (default to -1)

try:
    # Get the result of a Collector debug command
    api_response = api_instance.get_debug_command_result(id, collector_id=collector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_debug_command_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **collector_id** | **int**|  | [optional] [default to -1]

### Return type

[**Debug**](Debug.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_by_id**
> Device get_device_by_id(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields)

get device by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    # get device by id
    api_response = api_instance.get_device_by_id(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_config_source_config_by_id**
> DeviceDataSourceInstanceConfig get_device_config_source_config_by_id(device_id, hds_id, instance_id, id, format=format, start_epoch=start_epoch, fields=fields)

get a config for a device



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | 
instance_id = 56 # int | 
id = 'id_example' # str | 
format = 'json' # str |  (optional) (default to json)
start_epoch = 0 # int |  (optional) (default to 0)
fields = 'fields_example' # str |  (optional)

try:
    # get a config for a device
    api_response = api_instance.get_device_config_source_config_by_id(device_id, hds_id, instance_id, id, format=format, start_epoch=start_epoch, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_config_source_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **instance_id** | **int**|  | 
 **id** | **str**|  | 
 **format** | **str**|  | [optional] [default to json]
 **start_epoch** | **int**|  | [optional] [default to 0]
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceDataSourceInstanceConfig**](DeviceDataSourceInstanceConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_config_source_config_list**
> DeviceDatasourceInstanceConfigPaginationResponse get_device_config_source_config_list(device_id, hds_id, instance_id, fields=fields, size=size, offset=offset, filter=filter)

get config instances for a configsource



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | 
instance_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get config instances for a configsource
    api_response = api_instance.get_device_config_source_config_list(device_id, hds_id, instance_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_config_source_config_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **instance_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceDatasourceInstanceConfigPaginationResponse**](DeviceDatasourceInstanceConfigPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_by_id**
> DeviceDataSource get_device_datasource_by_id(device_id, id, fields=fields)

get device datasource 



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get device datasource 
    api_response = api_instance.get_device_datasource_by_id(device_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceDataSource**](DeviceDataSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_data_by_id**
> DeviceDataSourceData get_device_datasource_data_by_id(device_id, id, period=period, start=start, end=end, datapoints=datapoints, format=format)

get device datasource data 



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
id = 56 # int | 
period = 1 # float |  (optional) (default to 1)
start = 0 # int |  (optional) (default to 0)
end = 0 # int |  (optional) (default to 0)
datapoints = 'datapoints_example' # str |  (optional)
format = 'json' # str |  (optional) (default to json)

try:
    # get device datasource data 
    api_response = api_instance.get_device_datasource_data_by_id(device_id, id, period=period, start=start, end=end, datapoints=datapoints, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_data_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **id** | **int**|  | 
 **period** | **float**|  | [optional] [default to 1]
 **start** | **int**|  | [optional] [default to 0]
 **end** | **int**|  | [optional] [default to 0]
 **datapoints** | **str**|  | [optional] 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**DeviceDataSourceData**](DeviceDataSourceData.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_alert_setting_by_id**
> DeviceDataSourceInstanceAlertSetting get_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, fields=fields)

get device instance alert setting



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | Device-DataSource ID
instance_id = 56 # int | 
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get device instance alert setting
    api_response = api_instance.get_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_alert_setting_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| Device-DataSource ID | 
 **instance_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceDataSourceInstanceAlertSetting**](DeviceDataSourceInstanceAlertSetting.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_alert_setting_list**
> DeviceDataSourceInstanceAlertSettingPaginationResponse get_device_datasource_instance_alert_setting_list(device_id, hds_id, instance_id)

get a list of alert settings for a device



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | Device-DataSource ID
instance_id = 56 # int | 

try:
    # get a list of alert settings for a device
    api_response = api_instance.get_device_datasource_instance_alert_setting_list(device_id, hds_id, instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_alert_setting_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| Device-DataSource ID | 
 **instance_id** | **int**|  | 

### Return type

[**DeviceDataSourceInstanceAlertSettingPaginationResponse**](DeviceDataSourceInstanceAlertSettingPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_by_id**
> DeviceDataSourceInstance get_device_datasource_instance_by_id(device_id, hds_id, id, fields=fields)

get device instance 



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get device instance 
    api_response = api_instance.get_device_datasource_instance_by_id(device_id, hds_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_data**
> DeviceDataSourceInstanceData get_device_datasource_instance_data(device_id, hds_id, id, period=period, start=start, end=end, datapoints=datapoints, format=format)

get device instance data



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
id = 56 # int | 
period = 1 # float |  (optional) (default to 1)
start = 0 # int |  (optional) (default to 0)
end = 0 # int |  (optional) (default to 0)
datapoints = 'datapoints_example' # str |  (optional)
format = 'json' # str |  (optional) (default to json)

try:
    # get device instance data
    api_response = api_instance.get_device_datasource_instance_data(device_id, hds_id, id, period=period, start=start, end=end, datapoints=datapoints, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **id** | **int**|  | 
 **period** | **float**|  | [optional] [default to 1]
 **start** | **int**|  | [optional] [default to 0]
 **end** | **int**|  | [optional] [default to 0]
 **datapoints** | **str**|  | [optional] 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**DeviceDataSourceInstanceData**](DeviceDataSourceInstanceData.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_graph_data**
> GraphPlot get_device_datasource_instance_graph_data(device_id, hds_id, id, graph_id, start=start, end=end, format=format)

get device instance graph data 



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
id = 56 # int | 
graph_id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
format = 'format_example' # str |  (optional)

try:
    # get device instance graph data 
    api_response = api_instance.get_device_datasource_instance_graph_data(device_id, hds_id, id, graph_id, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **id** | **int**|  | 
 **graph_id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**GraphPlot**](GraphPlot.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_group_by_id**
> DeviceDataSourceInstanceGroup get_device_datasource_instance_group_by_id(device_id, device_ds_id, id, fields=fields)

get device datasource instance group 



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get device datasource instance group 
    api_response = api_instance.get_device_datasource_instance_group_by_id(device_id, device_ds_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**| The device-datasource ID you&#39;d like to add an instance group for | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceDataSourceInstanceGroup**](DeviceDataSourceInstanceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_group_list**
> DeviceDatasourceInstanceGroupPaginationResponse get_device_datasource_instance_group_list(device_id, device_ds_id, fields=fields, size=size, offset=offset, filter=filter)

get device datasource instance group list 



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device datasource instance group list 
    api_response = api_instance.get_device_datasource_instance_group_list(device_id, device_ds_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**| The device-datasource ID you&#39;d like to add an instance group for | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceDatasourceInstanceGroupPaginationResponse**](DeviceDatasourceInstanceGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_group_overview_graph_data**
> GraphPlot get_device_datasource_instance_group_overview_graph_data(device_id, device_ds_id, dsig_id, ograph_id, start=start, end=end, format=format)

get device instance group overview graph data 



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
dsig_id = 56 # int | 
ograph_id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
format = 'format_example' # str |  (optional)

try:
    # get device instance group overview graph data 
    api_response = api_instance.get_device_datasource_instance_group_overview_graph_data(device_id, device_ds_id, dsig_id, ograph_id, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_group_overview_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**| The device-datasource ID you&#39;d like to add an instance group for | 
 **dsig_id** | **int**|  | 
 **ograph_id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**GraphPlot**](GraphPlot.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_list**
> DeviceDatasourceInstancePaginationResponse get_device_datasource_instance_list(device_id, hds_id)

get device instance list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID

try:
    # get device instance list
    api_response = api_instance.get_device_datasource_instance_list(device_id, hds_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 

### Return type

[**DeviceDatasourceInstancePaginationResponse**](DeviceDatasourceInstancePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_sdt_history**
> DeviceGroupSDTHistoryPaginationResponse get_device_datasource_instance_sdt_history(device_id, hds_id, id, fields=fields, size=size, offset=offset, filter=filter)

get device instance SDT history



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device instance SDT history
    api_response = api_instance.get_device_datasource_instance_sdt_history(device_id, hds_id, id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_sdt_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceGroupSDTHistoryPaginationResponse**](DeviceGroupSDTHistoryPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_list**
> DeviceDatasourcePaginationResponse get_device_datasource_list(device_id, fields=fields, size=size, offset=offset, filter=filter)

get device datasource list 



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device datasource list 
    api_response = api_instance.get_device_datasource_list(device_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceDatasourcePaginationResponse**](DeviceDatasourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_by_id**
> DeviceGroup get_device_group_by_id(id, fields=fields)

get device group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get device group
    api_response = api_instance.get_device_group_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_cluster_alert_conf_by_id**
> DeviceClusterAlertConfig get_device_group_cluster_alert_conf_by_id(device_group_id, id)

Get cluster alert configuration by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
id = 56 # int | 

try:
    # Get cluster alert configuration by id
    api_response = api_instance.get_device_group_cluster_alert_conf_by_id(device_group_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_cluster_alert_conf_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **id** | **int**|  | 

### Return type

[**DeviceClusterAlertConfig**](DeviceClusterAlertConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_cluster_alert_conf_list**
> DeviceClusterAlertConfigPaginationResponse get_device_group_cluster_alert_conf_list(device_group_id, fields=fields, size=size, offset=offset, filter=filter)

get a list of cluster alert configurations for a device group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get a list of cluster alert configurations for a device group
    api_response = api_instance.get_device_group_cluster_alert_conf_list(device_group_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_cluster_alert_conf_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceClusterAlertConfigPaginationResponse**](DeviceClusterAlertConfigPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_datasource_alert_setting**
> DeviceGroupDataSourceAlertConfig get_device_group_datasource_alert_setting(device_group_id, ds_id, fields=fields)

get device group datasource alert setting 



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
ds_id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get device group datasource alert setting 
    api_response = api_instance.get_device_group_datasource_alert_setting(device_group_id, ds_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_datasource_alert_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **ds_id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceGroupDataSourceAlertConfig**](DeviceGroupDataSourceAlertConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_datasource_by_id**
> DeviceGroupDataSource get_device_group_datasource_by_id(device_group_id, id, fields=fields)

get device group datasource



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get device group datasource
    api_response = api_instance.get_device_group_datasource_by_id(device_group_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceGroupDataSource**](DeviceGroupDataSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_datasource_list**
> DeviceGroupDatasourcePaginationResponse get_device_group_datasource_list(device_group_id, include_disabled_data_source_without_instance=include_disabled_data_source_without_instance, fields=fields, size=size, offset=offset, filter=filter)

get device group datasource list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
include_disabled_data_source_without_instance = false # bool |  (optional) (default to false)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device group datasource list
    api_response = api_instance.get_device_group_datasource_list(device_group_id, include_disabled_data_source_without_instance=include_disabled_data_source_without_instance, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_datasource_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **include_disabled_data_source_without_instance** | **bool**|  | [optional] [default to false]
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceGroupDatasourcePaginationResponse**](DeviceGroupDatasourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_list**
> DeviceGroupPaginationResponse get_device_group_list(fields=fields, size=size, offset=offset, filter=filter)

get device group list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device group list
    api_response = api_instance.get_device_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceGroupPaginationResponse**](DeviceGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_property_by_name**
> EntityProperty get_device_group_property_by_name(gid, name, fields=fields)

get device group property by name



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
gid = 56 # int | group ID
name = 'name_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    # get device group property by name
    api_response = api_instance.get_device_group_property_by_name(gid, name, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**| group ID | 
 **name** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_property_list**
> PropertyPaginationResponse get_device_group_property_list(gid, fields=fields, size=size, offset=offset, filter=filter)

get device group properties



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
gid = 56 # int | group ID
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device group properties
    api_response = api_instance.get_device_group_property_list(gid, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_property_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**| group ID | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**PropertyPaginationResponse**](PropertyPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_sdt_list**
> SDTPaginationResponse get_device_group_sdt_list(id, fields=fields, size=size, offset=offset, filter=filter)

get device group SDTs



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device group SDTs
    api_response = api_instance.get_device_group_sdt_list(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_sdt_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**SDTPaginationResponse**](SDTPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_instance_graph_data_only_by_instance_id**
> GraphPlot get_device_instance_graph_data_only_by_instance_id(instance_id, graph_id, start=start, end=end, format=format)

get device instance data



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
instance_id = 56 # int | 
graph_id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
format = 'format_example' # str |  (optional)

try:
    # get device instance data
    api_response = api_instance.get_device_instance_graph_data_only_by_instance_id(instance_id, graph_id, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_instance_graph_data_only_by_instance_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**|  | 
 **graph_id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**GraphPlot**](GraphPlot.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_list**
> DevicePaginationResponse get_device_list(start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)

get device list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device list
    api_response = api_instance.get_device_list(start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DevicePaginationResponse**](DevicePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_property_by_name**
> EntityProperty get_device_property_by_name(device_id, name, fields=fields)

get device property by name



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
name = 'name_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    # get device property by name
    api_response = api_instance.get_device_property_by_name(device_id, name, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **name** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_property_list**
> PropertyPaginationResponse get_device_property_list(device_id, fields=fields, size=size, offset=offset, filter=filter)

get device properties



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device properties
    api_response = api_instance.get_device_property_list(device_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_property_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**PropertyPaginationResponse**](PropertyPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_escalation_chain_by_id**
> EscalatingChain get_escalation_chain_by_id(id, fields=fields)

get escalation chain by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get escalation chain by id
    api_response = api_instance.get_escalation_chain_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_escalation_chain_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**EscalatingChain**](EscalatingChain.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_escalation_chain_list**
> EscalationChainPaginationResponse get_escalation_chain_list(fields=fields, size=size, offset=offset, filter=filter)

get escalation chain list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get escalation chain list
    api_response = api_instance.get_escalation_chain_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_escalation_chain_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**EscalationChainPaginationResponse**](EscalationChainPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_immediate_device_list_by_device_group_id**
> DevicePaginationResponse get_immediate_device_list_by_device_group_id(id, fields=fields, size=size, offset=offset, filter=filter)

get immediate devices under group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get immediate devices under group
    api_response = api_instance.get_immediate_device_list_by_device_group_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_immediate_device_list_by_device_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DevicePaginationResponse**](DevicePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_immediate_website_list_by_website_group_id**
> WebsitePaginationResponse get_immediate_website_list_by_website_group_id(id, fields=fields, size=size, offset=offset, filter=filter)

get a list of websites for a group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get a list of websites for a group
    api_response = api_instance.get_immediate_website_list_by_website_group_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_immediate_website_list_by_website_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**WebsitePaginationResponse**](WebsitePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_netflow_endpoint_list**
> EndpointPaginationResponse get_netflow_endpoint_list(id, start=start, end=end, netflow_filter=netflow_filter, port=port, fields=fields, size=size, offset=offset, filter=filter)

get netflow endpoint list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
port = 'port_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get netflow endpoint list
    api_response = api_instance.get_netflow_endpoint_list(id, start=start, end=end, netflow_filter=netflow_filter, port=port, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_netflow_endpoint_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **port** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**EndpointPaginationResponse**](EndpointPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_netflow_flow_list**
> FlowRecordPaginationResponse get_netflow_flow_list(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)

get netflow flow list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get netflow flow list
    api_response = api_instance.get_netflow_flow_list(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_netflow_flow_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**FlowRecordPaginationResponse**](FlowRecordPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_netflow_port_list**
> PortPaginationResponse get_netflow_port_list(id, start=start, end=end, netflow_filter=netflow_filter, ip=ip, fields=fields, size=size, offset=offset, filter=filter)

get netflow port list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
ip = 'ip_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get netflow port list
    api_response = api_instance.get_netflow_port_list(id, start=start, end=end, netflow_filter=netflow_filter, ip=ip, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_netflow_port_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **ip** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**PortPaginationResponse**](PortPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_netscan_by_id**
> Netscan get_netscan_by_id(id)

get netscan by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # get netscan by id
    api_response = api_instance.get_netscan_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_netscan_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Netscan**](Netscan.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_netscan_list**
> NetscanPaginationResponse get_netscan_list(fields=fields, size=size, offset=offset, filter=filter)

get netscan list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get netscan list
    api_response = api_instance.get_netscan_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_netscan_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**NetscanPaginationResponse**](NetscanPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ops_note_by_id**
> OpsNote get_ops_note_by_id(id, fields=fields)

get opsnote by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    # get opsnote by id
    api_response = api_instance.get_ops_note_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_ops_note_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**OpsNote**](OpsNote.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ops_note_list**
> OpsNotePaginationResponse get_ops_note_list(fields=fields, size=size, offset=offset, filter=filter)

get opsnote list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get opsnote list
    api_response = api_instance.get_ops_note_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_ops_note_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**OpsNotePaginationResponse**](OpsNotePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipient_group_by_id**
> RecipientGroup get_recipient_group_by_id(id)

get recipient group by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # get recipient group by id
    api_response = api_instance.get_recipient_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_recipient_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RecipientGroup**](RecipientGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipient_group_list**
> RecipientGroupPaginationResponse get_recipient_group_list(fields=fields, size=size, offset=offset, filter=filter)

get recipient group List



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get recipient group List
    api_response = api_instance.get_recipient_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_recipient_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RecipientGroupPaginationResponse**](RecipientGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_by_id**
> ReportBase get_report_by_id(id, fields=fields)

get report by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get report by id
    api_response = api_instance.get_report_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**ReportBase**](ReportBase.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_group_by_id**
> ReportGroup get_report_group_by_id(id)

get report group by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # get report group by id
    api_response = api_instance.get_report_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_report_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReportGroup**](ReportGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_group_list**
> ReportGroupPaginationResponse get_report_group_list(fields=fields, size=size, offset=offset, filter=filter)

get report group list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get report group list
    api_response = api_instance.get_report_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_report_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**ReportGroupPaginationResponse**](ReportGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_list**
> ReportPaginationResponse get_report_list(fields=fields, size=size, offset=offset, filter=filter)

get report list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get report list
    api_response = api_instance.get_report_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_report_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**ReportPaginationResponse**](ReportPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_by_id**
> Role get_role_by_id(id, fields=fields)

get role by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get role by id
    api_response = api_instance.get_role_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_role_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_list**
> RolePaginationResponse get_role_list(fields=fields, size=size, offset=offset, filter=filter)

get role list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get role list
    api_response = api_instance.get_role_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_role_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RolePaginationResponse**](RolePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdt_by_id**
> SDT get_sdt_by_id(id, fields=fields)

get SDT by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    # get SDT by id
    api_response = api_instance.get_sdt_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_sdt_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**SDT**](SDT.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdt_history_by_device_data_source_id**
> DeviceDataSourceSDTHistoryPaginationResponse get_sdt_history_by_device_data_source_id(device_id, id, fields=fields, size=size, offset=offset, filter=filter)

get SDT history for the device dataSource



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get SDT history for the device dataSource
    api_response = api_instance.get_sdt_history_by_device_data_source_id(device_id, id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_sdt_history_by_device_data_source_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceDataSourceSDTHistoryPaginationResponse**](DeviceDataSourceSDTHistoryPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdt_history_by_device_group_id**
> DeviceGroupSDTHistoryPaginationResponse get_sdt_history_by_device_group_id(id, fields=fields, size=size, offset=offset, filter=filter)

get SDT history for the group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get SDT history for the group
    api_response = api_instance.get_sdt_history_by_device_group_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_sdt_history_by_device_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceGroupSDTHistoryPaginationResponse**](DeviceGroupSDTHistoryPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdt_history_by_device_id**
> DeviceSDTHistoryPaginationResponse get_sdt_history_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)

get SDT history for the device



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get SDT history for the device
    api_response = api_instance.get_sdt_history_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_sdt_history_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceSDTHistoryPaginationResponse**](DeviceSDTHistoryPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdt_list**
> SDTPaginationResponse get_sdt_list(fields=fields, size=size, offset=offset, filter=filter)

get SDT list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get SDT list
    api_response = api_instance.get_sdt_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_sdt_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**SDTPaginationResponse**](SDTPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_monitor_check_point_list**
> SiteMonitorCheckPointPaginationResponse get_site_monitor_check_point_list(fields=fields, size=size, offset=offset, filter=filter)

get website checkpoint list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get website checkpoint list
    api_response = api_instance.get_site_monitor_check_point_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_site_monitor_check_point_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**SiteMonitorCheckPointPaginationResponse**](SiteMonitorCheckPointPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_talkers_graph**
> GraphPlot get_top_talkers_graph(id, start=start, end=end, netflow_filter=netflow_filter, format=format, keyword=keyword)

get top talkers graph



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
format = 'format_example' # str |  (optional)
keyword = 'keyword_example' # str |  (optional)

try:
    # get top talkers graph
    api_response = api_instance.get_top_talkers_graph(id, start=start, end=end, netflow_filter=netflow_filter, format=format, keyword=keyword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_top_talkers_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **format** | **str**|  | [optional] 
 **keyword** | **str**|  | [optional] 

### Return type

[**GraphPlot**](GraphPlot.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unmonitored_device_list**
> UnmonitoredDevicePaginationResponse get_unmonitored_device_list(fields=fields, size=size, offset=offset, filter=filter)

get unmonitored device list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get unmonitored device list
    api_response = api_instance.get_unmonitored_device_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_unmonitored_device_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**UnmonitoredDevicePaginationResponse**](UnmonitoredDevicePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_update_reason_list_by_data_source_id**
> DataSourceUpdateReasonsPaginationResponse get_update_reason_list_by_data_source_id(id, fields=fields, size=size, offset=offset, filter=filter)

get update history for a datasource



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get update history for a datasource
    api_response = api_instance.get_update_reason_list_by_data_source_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_update_reason_list_by_data_source_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DataSourceUpdateReasonsPaginationResponse**](DataSourceUpdateReasonsPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_alert_list_by_website_id**
> AlertPaginationResponse get_website_alert_list_by_website_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, filter=filter)

get alerts for a website



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
need_message = false # bool |  (optional) (default to false)
custom_columns = 'custom_columns_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get alerts for a website
    api_response = api_instance.get_website_alert_list_by_website_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_alert_list_by_website_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**AlertPaginationResponse**](AlertPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_by_id**
> Website get_website_by_id(id, format=format)

get website by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
format = 'json' # str |  (optional) (default to json)

try:
    # get website by id
    api_response = api_instance.get_website_by_id(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**Website**](Website.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_checkpoint_data_by_id**
> WebsiteCheckpointRawData get_website_checkpoint_data_by_id(srv_id, check_id, period=period, start=start, end=end, datapoints=datapoints, format=format)

get data for a website checkpoint



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
srv_id = 56 # int | 
check_id = 56 # int | 
period = 1 # float |  (optional) (default to 1)
start = 0 # int |  (optional) (default to 0)
end = 0 # int |  (optional) (default to 0)
datapoints = 'datapoints_example' # str |  (optional)
format = 'json' # str |  (optional) (default to json)

try:
    # get data for a website checkpoint
    api_response = api_instance.get_website_checkpoint_data_by_id(srv_id, check_id, period=period, start=start, end=end, datapoints=datapoints, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_checkpoint_data_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **srv_id** | **int**|  | 
 **check_id** | **int**|  | 
 **period** | **float**|  | [optional] [default to 1]
 **start** | **int**|  | [optional] [default to 0]
 **end** | **int**|  | [optional] [default to 0]
 **datapoints** | **str**|  | [optional] 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**WebsiteCheckpointRawData**](WebsiteCheckpointRawData.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_data_by_graph_name**
> GraphPlot get_website_data_by_graph_name(id, graph_name, start=start, end=end, format=format)

get website data by graph name



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
graph_name = 'graph_name_example' # str | 
start = 0 # int |  (optional) (default to 0)
end = 0 # int |  (optional) (default to 0)
format = 'format_example' # str |  (optional)

try:
    # get website data by graph name
    api_response = api_instance.get_website_data_by_graph_name(id, graph_name, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_data_by_graph_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **graph_name** | **str**|  | 
 **start** | **int**|  | [optional] [default to 0]
 **end** | **int**|  | [optional] [default to 0]
 **format** | **str**|  | [optional] 

### Return type

[**GraphPlot**](GraphPlot.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_graph_data**
> GraphPlot get_website_graph_data(website_id, checkpoint_id, graph_name, start=start, end=end, format=format)

get website graph data



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
website_id = 56 # int | 
checkpoint_id = 56 # int | 
graph_name = 'graph_name_example' # str | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
format = 'format_example' # str |  (optional)

try:
    # get website graph data
    api_response = api_instance.get_website_graph_data(website_id, checkpoint_id, graph_name, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **int**|  | 
 **checkpoint_id** | **int**|  | 
 **graph_name** | **str**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**GraphPlot**](GraphPlot.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_group_by_id**
> WebsiteGroup get_website_group_by_id(id)

get website group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # get website group
    api_response = api_instance.get_website_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**WebsiteGroup**](WebsiteGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_group_list**
> WebsiteGroupPaginationResponse get_website_group_list(fields=fields, size=size, offset=offset, filter=filter)

get website group list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get website group list
    api_response = api_instance.get_website_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**WebsiteGroupPaginationResponse**](WebsiteGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_list**
> WebsitePaginationResponse get_website_list(collector_ids=collector_ids, fields=fields, size=size, offset=offset, filter=filter)

get website list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
collector_ids = 'collector_ids_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get website list
    api_response = api_instance.get_website_list(collector_ids=collector_ids, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_ids** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**WebsitePaginationResponse**](WebsitePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_property_list_by_website_id**
> PropertyPaginationResponse get_website_property_list_by_website_id(id, fields=fields, size=size, offset=offset, filter=filter)

get a list of properties for a website



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get a list of properties for a website
    api_response = api_instance.get_website_property_list_by_website_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_property_list_by_website_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**PropertyPaginationResponse**](PropertyPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_sdt_list_by_website_id**
> SDTPaginationResponse get_website_sdt_list_by_website_id(id, fields=fields, size=size, offset=offset, filter=filter)

get a list of SDTs for a website



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get a list of SDTs for a website
    api_response = api_instance.get_website_sdt_list_by_website_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_sdt_list_by_website_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**SDTPaginationResponse**](SDTPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_by_id**
> Widget get_widget_by_id(id, fields=fields)

get widget by id



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get widget by id
    api_response = api_instance.get_widget_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_widget_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_data_by_id**
> WidgetData get_widget_data_by_id(id, start=start, end=end, format=format)

get widget data



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
format = 'format_example' # str |  (optional)

try:
    # get widget data
    api_response = api_instance.get_widget_data_by_id(id, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_widget_data_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**WidgetData**](WidgetData.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_list**
> WidgetPaginationResponse get_widget_list(fields=fields, size=size, offset=offset, filter=filter)

get widget list



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get widget list
    api_response = api_instance.get_widget_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_widget_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**WidgetPaginationResponse**](WidgetPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_list_by_dashboard_id**
> WidgetPaginationResponse get_widget_list_by_dashboard_id(id, fields=fields, size=size, offset=offset, filter=filter)

get widget list by DashboardId



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get widget list by DashboardId
    api_response = api_instance.get_widget_list_by_dashboard_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_widget_list_by_dashboard_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**WidgetPaginationResponse**](WidgetPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_batch_job**
> object import_batch_job(file)

import batch job via xml



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = '/path/to/file.txt' # file | 

try:
    # import batch job via xml
    api_response = api_instance.import_batch_job(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_batch_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_config_source**
> object import_config_source(file)

import config source via xml



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = '/path/to/file.txt' # file | 

try:
    # import config source via xml
    api_response = api_instance.import_config_source(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_config_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_data_source**
> object import_data_source(file)

import datasource via xml



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = '/path/to/file.txt' # file | 

try:
    # import datasource via xml
    api_response = api_instance.import_data_source(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_event_source**
> object import_event_source(file)

import eventsource via xml



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = '/path/to/file.txt' # file | 

try:
    # import eventsource via xml
    api_response = api_instance.import_event_source(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_event_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_admin_by_id**
> Admin patch_admin_by_id(id, body, change_password=change_password)

update user



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Admin() # Admin | 
change_password = false # bool |  (optional) (default to false)

try:
    # update user
    api_response = api_instance.patch_admin_by_id(id, body, change_password=change_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_admin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Admin**](Admin.md)|  | 
 **change_password** | **bool**|  | [optional] [default to false]

### Return type

[**Admin**](Admin.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_alert_rule_by_id**
> AlertRule patch_alert_rule_by_id(id, body)

update alert rule



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.AlertRule() # AlertRule | 

try:
    # update alert rule
    api_response = api_instance.patch_alert_rule_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_alert_rule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**AlertRule**](AlertRule.md)|  | 

### Return type

[**AlertRule**](AlertRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_api_token_by_admin_id**
> APIToken patch_api_token_by_admin_id(admin_id, apitoken_id, body)

update api tokens for a user



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
admin_id = 56 # int | 
apitoken_id = 56 # int | 
body = logicmonitor_sdk.APIToken() # APIToken | 

try:
    # update api tokens for a user
    api_response = api_instance.patch_api_token_by_admin_id(admin_id, apitoken_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_api_token_by_admin_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**|  | 
 **apitoken_id** | **int**|  | 
 **body** | [**APIToken**](APIToken.md)|  | 

### Return type

[**APIToken**](APIToken.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_collector_by_id**
> Collector patch_collector_by_id(id, body, collector_load_balanced=collector_load_balanced, force_update_failed_over_devices=force_update_failed_over_devices)

update collector



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Collector() # Collector | 
collector_load_balanced = false # bool |  (optional) (default to false)
force_update_failed_over_devices = false # bool |  (optional) (default to false)

try:
    # update collector
    api_response = api_instance.patch_collector_by_id(id, body, collector_load_balanced=collector_load_balanced, force_update_failed_over_devices=force_update_failed_over_devices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_collector_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Collector**](Collector.md)|  | 
 **collector_load_balanced** | **bool**|  | [optional] [default to false]
 **force_update_failed_over_devices** | **bool**|  | [optional] [default to false]

### Return type

[**Collector**](Collector.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_collector_group_by_id**
> CollectorGroup patch_collector_group_by_id(id, body, collector_load_balanced=collector_load_balanced, force_update_failed_over_devices=force_update_failed_over_devices)

update collector group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.CollectorGroup() # CollectorGroup | 
collector_load_balanced = false # bool |  (optional) (default to false)
force_update_failed_over_devices = false # bool |  (optional) (default to false)

try:
    # update collector group
    api_response = api_instance.patch_collector_group_by_id(id, body, collector_load_balanced=collector_load_balanced, force_update_failed_over_devices=force_update_failed_over_devices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_collector_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**CollectorGroup**](CollectorGroup.md)|  | 
 **collector_load_balanced** | **bool**|  | [optional] [default to false]
 **force_update_failed_over_devices** | **bool**|  | [optional] [default to false]

### Return type

[**CollectorGroup**](CollectorGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_dashboard_by_id**
> Dashboard patch_dashboard_by_id(id, body, overwrite_group_fields=overwrite_group_fields)

update dashboard



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Dashboard() # Dashboard | 
overwrite_group_fields = false # bool |  (optional) (default to false)

try:
    # update dashboard
    api_response = api_instance.patch_dashboard_by_id(id, body, overwrite_group_fields=overwrite_group_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_dashboard_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Dashboard**](Dashboard.md)|  | 
 **overwrite_group_fields** | **bool**|  | [optional] [default to false]

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_dashboard_group_by_id**
> DashboardGroup patch_dashboard_group_by_id(id, body)

update dashboard group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.DashboardGroup() # DashboardGroup | 

try:
    # update dashboard group
    api_response = api_instance.patch_dashboard_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_dashboard_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DashboardGroup**](DashboardGroup.md)|  | 

### Return type

[**DashboardGroup**](DashboardGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device**
> Device patch_device(id, body, start=start, end=end, netflow_filter=netflow_filter, op_type=op_type)

update a device



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Device() # Device | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update a device
    api_response = api_instance.patch_device(id, body, start=start, end=end, netflow_filter=netflow_filter, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Device**](Device.md)|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**Device**](Device.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_datasource_instance_alert_setting_by_id**
> DeviceDataSourceInstanceAlertSetting patch_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, body)

update device instance alert setting



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | Device-DataSource ID
instance_id = 56 # int | 
id = 56 # int | 
body = logicmonitor_sdk.DeviceDataSourceInstanceAlertSetting() # DeviceDataSourceInstanceAlertSetting | 

try:
    # update device instance alert setting
    api_response = api_instance.patch_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_datasource_instance_alert_setting_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| Device-DataSource ID | 
 **instance_id** | **int**|  | 
 **id** | **int**|  | 
 **body** | [**DeviceDataSourceInstanceAlertSetting**](DeviceDataSourceInstanceAlertSetting.md)|  | 

### Return type

[**DeviceDataSourceInstanceAlertSetting**](DeviceDataSourceInstanceAlertSetting.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_datasource_instance_by_id**
> DeviceDataSourceInstance patch_device_datasource_instance_by_id(device_id, hds_id, id, body, op_type=op_type)

update device instance



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
id = 56 # int | 
body = logicmonitor_sdk.DeviceDataSourceInstance() # DeviceDataSourceInstance | 
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update device instance
    api_response = api_instance.patch_device_datasource_instance_by_id(device_id, hds_id, id, body, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_datasource_instance_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **id** | **int**|  | 
 **body** | [**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)|  | 
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_datasource_instance_group_by_id**
> DeviceDataSourceInstanceGroup patch_device_datasource_instance_group_by_id(device_id, device_ds_id, id, body)

update device datasource instance group 



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
id = 56 # int | 
body = logicmonitor_sdk.DeviceDataSourceInstanceGroup() # DeviceDataSourceInstanceGroup | 

try:
    # update device datasource instance group 
    api_response = api_instance.patch_device_datasource_instance_group_by_id(device_id, device_ds_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_datasource_instance_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**| The device-datasource ID you&#39;d like to add an instance group for | 
 **id** | **int**|  | 
 **body** | [**DeviceDataSourceInstanceGroup**](DeviceDataSourceInstanceGroup.md)|  | 

### Return type

[**DeviceDataSourceInstanceGroup**](DeviceDataSourceInstanceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_group_by_id**
> DeviceGroup patch_device_group_by_id(id, body)

update device group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.DeviceGroup() # DeviceGroup | 

try:
    # update device group
    api_response = api_instance.patch_device_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DeviceGroup**](DeviceGroup.md)|  | 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_group_cluster_alert_conf_by_id**
> DeviceClusterAlertConfig patch_device_group_cluster_alert_conf_by_id(device_group_id, id, body)

Update cluster alert configuration



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
id = 56 # int | 
body = logicmonitor_sdk.DeviceClusterAlertConfig() # DeviceClusterAlertConfig | 

try:
    # Update cluster alert configuration
    api_response = api_instance.patch_device_group_cluster_alert_conf_by_id(device_group_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_group_cluster_alert_conf_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **id** | **int**|  | 
 **body** | [**DeviceClusterAlertConfig**](DeviceClusterAlertConfig.md)|  | 

### Return type

[**DeviceClusterAlertConfig**](DeviceClusterAlertConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_group_datasource_alert_setting**
> DeviceGroupDataSourceAlertConfig patch_device_group_datasource_alert_setting(device_group_id, ds_id, body)

update device group datasource alert setting



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
ds_id = 56 # int | 
body = logicmonitor_sdk.DeviceGroupDataSourceAlertConfig() # DeviceGroupDataSourceAlertConfig | 

try:
    # update device group datasource alert setting
    api_response = api_instance.patch_device_group_datasource_alert_setting(device_group_id, ds_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_group_datasource_alert_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **ds_id** | **int**|  | 
 **body** | [**DeviceGroupDataSourceAlertConfig**](DeviceGroupDataSourceAlertConfig.md)|  | 

### Return type

[**DeviceGroupDataSourceAlertConfig**](DeviceGroupDataSourceAlertConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_group_property_by_name**
> EntityProperty patch_device_group_property_by_name(gid, name, body)

update device group property



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
gid = 56 # int | group ID
name = 'name_example' # str | 
body = logicmonitor_sdk.EntityProperty() # EntityProperty | 

try:
    # update device group property
    api_response = api_instance.patch_device_group_property_by_name(gid, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_group_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**| group ID | 
 **name** | **str**|  | 
 **body** | [**EntityProperty**](EntityProperty.md)|  | 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_property_by_name**
> EntityProperty patch_device_property_by_name(device_id, name, body)

update device property



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
name = 'name_example' # str | 
body = logicmonitor_sdk.EntityProperty() # EntityProperty | 

try:
    # update device property
    api_response = api_instance.patch_device_property_by_name(device_id, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **name** | **str**|  | 
 **body** | [**EntityProperty**](EntityProperty.md)|  | 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_escalation_chain_by_id**
> EscalatingChain patch_escalation_chain_by_id(id, body)

update escalation chain



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.EscalatingChain() # EscalatingChain | 

try:
    # update escalation chain
    api_response = api_instance.patch_escalation_chain_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_escalation_chain_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**EscalatingChain**](EscalatingChain.md)|  | 

### Return type

[**EscalatingChain**](EscalatingChain.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_netscan**
> Netscan patch_netscan(id, body=body, reason=reason)

update a netscan



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Netscan() # Netscan |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # update a netscan
    api_response = api_instance.patch_netscan(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_netscan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Netscan**](Netscan.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**Netscan**](Netscan.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_ops_note_by_id**
> OpsNote patch_ops_note_by_id(id, body)

update opsnote



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
body = logicmonitor_sdk.OpsNote() # OpsNote | 

try:
    # update opsnote
    api_response = api_instance.patch_ops_note_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_ops_note_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**OpsNote**](OpsNote.md)|  | 

### Return type

[**OpsNote**](OpsNote.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_recipient_group_by_id**
> RecipientGroup patch_recipient_group_by_id(id, body)

update recipient group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.RecipientGroup() # RecipientGroup | 

try:
    # update recipient group
    api_response = api_instance.patch_recipient_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_recipient_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RecipientGroup**](RecipientGroup.md)|  | 

### Return type

[**RecipientGroup**](RecipientGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_report_by_id**
> ReportBase patch_report_by_id(id, body)

update report



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.ReportBase() # ReportBase | 

try:
    # update report
    api_response = api_instance.patch_report_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ReportBase**](ReportBase.md)|  | 

### Return type

[**ReportBase**](ReportBase.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_report_group_by_id**
> ReportGroup patch_report_group_by_id(id, body)

update report group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.ReportGroup() # ReportGroup | 

try:
    # update report group
    api_response = api_instance.patch_report_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_report_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ReportGroup**](ReportGroup.md)|  | 

### Return type

[**ReportGroup**](ReportGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_role_by_id**
> Role patch_role_by_id(id, body)

update role



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Role() # Role | 

try:
    # update role
    api_response = api_instance.patch_role_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_role_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sdt_by_id**
> SDT patch_sdt_by_id(id, body)

update SDT



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
body = logicmonitor_sdk.SDT() # SDT | 

try:
    # update SDT
    api_response = api_instance.patch_sdt_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_sdt_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SDT**](SDT.md)|  | 

### Return type

[**SDT**](SDT.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_website_by_id**
> Website patch_website_by_id(id, body)

update website



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Website() # Website | 

try:
    # update website
    api_response = api_instance.patch_website_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_website_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Website**](Website.md)|  | 

### Return type

[**Website**](Website.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_website_group_by_id**
> WebsiteGroup patch_website_group_by_id(id, body)

update website group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.WebsiteGroup() # WebsiteGroup | 

try:
    # update website group
    api_response = api_instance.patch_website_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_website_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**WebsiteGroup**](WebsiteGroup.md)|  | 

### Return type

[**WebsiteGroup**](WebsiteGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_widget_by_id**
> Widget patch_widget_by_id(id, body)

update widget



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Widget() # Widget | 

try:
    # update widget
    api_response = api_instance.patch_widget_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_widget_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Widget**](Widget.md)|  | 

### Return type

[**Widget**](Widget.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_auto_discovery_by_device_id**
> object schedule_auto_discovery_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter)

schedule active discovery for a device



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)

try:
    # schedule active discovery for a device
    api_response = api_instance.schedule_auto_discovery_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->schedule_auto_discovery_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_admin_by_id**
> Admin update_admin_by_id(id, body, change_password=change_password)

update user



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Admin() # Admin | 
change_password = false # bool |  (optional) (default to false)

try:
    # update user
    api_response = api_instance.update_admin_by_id(id, body, change_password=change_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_admin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Admin**](Admin.md)|  | 
 **change_password** | **bool**|  | [optional] [default to false]

### Return type

[**Admin**](Admin.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_rule_by_id**
> AlertRule update_alert_rule_by_id(id, body)

update alert rule



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.AlertRule() # AlertRule | 

try:
    # update alert rule
    api_response = api_instance.update_alert_rule_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_alert_rule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**AlertRule**](AlertRule.md)|  | 

### Return type

[**AlertRule**](AlertRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_token_by_admin_id**
> APIToken update_api_token_by_admin_id(admin_id, apitoken_id, body)

update api tokens for a user



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
admin_id = 56 # int | 
apitoken_id = 56 # int | 
body = logicmonitor_sdk.APIToken() # APIToken | 

try:
    # update api tokens for a user
    api_response = api_instance.update_api_token_by_admin_id(admin_id, apitoken_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_api_token_by_admin_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**|  | 
 **apitoken_id** | **int**|  | 
 **body** | [**APIToken**](APIToken.md)|  | 

### Return type

[**APIToken**](APIToken.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collector_by_id**
> Collector update_collector_by_id(id, body, collector_load_balanced=collector_load_balanced, force_update_failed_over_devices=force_update_failed_over_devices)

update collector



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Collector() # Collector | 
collector_load_balanced = false # bool |  (optional) (default to false)
force_update_failed_over_devices = false # bool |  (optional) (default to false)

try:
    # update collector
    api_response = api_instance.update_collector_by_id(id, body, collector_load_balanced=collector_load_balanced, force_update_failed_over_devices=force_update_failed_over_devices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_collector_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Collector**](Collector.md)|  | 
 **collector_load_balanced** | **bool**|  | [optional] [default to false]
 **force_update_failed_over_devices** | **bool**|  | [optional] [default to false]

### Return type

[**Collector**](Collector.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collector_group_by_id**
> CollectorGroup update_collector_group_by_id(id, body, collector_load_balanced=collector_load_balanced, force_update_failed_over_devices=force_update_failed_over_devices)

update collector group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.CollectorGroup() # CollectorGroup | 
collector_load_balanced = false # bool |  (optional) (default to false)
force_update_failed_over_devices = false # bool |  (optional) (default to false)

try:
    # update collector group
    api_response = api_instance.update_collector_group_by_id(id, body, collector_load_balanced=collector_load_balanced, force_update_failed_over_devices=force_update_failed_over_devices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_collector_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**CollectorGroup**](CollectorGroup.md)|  | 
 **collector_load_balanced** | **bool**|  | [optional] [default to false]
 **force_update_failed_over_devices** | **bool**|  | [optional] [default to false]

### Return type

[**CollectorGroup**](CollectorGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_by_id**
> Dashboard update_dashboard_by_id(id, body, overwrite_group_fields=overwrite_group_fields)

update dashboard



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Dashboard() # Dashboard | 
overwrite_group_fields = false # bool |  (optional) (default to false)

try:
    # update dashboard
    api_response = api_instance.update_dashboard_by_id(id, body, overwrite_group_fields=overwrite_group_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_dashboard_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Dashboard**](Dashboard.md)|  | 
 **overwrite_group_fields** | **bool**|  | [optional] [default to false]

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_group_by_id**
> DashboardGroup update_dashboard_group_by_id(id, body)

update dashboard group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.DashboardGroup() # DashboardGroup | 

try:
    # update dashboard group
    api_response = api_instance.update_dashboard_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_dashboard_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DashboardGroup**](DashboardGroup.md)|  | 

### Return type

[**DashboardGroup**](DashboardGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> Device update_device(id, body, start=start, end=end, netflow_filter=netflow_filter, op_type=op_type)

update a device



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Device() # Device | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update a device
    api_response = api_instance.update_device(id, body, start=start, end=end, netflow_filter=netflow_filter, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Device**](Device.md)|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**Device**](Device.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_datasource_instance_alert_setting_by_id**
> DeviceDataSourceInstanceAlertSetting update_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, body)

update device instance alert setting



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | Device-DataSource ID
instance_id = 56 # int | 
id = 56 # int | 
body = logicmonitor_sdk.DeviceDataSourceInstanceAlertSetting() # DeviceDataSourceInstanceAlertSetting | 

try:
    # update device instance alert setting
    api_response = api_instance.update_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_datasource_instance_alert_setting_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| Device-DataSource ID | 
 **instance_id** | **int**|  | 
 **id** | **int**|  | 
 **body** | [**DeviceDataSourceInstanceAlertSetting**](DeviceDataSourceInstanceAlertSetting.md)|  | 

### Return type

[**DeviceDataSourceInstanceAlertSetting**](DeviceDataSourceInstanceAlertSetting.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_datasource_instance_by_id**
> DeviceDataSourceInstance update_device_datasource_instance_by_id(device_id, hds_id, id, body, op_type=op_type)

update device instance



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
id = 56 # int | 
body = logicmonitor_sdk.DeviceDataSourceInstance() # DeviceDataSourceInstance | 
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update device instance
    api_response = api_instance.update_device_datasource_instance_by_id(device_id, hds_id, id, body, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_datasource_instance_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **id** | **int**|  | 
 **body** | [**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)|  | 
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_datasource_instance_group_by_id**
> DeviceDataSourceInstanceGroup update_device_datasource_instance_group_by_id(device_id, device_ds_id, id, body)

update device datasource instance group 



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
id = 56 # int | 
body = logicmonitor_sdk.DeviceDataSourceInstanceGroup() # DeviceDataSourceInstanceGroup | 

try:
    # update device datasource instance group 
    api_response = api_instance.update_device_datasource_instance_group_by_id(device_id, device_ds_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_datasource_instance_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**| The device-datasource ID you&#39;d like to add an instance group for | 
 **id** | **int**|  | 
 **body** | [**DeviceDataSourceInstanceGroup**](DeviceDataSourceInstanceGroup.md)|  | 

### Return type

[**DeviceDataSourceInstanceGroup**](DeviceDataSourceInstanceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_by_id**
> DeviceGroup update_device_group_by_id(id, body)

update device group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.DeviceGroup() # DeviceGroup | 

try:
    # update device group
    api_response = api_instance.update_device_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DeviceGroup**](DeviceGroup.md)|  | 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_cluster_alert_conf_by_id**
> DeviceClusterAlertConfig update_device_group_cluster_alert_conf_by_id(device_group_id, id, body)

Update cluster alert configuration



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
id = 56 # int | 
body = logicmonitor_sdk.DeviceClusterAlertConfig() # DeviceClusterAlertConfig | 

try:
    # Update cluster alert configuration
    api_response = api_instance.update_device_group_cluster_alert_conf_by_id(device_group_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_group_cluster_alert_conf_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **id** | **int**|  | 
 **body** | [**DeviceClusterAlertConfig**](DeviceClusterAlertConfig.md)|  | 

### Return type

[**DeviceClusterAlertConfig**](DeviceClusterAlertConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_datasource_alert_setting**
> DeviceGroupDataSourceAlertConfig update_device_group_datasource_alert_setting(device_group_id, ds_id, body)

update device group datasource alert setting



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
ds_id = 56 # int | 
body = logicmonitor_sdk.DeviceGroupDataSourceAlertConfig() # DeviceGroupDataSourceAlertConfig | 

try:
    # update device group datasource alert setting
    api_response = api_instance.update_device_group_datasource_alert_setting(device_group_id, ds_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_group_datasource_alert_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **ds_id** | **int**|  | 
 **body** | [**DeviceGroupDataSourceAlertConfig**](DeviceGroupDataSourceAlertConfig.md)|  | 

### Return type

[**DeviceGroupDataSourceAlertConfig**](DeviceGroupDataSourceAlertConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_property_by_name**
> EntityProperty update_device_group_property_by_name(gid, name, body)

update device group property



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
gid = 56 # int | group ID
name = 'name_example' # str | 
body = logicmonitor_sdk.EntityProperty() # EntityProperty | 

try:
    # update device group property
    api_response = api_instance.update_device_group_property_by_name(gid, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_group_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**| group ID | 
 **name** | **str**|  | 
 **body** | [**EntityProperty**](EntityProperty.md)|  | 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_property_by_name**
> EntityProperty update_device_property_by_name(device_id, name, body)

update device property



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
name = 'name_example' # str | 
body = logicmonitor_sdk.EntityProperty() # EntityProperty | 

try:
    # update device property
    api_response = api_instance.update_device_property_by_name(device_id, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **name** | **str**|  | 
 **body** | [**EntityProperty**](EntityProperty.md)|  | 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_escalation_chain_by_id**
> EscalatingChain update_escalation_chain_by_id(id, body)

update escalation chain



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.EscalatingChain() # EscalatingChain | 

try:
    # update escalation chain
    api_response = api_instance.update_escalation_chain_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_escalation_chain_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**EscalatingChain**](EscalatingChain.md)|  | 

### Return type

[**EscalatingChain**](EscalatingChain.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_netscan**
> Netscan update_netscan(id, body=body, reason=reason)

update a netscan



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Netscan() # Netscan |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # update a netscan
    api_response = api_instance.update_netscan(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_netscan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Netscan**](Netscan.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**Netscan**](Netscan.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ops_note_by_id**
> OpsNote update_ops_note_by_id(id, body)

update opsnote



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
body = logicmonitor_sdk.OpsNote() # OpsNote | 

try:
    # update opsnote
    api_response = api_instance.update_ops_note_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_ops_note_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**OpsNote**](OpsNote.md)|  | 

### Return type

[**OpsNote**](OpsNote.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recipient_group_by_id**
> RecipientGroup update_recipient_group_by_id(id, body)

update recipient group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.RecipientGroup() # RecipientGroup | 

try:
    # update recipient group
    api_response = api_instance.update_recipient_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_recipient_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RecipientGroup**](RecipientGroup.md)|  | 

### Return type

[**RecipientGroup**](RecipientGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_by_id**
> ReportBase update_report_by_id(id, body)

update report



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.ReportBase() # ReportBase | 

try:
    # update report
    api_response = api_instance.update_report_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ReportBase**](ReportBase.md)|  | 

### Return type

[**ReportBase**](ReportBase.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_group_by_id**
> ReportGroup update_report_group_by_id(id, body)

update report group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.ReportGroup() # ReportGroup | 

try:
    # update report group
    api_response = api_instance.update_report_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_report_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ReportGroup**](ReportGroup.md)|  | 

### Return type

[**ReportGroup**](ReportGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_by_id**
> Role update_role_by_id(id, body)

update role



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Role() # Role | 

try:
    # update role
    api_response = api_instance.update_role_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_role_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sdt_by_id**
> SDT update_sdt_by_id(id, body)

update SDT



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
body = logicmonitor_sdk.SDT() # SDT | 

try:
    # update SDT
    api_response = api_instance.update_sdt_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_sdt_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SDT**](SDT.md)|  | 

### Return type

[**SDT**](SDT.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_website_by_id**
> Website update_website_by_id(id, body)

update website



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Website() # Website | 

try:
    # update website
    api_response = api_instance.update_website_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_website_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Website**](Website.md)|  | 

### Return type

[**Website**](Website.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_website_group_by_id**
> WebsiteGroup update_website_group_by_id(id, body)

update website group



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.WebsiteGroup() # WebsiteGroup | 

try:
    # update website group
    api_response = api_instance.update_website_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_website_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**WebsiteGroup**](WebsiteGroup.md)|  | 

### Return type

[**WebsiteGroup**](WebsiteGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_widget_by_id**
> Widget update_widget_by_id(id, body)

update widget



### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'YOUR_COMPANY'
configuration.access_id = 'YOUR_ACCESS_ID'
configuration.access_key = 'YOUR_ACCESS_KEY'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Widget() # Widget | 

try:
    # update widget
    api_response = api_instance.update_widget_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_widget_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Widget**](Widget.md)|  | 

### Return type

[**Widget**](Widget.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

