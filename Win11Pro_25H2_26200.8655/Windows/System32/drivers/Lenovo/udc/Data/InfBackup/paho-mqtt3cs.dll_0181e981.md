# Binary Specification: paho-mqtt3cs.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Data\InfBackup\paho-mqtt3cs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0181e98126e50f4df4b9df32153f052d105abdecc7b9147255dd011be1f4539d`
* **Total Exported Functions:** 54

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `MQTTClient_connect` | `0x1500` | 77 | UnwindData |  |
| 3 | `MQTTClient_connect5` | `0x1550` | 126 | UnwindData |  |
| 4 | `MQTTClient_create` | `0x2B50` | 33 | UnwindData |  |
| 5 | `MQTTClient_createWithOptions` | `0x2B80` | 73 | UnwindData |  |
| 6 | `MQTTClient_destroy` | `0x3440` | 85 | UnwindData |  |
| 7 | `MQTTClient_disconnect` | `0x3650` | 82 | UnwindData |  |
| 8 | `MQTTClient_disconnect5` | `0x3930` | 108 | UnwindData |  |
| 9 | `MQTTClient_free` | `0x3AC0` | 83 | UnwindData |  |
| 10 | `MQTTClient_freeMessage` | `0x3B20` | 126 | UnwindData |  |
| 11 | `MQTTClient_getPendingDeliveryTokens` | `0x3BA0` | 181 | UnwindData |  |
| 12 | `MQTTClient_getVersionInfo` | `0x3CE0` | 263 | UnwindData |  |
| 13 | `MQTTClient_global_init` | `0x3DF0` | 27 | UnwindData |  |
| 14 | `MQTTClient_isConnected` | `0x3FE0` | 129 | UnwindData |  |
| 15 | `MQTTClient_publish` | `0x4070` | 138 | UnwindData |  |
| 16 | `MQTTClient_publish5` | `0x4100` | 988 | UnwindData |  |
| 17 | `MQTTClient_publishMessage` | `0x44E0` | 158 | UnwindData |  |
| 18 | `MQTTClient_publishMessage5` | `0x4580` | 273 | UnwindData |  |
| 19 | `MQTTClient_receive` | `0x46A0` | 137 | UnwindData |  |
| 20 | `MQTTClient_setCallbacks` | `0x5260` | 194 | UnwindData |  |
| 21 | `MQTTClient_setCommandTimeout` | `0x5330` | 113 | UnwindData |  |
| 22 | `MQTTClient_setDisconnected` | `0x53B0` | 163 | UnwindData |  |
| 23 | `MQTTClient_setPublished` | `0x5460` | 163 | UnwindData |  |
| 24 | `MQTTClient_setTraceCallback` | `0x5510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `MQTTClient_setTraceLevel` | `0x5520` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `MQTTClient_strerror` | `0x5690` | 368 | UnwindData |  |
| 27 | `MQTTClient_subscribe` | `0x5800` | 241 | UnwindData |  |
| 28 | `MQTTClient_subscribe5` | `0x5900` | 190 | UnwindData |  |
| 29 | `MQTTClient_subscribeMany` | `0x59C0` | 116 | UnwindData |  |
| 30 | `MQTTClient_subscribeMany5` | `0x5A40` | 1,065 | UnwindData |  |
| 31 | `MQTTClient_unsubscribe` | `0x5E70` | 56 | UnwindData |  |
| 32 | `MQTTClient_unsubscribe5` | `0x5EB0` | 43 | UnwindData |  |
| 33 | `MQTTClient_unsubscribeMany` | `0x5EE0` | 99 | UnwindData |  |
| 34 | `MQTTClient_unsubscribeMany5` | `0x5F50` | 864 | UnwindData |  |
| 35 | `MQTTClient_waitForCompletion` | `0x62B0` | 262 | UnwindData |  |
| 36 | `MQTTClient_yield` | `0x6820` | 75 | UnwindData |  |
| 49 | `MQTTResponse_free` | `0x6D00` | 132 | UnwindData |  |
| 50 | `Thread_create_mutex` | `0x13EF0` | 113 | UnwindData |  |
| 51 | `Thread_getid` | `0x140B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `Thread_lock_mutex` | `0x140C0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `Thread_start` | `0x14190` | 108 | UnwindData |  |
| 54 | `Thread_unlock_mutex` | `0x14200` | 32 | UnwindData |  |
| 37 | `MQTTProperties_add` | `0x17790` | 208 | UnwindData |  |
| 38 | `MQTTProperties_copy` | `0x179D0` | 74 | UnwindData |  |
| 39 | `MQTTProperties_free` | `0x17C80` | 41 | UnwindData |  |
| 40 | `MQTTProperties_getNumericValue` | `0x17DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `MQTTProperties_getNumericValueAt` | `0x17DB0` | 22 | UnwindData |  |
| 42 | `MQTTProperties_getProperty` | `0x17EC0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `MQTTProperties_getPropertyAt` | `0x17F10` | 17 | UnwindData |  |
| 44 | `MQTTProperties_hasProperty` | `0x17F80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `MQTTProperties_propertyCount` | `0x17FE0` | 11 | UnwindData |  |
| 46 | `MQTTPropertyName` | `0x185F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `MQTTProperty_getType` | `0x18620` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `MQTTReasonCode_toString` | `0x18990` | 10,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `Heap_get_info` | `0x1B100` | 4,248 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
