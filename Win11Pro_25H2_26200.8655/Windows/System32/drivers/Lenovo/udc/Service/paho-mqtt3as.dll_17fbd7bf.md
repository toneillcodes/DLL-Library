# Binary Specification: paho-mqtt3as.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Service\paho-mqtt3as.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `17fbd7bfba914a8230319437345f680d899a3e900f4ae627b7e5c0f32d53d09a`
* **Total Exported Functions:** 51

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `MQTTAsync_connect` | `0x114150` | 3,227 | UnwindData |  |
| 3 | `MQTTAsync_create` | `0x114DF0` | 102 | UnwindData |  |
| 4 | `MQTTAsync_createWithOptions` | `0x114E60` | 1,415 | UnwindData |  |
| 5 | `MQTTAsync_destroy` | `0x1153F0` | 69 | UnwindData |  |
| 6 | `MQTTAsync_disconnect` | `0x115610` | 93 | UnwindData |  |
| 7 | `MQTTAsync_free` | `0x115670` | 83 | UnwindData |  |
| 8 | `MQTTAsync_freeMessage` | `0x1156D0` | 126 | UnwindData |  |
| 9 | `MQTTAsync_getPendingTokens` | `0x1157E0` | 262 | UnwindData |  |
| 10 | `MQTTAsync_getVersionInfo` | `0x115A10` | 263 | UnwindData |  |
| 11 | `MQTTAsync_global_init` | `0x115B20` | 27 | UnwindData |  |
| 12 | `MQTTAsync_isComplete` | `0x115D20` | 313 | UnwindData |  |
| 13 | `MQTTAsync_isConnected` | `0x115E60` | 129 | UnwindData |  |
| 14 | `MQTTAsync_malloc` | `0x115EF0` | 104 | UnwindData |  |
| 15 | `MQTTAsync_reconnect` | `0x115F60` | 130 | UnwindData |  |
| 16 | `MQTTAsync_send` | `0x1160F0` | 789 | UnwindData |  |
| 17 | `MQTTAsync_sendMessage` | `0x116410` | 235 | UnwindData |  |
| 18 | `MQTTAsync_setAfterPersistenceRead` | `0x116500` | 164 | UnwindData |  |
| 19 | `MQTTAsync_setBeforePersistenceWrite` | `0x1165B0` | 164 | UnwindData |  |
| 20 | `MQTTAsync_setCallbacks` | `0x116660` | 207 | UnwindData |  |
| 21 | `MQTTAsync_setConnected` | `0x116730` | 163 | UnwindData |  |
| 22 | `MQTTAsync_setConnectionLostCallback` | `0x1167E0` | 163 | UnwindData |  |
| 23 | `MQTTAsync_setDeliveryCompleteCallback` | `0x116890` | 163 | UnwindData |  |
| 24 | `MQTTAsync_setDisconnected` | `0x116940` | 163 | UnwindData |  |
| 25 | `MQTTAsync_setMessageArrivedCallback` | `0x1169F0` | 168 | UnwindData |  |
| 26 | `MQTTAsync_setTraceCallback` | `0x116AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `MQTTAsync_setTraceLevel` | `0x116AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `MQTTAsync_setUpdateConnectOptions` | `0x116AC0` | 150 | UnwindData |  |
| 29 | `MQTTAsync_strerror` | `0x116B60` | 436 | UnwindData |  |
| 30 | `MQTTAsync_subscribe` | `0x116D20` | 124 | UnwindData |  |
| 31 | `MQTTAsync_subscribeMany` | `0x116DA0` | 912 | UnwindData |  |
| 32 | `MQTTAsync_unsubscribe` | `0x117130` | 112 | UnwindData |  |
| 33 | `MQTTAsync_unsubscribeMany` | `0x1171A0` | 592 | UnwindData |  |
| 34 | `MQTTAsync_waitForCompletion` | `0x1173F0` | 362 | UnwindData |  |
| 47 | `Thread_create_mutex` | `0x1243A0` | 113 | UnwindData |  |
| 48 | `Thread_getid` | `0x124560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `Thread_lock_mutex` | `0x124570` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `Thread_start` | `0x124640` | 108 | UnwindData |  |
| 51 | `Thread_unlock_mutex` | `0x1246B0` | 32 | UnwindData |  |
| 35 | `MQTTProperties_add` | `0x127C40` | 208 | UnwindData |  |
| 36 | `MQTTProperties_copy` | `0x127E80` | 74 | UnwindData |  |
| 37 | `MQTTProperties_free` | `0x128130` | 41 | UnwindData |  |
| 38 | `MQTTProperties_getNumericValue` | `0x128250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `MQTTProperties_getNumericValueAt` | `0x128260` | 22 | UnwindData |  |
| 40 | `MQTTProperties_getProperty` | `0x128370` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `MQTTProperties_getPropertyAt` | `0x1283C0` | 17 | UnwindData |  |
| 42 | `MQTTProperties_hasProperty` | `0x128430` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `MQTTProperties_propertyCount` | `0x128490` | 11 | UnwindData |  |
| 44 | `MQTTPropertyName` | `0x128AA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `MQTTProperty_getType` | `0x128AD0` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `MQTTReasonCode_toString` | `0x128E40` | 10,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `Heap_get_info` | `0x12B5B0` | 3,193,816 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
