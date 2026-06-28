# Binary Specification: MqttClientAdapter.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Data\InfBackup\MqttClientAdapter.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `03ff604c0e47b69829489601c1264eee2284543b99c451a89c33e1d0e92855fd`
* **Total Exported Functions:** 75

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0ActionListener@@QEAA@$$QEAV0@@Z` | `0x22F0` | 171 | UnwindData |  |
| 2 | `??0ActionListener@@QEAA@AEBV0@@Z` | `0x23A0` | 210 | UnwindData |  |
| 3 | `??0ActionListener@@QEAA@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V?$function@$$A6AXAEBVtoken@mqtt@@@Z@2@1AEAVLoggerCallback@utility@common@@@Z` | `0x2480` | 395 | UnwindData |  |
| 10 | `??1ActionListener@@UEAA@XZ` | `0x28A0` | 64 | UnwindData |  |
| 20 | `??_DActionListener@@QEAAXXZ` | `0x2A50` | 37 | UnwindData |  |
| 38 | `?getName@ActionListener@@QEBAAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@XZ` | `0x3170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `?on_failure@ActionListener@@UEAAXAEBVtoken@mqtt@@@Z` | `0x3190` | 257 | UnwindData |  |
| 59 | `?on_success@ActionListener@@UEAAXAEBVtoken@mqtt@@@Z` | `0x32A0` | 1,405 | UnwindData |  |
| 4 | `??0Callback@@QEAA@$$QEAV0@@Z` | `0x48F0` | 268 | UnwindData |  |
| 5 | `??0Callback@@QEAA@AEBV0@@Z` | `0x4A00` | 341 | UnwindData |  |
| 6 | `??0Callback@@QEAA@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEAV?$function@$$A6AXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@0@Z@2@V?$function@$$A6AXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z@2@V?$function@$$A6AXAEBVtoken@mqtt@@@Z@2@V?$function@$$A6AXXZ@2@3AEAVLoggerCallback@utility@common@@@Z` | `0x4B60` | 698 | UnwindData |  |
| 11 | `??1Callback@@UEAA@XZ` | `0x4E20` | 68 | UnwindData |  |
| 21 | `??_DCallback@@QEAAXXZ` | `0x4F30` | 64 | UnwindData |  |
| 31 | `?connected@Callback@@UEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x5090` | 238 | UnwindData |  |
| 32 | `?connection_lost@Callback@@UEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x5190` | 237 | UnwindData |  |
| 33 | `?delivery_complete@Callback@@UEAAXV?$shared_ptr@Vdelivery_token@mqtt@@@std@@@Z` | `0x5290` | 150 | UnwindData |  |
| 42 | `?message_arrived@Callback@@UEAAXV?$shared_ptr@$$CBVmessage@mqtt@@@std@@@Z` | `0x5420` | 691 | UnwindData |  |
| 58 | `?on_failure@Callback@@UEAAXAEBVtoken@mqtt@@@Z` | `0x56E0` | 249 | UnwindData |  |
| 60 | `?on_success@Callback@@UEAAXAEBVtoken@mqtt@@@Z` | `0x57F0` | 241 | UnwindData |  |
| 7 | `??0MqttClientAdapter@@QEAA@AEAUMqttConnectionDetails@@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V?$function@$$A6AXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@0@Z@3@V?$function@$$A6AXV?$vector@V?$shared_ptr@UMqttMessage@@@std@@V?$allocator@V?$shared_ptr@UMqttMessage@@@std@@@2@@std@@@Z@3@V?$function@$$A6AXW4MqttConnectStatus@@HV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z@3@V?$function@$$A6AXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@` | `0xF7E0` | 1,055 | UnwindData |  |
| 8 | `??0MqttClientAdapter@@QEAA@AEBV0@@Z` | `0xFC00` | 349 | UnwindData |  |
| 12 | `??1MqttClientAdapter@@QEAA@XZ` | `0xFD60` | 474 | UnwindData |  |
| 26 | `?__autoclassinit2@MqttClientAdapter@@QEAAX_K@Z` | `0x10160` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `?__autoclassinit2@PahoMqttProxy@@QEAAX_K@Z` | `0x10160` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `?disconnect@MqttClientAdapter@@QEAAXXZ` | `0x102E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `?init@MqttClientAdapter@@QEAAXPEAVIMqttManager@mqtt_interactions@@@Z` | `0x102F0` | 543 | UnwindData |  |
| 61 | `?postSubscription@MqttClientAdapter@@QEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x10510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `?postUnsubscription@MqttClientAdapter@@QEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x10520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `?publishToMqtt@MqttClientAdapter@@QEAAXV?$shared_ptr@UMqttMessage@@@std@@@Z` | `0x10530` | 481 | UnwindData |  |
| 69 | `?quit@MqttClientAdapter@@QEAAXXZ` | `0x10720` | 44 | UnwindData |  |
| 71 | `?reconnect@MqttClientAdapter@@QEAAXXZ` | `0x10750` | 30,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0PahoMqttProxy@@QEAA@AEAUMqttConnectionDetails@@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEAV?$function@$$A6AXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@0@Z@3@AEAV?$function@$$A6AXV?$vector@V?$shared_ptr@UMqttMessage@@@std@@V?$allocator@V?$shared_ptr@UMqttMessage@@@std@@@2@@std@@@Z@3@AEAV?$function@$$A6AXW4MqttConnectStatus@@HV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z@3@AEAV?$function@$$A6AXAEBV?$basic_string@DU?$char_traits@D@std@@V?$alloca` | `0x17F00` | 2,363 | UnwindData |  |
| 13 | `??1PahoMqttProxy@@UEAA@XZ` | `0x190E0` | 602 | UnwindData |  |
| 22 | `?GetAutoProxyUrl@PahoMqttProxy@@AEAAXAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V23@@Z` | `0x1A240` | 1,276 | UnwindData |  |
| 23 | `?GetProxyServer@PahoMqttProxy@@AEAA_NAEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x1A740` | 2,406 | UnwindData |  |
| 24 | `?ParseHttpsProxy@PahoMqttProxy@@AEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V23@@Z` | `0x1B0B0` | 1,190 | UnwindData |  |
| 25 | `?SetMqttManager@PahoMqttProxy@@UEAAXPEAVIMqttManager@mqtt_interactions@@@Z` | `0x1B560` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `?addToOfflineMessageBuffer@PahoMqttProxy@@QEAAXV?$shared_ptr@$$CBVmessage@mqtt@@@std@@@Z` | `0x1C0C0` | 418 | UnwindData |  |
| 29 | `?connect@PahoMqttProxy@@UEAAXXZ` | `0x1C480` | 89 | UnwindData |  |
| 30 | `?connectPahoClient@PahoMqttProxy@@AEAAXXZ` | `0x1C4E0` | 1,707 | UnwindData |  |
| 35 | `?disconnect@PahoMqttProxy@@UEAAXXZ` | `0x1CC30` | 89 | UnwindData |  |
| 36 | `?disconnectPahoClient@PahoMqttProxy@@AEAAXXZ` | `0x1CC90` | 1,369 | UnwindData |  |
| 37 | `?getConnectOptions@PahoMqttProxy@@AEAA?AVconnect_options@mqtt@@AEBUMqttConnectionDetails@@@Z` | `0x1D330` | 2,022 | UnwindData |  |
| 39 | `?getServerAddress@PahoMqttProxy@@CA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEBUMqttConnectionDetails@@@Z` | `0x1DB20` | 388 | UnwindData |  |
| 40 | `?getSslOptions@PahoMqttProxy@@AEAA?AVssl_options@mqtt@@AEBUMqttConnectionDetails@@@Z` | `0x1DCB0` | 714 | UnwindData |  |
| 43 | `?onActionFailure@PahoMqttProxy@@AEAAXAEBVtoken@mqtt@@@Z` | `0x1E240` | 315 | UnwindData |  |
| 44 | `?onActionSuccess@PahoMqttProxy@@AEAAXAEBVtoken@mqtt@@@Z` | `0x1E380` | 513 | UnwindData |  |
| 45 | `?onConnectFailure@PahoMqttProxy@@AEAAXAEBVtoken@mqtt@@@Z` | `0x1E590` | 797 | UnwindData |  |
| 46 | `?onConnectSuccess@PahoMqttProxy@@AEAAXAEBVtoken@mqtt@@@Z` | `0x1E8B0` | 791 | UnwindData |  |
| 47 | `?onConnected@PahoMqttProxy@@AEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x1EBD0` | 406 | UnwindData |  |
| 48 | `?onConnectionLost@PahoMqttProxy@@AEAAXXZ` | `0x1ED70` | 453 | UnwindData |  |
| 49 | `?onMessageDeliveryFailure@PahoMqttProxy@@AEAAXAEBVtoken@mqtt@@@Z` | `0x1EF40` | 805 | UnwindData |  |
| 50 | `?onMessageDeliverySuccess@PahoMqttProxy@@AEAAXAEBVtoken@mqtt@@@Z` | `0x1F270` | 33 | UnwindData |  |
| 51 | `?onMqttCommandExecutionFailure@PahoMqttProxy@@AEAAXW4CommandType@command@proxy@@HV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x1F2A0` | 287 | UnwindData |  |
| 52 | `?onMqttConnectAsync@PahoMqttProxy@@AEAAXUMqttConnectCallbackParams@proxy@@@Z` | `0x1F3C0` | 151 | UnwindData |  |
| 53 | `?onSubscriptionRequestFailure@PahoMqttProxy@@AEAAXAEBVtoken@mqtt@@@Z` | `0x1F460` | 415 | UnwindData |  |
| 54 | `?onSubscriptionRequestSuccess@PahoMqttProxy@@AEAAXAEBVtoken@mqtt@@@Z` | `0x1F600` | 443 | UnwindData |  |
| 55 | `?onUnsubscriptionRequestFailure@PahoMqttProxy@@AEAAXAEBVtoken@mqtt@@@Z` | `0x1F7C0` | 528 | UnwindData |  |
| 56 | `?onUnsubscriptionRequestSuccess@PahoMqttProxy@@AEAAXAEBVtoken@mqtt@@@Z` | `0x1F9D0` | 651 | UnwindData |  |
| 62 | `?postSubscription@PahoMqttProxy@@UEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x1FC60` | 448 | UnwindData |  |
| 63 | `?postUnsubscribe@PahoMqttProxy@@UEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x1FE20` | 316 | UnwindData |  |
| 65 | `?publishMessagesFromBuffer@PahoMqttProxy@@QEAAXAEAV?$vector@V?$shared_ptr@$$CBVmessage@mqtt@@@std@@V?$allocator@V?$shared_ptr@$$CBVmessage@mqtt@@@std@@@2@@std@@@Z` | `0x20480` | 240 | UnwindData |  |
| 66 | `?publishPendingMessages@PahoMqttProxy@@QEAAXXZ` | `0x20570` | 677 | UnwindData |  |
| 68 | `?publishToMqtt@PahoMqttProxy@@UEAAXAEBV?$shared_ptr@$$CBVmessage@mqtt@@@std@@@Z` | `0x20820` | 442 | UnwindData |  |
| 70 | `?quit@PahoMqttProxy@@UEAAXXZ` | `0x209E0` | 317 | UnwindData |  |
| 72 | `?reconnect@PahoMqttProxy@@UEAAXXZ` | `0x20B20` | 280 | UnwindData |  |
| 73 | `?resetOnConnectSuccess@PahoMqttProxy@@AEAAXXZ` | `0x20C40` | 263 | UnwindData |  |
| 74 | `?subscribeAllTopics@PahoMqttProxy@@AEAAXXZ` | `0x20D50` | 1,441 | UnwindData |  |
| 75 | `?subscribeToMqtt@PahoMqttProxy@@AEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x21300` | 256 | UnwindData |  |
| 14 | `??_7ActionListener@@6B@` | `0x368C8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??_8ActionListener@@7B@` | `0x368E0` | 232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??_7Callback@@6Bcallback@mqtt@@@` | `0x369C8` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??_7Callback@@6Biaction_listener@mqtt@@@` | `0x369F8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??_8Callback@@7B@` | `0x36A10` | 3,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??_7PahoMqttProxy@@6B@` | `0x37678` | 0 | Indeterminate |  |
