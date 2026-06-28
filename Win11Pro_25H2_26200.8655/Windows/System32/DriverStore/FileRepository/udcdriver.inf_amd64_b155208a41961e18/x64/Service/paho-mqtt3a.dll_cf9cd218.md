# Binary Specification: paho-mqtt3a.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\udcdriver.inf_amd64_b155208a41961e18\x64\Service\paho-mqtt3a.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cf9cd21840f4b7d9ac77e1197e7e6a8b5c757c363bff410d73d0e422658e933e`
* **Total Exported Functions:** 51

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `MQTTAsync_connect` | `0x81F0` | 2,328 | UnwindData |  |
| 3 | `MQTTAsync_create` | `0x8B10` | 102 | UnwindData |  |
| 4 | `MQTTAsync_createWithOptions` | `0x8B80` | 1,312 | UnwindData |  |
| 5 | `MQTTAsync_destroy` | `0x90A0` | 69 | UnwindData |  |
| 6 | `MQTTAsync_disconnect` | `0x92C0` | 93 | UnwindData |  |
| 7 | `MQTTAsync_free` | `0x9320` | 83 | UnwindData |  |
| 8 | `MQTTAsync_freeMessage` | `0x9380` | 126 | UnwindData |  |
| 9 | `MQTTAsync_getPendingTokens` | `0x9490` | 262 | UnwindData |  |
| 10 | `MQTTAsync_getVersionInfo` | `0x96C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `MQTTAsync_global_init` | `0x9730` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `MQTTAsync_isComplete` | `0x9920` | 313 | UnwindData |  |
| 13 | `MQTTAsync_isConnected` | `0x9A60` | 129 | UnwindData |  |
| 14 | `MQTTAsync_malloc` | `0x9AF0` | 104 | UnwindData |  |
| 15 | `MQTTAsync_reconnect` | `0x9B60` | 130 | UnwindData |  |
| 16 | `MQTTAsync_send` | `0x9CF0` | 789 | UnwindData |  |
| 17 | `MQTTAsync_sendMessage` | `0xA010` | 235 | UnwindData |  |
| 18 | `MQTTAsync_setAfterPersistenceRead` | `0xA100` | 164 | UnwindData |  |
| 19 | `MQTTAsync_setBeforePersistenceWrite` | `0xA1B0` | 164 | UnwindData |  |
| 20 | `MQTTAsync_setCallbacks` | `0xA260` | 207 | UnwindData |  |
| 21 | `MQTTAsync_setConnected` | `0xA330` | 163 | UnwindData |  |
| 22 | `MQTTAsync_setConnectionLostCallback` | `0xA3E0` | 163 | UnwindData |  |
| 23 | `MQTTAsync_setDeliveryCompleteCallback` | `0xA490` | 163 | UnwindData |  |
| 24 | `MQTTAsync_setDisconnected` | `0xA540` | 163 | UnwindData |  |
| 25 | `MQTTAsync_setMessageArrivedCallback` | `0xA5F0` | 168 | UnwindData |  |
| 26 | `MQTTAsync_setTraceCallback` | `0xA6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `MQTTAsync_setTraceLevel` | `0xA6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `MQTTAsync_setUpdateConnectOptions` | `0xA6C0` | 150 | UnwindData |  |
| 29 | `MQTTAsync_strerror` | `0xA760` | 436 | UnwindData |  |
| 30 | `MQTTAsync_subscribe` | `0xA920` | 124 | UnwindData |  |
| 31 | `MQTTAsync_subscribeMany` | `0xA9A0` | 912 | UnwindData |  |
| 32 | `MQTTAsync_unsubscribe` | `0xAD30` | 112 | UnwindData |  |
| 33 | `MQTTAsync_unsubscribeMany` | `0xADA0` | 592 | UnwindData |  |
| 34 | `MQTTAsync_waitForCompletion` | `0xAFF0` | 362 | UnwindData |  |
| 47 | `Thread_create_mutex` | `0x16140` | 113 | UnwindData |  |
| 48 | `Thread_getid` | `0x16300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `Thread_lock_mutex` | `0x16310` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `Thread_start` | `0x163E0` | 108 | UnwindData |  |
| 51 | `Thread_unlock_mutex` | `0x16450` | 32 | UnwindData |  |
| 35 | `MQTTProperties_add` | `0x19850` | 208 | UnwindData |  |
| 36 | `MQTTProperties_copy` | `0x19A90` | 74 | UnwindData |  |
| 37 | `MQTTProperties_free` | `0x19D40` | 41 | UnwindData |  |
| 38 | `MQTTProperties_getNumericValue` | `0x19E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `MQTTProperties_getNumericValueAt` | `0x19E70` | 22 | UnwindData |  |
| 40 | `MQTTProperties_getProperty` | `0x19F80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `MQTTProperties_getPropertyAt` | `0x19FD0` | 17 | UnwindData |  |
| 42 | `MQTTProperties_hasProperty` | `0x1A040` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `MQTTProperties_propertyCount` | `0x1A0A0` | 11 | UnwindData |  |
| 44 | `MQTTPropertyName` | `0x1A6B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `MQTTProperty_getType` | `0x1A6E0` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `MQTTReasonCode_toString` | `0x1AA50` | 10,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `Heap_get_info` | `0x1D510` | 3,960 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
