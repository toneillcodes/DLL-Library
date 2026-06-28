# Binary Specification: SensorsNativeApi.V2.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SensorsNativeApi.V2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b1e8da9455518d05d87271630590dacc192cfe795ba823f26cbcaa5fc9cb5579`
* **Total Exported Functions:** 72

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `SensorCloseV2` | `0x13FA0` | 132 | UnwindData |  |
| 4 | `SensorDeviceIoControlV2` | `0x142B0` | 70 | UnwindData |  |
| 5 | `SensorDisableIoPathForDataNotificationsV2` | `0x14770` | 36 | UnwindData |  |
| 7 | `SensorEnableIdleOperationV2` | `0x147A0` | 164 | UnwindData |  |
| 14 | `SensorGetCapabilitiesV2` | `0x14850` | 521 | UnwindData |  |
| 21 | `SensorGetDataV2` | `0x14A60` | 730 | UnwindData |  |
| 23 | `SensorGetDeviceIdV2` | `0x14D40` | 295 | UnwindData |  |
| 31 | `SensorGetRangeResolutionV2` | `0x14E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `SensorNotificationConfigureV2` | `0x14E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `SensorNotificationStartV2` | `0x14E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `SensorNotificationStopV2` | `0x14E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `SensorSetRangeResolutionV2` | `0x14E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `SensorOpenV2` | `0x14E80` | 345 | UnwindData |  |
| 39 | `SensorRegisterDeviceRemovalNotificationV2` | `0x14FE0` | 482 | UnwindData |  |
| 56 | `SensorStartV2` | `0x151D0` | 277 | UnwindData |  |
| 59 | `SensorStopV2` | `0x15800` | 1,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `SensorUnregisterDeviceRemovalNotificationV2` | `0x15CD0` | 660 | UnwindData |  |
| 72 | `DllMain` | `0x16400` | 363 | UnwindData |  |
| 1 | `SensorCancelHistoryRetrievalV2` | `0x1B480` | 103 | UnwindData |  |
| 2 | `SensorClearHistoryV2` | `0x1B4F0` | 200 | UnwindData |  |
| 6 | `SensorDisableWakeV2` | `0x1B5C0` | 200 | UnwindData |  |
| 8 | `SensorEnableWakeV2` | `0x1B690` | 200 | UnwindData |  |
| 9 | `SensorGetAccDataV2` | `0x1B760` | 76 | UnwindData |  |
| 10 | `SensorGetAlsDataV2` | `0x1B7C0` | 55 | UnwindData |  |
| 11 | `SensorGetAlsDataWithColorV2` | `0x1B800` | 86 | UnwindData |  |
| 12 | `SensorGetBarDataV2` | `0x1B860` | 62 | UnwindData |  |
| 13 | `SensorGetCapabilitiesCollectionV2` | `0x1B8B0` | 498 | UnwindData |  |
| 15 | `SensorGetCurrentReadingV2` | `0x1BAB0` | 463 | UnwindData |  |
| 16 | `SensorGetDataCollectionV2` | `0x1BC90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `SensorGetDataDeliveryModeV2` | `0x1BCA0` | 499 | UnwindData |  |
| 18 | `SensorGetDataFieldPropertiesV2` | `0x1BEA0` | 637 | UnwindData |  |
| 19 | `SensorGetDataIntervalV2` | `0x1C130` | 496 | UnwindData |  |
| 20 | `SensorGetDataThresholdsV2` | `0x1C330` | 677 | UnwindData |  |
| 22 | `SensorGetDefaultDataThresholdsV2` | `0x1C5E0` | 677 | UnwindData |  |
| 24 | `SensorGetFifoMaxSizeV2` | `0x1C890` | 340 | UnwindData |  |
| 25 | `SensorGetFusDataV2` | `0x1C9F0` | 112 | UnwindData |  |
| 26 | `SensorGetGyrDataV2` | `0x1CA70` | 55 | UnwindData |  |
| 27 | `SensorGetHistoryV2` | `0x1CAB0` | 946 | UnwindData |  |
| 28 | `SensorGetMagDataV2` | `0x1CE70` | 71 | UnwindData |  |
| 29 | `SensorGetPropertiesV2` | `0x1CEC0` | 681 | UnwindData |  |
| 30 | `SensorGetPrxDataV2` | `0x1D170` | 76 | UnwindData |  |
| 32 | `SensorGetSupportedDataFieldsV2` | `0x1D1D0` | 493 | UnwindData |  |
| 33 | `SensorIsWakeEnabledV2` | `0x1D430` | 217 | UnwindData |  |
| 37 | `SensorOpenByInterfaceV2` | `0x1D510` | 396 | UnwindData |  |
| 40 | `SensorSetAccThresholdsV2` | `0x1D6B0` | 388 | UnwindData |  |
| 41 | `SensorSetAlsThresholdsV2` | `0x1D840` | 27 | UnwindData |  |
| 42 | `SensorSetAlsWithColorThresholdsV2` | `0x1D870` | 563 | UnwindData |  |
| 43 | `SensorSetBarThresholdsV2` | `0x1DAB0` | 184 | UnwindData |  |
| 44 | `SensorSetDataDeliveryModeV2` | `0x1DB70` | 474 | UnwindData |  |
| 45 | `SensorSetDataIntervalV2` | `0x1DD50` | 282 | UnwindData |  |
| 46 | `SensorSetDataThresholdsV2` | `0x1DE70` | 378 | UnwindData |  |
| 47 | `SensorSetFusThresholdsV2` | `0x1DFF0` | 474 | UnwindData |  |
| 48 | `SensorSetGyrThresholdsV2` | `0x1E1D0` | 388 | UnwindData |  |
| 49 | `SensorSetMagThresholdsV2` | `0x1E360` | 388 | UnwindData |  |
| 50 | `SensorSetOrientationSensorThresholdsV2` | `0x1E4F0` | 175 | UnwindData |  |
| 52 | `SensorSetReportLatencyV2` | `0x1E5B0` | 474 | UnwindData |  |
| 53 | `SensorStartCollectionV2` | `0x1E790` | 277 | UnwindData |  |
| 54 | `SensorStartHistoryV2` | `0x1E8B0` | 690 | UnwindData |  |
| 55 | `SensorStartStateChangeNotificationV2` | `0x1EB70` | 465 | UnwindData |  |
| 57 | `SensorStopHistoryV2` | `0x1ED50` | 697 | UnwindData |  |
| 58 | `SensorStopStateChangeNotificationV2` | `0x1F010` | 338 | UnwindData |  |
| 61 | `SimpleOrientationClose` | `0x217D0` | 98 | UnwindData |  |
| 62 | `SimpleOrientationEnableInLowPowerMode` | `0x21840` | 102 | UnwindData |  |
| 63 | `SimpleOrientationGetCapabilitiesCollectionV2` | `0x218B0` | 175 | UnwindData |  |
| 64 | `SimpleOrientationGetCurrentOrientation` | `0x21970` | 107 | UnwindData |  |
| 65 | `SimpleOrientationGetDeviceId` | `0x219F0` | 112 | UnwindData |  |
| 66 | `SimpleOrientationGetProperties` | `0x21A70` | 112 | UnwindData |  |
| 67 | `SimpleOrientationOpen` | `0x21AF0` | 171 | UnwindData |  |
| 68 | `SimpleOrientationRegisterDeviceRemovalNotification` | `0x21BB0` | 112 | UnwindData |  |
| 69 | `SimpleOrientationStart` | `0x21C30` | 112 | UnwindData |  |
| 70 | `SimpleOrientationStop` | `0x21CB0` | 98 | UnwindData |  |
| 71 | `SimpleOrientationUnregisterDeviceRemovalNotification` | `0x21D20` | 98 | UnwindData |  |
