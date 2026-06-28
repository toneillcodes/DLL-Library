# Binary Specification: NotificationAgent.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Data\InfBackup\NotificationAgent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `025cd49af3046e94a7f18a7cdcc9a1bbbca87b764a52d6c64753b67af771cd8b`
* **Total Exported Functions:** 171

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `??0NotificationMessage@@QEAA@AEBV0@@Z` | `0x1250` | 69 | UnwindData |  |
| 26 | `??4NotificationMessage@@QEAAAEAV0@AEBV0@@Z` | `0x12A0` | 118 | UnwindData |  |
| 2 | `??0Notification@@QEAA@AEBV0@@Z` | `0x1320` | 101 | UnwindData |  |
| 25 | `??4Notification@@QEAAAEAV0@AEBV0@@Z` | `0x1390` | 67 | UnwindData |  |
| 4 | `??0Notification@@QEAA@XZ` | `0x13E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??1Notification@@QEAA@XZ` | `0x1430` | 107 | UnwindData |  |
| 3 | `??0Notification@@QEAA@VValue@Json@@@Z` | `0x14A0` | 625 | UnwindData |  |
| 129 | `?message_id@Notification@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x1720` | 29 | UnwindData |  |
| 130 | `?message_type@NotificationMessage@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x1720` | 29 | UnwindData |  |
| 128 | `?message@Notification@@QEAA?AVNotificationMessage@@XZ` | `0x1740` | 76 | UnwindData |  |
| 152 | `?setDeviceActionCallbac@NotificationAgent@@QEAAXV?$function@$$A6AXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z@std@@@Z` | `0x3C90` | 61 | UnwindData |  |
| 154 | `?setDeviceStatusTelemetryCallback@NotificationAgent@@QEAAXV?$function@$$A6AXXZ@std@@@Z` | `0x3CD0` | 61 | UnwindData |  |
| 151 | `?setCertPath@NotificationAgent@@QEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x3D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `?setDeviceStatusParam@NotificationAgent@@QEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0x3D30` | 447 | UnwindData |  |
| 98 | `?__autoclassinit2@AppAndTagCollection@@QEAAX_K@Z` | `0x3EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `?__autoclassinit2@ApplicabilityEvaluator@@QEAAX_K@Z` | `0x3EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `?__autoclassinit2@LogThrottler@@QEAAX_K@Z` | `0x3EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `?__autoclassinit2@NotificationAgent@@QEAAX_K@Z` | `0x3EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `?__autoclassinit2@UDCHelperFactory@udc@@QEAAX_K@Z` | `0x3EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `?__autoclassinit2@UdcMqttNotificationManager@@QEAAX_K@Z` | `0x3EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `?__autoclassinit2@UdcStatusManager@UDC@@QEAAX_K@Z` | `0x3EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `??_FNotificationAgent@@QEAAXXZ` | `0x3F00` | 90 | UnwindData |  |
| 116 | `?getMqttConnectionStatus@UdcMqttNotificationManager@@QEAA?AW4MqttConnectStatus@@XZ` | `0x4960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `?setMqttConnectionStatus@UdcMqttNotificationManager@@QEAAXW4MqttConnectStatus@@@Z` | `0x4970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0NotificationAgent@@QEAA@V?$function@$$A6AXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@0@Z@std@@0000@Z` | `0x4990` | 2,267 | UnwindData |  |
| 18 | `??1NotificationAgent@@UEAA@XZ` | `0x60C0` | 1,040 | UnwindData |  |
| 56 | `?FullInit@NotificationAgent@@UEAAXXZ` | `0x64D0` | 4,009 | UnwindData |  |
| 65 | `?Init@NotificationAgent@@UEAAXAEAPEAX@Z` | `0x7500` | 600 | UnwindData |  |
| 93 | `?UnInit@NotificationAgent@@UEAAXXZ` | `0x7760` | 977 | UnwindData |  |
| 50 | `?DeleteMqttPersistanceFolder@NotificationAgent@@AEAAXXZ` | `0x7BB0` | 366 | UnwindData |  |
| 66 | `?IsCleanSessionRequired@NotificationAgent@@AEAA_NXZ` | `0x7D20` | 241 | UnwindData |  |
| 80 | `?OnNotification@NotificationAgent@@AEAAXAEAVUDCNotificationData@@@Z` | `0x7E20` | 3,841 | UnwindData |  |
| 96 | `?UpdateDeviceActionState@NotificationAgent@@QEAAXW4DevcieActionStates@1@@Z` | `0x8D30` | 565 | UnwindData |  |
| 75 | `?NotifyLCP@NotificationAgent@@UEAAKAEAVUDCNotificationData@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x8F70` | 3,281 | UnwindData |  |
| 20 | `??1UDCTag@@QEAA@XZ` | `0x9C50` | 183 | UnwindData |  |
| 54 | `?DeviceStatusNotify@NotificationAgent@@AEAAXXZ` | `0x9D10` | 67 | UnwindData |  |
| 162 | `?timer_start@NotificationAgent@@AEAAXV?$function@$$A6AXXZ@std@@I@Z` | `0x9D60` | 489 | UnwindData |  |
| 47 | `?BreakMqttTimeIntervalWait@NotificationAgent@@QEAAXXZ` | `0x9F80` | 55 | UnwindData |  |
| 89 | `?Start_MqttConnectDisconnectThread@NotificationAgent@@AEAAXV?$function@$$A6AX_N@Z@std@@I@Z` | `0x9FC0` | 468 | UnwindData |  |
| 91 | `?StopMqttConnectDisconnectThread@NotificationAgent@@AEAAXXZ` | `0xA4A0` | 329 | UnwindData |  |
| 59 | `?GetInstance@NotificationAgent@@SAPEAV1@V?$function@$$A6AXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@0@Z@std@@0000@Z` | `0xA5F0` | 1,142 | UnwindData |  |
| 81 | `?PauseMqttConnection@NotificationAgent@@QEAAX_N@Z` | `0xAA70` | 105 | UnwindData |  |
| 138 | `?onNetworkChange@NotificationAgent@@QEAAX_N@Z` | `0xAAE0` | 32 | UnwindData |  |
| 132 | `?onMqttCertificateChange@NotificationAgent@@QEAAXXZ` | `0xAB00` | 190 | UnwindData |  |
| 109 | `?checkMqttNotificationManager@NotificationAgent@@AEBAXXZ` | `0xABC0` | 140 | UnwindData |  |
| 161 | `?subscribeTopics@NotificationAgent@@AEBAXXZ` | `0xAC50` | 3,108 | UnwindData |  |
| 92 | `?StopMqttManager@NotificationAgent@@AEAAXXZ` | `0xB880` | 66 | UnwindData |  |
| 76 | `?OnHTTPNotificiation@NotificationAgent@@QEAAKPEAVNotification@@@Z` | `0xB8D0` | 238 | UnwindData |  |
| 77 | `?OnMQTTNotificiation@NotificationAgent@@QEAAKV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0xB9C0` | 2,047 | UnwindData |  |
| 78 | `?OnMQTTProxyMsgCbk@NotificationAgent@@QEAAKV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xC1C0` | 608 | UnwindData |  |
| 49 | `?ConstructPayloadForUDCLogging@NotificationAgent@@AEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0xC420` | 2,638 | UnwindData |  |
| 48 | `?ConstructLCPParams@NotificationAgent@@SA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$map@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@U?$less@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@@std@@@2@@3@V23@@Z` | `0xCE70` | 2,625 | UnwindData |  |
| 87 | `?RetrieveAndUpdateDeviceActionState@NotificationAgent@@AEAAXAEAVUDCNotificationData@@@Z` | `0xD8C0` | 464 | UnwindData |  |
| 73 | `?LogException@NotificationAgent@@CAXAEBVexception@std@@AEAV?$function@$$A6AXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@0@Z@3@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@@Z` | `0xDAF0` | 541 | UnwindData |  |
| 110 | `?convertFreqToChrono@NotificationAgent@@AEAAIV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xDD10` | 1,330 | UnwindData |  |
| 88 | `?StartMqttManager@NotificationAgent@@QEAAXXZ` | `0xE250` | 2,350 | UnwindData |  |
| 72 | `?IsMqttStarted@NotificationAgent@@UEAA_NXZ` | `0xEB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `?IsMqttConnected@NotificationAgent@@UEAA_NXZ` | `0xEBA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `?StopAndDeleteMqttManager@NotificationAgent@@QEAAXXZ` | `0xEBD0` | 152 | UnwindData |  |
| 58 | `?GetDeviceStatusTelemetry@NotificationAgent@@AEAAXXZ` | `0xEC70` | 565 | UnwindData |  |
| 137 | `?onMqttSettingsChange@NotificationAgent@@AEAAXXZ` | `0xF070` | 1,188 | UnwindData |  |
| 57 | `?FullInitializeWorker@NotificationAgent@@AEAAXXZ` | `0xF520` | 384 | UnwindData |  |
| 74 | `?NotifyFullInitializeWorker@NotificationAgent@@AEAAXW4fullInitializeState@1@@Z` | `0xF6A0` | 94 | UnwindData |  |
| 60 | `?GetLCPNotificationTopicPrefix@NotificationAgent@@UEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0xF700` | 578 | UnwindData |  |
| 83 | `?RequestForMqttConnection@NotificationAgent@@UEAA?AW4MqttConnectionState@Notification@AgentInterface@UDC@@AEBUMqttConnectionRequestParams@345@@Z` | `0xF950` | 712 | UnwindData |  |
| 85 | `?RequestForMqttDisconnect@NotificationAgent@@UEAA?AW4MqttConnectionState@Notification@AgentInterface@UDC@@AEBUMqttConnectionRequestParams@345@@Z` | `0xFC20` | 267 | UnwindData |  |
| 62 | `?GetMqttConnectionState@NotificationAgent@@UEAA?AW4MqttConnectionState@Notification@AgentInterface@UDC@@XZ` | `0xFD30` | 75 | UnwindData |  |
| 53 | `?DeregisterConnectionStatusCallback@NotificationAgent@@UEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xFD80` | 77 | UnwindData |  |
| 69 | `?IsConnectionRequestQueued@NotificationAgent@@AEAA?AW4RequestType@Notification@AgentInterface@UDC@@AEBUMqttConnectionRequestParams@345@@Z` | `0xFDD0` | 258 | UnwindData |  |
| 55 | `?EnqueueConnectionRequest@NotificationAgent@@AEAA_NAEBUMqttConnectionRequestParams@Notification@AgentInterface@UDC@@@Z` | `0xFEE0` | 486 | UnwindData |  |
| 51 | `?DequeueConnectionRequest@NotificationAgent@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x100D0` | 276 | UnwindData |  |
| 70 | `?IsMqttAllowedByConfigPolicy@NotificationAgent@@AEAA_NXZ` | `0x101F0` | 935 | UnwindData |  |
| 61 | `?GetMqttConnectFrequencyType@NotificationAgent@@UEAA?AW4MqttConnectFrequencyType@Notification@AgentInterface@UDC@@XZ` | `0x105A0` | 503 | UnwindData |  |
| 122 | `?hasRetriesExceededStrict@NotificationAgent@@UEAA_NXZ` | `0x107A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `?ReInit@NotificationAgent@@IEAAXXZ` | `0x107C0` | 3,821 | UnwindData |  |
| 79 | `?OnMaintenanceTaskTrigger@NotificationAgent@@AEAAXXZ` | `0x116B0` | 466 | UnwindData |  |
| 64 | `?HandleMaintenanceTrigger@NotificationAgent@@IEAA_NXZ` | `0x11890` | 69 | UnwindData |  |
| 63 | `?GetMqttDiconnectTimerThreshold@NotificationAgent@@IEAAKXZ` | `0x11A50` | 45 | UnwindData |  |
| 68 | `?IsCommercialIntent@NotificationAgent@@IEBA_NXZ` | `0x11A80` | 38 | UnwindData |  |
| 97 | `?WaitForTrigger@NotificationAgent@@AEAAXAEAV?$future@X@std@@@Z` | `0x11AB0` | 79 | UnwindData |  |
| 171 | `?waitForFuture@UdcMqttNotificationManager@@AEAAXAEAV?$future@X@std@@@Z` | `0x11AB0` | 79 | UnwindData |  |
| 126 | `?isMqttDisabledInCustomSettings@NotificationAgent@@AEAA_NXZ` | `0x11B00` | 53 | UnwindData |  |
| 124 | `?isCustomSettingsEnabled@NotificationAgent@@MEAA_NXZ` | `0x11B40` | 19 | UnwindData |  |
| 118 | `?getMqttDisconnectTimerSettingFromRegistry@NotificationAgent@@MEAAKXZ` | `0x11B60` | 482 | UnwindData |  |
| 117 | `?getMqttDisabledSettingFromRegistry@NotificationAgent@@MEAA_NXZ` | `0x11D50` | 304 | UnwindData |  |
| 147 | `?requestAndWaitForConfigFetch@NotificationAgent@@MEAA_NK@Z` | `0x11E80` | 652 | UnwindData |  |
| 170 | `?verifyPreConditionsForMaintenanceTrigger@NotificationAgent@@MEAA_NXZ` | `0x12110` | 89 | UnwindData |  |
| 119 | `?getMqttLastDisconnectedTime@NotificationAgent@@MEAA_JXZ` | `0x12170` | 138 | UnwindData |  |
| 149 | `?restartMqttManager@NotificationAgent@@MEAAXXZ` | `0x12200` | 217 | UnwindData |  |
| 125 | `?isDeviceIdChanged@NotificationAgent@@AEAA_NXZ` | `0x122E0` | 433 | UnwindData |  |
| 23 | `??4GpuTagGenerator@@QEAAAEAV0@$$QEAV0@@Z` | `0x15DF0` | 18,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??4GpuTagGenerator@@QEAAAEAV0@AEBV0@@Z` | `0x15DF0` | 18,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??4Persona@udc@@QEAAAEAV01@$$QEAV01@@Z` | `0x15DF0` | 18,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??4Persona@udc@@QEAAAEAV01@AEBV01@@Z` | `0x15DF0` | 18,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??4PersonaUtility@udc@@QEAAAEAV01@$$QEAV01@@Z` | `0x15DF0` | 18,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `??4PersonaUtility@udc@@QEAAAEAV01@AEBV01@@Z` | `0x15DF0` | 18,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0NotificationMessage@@QEAA@XZ` | `0x1A640` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??1NotificationMessage@@QEAA@XZ` | `0x1A680` | 263 | UnwindData |  |
| 7 | `??0NotificationMessage@@QEAA@VValue@Json@@@Z` | `0x1A790` | 748 | UnwindData |  |
| 127 | `?json_message@NotificationMessage@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x1AA80` | 30 | UnwindData |  |
| 106 | `?action_type@NotificationMessage@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x1AAA0` | 30 | UnwindData |  |
| 14 | `??0UDCTag@@QEAA@AEBV0@@Z` | `0x1D4B0` | 55 | UnwindData |  |
| 13 | `??0UDCTag@@QEAA@$$QEAV0@@Z` | `0x1D4F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??4UDCTag@@QEAAAEAV0@AEBV0@@Z` | `0x1D550` | 86 | UnwindData |  |
| 32 | `??4UDCTag@@QEAAAEAV0@$$QEAV0@@Z` | `0x1D5B0` | 48 | UnwindData |  |
| 9 | `??0PersonaUtility@udc@@QEAA@$$QEAV01@@Z` | `0x1D5E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0PersonaUtility@udc@@QEAA@AEBV01@@Z` | `0x1D5E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0PersonaUtility@udc@@QEAA@XZ` | `0x1D5E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0LogThrottler@@QEAA@XZ` | `0x1D5F0` | 291 | UnwindData |  |
| 16 | `??1LogThrottler@@QEAA@XZ` | `0x1D720` | 107 | UnwindData |  |
| 36 | `??8Version@@QEAA_NAEBV0@@Z` | `0x1D790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??9Version@@QEAA_NAEBV0@@Z` | `0x1D7A0` | 20 | UnwindData |  |
| 38 | `??MVersion@@QEAA_NAEBV0@@Z` | `0x1D7C0` | 20 | UnwindData |  |
| 39 | `??NVersion@@QEAA_NAEBV0@@Z` | `0x1D7E0` | 20 | UnwindData |  |
| 40 | `??OVersion@@QEAA_NAEBV0@@Z` | `0x1D800` | 20 | UnwindData |  |
| 41 | `??PVersion@@QEAA_NAEBV0@@Z` | `0x1D820` | 20 | UnwindData |  |
| 35 | `??4Version@@QEAAAEAV0@AEBV0@@Z` | `0x1D840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??4Version@@QEAAAEAV0@$$QEAV0@@Z` | `0x1D850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??1UdcStatusManager@UDC@@QEAA@XZ` | `0x1D870` | 394 | UnwindData |  |
| 12 | `??0UDCHelperFactory@udc@@QEAA@AEBV01@@Z` | `0x1DA00` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `??4UDCHelperFactory@udc@@QEAAAEAV01@AEBV01@@Z` | `0x1DAA0` | 369 | UnwindData |  |
| 15 | `??0UdcMqttNotificationManager@@QEAA@VLoggerCallback@utility@common@@V?$function@$$A6AKV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z@std@@V?$function@$$A6AKV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z@5@V?$shared_ptr@UIDeviceRegistration@registration@udc@@@5@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@5@V?$duration@_JU?$ratio@$00$00@std@@@chrono@5@H@Z` | `0x1DC20` | 1,050 | UnwindData |  |
| 158 | `?start@UdcMqttNotificationManager@@QEAAXXZ` | `0x1E060` | 2,692 | UnwindData |  |
| 135 | `?onMqttNotification@UdcMqttNotificationManager@@AEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@0@Z` | `0x1EBC0` | 362 | UnwindData |  |
| 136 | `?onMqttProxyMsgCbk@UdcMqttNotificationManager@@AEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x1ED30` | 203 | UnwindData |  |
| 160 | `?subscribe@UdcMqttNotificationManager@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1EE00` | 104 | UnwindData |  |
| 165 | `?unsubscribe@UdcMqttNotificationManager@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1EE70` | 104 | UnwindData |  |
| 121 | `?getTopicPrefix@UdcMqttNotificationManager@@AEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x1EEE0` | 657 | UnwindData |  |
| 112 | `?getClientCertDetails@UdcMqttNotificationManager@@AEAA?AUMqttClientCert@@XZ` | `0x1F180` | 3,369 | UnwindData |  |
| 144 | `?publishMessage@UdcMqttNotificationManager@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0x203F0` | 1,235 | UnwindData |  |
| 145 | `?quit@UdcMqttNotificationManager@@QEAAXXZ` | `0x208D0` | 1,206 | UnwindData |  |
| 141 | `?pauseMqttConnection@UdcMqttNotificationManager@@QEAAX_N@Z` | `0x20D90` | 357 | UnwindData |  |
| 111 | `?getBrokerUrl@UdcMqttNotificationManager@@AEAA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@XZ` | `0x20F00` | 2,327 | UnwindData |  |
| 163 | `?unpublishedMessages@UdcMqttNotificationManager@@AEAAXV?$vector@V?$shared_ptr@UMqttMessage@@@std@@V?$allocator@V?$shared_ptr@UMqttMessage@@@std@@@2@@std@@@Z` | `0x21820` | 977 | UnwindData |  |
| 159 | `?subscribe@UdcMqttNotificationManager@@QEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x21C00` | 553 | UnwindData |  |
| 164 | `?unsubscribe@UdcMqttNotificationManager@@QEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x21E30` | 553 | UnwindData |  |
| 143 | `?publishMessage@UdcMqttNotificationManager@@QEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@0@Z` | `0x22060` | 282 | UnwindData |  |
| 108 | `?checkAvailability@UdcMqttNotificationManager@@AEAAXXZ` | `0x22180` | 89 | UnwindData |  |
| 21 | `??1UdcMqttNotificationManager@@UEAA@XZ` | `0x22240` | 684 | UnwindData |  |
| 166 | `?updateConnectionDetails@UdcMqttNotificationManager@@AEAAXXZ` | `0x224F0` | 788 | UnwindData |  |
| 115 | `?getMqttClientId@UdcMqttNotificationManager@@AEAA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@XZ` | `0x22850` | 1,519 | UnwindData |  |
| 140 | `?onReconnectHandler@UdcMqttNotificationManager@@AEAAXXZ` | `0x22EA0` | 22 | UnwindData |  |
| 167 | `?updateHeartBeat@UdcMqttNotificationManager@@QEAAXV?$duration@_JU?$ratio@$00$00@std@@@chrono@std@@@Z` | `0x22EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `?canAcceptMessages@UdcMqttNotificationManager@@QEBA_NXZ` | `0x22EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `?reconnect@UdcMqttNotificationManager@@AEAAXXZ` | `0x22EF0` | 40 | UnwindData |  |
| 67 | `?IsCleanSessionRequired@UdcMqttNotificationManager@@UEAA_NXZ` | `0x22F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `?UpdateCleanSession@UdcMqttNotificationManager@@UEAAX_N@Z` | `0x22F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `?getConnectionOptions@UdcMqttNotificationManager@@AEAA?AUMqttConnectionOptions@@XZ` | `0x22F40` | 223 | UnwindData |  |
| 113 | `?getConnectionDetails@UdcMqttNotificationManager@@AEAA?AUMqttConnectionDetails@@XZ` | `0x23020` | 630 | UnwindData |  |
| 134 | `?onMqttConnectionCallback@UdcMqttNotificationManager@@AEAAXW4MqttConnectStatus@@HV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x232A0` | 2,980 | UnwindData |  |
| 133 | `?onMqttCertificateChange@UdcMqttNotificationManager@@QEAAXXZ` | `0x23E50` | 256 | UnwindData |  |
| 139 | `?onNetworkChange@UdcMqttNotificationManager@@QEAAX_N@Z` | `0x23F50` | 1,056 | UnwindData |  |
| 95 | `?UpdateConnectionRequestMapWith@UdcMqttNotificationManager@@QEAA_NAEBUMqttConnectionRequestParams@Notification@AgentInterface@UDC@@@Z` | `0x24370` | 1,215 | UnwindData |  |
| 52 | `?DequeueConnectionRequest@UdcMqttNotificationManager@@QEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x24840` | 437 | UnwindData |  |
| 84 | `?RequestForMqttConnection@UdcMqttNotificationManager@@QEAA?AW4MqttConnectionState@Notification@AgentInterface@UDC@@AEBUMqttConnectionRequestParams@345@@Z` | `0x24A00` | 1,711 | UnwindData |  |
| 86 | `?RequestForMqttDisconnect@UdcMqttNotificationManager@@QEAA?AW4MqttConnectionState@Notification@AgentInterface@UDC@@AEBUMqttConnectionRequestParams@345@@Z` | `0x25120` | 609 | UnwindData |  |
| 123 | `?hasRetriesExceededStrict@UdcMqttNotificationManager@@QEAA_NXZ` | `0x25390` | 27 | UnwindData |  |
| 142 | `?preConnect@UdcMqttNotificationManager@@AEAAXXZ` | `0x253B0` | 1,768 | UnwindData |  |
| 168 | `?validateAndDeleteInvalidCommandFiles@UdcMqttNotificationManager@@AEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x25AA0` | 1,483 | UnwindData |  |
| 169 | `?validateAndDeleteInvalidPublishFiles@UdcMqttNotificationManager@@AEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x26070` | 1,779 | UnwindData |  |
| 157 | `?shouldKeepFile@UdcMqttNotificationManager@@AEAA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x26770` | 1,588 | UnwindData |  |
| 131 | `?onExternalConnectionRequest@UdcMqttNotificationManager@@QEAAXAEBUMqttConnectionRequestParams@Notification@AgentInterface@UDC@@@Z` | `0x26E80` | 207 | UnwindData |  |
| 120 | `?getMqttLastDisconnectedTime@UdcMqttNotificationManager@@QEAA_JXZ` | `0x26F50` | 75 | UnwindData |  |
| 156 | `?setMqttLastDisconnectedTime@UdcMqttNotificationManager@@IEAAXXZ` | `0x26FA0` | 153 | UnwindData |  |
| 148 | `?resetMqttLastDisconnectedTime@UdcMqttNotificationManager@@IEAAXXZ` | `0x27040` | 77 | UnwindData |  |
| 43 | `??_7NotificationAgent@@6BIUDCAgent@@@` | `0x4D188` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??_7NotificationAgent@@6BINotificationAgent@Notification@AgentInterface@UDC@@@` | `0x4D1A8` | 1,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??_7UdcMqttNotificationManager@@6B@` | `0x4D920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `??_7PersonaUtility@udc@@6B@` | `0x4D940` | 96,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `?_formatTime@NotificationAgent@@0PEBGEB` | `0x65058` | 18,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `?s_pInstance@NotificationAgent@@0PEAV1@EA` | `0x699B0` | 0 | Indeterminate |  |
