---
name: csa5-legacy-ibm-mq
description: Detection heuristics for IBM MQ (native com.ibm.mq and JMS) queue managers, channels, queues, and put/get patterns in legacy Java. Use during Discover and Integration analysis. Do not hardcode customer queue names.
---

# Legacy IBM MQ Skill

## Schema

Findings contract: [schema.json](schema.json)

## Goal

Find MQ integration points and document them as CSA integrations with evidence — supporting both **native IBM MQ Java API** and **JMS** variants.

## Detection signals (generic)

### Native API

- Imports/types: `com.ibm.mq.MQQueueManager`, `MQQueue`, `MQMessage`, `MQEnvironment`, `MQPutMessageOptions`, `MQGetMessageOptions`, `MQSecurityExit`
- Helper class-name hints only when paired with IBM imports: `*MQInterface*`, `*MqClient*`

### JMS variant (also detect)

- `com.ibm.mq.jms.*`, `MQConnectionFactory`, `MQQueueConnectionFactory`, `javax.jms.*` with IBM factories

### Config

- Property key regex: `(?i)(mq|ibm\.mq|wmq|ldap\.mq)\.(host|hostname|port|channel|queue|queueName|queueManager|qmgr|queueManagerName|channelName|portNumber|maxMessageSize|securityExit)`
- Files: `**/*mq*.properties`, `**/*queue*.properties`, `**/.bindings`

### Runtime clues

- Default MQ listener port `1414` near channel/qmgr settings
- Put/get option usage, syncpoint, message format (string/bytes)

## Emit into CSA artifacts

### Discover

- Framework/integration tech: IBM MQ (native or JMS) with config evidence
- Missing `.bindings` / qmgr config → `missing_artifacts` if code references MQ but config absent

### Integration

For each distinct queue/qmgr usage:

```json
{
  "integration_id": "INT-<slug>",
  "pattern_type": "asynchronous|legacy",
  "sync_async": "asynchronous|hybrid",
  "technology_stack": {
    "protocol": "IBM_MQ",
    "message_format": "unknown|string|bytes|xml|json",
    "transport_security": "unknown"
  },
  "endpoints": [],
  "evidence": []
}
```

Populate queue/qmgr/channel/host/port from properties into `technology_stack` or endpoint metadata — **copy values found in files**, do not invent.

### Tech Architecture

- MQ adapters as `integration` layer components (`CMP-*`)
- Note syncpoint / transaction coupling to DB when evident

## Anti-patterns

- Do not invent queue manager or queue names.
- Do not assume JMS when only `com.ibm.mq` native API is present.
- Do not classify as Kafka/Rabbit without evidence.