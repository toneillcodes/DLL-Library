# Binary Specification: ClientBrokerAgent.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Service\ClientBrokerAgent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d99f882bf54b02b3b2cc3387735216d2d516b1139dab0bf2e5c8639a1d96e423`
* **Total Exported Functions:** 64

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0ClientBrokerAgent@@QEAA@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$function@$$A6A_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z@2@_N@Z` | `0x1D30` | 797 | UnwindData |  |
| 2 | `??0ClientBrokerManager@@QEAA@XZ` | `0x2050` | 372 | UnwindData |  |
| 3 | `??0ClientBrokerMessage@@QEAA@AEBV0@@Z` | `0x21D0` | 109 | UnwindData |  |
| 4 | `??0ClientBrokerMessage@@QEAA@XZ` | `0x2240` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0TopicPubSubMessage@@QEAA@AEAVUDCNotificationData@@@Z` | `0x22C0` | 418 | UnwindData |  |
| 6 | `??0TopicPubSubMessage@@QEAA@AEBV0@@Z` | `0x2470` | 83 | UnwindData |  |
| 7 | `??0TopicPubSubMessage@@QEAA@XZ` | `0x24D0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0UDCHelperFactory@udc@@QEAA@AEBV01@@Z` | `0x2530` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??1ClientBrokerAgent@@UEAA@XZ` | `0x2D00` | 323 | UnwindData |  |
| 10 | `??1ClientBrokerManager@@UEAA@XZ` | `0x2E50` | 89 | UnwindData |  |
| 11 | `??1ClientBrokerMessage@@QEAA@XZ` | `0x2EB0` | 61 | UnwindData |  |
| 12 | `??1TopicPubSubMessage@@QEAA@XZ` | `0x2F80` | 49 | UnwindData |  |
| 13 | `??1UdcStatusManager@UDC@@QEAA@XZ` | `0x2FC0` | 392 | UnwindData |  |
| 14 | `??4ClientBrokerMessage@@QEAAAEAV0@AEBV0@@Z` | `0x3260` | 194 | UnwindData |  |
| 15 | `??4TopicPubSubMessage@@QEAAAEAV0@AEBV0@@Z` | `0x3430` | 150 | UnwindData |  |
| 16 | `??4UDCHelperFactory@udc@@QEAAAEAV01@AEBV01@@Z` | `0x34D0` | 369 | UnwindData |  |
| 19 | `?AddToPendingNotificationQueue@ClientBrokerManager@@AEAAXHAEAVUDCNotificationData@@@Z` | `0x3860` | 297 | UnwindData |  |
| 20 | `?CheckInternetError@ClientBrokerAgent@@AEAA_NAEAK@Z` | `0x3990` | 116 | UnwindData |  |
| 21 | `?ClientBrokerAgentDisconnectionHandler@ClientBrokerManager@@SAXPEAV1@PEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x3A10` | 42 | UnwindData |  |
| 22 | `?ClientListener@ClientBrokerManager@@AEAAXAEAV?$basic_stringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x3BC0` | 1,862 | UnwindData |  |
| 23 | `?ClientMsgCallback@ClientBrokerAgent@@AEAAXAEAV?$basic_stringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x4310` | 317 | UnwindData |  |
| 24 | `?ConstructClientResponseMessage@ClientBrokerAgent@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAVUDCNotificationData@@@Z` | `0x4450` | 140 | UnwindData |  |
| 25 | `?ConstructTopicPublishResponseMessage@ClientBrokerAgent@@AEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAVTopicPubSubMessage@@_N@Z` | `0x44E0` | 35 | UnwindData |  |
| 26 | `?FullInit@ClientBrokerManager@@UEAAXXZ` | `0x4510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `?GetInstallEntitledAppsStatus@ClientBrokerAgent@@AEAA_NAEAVClientBrokerMessage@@@Z` | `0x4520` | 1,030 | UnwindData |  |
| 28 | `?GetInstance@ClientBrokerManager@@SAPEAV1@XZ` | `0x4930` | 158 | UnwindData |  |
| 29 | `?HandleGetAppsRedemptionCodes@ClientBrokerAgent@@AEAA_NAEAVClientBrokerMessage@@@Z` | `0x49D0` | 1,042 | UnwindData |  |
| 30 | `?HandleGetEntitledApps@ClientBrokerAgent@@AEAA_NAEAVClientBrokerMessage@@@Z` | `0x4DF0` | 957 | UnwindData |  |
| 31 | `?HandleInstallEntitledApps@ClientBrokerAgent@@AEAA_NAEAVClientBrokerMessage@@@Z` | `0x51B0` | 1,052 | UnwindData |  |
| 32 | `?HandleIsEntitled@ClientBrokerAgent@@AEAA_NAEAVClientBrokerMessage@@@Z` | `0x55D0` | 808 | UnwindData |  |
| 33 | `?HandleSendHttpRequest@ClientBrokerAgent@@AEAA_NAEAVClientBrokerMessage@@@Z` | `0x5900` | 4,645 | UnwindData |  |
| 34 | `?HandleTopicPublishCommand@ClientBrokerAgent@@AEAAXAEAVClientBrokerMessage@@@Z` | `0x6B30` | 1,154 | UnwindData |  |
| 35 | `?HandleTopicSubscribeCommand@ClientBrokerAgent@@AEAAXAEAVClientBrokerMessage@@@Z` | `0x6FC0` | 1,039 | UnwindData |  |
| 36 | `?Init@ClientBrokerManager@@UEAAXAEAPEAX@Z` | `0x73D0` | 1,613 | UnwindData |  |
| 37 | `?IsMqttPubMessage@ClientBrokerAgent@@AEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x7A20` | 221 | UnwindData |  |
| 38 | `?IsTopicSubscribedByClient@ClientBrokerAgent@@QEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x7B00` | 371 | UnwindData |  |
| 39 | `?IsValidTopic@ClientBrokerAgent@@SA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x7C80` | 218 | UnwindData |  |
| 40 | `?JsonReadToObject@ClientBrokerMessage@@SA?AV1@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x7D60` | 2,046 | UnwindData |  |
| 41 | `?JsonReadToObject@TopicPubSubMessage@@SA?AV1@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@_N@Z` | `0x8560` | 1,735 | UnwindData |  |
| 42 | `?JsonWriteFromObject@ClientBrokerMessage@@SA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV1@@Z` | `0x8C30` | 1,283 | UnwindData |  |
| 43 | `?JsonWriteFromObject@TopicPubSubMessage@@SA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV1@_N1@Z` | `0x9140` | 1,123 | UnwindData |  |
| 44 | `?OnBrokenPipe@ClientBrokerAgent@@AEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x95B0` | 84 | UnwindData |  |
| 45 | `?OnClientBrokerAgentDisconnection@ClientBrokerManager@@AEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x9610` | 312 | UnwindData |  |
| 46 | `?OnStart@ClientBrokerAgent@@AEAAXXZ` | `0x9750` | 399 | UnwindData |  |
| 47 | `?OnUDCNotification@ClientBrokerManager@@AEAAXAEAVUDCNotificationData@@@Z` | `0x98E0` | 1,437 | UnwindData |  |
| 48 | `?ProcessClientMessage@ClientBrokerAgent@@AEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x9E80` | 3,858 | UnwindData |  |
| 49 | `?ProcessInternalNotifications@ClientBrokerManager@@AEAAXAEAVUDCNotificationData@@@Z` | `0xADA0` | 792 | UnwindData |  |
| 50 | `?ProcessMsgWorker@ClientBrokerAgent@@AEAAXXZ` | `0xB0C0` | 764 | UnwindData |  |
| 51 | `?ProcessPendingNotificationQueue@ClientBrokerManager@@AEAAXXZ` | `0xB3C0` | 312 | UnwindData |  |
| 52 | `?SendMessageToClient@ClientBrokerManager@@AEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAVClientBrokerMessage@@@Z` | `0xB500` | 504 | UnwindData |  |
| 53 | `?SendMessageW@ClientBrokerAgent@@QEAA_NAEAVClientBrokerMessage@@@Z` | `0xB700` | 144 | UnwindData |  |
| 54 | `?SetCachedAccessLevel@ClientBrokerAgent@@AEAAXAEAVValue@Json@@@Z` | `0xB790` | 2,464 | UnwindData |  |
| 55 | `?Start@ClientBrokerAgent@@QEAAXXZ` | `0xC130` | 730 | UnwindData |  |
| 56 | `?Stop@ClientBrokerAgent@@QEAAXXZ` | `0xC410` | 166 | UnwindData |  |
| 57 | `?UnInit@ClientBrokerManager@@UEAAXXZ` | `0xC5F0` | 33 | UnwindData |  |
| 58 | `?ValidateDeviceIdForAPS@ClientBrokerAgent@@AEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xC800` | 24 | UnwindData |  |
| 59 | `?__autoclassinit2@ClientBrokerAgent@@QEAAX_K@Z` | `0xD590` | 16,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `?__autoclassinit2@ClientBrokerManager@@QEAAX_K@Z` | `0xD590` | 16,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?__autoclassinit2@UDCHelperFactory@udc@@QEAAX_K@Z` | `0xD590` | 16,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `?__autoclassinit2@UdcStatusManager@UDC@@QEAAX_K@Z` | `0xD590` | 16,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??_7ClientBrokerAgent@@6B@` | `0x116C8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??_7ClientBrokerManager@@6B@` | `0x116D8` | 35,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `?m_ludpDeviceId@ClientBrokerAgent@@0V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@A` | `0x1A000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `?m_jsonEntitledSoftwaresCached@ClientBrokerAgent@@0V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@A` | `0x1A020` | 0 | Indeterminate |  |
