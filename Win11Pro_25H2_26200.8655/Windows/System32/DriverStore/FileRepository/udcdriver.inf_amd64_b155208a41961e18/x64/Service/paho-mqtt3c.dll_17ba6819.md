# Binary Specification: paho-mqtt3c.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\udcdriver.inf_amd64_b155208a41961e18\x64\Service\paho-mqtt3c.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `17ba681930c827dc98e621388248ceab7ec7fcf48d6f7d8102e5f897477f4a3d`
* **Total Exported Functions:** 54

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `MQTTClient_connect` | `0x14E0` | 77 | UnwindData |  |
| 3 | `MQTTClient_connect5` | `0x1530` | 126 | UnwindData |  |
| 4 | `MQTTClient_create` | `0x24E0` | 33 | UnwindData |  |
| 5 | `MQTTClient_createWithOptions` | `0x2510` | 73 | UnwindData |  |
| 6 | `MQTTClient_destroy` | `0x2DC0` | 85 | UnwindData |  |
| 7 | `MQTTClient_disconnect` | `0x2FD0` | 82 | UnwindData |  |
| 8 | `MQTTClient_disconnect5` | `0x3270` | 108 | UnwindData |  |
| 9 | `MQTTClient_free` | `0x3400` | 83 | UnwindData |  |
| 10 | `MQTTClient_freeMessage` | `0x3460` | 126 | UnwindData |  |
| 11 | `MQTTClient_getPendingDeliveryTokens` | `0x34E0` | 181 | UnwindData |  |
| 12 | `MQTTClient_getVersionInfo` | `0x3620` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `MQTTClient_global_init` | `0x3690` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MQTTClient_isConnected` | `0x3870` | 129 | UnwindData |  |
| 15 | `MQTTClient_publish` | `0x3900` | 138 | UnwindData |  |
| 16 | `MQTTClient_publish5` | `0x3990` | 988 | UnwindData |  |
| 17 | `MQTTClient_publishMessage` | `0x3D70` | 158 | UnwindData |  |
| 18 | `MQTTClient_publishMessage5` | `0x3E10` | 273 | UnwindData |  |
| 19 | `MQTTClient_receive` | `0x3F30` | 137 | UnwindData |  |
| 20 | `MQTTClient_setCallbacks` | `0x4A30` | 194 | UnwindData |  |
| 21 | `MQTTClient_setCommandTimeout` | `0x4B00` | 113 | UnwindData |  |
| 22 | `MQTTClient_setDisconnected` | `0x4B80` | 163 | UnwindData |  |
| 23 | `MQTTClient_setPublished` | `0x4C30` | 163 | UnwindData |  |
| 24 | `MQTTClient_setTraceCallback` | `0x4CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `MQTTClient_setTraceLevel` | `0x4CF0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `MQTTClient_strerror` | `0x4E60` | 368 | UnwindData |  |
| 27 | `MQTTClient_subscribe` | `0x4FD0` | 241 | UnwindData |  |
| 28 | `MQTTClient_subscribe5` | `0x50D0` | 190 | UnwindData |  |
| 29 | `MQTTClient_subscribeMany` | `0x5190` | 116 | UnwindData |  |
| 30 | `MQTTClient_subscribeMany5` | `0x5210` | 1,065 | UnwindData |  |
| 31 | `MQTTClient_unsubscribe` | `0x5640` | 56 | UnwindData |  |
| 32 | `MQTTClient_unsubscribe5` | `0x5680` | 43 | UnwindData |  |
| 33 | `MQTTClient_unsubscribeMany` | `0x56B0` | 99 | UnwindData |  |
| 34 | `MQTTClient_unsubscribeMany5` | `0x5720` | 864 | UnwindData |  |
| 35 | `MQTTClient_waitForCompletion` | `0x5A80` | 262 | UnwindData |  |
| 36 | `MQTTClient_yield` | `0x5F60` | 72 | UnwindData |  |
| 49 | `MQTTResponse_free` | `0x6430` | 132 | UnwindData |  |
| 50 | `Thread_create_mutex` | `0x117C0` | 113 | UnwindData |  |
| 51 | `Thread_getid` | `0x11980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `Thread_lock_mutex` | `0x11990` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `Thread_start` | `0x11A60` | 108 | UnwindData |  |
| 54 | `Thread_unlock_mutex` | `0x11AD0` | 32 | UnwindData |  |
| 37 | `MQTTProperties_add` | `0x14ED0` | 208 | UnwindData |  |
| 38 | `MQTTProperties_copy` | `0x15110` | 74 | UnwindData |  |
| 39 | `MQTTProperties_free` | `0x153C0` | 41 | UnwindData |  |
| 40 | `MQTTProperties_getNumericValue` | `0x154E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `MQTTProperties_getNumericValueAt` | `0x154F0` | 22 | UnwindData |  |
| 42 | `MQTTProperties_getProperty` | `0x15600` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `MQTTProperties_getPropertyAt` | `0x15650` | 17 | UnwindData |  |
| 44 | `MQTTProperties_hasProperty` | `0x156C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `MQTTProperties_propertyCount` | `0x15720` | 11 | UnwindData |  |
| 46 | `MQTTPropertyName` | `0x15D30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `MQTTProperty_getType` | `0x15D60` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `MQTTReasonCode_toString` | `0x160D0` | 10,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `Heap_get_info` | `0x18B90` | 3,944 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
