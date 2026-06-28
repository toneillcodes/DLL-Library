# Binary Specification: DataSync.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\udcdriver.inf_amd64_b155208a41961e18\x64\Service\DataSync.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fc3a8c8eeab951dc281e8d35b63ef73e7f7250ad091afcc88bc701589f1655d5`
* **Total Exported Functions:** 225

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0ConfigPolicyHelper@DataSync@UDC@@QEAA@$$QEAV012@@Z` | `0x3880` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0ConfigPolicyHelper@DataSync@UDC@@QEAA@AEBV012@@Z` | `0x3880` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0ConfigPolicyHelper@DataSync@UDC@@QEAA@XZ` | `0x3880` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??4ConfigPolicyHelper@DataSync@UDC@@QEAAAEAV012@$$QEAV012@@Z` | `0x3F00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??4ConfigPolicyHelper@DataSync@UDC@@QEAAAEAV012@AEBV012@@Z` | `0x3F00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??4CustomDataFilter@DataSync@UDC@@QEAAAEAV012@$$QEAV012@@Z` | `0x3F00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??4CustomDataFilter@DataSync@UDC@@QEAAAEAV012@AEBV012@@Z` | `0x3F00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??4DeviceManagementStatus@@QEAAAEAV0@$$QEAV0@@Z` | `0x3F00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??4DeviceManagementStatus@@QEAAAEAV0@AEBV0@@Z` | `0x3F00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??4JsonFormater@DataSync@UDC@@QEAAAEAV012@$$QEAV012@@Z` | `0x3F00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `??4JsonFormater@DataSync@UDC@@QEAAAEAV012@AEBV012@@Z` | `0x3F00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `??4Persona@udc@@QEAAAEAV01@$$QEAV01@@Z` | `0x3F00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `??4Persona@udc@@QEAAAEAV01@AEBV01@@Z` | `0x3F00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??4PersonaUtility@udc@@QEAAAEAV01@$$QEAV01@@Z` | `0x3F00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `??4PersonaUtility@udc@@QEAAAEAV01@AEBV01@@Z` | `0x3F00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `??4RetentionUtils@TelemetryUtils@@QEAAAEAV01@$$QEAV01@@Z` | `0x3F00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `??4RetentionUtils@TelemetryUtils@@QEAAAEAV01@AEBV01@@Z` | `0x3F00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `?GetIncludeEventsForDataset@ConfigPolicyHelper@DataSync@UDC@@QEAAXAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV?$list@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@5@@Z` | `0x4030` | 746 | UnwindData |  |
| 114 | `?GetTelemetryPolicy@ConfigPolicyHelper@DataSync@UDC@@UEAA?AV?$unique_ptr@VTelemetryPolicy@@U?$default_delete@VTelemetryPolicy@@@std@@@std@@XZ` | `0x4320` | 185 | UnwindData |  |
| 95 | `?FilterEvents@CustomDataFilter@DataSync@UDC@@SAXAEAV?$list@VDatasetContext@@V?$allocator@VDatasetContext@@@std@@@std@@AEAV?$list@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@5@@Z` | `0x4600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `?FilterEvents@CustomDataFilter@DataSync@UDC@@SAXAEAV?$list@VDeviceContext@@V?$allocator@VDeviceContext@@@std@@@std@@AEAV?$list@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@5@@Z` | `0x4600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `?FilterEvents@CustomDataFilter@DataSync@UDC@@SAXAEAV?$list@VItemContext@@V?$allocator@VItemContext@@@std@@@std@@AEAV?$list@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@5@@Z` | `0x4600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `?FilterEvents@CustomDataFilter@DataSync@UDC@@SAXAEAV?$list@VItemEvent@@V?$allocator@VItemEvent@@@std@@@std@@AEAV?$list@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@5@@Z` | `0x4610` | 663 | UnwindData |  |
| 16 | `??0SyncAgentsHelper@DataSync@UDC@@QEAA@$$QEAV012@@Z` | `0x48B0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??0SyncAgentsHelper@DataSync@UDC@@QEAA@AEBV012@@Z` | `0x49A0` | 108 | UnwindData |  |
| 18 | `??0SyncAgentsHelper@DataSync@UDC@@QEAA@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0AEBW4SyncTypes@12@0AEBW4EGetDBPathMethod@utility@2@@Z` | `0x4A10` | 161 | UnwindData |  |
| 19 | `??0SyncAgentsHelper@DataSync@UDC@@QEAA@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0AEBW4SyncTypes@12@0V34@W4HttpAuthType@UDCCore@@_NAEBW4EGetDBPathMethod@utility@2@@Z` | `0x4AC0` | 187 | UnwindData |  |
| 28 | `??1SyncAgentsHelper@DataSync@UDC@@QEAA@XZ` | `0x4B80` | 49 | UnwindData |  |
| 49 | `??4SyncAgentsHelper@DataSync@UDC@@QEAAAEAV012@$$QEAV012@@Z` | `0x4BC0` | 285 | UnwindData |  |
| 50 | `??4SyncAgentsHelper@DataSync@UDC@@QEAAAEAV012@AEBV012@@Z` | `0x4CE0` | 175 | UnwindData |  |
| 54 | `??4Version@@QEAAAEAV0@AEBV0@@Z` | `0x8F90` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0DataSyncAgent@@IEAA@XZ` | `0x9050` | 5,295 | UnwindData |  |
| 5 | `??0DeviceInfoProvider@UDC@@QEAA@XZ` | `0xA500` | 502 | UnwindData |  |
| 6 | `??0LogThrottler@@QEAA@XZ` | `0xA920` | 290 | UnwindData |  |
| 7 | `??0LudpHeader@UDC@@QEAA@AEBV01@@Z` | `0xAA50` | 63 | UnwindData |  |
| 9 | `??0LudpSyncAgent@DataSync@UDC@@QEAA@$$QEAV012@@Z` | `0xAA90` | 237 | UnwindData |  |
| 11 | `??0LudpSyncAgent@DataSync@UDC@@QEAA@AEBV012@@Z` | `0xAB80` | 131 | UnwindData |  |
| 13 | `??0PersonaUtility@udc@@QEAA@$$QEAV01@@Z` | `0xAE50` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??0PersonaUtility@udc@@QEAA@AEBV01@@Z` | `0xAE50` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??0PersonaUtility@udc@@QEAA@XZ` | `0xAE50` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??0SyncEP@@QEAA@AEBV0@@Z` | `0xAF00` | 139 | UnwindData |  |
| 21 | `??0SyncEP@@QEAA@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xAF90` | 241 | UnwindData |  |
| 23 | `??0UDCHelperFactory@udc@@QEAA@AEBV01@@Z` | `0xB090` | 5,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??1DataSyncAgent@@UEAA@XZ` | `0xC7E0` | 852 | UnwindData |  |
| 25 | `??1LogThrottler@@QEAA@XZ` | `0xCC80` | 31 | UnwindData |  |
| 27 | `??1LudpSyncAgent@DataSync@UDC@@QEAA@XZ` | `0xCCA0` | 46 | UnwindData |  |
| 29 | `??1SyncEP@@UEAA@XZ` | `0xCDA0` | 64 | UnwindData |  |
| 31 | `??1UdcStatusManager@UDC@@QEAA@XZ` | `0xCE80` | 392 | UnwindData |  |
| 40 | `??4LudpHeader@UDC@@QEAAAEAV01@AEBV01@@Z` | `0xD530` | 63 | UnwindData |  |
| 41 | `??4LudpSyncAgent@DataSync@UDC@@QEAAAEAV012@$$QEAV012@@Z` | `0xD570` | 238 | UnwindData |  |
| 42 | `??4LudpSyncAgent@DataSync@UDC@@QEAAAEAV012@AEBV012@@Z` | `0xD660` | 163 | UnwindData |  |
| 51 | `??4SyncEP@@QEAAAEAV0@AEBV0@@Z` | `0xD7B0` | 110 | UnwindData |  |
| 52 | `??4UDCHelperFactory@udc@@QEAAAEAV01@AEBV01@@Z` | `0xD820` | 369 | UnwindData |  |
| 53 | `??4Version@@QEAAAEAV0@$$QEAV0@@Z` | `0xD9A0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `??8Version@@QEAA_NAEBV0@@Z` | `0xDA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??9Version@@QEAA_NAEBV0@@Z` | `0xDA60` | 19 | UnwindData |  |
| 57 | `??MVersion@@QEAA_NAEBV0@@Z` | `0xDDB0` | 19 | UnwindData |  |
| 58 | `??NVersion@@QEAA_NAEBV0@@Z` | `0xDDD0` | 19 | UnwindData |  |
| 59 | `??OVersion@@QEAA_NAEBV0@@Z` | `0xDDF0` | 19 | UnwindData |  |
| 60 | `??PVersion@@QEAA_NAEBV0@@Z` | `0xDE10` | 19 | UnwindData |  |
| 67 | `??_FLudpHeader@UDC@@QEAAXXZ` | `0xE240` | 31 | UnwindData |  |
| 68 | `?AddDeviceContextRecordToSync@DataSyncAgent@@UEAAX_J@Z` | `0xEA70` | 284 | UnwindData |  |
| 69 | `?AddFileNamesToRecollectedTelemetry@DataSyncAgent@@IEAAXXZ` | `0xEB90` | 2,171 | UnwindData |  |
| 70 | `?AllowSyncOfOnDemandTelemetry@DataSyncAgent@@AEAAXXZ` | `0xF410` | 3,132 | UnwindData |  |
| 72 | `?CheckAndHandle403DeviceMissingError@DataSyncAgent@@IEAA_NAEAUInvokeHttpResponse@UDCCore@@@Z` | `0x10050` | 466 | UnwindData |  |
| 73 | `?CheckAndHandleCertificateExpiryError@DataSyncAgent@@IEAA_NAEBUInvokeHttpResponse@UDCCore@@@Z` | `0x10230` | 793 | UnwindData |  |
| 74 | `?CheckApplicabilityFilterForDataset@DataSyncAgent@@AEAA_NAEBVDataSet@@@Z` | `0x10550` | 527 | UnwindData |  |
| 75 | `?CheckDBType@DataSyncAgent@@AEAAHV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x10760` | 546 | UnwindData |  |
| 76 | `?CheckForExponentialBackoffRetry@DataSyncAgent@@AEAA_NHAEBW4SyncEp_type@SyncEP@@@Z` | `0x10990` | 1,421 | UnwindData |  |
| 77 | `?CheckTelemetrySyncNeedsRegistration@DataSyncAgent@@AEAA_NXZ` | `0x10F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `?CheckTimeLimitAndResetThe403DeviceError@DataSyncAgent@@IEAAXXZ` | `0x10F40` | 29 | UnwindData |  |
| 80 | `?CreateGlobalEvents@DataSyncAgent@@QEAAXXZ` | `0x10FD0` | 533 | UnwindData |  |
| 81 | `?DBChangesNotify@DataSyncAgent@@AEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@W4EGetDBPathMethod@utility@UDC@@@Z` | `0x111F0` | 570 | UnwindData |  |
| 83 | `?DeviceContextSyncThread@DataSyncAgent@@QEAAXXZ` | `0x11430` | 698 | UnwindData |  |
| 84 | `?DeviceReadySync@DataSyncAgent@@AEAAX_N@Z` | `0x116F0` | 2,822 | UnwindData |  |
| 85 | `?DoLcpPost@DataSyncAgent@@AEAA_NAEBVDataSet@@W4SyncTypes@DataSync@UDC@@W4EGetDBPathMethod@utility@5@@Z` | `0x12200` | 1,550 | UnwindData |  |
| 86 | `?DoLudpPost@DataSyncAgent@@AEAA_NAEBVDataSet@@W4_LudpSyncType@DataSync@UDC@@W4EGetDBPathMethod@utility@5@@Z` | `0x12810` | 565 | UnwindData |  |
| 87 | `?DoLudsPost@DataSyncAgent@@AEAA_NAEBVDataSet@@W4SyncTypes@DataSync@UDC@@W4EGetDBPathMethod@utility@5@@Z` | `0x12A50` | 1,524 | UnwindData |  |
| 88 | `?DoPost@DataSyncAgent@@AEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@HW4EGetDBPathMethod@utility@UDC@@_N@Z` | `0x13050` | 1,357 | UnwindData |  |
| 89 | `?DoPostWithLogonUser@DataSyncAgent@@AEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@HW4EGetDBPathMethod@utility@UDC@@@Z` | `0x135A0` | 279 | UnwindData |  |
| 90 | `?DoTimerPost@DataSyncAgent@@AEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x136C0` | 2,466 | UnwindData |  |
| 91 | `?DuplicateLastRecordInDB@DataSyncAgent@@IEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0x14530` | 1,720 | UnwindData |  |
| 92 | `?DuplicateTelemetryHandler@DataSyncAgent@@IEAAXAEAUSendTelemetryCommandParams@UDC@@@Z` | `0x14BF0` | 838 | UnwindData |  |
| 99 | `?FullInit@DataSyncAgent@@UEAAXXZ` | `0x14F40` | 8,789 | UnwindData |  |
| 100 | `?GetCurrTimeGivenFilePath@DataSyncAgent@@AEAA_JAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x171A0` | 46 | UnwindData |  |
| 101 | `?GetDataItemType@DataSyncAgent@@CAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x172D0` | 28 | UnwindData |  |
| 102 | `?GetDatasetPolicy@DataSyncAgent@@AEAA?AVDataSet@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@H@Z` | `0x17A90` | 584 | UnwindData |  |
| 106 | `?GetInstance@DataSyncAgent@@SAPEAV1@XZ` | `0x17CE0` | 158 | UnwindData |  |
| 113 | `?GetRetryInfo@DataSyncAgent@@IEAA_NAEBW4SyncEp_type@SyncEP@@AEAURetryInfo@1@@Z` | `0x17E60` | 163 | UnwindData |  |
| 115 | `?HandleDeviceContext@DataSyncAgent@@EEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x17F10` | 4,413 | UnwindData |  |
| 116 | `?HandleNRT@DataSyncAgent@@EEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x19050` | 480 | UnwindData |  |
| 117 | `?HandleResetBackoffState@DataSyncAgent@@AEAA_NXZ` | `0x19230` | 868 | UnwindData |  |
| 118 | `?HandleResetBackoffStateOnDnsRecovery@DataSyncAgent@@IEAA_NXZ` | `0x195A0` | 1,051 | UnwindData |  |
| 119 | `?HandleSharedNRT@DataSyncAgent@@EEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x199C0` | 509 | UnwindData |  |
| 125 | `?IncrementRetriesExpired@DataSyncAgent@@AEAAXHAEAURetryInfo@1@@Z` | `0x19BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `?Init@DataSyncAgent@@UEAAXAEAPEAX@Z` | `0x19BE0` | 575 | UnwindData |  |
| 128 | `?InitTimerDatasetStates@DataSyncAgent@@AEAAXXZ` | `0x19E20` | 5,925 | UnwindData |  |
| 129 | `?InternalDBChangesNotify@DataSyncAgent@@AEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1B550` | 99 | UnwindData |  |
| 130 | `?IsApplicableForSync@DataSyncAgent@@EEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1B5C0` | 1,010 | UnwindData |  |
| 131 | `?IsApplicableForSyncWithThrottling@DataSyncAgent@@QEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAU_sync_data@1@@Z` | `0x1B9C0` | 47 | UnwindData |  |
| 132 | `?IsCertificateExpiryError@DataSyncAgent@@IEAA_NAEBUInvokeHttpResponse@UDCCore@@@Z` | `0x1BB50` | 50 | UnwindData |  |
| 133 | `?IsDataSyncPausedDueToCertExpiry@DataSyncAgent@@IEBA_NXZ` | `0x1BB90` | 340 | UnwindData |  |
| 135 | `?IsDeviceIn403DeviceMissingErrorState@DataSyncAgent@@IEAA_NXZ` | `0x1BCF0` | 70 | UnwindData |  |
| 136 | `?IsLcpSyncReady@DataSyncAgent@@AEAA_NXZ` | `0x1BD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `?IsLudpSyncReady@DataSyncAgent@@AEAA_NXZ` | `0x1BD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `?IsLudsSyncReady@DataSyncAgent@@AEAA_NXZ` | `0x1BD70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `?IsMaxLimitReachedFor403DeviceMissingCounter@DataSyncAgent@@IEAA_NXZ` | `0x1BD90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `?IsNullOrNoneDataSet@DataSyncAgent@@AEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1BDA0` | 413 | UnwindData |  |
| 141 | `?IsSyncAllowedByMetrics@DataSyncAgent@@AEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1BF40` | 90 | UnwindData |  |
| 142 | `?IsSyncAllowedByMetrics@DataSyncAgent@@AEAA_NXZ` | `0x1BFA0` | 43 | UnwindData |  |
| 143 | `?IsSyncAllowedByMetricsForFile@DataSyncAgent@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1BFD0` | 743 | UnwindData |  |
| 145 | `?IsTelemetryReadyToSync@DataSyncAgent@@AEAA_NXZ` | `0x1C2C0` | 1,503 | UnwindData |  |
| 146 | `?IsTimeLimitFor403ErrorExceeded@DataSyncAgent@@IEAA_NXZ` | `0x1C8A0` | 99 | UnwindData |  |
| 147 | `?IsUdcFacingCirticalGatewayError@DataSyncAgent@@AEAA_NXZ` | `0x1C910` | 153 | UnwindData |  |
| 152 | `?ListenToCollectionDoneNotification@DataSyncAgent@@IEAAXXZ` | `0x1C9B0` | 60 | UnwindData |  |
| 155 | `?MsgHandleProc@DataSyncAgent@@AEAAXXZ` | `0x1C9F0` | 1,162 | UnwindData |  |
| 156 | `?NotifyAndWaitForAck@DataSyncAgent@@IEAA_NH@Z` | `0x1CE80` | 310 | UnwindData |  |
| 157 | `?NullInit@DataSyncAgent@@IEAAXXZ` | `0x1CFC0` | 805 | UnwindData |  |
| 158 | `?OnNotification@DataSyncAgent@@IEAAXAEAVUDCNotificationData@@@Z` | `0x1D2F0` | 4,232 | UnwindData |  |
| 159 | `?OnSendTelemetryCommand@DataSyncAgent@@IEAAXAEAVUDCNotificationData@@@Z` | `0x1E380` | 385 | UnwindData |  |
| 161 | `?ParseSyncEPs@SyncEP@@IEAAXXZ` | `0x1E510` | 1,479 | UnwindData |  |
| 162 | `?PauseDataSyncDueToCertExpiry@DataSyncAgent@@IEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1EAE0` | 285 | UnwindData |  |
| 164 | `?ProcessDuplicateTelemetryList@DataSyncAgent@@IEAAXAEAV?$list@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@std@@@Z` | `0x1EC00` | 2,075 | UnwindData |  |
| 167 | `?ReadLastNotifications@DataSyncAgent@@AEAAXXZ` | `0x1F530` | 355 | UnwindData |  |
| 168 | `?RecheckNrtDatasetStates@DataSyncAgent@@AEAAXXZ` | `0x1F6A0` | 172 | UnwindData |  |
| 169 | `?RemainData2Sync@DataSyncAgent@@AEAA_NHV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1F750` | 1,581 | UnwindData |  |
| 170 | `?RemainData2SyncEx@DataSyncAgent@@AEAA_NHV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@KAEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@@Z` | `0x1FD80` | 1,619 | UnwindData |  |
| 171 | `?Reset403DeviceMissingError@DataSyncAgent@@IEAAXXZ` | `0x203E0` | 65 | UnwindData |  |
| 172 | `?ResetExponentialBackoff@DataSyncAgent@@AEAAXHAEAURetryInfo@1@@Z` | `0x20430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `?ResumeDataSyncAfterCertRenewal@DataSyncAgent@@IEAAXXZ` | `0x20450` | 259 | UnwindData |  |
| 175 | `?SendRegistrationRequest@DataSyncAgent@@AEAA_NXZ` | `0x20560` | 332 | UnwindData |  |
| 176 | `?Set403DeviceMissingError@DataSyncAgent@@IEAAXXZ` | `0x206B0` | 81 | UnwindData |  |
| 177 | `?SetRetryInfo@DataSyncAgent@@IEAAXAEBW4SyncEp_type@SyncEP@@AEBURetryInfo@1@@Z` | `0x20710` | 274 | UnwindData |  |
| 179 | `?SharedDBChangesNotify@DataSyncAgent@@AEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x20840` | 99 | UnwindData |  |
| 180 | `?ShouldPostForLcp@DataSyncAgent@@AEAA_NXZ` | `0x208B0` | 758 | UnwindData |  |
| 181 | `?ShouldPostForLuds@DataSyncAgent@@AEAA_NXZ` | `0x20BB0` | 742 | UnwindData |  |
| 182 | `?ShouldSuppressDeviceStatusHeartbeatSync@DataSyncAgent@@IEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x20EA0` | 1,521 | UnwindData |  |
| 183 | `?ShouldSyncHeartbeatTelemetry@DataSyncAgent@@AEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x214A0` | 621 | UnwindData |  |
| 186 | `?SyncDB@DataSyncAgent@@AEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x21800` | 2,217 | UnwindData |  |
| 187 | `?SyncImmediateTelemetries@DataSyncAgent@@AEAAXXZ` | `0x220B0` | 1,142 | UnwindData |  |
| 188 | `?SyncOnDemandTimerTelemetry@DataSyncAgent@@AEAAXXZ` | `0x22530` | 777 | UnwindData |  |
| 191 | `?UnInit@DataSyncAgent@@UEAAXXZ` | `0x22840` | 555 | UnwindData |  |
| 193 | `?UpdateRetryValues@DataSyncAgent@@AEAAXAEBHAEAH111AEAURetryInfo@1@@Z` | `0x22A70` | 11,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `?__autoclassinit2@ApplicabilityEvaluator@@QEAAX_K@Z` | `0x257B0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `?__autoclassinit2@DataSyncAgent@@QEAAX_K@Z` | `0x257B0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `?__autoclassinit2@DeviceInfoProvider@UDC@@QEAAX_K@Z` | `0x257B0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `?__autoclassinit2@LogThrottler@@QEAAX_K@Z` | `0x257B0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `?__autoclassinit2@LudpHeader@UDC@@QEAAX_K@Z` | `0x257B0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `?__autoclassinit2@LudpSyncAgent@DataSync@UDC@@QEAAX_K@Z` | `0x257B0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `?__autoclassinit2@SyncEP@@QEAAX_K@Z` | `0x257B0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `?__autoclassinit2@TelemetryRetentionHandler@@QEAAX_K@Z` | `0x257B0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `?__autoclassinit2@UDCHelperFactory@udc@@QEAAX_K@Z` | `0x257B0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `?__autoclassinit2@UdcStatusManager@UDC@@QEAAX_K@Z` | `0x257B0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `?init@SyncEP@@IEAAXXZ` | `0x25D60` | 88 | UnwindData |  |
| 212 | `?isLCPEnabled@SyncEP@@QEAA_NXZ` | `0x261E0` | 34 | UnwindData |  |
| 213 | `?isLCPOnlyEnabled@SyncEP@@QEAA_NXZ` | `0x26210` | 104 | UnwindData |  |
| 214 | `?isLUDPEnabled@SyncEP@@QEAA_NXZ` | `0x26280` | 34 | UnwindData |  |
| 215 | `?isLUDPOnlyEnabled@SyncEP@@QEAA_NXZ` | `0x262B0` | 104 | UnwindData |  |
| 216 | `?isLUDSEnabled@SyncEP@@QEAA_NXZ` | `0x26320` | 34 | UnwindData |  |
| 217 | `?isLUDSOnlyEnabled@SyncEP@@QEAA_NXZ` | `0x26350` | 104 | UnwindData |  |
| 218 | `?isValid@SyncEP@@QEAA_NXZ` | `0x263C0` | 104 | UnwindData |  |
| 8 | `??0LudpHeader@UDC@@QEAA@PEAVEventDataLogging@1@@Z` | `0x26E80` | 50 | UnwindData |  |
| 26 | `??1LudpHeader@UDC@@QEAA@XZ` | `0x26EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `?FillLudpHead@LudpHeader@UDC@@QEAA_NAEAVValue@Json@@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x26ED0` | 5,691 | UnwindData |  |
| 107 | `?GetInstance@LudpHeader@UDC@@SAPEAV12@XZ` | `0x28510` | 162 | UnwindData |  |
| 153 | `?LoadDeviceContext@LudpHeader@UDC@@QEAA_NXZ` | `0x285C0` | 89 | UnwindData |  |
| 10 | `??0LudpSyncAgent@DataSync@UDC@@QEAA@AEAVLudpHeader@2@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x2E4A0` | 142 | UnwindData |  |
| 12 | `??0LudpSyncAgent@DataSync@UDC@@QEAA@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0AEBW4_LudpSyncType@12@AEBW4EGetDBPathMethod@utility@2@@Z` | `0x2E530` | 131 | UnwindData |  |
| 110 | `?GetLudpSyncEndpoint@LudpSyncAgent@DataSync@UDC@@CA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x30420` | 737 | UnwindData |  |
| 111 | `?GetLudpSyncPointDbPath@LudpSyncAgent@DataSync@UDC@@SA?AVSyncPointDao@3@W4EGetDBPathMethod@utility@3@@Z` | `0x30710` | 123 | UnwindData |  |
| 121 | `?HaveData2Sync@LudpSyncAgent@DataSync@UDC@@QEAA_NH@Z` | `0x30790` | 1,296 | UnwindData |  |
| 123 | `?HaveData2SyncEx@LudpSyncAgent@DataSync@UDC@@QEAA_NHKAEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x30CA0` | 1,580 | UnwindData |  |
| 163 | `?PostDeviceContext@LudpSyncAgent@DataSync@UDC@@QEAAH_J@Z` | `0x36910` | 3,525 | UnwindData |  |
| 207 | `?doPost@LudpSyncAgent@DataSync@UDC@@QEAAHXZ` | `0x37720` | 362 | UnwindData |  |
| 103 | `?GetFirstIdFromDB@SyncAgentsHelper@DataSync@UDC@@QEAA_JV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x40DC0` | 113 | UnwindData |  |
| 104 | `?GetFirstIdFromDBWithDatasetId@SyncAgentsHelper@DataSync@UDC@@SA_JV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV45@W4EGetDBPathMethod@utility@3@@Z` | `0x40E40` | 530 | UnwindData |  |
| 108 | `?GetLastIdFromDB@SyncAgentsHelper@DataSync@UDC@@QEAA_JV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x41060` | 113 | UnwindData |  |
| 109 | `?GetLastIdFromDBWithDatasetId@SyncAgentsHelper@DataSync@UDC@@SA_JV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV45@W4EGetDBPathMethod@utility@3@@Z` | `0x410E0` | 530 | UnwindData |  |
| 122 | `?HaveData2Sync@SyncAgentsHelper@DataSync@UDC@@QEAA_NH@Z` | `0x41780` | 998 | UnwindData |  |
| 124 | `?HaveData2SyncEx@SyncAgentsHelper@DataSync@UDC@@QEAA_NHKAEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x41B70` | 1,121 | UnwindData |  |
| 134 | `?IsDeviceContextSyncSuccess@SyncAgentsHelper@DataSync@UDC@@SA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x41FE0` | 519 | UnwindData |  |
| 144 | `?IsSyncFrequencyElapsedSinceFirstTelemetryLogtime@SyncAgentsHelper@DataSync@UDC@@SA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0W4EGetDBPathMethod@utility@3@KAEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@5@@Z` | `0x421F0` | 348 | UnwindData |  |
| 148 | `?JsonSerializer@JsonFormater@DataSync@UDC@@SAHAEBV?$list@VDatasetContext@@V?$allocator@VDatasetContext@@@std@@@std@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@5@1AEAV65@PEA_J@Z` | `0x42350` | 4,113 | UnwindData |  |
| 149 | `?JsonSerializer@JsonFormater@DataSync@UDC@@SAHAEBV?$list@VDeviceContext@@V?$allocator@VDeviceContext@@@std@@@std@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@5@1AEAV65@PEA_J@Z` | `0x43370` | 165 | UnwindData |  |
| 150 | `?JsonSerializer@JsonFormater@DataSync@UDC@@SAHAEBV?$list@VItemContext@@V?$allocator@VItemContext@@@std@@@std@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@5@1AEAV65@PEA_J@Z` | `0x43420` | 2,997 | UnwindData |  |
| 151 | `?JsonSerializer@JsonFormater@DataSync@UDC@@SAHAEBV?$list@VItemEvent@@V?$allocator@VItemEvent@@@std@@@std@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@5@1AEAV65@PEA_J@Z` | `0x43FE0` | 7,156 | UnwindData |  |
| 174 | `?SaveResponseForDeviceSupport@SyncAgentsHelper@DataSync@UDC@@QEAAXAEAUHttpResponse@UDCCore@@@Z` | `0x45BE0` | 226 | UnwindData |  |
| 189 | `?SyncPointDaoForDbPath@SyncAgentsHelper@DataSync@UDC@@SA?AVSyncPointDao@3@W4EGetDBPathMethod@utility@3@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x45CD0` | 115 | UnwindData |  |
| 208 | `?doPost@SyncAgentsHelper@DataSync@UDC@@QEAAHAEAUInvokeHttpResponse@UDCCore@@@Z` | `0x45E50` | 1,969 | UnwindData |  |
| 22 | `??0TelemetryRetentionHandler@@QEAA@XZ` | `0x496D0` | 151 | UnwindData |  |
| 30 | `??1TelemetryRetentionHandler@@QEAA@XZ` | `0x49FA0` | 112 | UnwindData |  |
| 71 | `?CanStartNow@TelemetryRetentionHandler@@IEAA_NXZ` | `0x4A9F0` | 43 | UnwindData |  |
| 79 | `?ComputeCutoffUtc@TelemetryRetentionHandler@@AEAA?AV?$time_point@Usystem_clock@chrono@std@@V?$duration@_JU?$ratio@$00$0JIJGIA@@std@@@23@@chrono@std@@H@Z` | `0x4AA20` | 64 | UnwindData |  |
| 93 | `?ExecuteRetention@TelemetryRetentionHandler@@AEAAXW4EGetDBPathMethod@utility@UDC@@@Z` | `0x4AC70` | 4,484 | UnwindData |  |
| 112 | `?GetRetentionDays@TelemetryRetentionHandler@@AEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x4BE00` | 397 | UnwindData |  |
| 120 | `?HandleSingleDb@TelemetryRetentionHandler@@AEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@W4EGetDBPathMethod@utility@UDC@@@Z` | `0x4BF90` | 560 | UnwindData |  |
| 127 | `?Init@TelemetryRetentionHandler@@QEAAXXZ` | `0x4C1C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `?ReInit@TelemetryRetentionHandler@@QEAAXXZ` | `0x4C1C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `?ParseRetentionDays@RetentionUtils@TelemetryUtils@@SAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@HH@Z` | `0x4C1D0` | 1,104 | UnwindData |  |
| 166 | `?ReadDatasetSettingsFromConfigPolicy@TelemetryRetentionHandler@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV?$map@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@U?$less@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@@std@@@2@@3@@Z` | `0x4C620` | 631 | UnwindData |  |
| 178 | `?SetThreadState@TelemetryRetentionHandler@@AEAAXW4EGetDBPathMethod@utility@UDC@@_N@Z` | `0x4C8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `?Start@TelemetryRetentionHandler@@QEAA?AW4StartResult@1@_N@Z` | `0x4C8B0` | 1,342 | UnwindData |  |
| 185 | `?Stop@TelemetryRetentionHandler@@QEAAXXZ` | `0x4CDF0` | 202 | UnwindData |  |
| 190 | `?ToUpper@RetentionUtils@TelemetryUtils@@SA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV34@@Z` | `0x4CEC0` | 300 | UnwindData |  |
| 192 | `?UpdateRetentionSettings@TelemetryRetentionHandler@@AEAAXXZ` | `0x4CFF0` | 2,126 | UnwindData |  |
| 209 | `?ends_with@RetentionUtils@TelemetryUtils@@SA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0x538F0` | 35 | UnwindData |  |
| 61 | `??_7ConfigPolicyHelper@DataSync@UDC@@6B@` | `0x5D580` | 340 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `?DEFAULT_RETENTION_DAYS@TelemetryRetentionHandler@@1HB` | `0x5D6D4` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `?MinStartInterval@TelemetryRetentionHandler@@1V?$duration@HU?$ratio@$0DM@$00@std@@@chrono@std@@B` | `0x5D6D8` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `??_7SyncEP@@6B@` | `0x5D9F8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `??_7DataSyncAgent@@6BIDataSyncAgent@@@` | `0x5DA08` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `??_7DataSyncAgent@@6BIUDCAgent@@@` | `0x5DA40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `??_7PersonaUtility@udc@@6B@` | `0x5DAA0` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `??_7DeviceInfoProvider@UDC@@6B@` | `0x5DAE8` | 144,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `?ludpFileName@LudpSyncAgent@DataSync@UDC@@0V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@B` | `0x81000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `?m_certExpiryPauseReason@DataSyncAgent@@1V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@A` | `0x81020` | 168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `?_dataset_id_device_location@SyncAgentsHelper@DataSync@UDC@@0V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@B` | `0x810C8` | 9,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `?m_dataSyncPausedDueToCertExpiry@DataSyncAgent@@1U?$atomic@_N@std@@A` | `0x83590` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `?m_certExpiryPauseTime@DataSyncAgent@@1V?$time_point@Usteady_clock@chrono@std@@V?$duration@_JU?$ratio@$00$0DLJKMKAA@@std@@@23@@chrono@std@@A` | `0x83598` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `?m_lastHeartbeatCallTime@DataSyncAgent@@1V?$time_point@Usteady_clock@chrono@std@@V?$duration@_JU?$ratio@$00$0DLJKMKAA@@std@@@23@@chrono@std@@A` | `0x835A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `?m_heartbeatCallCount@DataSyncAgent@@1HA` | `0x835A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `?m_certExpiryStateMutex@DataSyncAgent@@1Vmutex@std@@A` | `0x835B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `?anonymousMetricsNotRequired@DataSyncAgent@@0V?$list@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@std@@A` | `0x83600` | 1,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `?datasetsRequiringLastItemSync@SyncAgentsHelper@DataSync@UDC@@2V?$vector@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@std@@B` | `0x83D38` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `?funcGetDBPathMethod@TelemetryRetentionHandler@@2V?$function@$$A6A?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@W4EGetDBPathMethod@utility@UDC@@@Z@std@@A` | `0x83DB0` | 0 | Indeterminate |  |
